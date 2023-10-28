"""공시정보 관련된 API 연동을 제공하는 Module"""
import logging
import tempfile
from typing import TYPE_CHECKING, Any, List, Dict, Optional
import zipfile

import requests
from xmlschema import XMLSchema

from stock_clue.error import HttpError
from stock_clue.opendart.disclosure_dto import CompanyOverviewInputDto
from stock_clue.opendart.disclosure_dto import CompanyOverviewOutputDto
from stock_clue.opendart.disclosure_dto import CorpCodeDto
from stock_clue.opendart.disclosure_dto import DisclosureSearchResultDto
from stock_clue.opendart.disclosure_dto import DownloadDocumentInputDto
from stock_clue.opendart.disclosure_dto import ListInputDto
from stock_clue.opendart.disclosure_dto import ListOutputDto

if TYPE_CHECKING:
    from stock_clue.opendart.open_dart import OpenDart


def _mapping_list(d: Any) -> ListOutputDto:
    return ListOutputDto(
        d["corp_cls"],
        d["corp_name"],
        d["corp_code"],
        d["stock_code"],
        d["report_nm"],
        d["rcept_no"],
        d["flr_nm"],
        d["rcept_dt"],
        d["rm"],
    )


def extract_file_name(response: requests.Response) -> str:
    """
    파일 다운로드 HTTP 응답값에서 파일명 추출

    """
    content_disposition: str = response.headers["Content-Disposition"]
    index_filename = content_disposition.find("filename=")
    if index_filename == -1:
        raise HttpError(
            f"Can't find filename in response header. Content-Disposition: {content_disposition}"
        )
    file_name = content_disposition[index_filename + 9 :]
    return file_name


def unzip(tmp_path: str, file_name: str):
    """
    다운로드 한 압축 파일을 압축 해제
    """
    # TODO path 마지막 '/' 있는지 판단하고 변경
    with zipfile.ZipFile(f"{tmp_path}/{file_name}") as z:
        z.extractall(path=tmp_path)


class Disclosure:
    def __init__(self, open_dart: "OpenDart"):
        super().__init__()
        self.open_dart = open_dart

    def list(
        self, input_dto: ListInputDto
    ) -> Optional[DisclosureSearchResultDto]:
        path = "/api/list.json"
        response = self.open_dart.get(path, input_dto.dict())
        # TODO status, message 까지 포함한 클래스 리턴하도록
        # TODO python generic 이용 가능?
        #   - https://medium.com/@steveYeah/using-generics-in-python-99010e5056eb

        if response.status_code != 200:
            raise HttpError()

        data = response.json()

        # TODO status error message와 응답 정보 로깅
        # TODO open dart 오류는 별도 class가 관리
        if data["status"] != "000":
            logging.error(
                "status: %s , message: %s", data["status"], data["message"]
            )
            return None

        return DisclosureSearchResultDto(
            status=data["status"],
            message=data["message"],
            page_no=data["page_no"],
            page_count=data["page_count"],
            total_count=data["total_count"],
            total_page=data["total_page"],
            list=list(map(_mapping_list, data["list"])),
        )

    def get_company_overview(
        self, params: CompanyOverviewInputDto
    ) -> Optional[CompanyOverviewOutputDto]:
        path = "/api/company.json"
        response = self.open_dart.get(path, params.dict())

        if response.status_code != 200:
            raise HttpError()

        data = response.json()

        if data["status"] != "000":
            logging.error(
                "status: %s, message %s", data["status"], data["message"]
            )
            return None

        return CompanyOverviewOutputDto(
            status=data["status"],
            message=data["message"],
            corp_name=data["corp_name"],
            corp_name_eng=data["corp_name_eng"],
            stock_name=data["stock_name"],
            stock_code=data["stock_code"],
            ceo_nm=data["ceo_nm"],
            corp_cls=data["corp_cls"],
            jurir_no=data["jurir_no"],
            bizr_no=data["bizr_no"],
            adres=data["adres"],
            hm_url=data["hm_url"],
            ir_url=data["ir_url"],
            phn_no=data["phn_no"],
            fax_no=data["fax_no"],
            induty_code=data["induty_code"],
            est_dt=data["est_dt"],
            acc_mt=data["acc_mt"],
        )

    def download_document(self, params: DownloadDocumentInputDto):
        if params.file_path is None:
            raise KeyError()

        path = "/api/document.xml"
        file_path = params.file_path
        response = self.open_dart.get(path, params.dict(), True)

        if response.status_code != 200:
            raise HttpError()

        file_name = extract_file_name(response)

        # TODO return값으로 적당한 것 고민하고 수정
        with open(f"{file_path}/{file_name}", mode="wb") as w:
            for chunk in response.iter_content(chunk_size=10 * 1024):
                w.write(chunk)

    def get_corp_code_list(self) -> List[CorpCodeDto]:
        path = "/api/corpCode.xml"

        response = self.open_dart.get(path, is_stream=True)

        if response.status_code != 200:
            raise HttpError()

        file_name = extract_file_name(response)

        with tempfile.TemporaryDirectory() as tmp_path:
            file_full_path = f"{tmp_path}/{file_name}"
            with open(file_full_path, mode="wb") as w:
                for chunk in response.iter_content(chunk_size=10 * 1024):
                    w.write(chunk)

            unzip(tmp_path, file_name)

            xml_schema = XMLSchema(
                """
            <xs:schema attributeFormDefault="unqualified" elementFormDefault="qualified" xmlns:xs="http://www.w3.org/2001/XMLSchema">
              <xs:element name="result">
                <xs:complexType>
                  <xs:sequence>
                    <xs:element maxOccurs="unbounded" name="list">
                      <xs:complexType>
                        <xs:sequence>
                          <xs:element name="corp_code" type="xs:string" />
                          <xs:element name="corp_name" type="xs:string" />
                          <xs:element name="stock_code" type="xs:string" />
                          <xs:element name="modify_date" type="xs:string" />
                        </xs:sequence>
                      </xs:complexType>
                    </xs:element>
                  </xs:sequence>
                </xs:complexType>
              </xs:element>
            </xs:schema>
             """
            )
            data: Dict[str, Any] = xml_schema.decode(f"{tmp_path}/CORPCODE.xml")

            return list(
                map(
                    lambda x: CorpCodeDto(
                        corp_code=x["corp_code"],
                        corp_name=x["corp_name"],
                        stock_code=x["stock_code"]
                        if len(x["stock_code"]) == 6
                        else None,
                        modify_date=x["modify_date"],
                    ),
                    data["list"],
                )
            )
