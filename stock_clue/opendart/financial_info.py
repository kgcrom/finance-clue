"""상장기업 재무정보 조회 모듈"""

from typing import Dict

from stock_clue.error import HttpError
from stock_clue.opendart import OpenDart
from stock_clue.opendart.base_dto import BaseListDto
from stock_clue.opendart.base_dto import BaseParamDto
from stock_clue.opendart.financial_info_dto import (
    WholeAccountSingleCompanyOutputDto,
)
from stock_clue.opendart.financial_info_dto import MajorAccountCompanyOutputDto
from stock_clue.opendart.financial_info_dto import XbrlTaxanomyOutputDto
from stock_clue.opendart.request import Request
from stock_clue.opendart.utils import extract_file_name
from stock_clue.opendart.utils import str_to_int


class FinancialInfo:
    def __init__(self, open_dart: OpenDart):
        self.request = Request(open_dart.api_key, open_dart.timeout)

    def get_major_account_single_company(
        self, corp_code: str, bsns_year: str, reprt_code: str
    ) -> BaseListDto[MajorAccountCompanyOutputDto]:
        """
        단일회사 주요계정 조회

        Args:
            corp_code (str): 고유번호
            bsns_year (str): 사업 연도
            reprt_code (str): 보고서 코드

        Returns:
            BaseListDto[MajorAccountCompanyOutputDto]: 단일 회사 주요계정 조회 결과
        """
        path = "/api/fnlttSinglAcnt.json"
        params = BaseParamDto(
            corp_code=corp_code, bsns_year=bsns_year, reprt_code=reprt_code
        )
        response = self.request.get(path, params.dict())

        if response.status_code != 200:
            raise HttpError(path)

        data = response.json()

        def _mapping(x) -> MajorAccountCompanyOutputDto:
            return MajorAccountCompanyOutputDto(
                rcept_no=x["rcept_no"],
                bsns_year=x["bsns_year"],
                stock_code=x["stock_code"],
                reprt_code=x["reprt_code"],
                account_nm=x["account_nm"],
                fs_div=x["fs_div"],
                fs_nm=x["fs_nm"],
                sj_div=x["sj_div"],
                sj_nm=x["sj_nm"],
                thstrm_nm=x["thstrm_nm"],
                thstrm_dt=x["thstrm_dt"],
                thstrm_amount=str_to_int(x["thstrm_amount"]),
                thstrm_add_amount=(
                    str_to_int(x["thstrm_add_amount"])
                    if "thstrm_add_amount" in x
                    else None
                ),
                frmtrm_nm=x["frmtrm_nm"],
                frmtrm_dt=x["frmtrm_dt"],
                frmtrm_amount=str_to_int(x["frmtrm_amount"]),
                frmtrm_add_amount=(
                    str_to_int(x["frmtrm_add_amount"])
                    if "frmtrm_add_amount" in x
                    else None
                ),
                bfefrmtrm_nm=x["bfefrmtrm_nm"],
                bfe_frmtrm_dt=(
                    x["bfe_frmtrm_dt"] if "bfe_frmtrm_dt" in x else None
                ),
                bfefrmtrm_amount=str_to_int(x["bfefrmtrm_amount"]),
                ord=str_to_int(x["ord"]),
                currency=x["currency"],
            )

        return BaseListDto(
            status=data["status"],
            message=data["message"],
            list=list(map(_mapping, data["list"])),
        )

    def get_major_account_multiple_company(
        self, corp_code: str, bsns_year: str, reprt_code: str
    ) -> BaseListDto[MajorAccountCompanyOutputDto]:
        """
        다중회사 주요계정 조회

        Args:
            corp_code (str): 고유번호
            bsns_year (str): 사업 연도
            reprt_code (str): 보고서 코드

        Returns:
            BaseListDto[MajorAccountCompanyOutputDto]: 다중 회사 주요계정 조회 결과
        """
        path = "/api/fnlttMultiAcnt.json"
        params = BaseParamDto(
            corp_code=corp_code, bsns_year=bsns_year, reprt_code=reprt_code
        )

        response = self.request.get(path, params.dict())
        if response.status_code != 200:
            raise HttpError(path)

        def _mapping(x) -> MajorAccountCompanyOutputDto:
            return MajorAccountCompanyOutputDto(
                rcept_no=x["rcept_no"],
                bsns_year=x["bsns_year"],
                stock_code=x["stock_code"],
                reprt_code=x["reprt_code"],
                account_nm=x["account_nm"],
                fs_div=x["fs_div"],
                fs_nm=x["fs_nm"],
                sj_div=x["sj_div"],
                sj_nm=x["sj_nm"],
                thstrm_nm=x["thstrm_nm"],
                thstrm_dt=x["thstrm_dt"],
                thstrm_amount=str_to_int(x["thstrm_amount"]),
                thstrm_add_amount=(
                    str_to_int(x["thstrm_add_amount"])
                    if "thstrm_add_amount" in x
                    else 0
                ),
                frmtrm_nm=x["frmtrm_nm"],
                frmtrm_dt=x["frmtrm_dt"],
                frmtrm_amount=str_to_int(x["frmtrm_amount"]),
                frmtrm_add_amount=(
                    str_to_int(x["frmtrm_add_amount"])
                    if "frmtrm_add_amount" in x
                    else 0
                ),
                bfefrmtrm_nm=x["bfefrmtrm_nm"],
                bfe_frmtrm_dt=(
                    x["bfe_frmtrm_dt"] if "bfe_frmtrm_dt" in x else None
                ),
                bfefrmtrm_amount=str_to_int(x["bfefrmtrm_amount"]),
                ord=str_to_int(x["ord"]),
                currency=x["currency"],
            )

        data = response.json()

        return BaseListDto[MajorAccountCompanyOutputDto](
            status=data["status"],
            message=data["message"],
            list=list(map(_mapping, data["list"])),
        )

    def get_whole_account_single_company(
        self, corp_code: str, bsns_year: str, reprt_code: str, fs_div: str
    ) -> BaseListDto[WholeAccountSingleCompanyOutputDto]:
        """
        단일회사 전체 재무제표 조회

        Args:
            corp_code (str): 고유번호
            bsns_year (str): 사업 연도
            reprt_code (str): 보고서 코드
            fs_div (str): 개별/연결구분 (CFS: 연결재무제표, OFS: 재무제표)

        Returns:
            BaseListDto[WholeAccountSingleCompanyOutputDto]: 단일회사 전체 재무제표 조회 결과
        """
        path = "/api/fnlttSinglAcntAll.json"
        params = BaseParamDto(
            corp_code=corp_code,
            bsns_year=bsns_year,
            reprt_code=reprt_code,
            fs_div=fs_div,
        )

        response = self.request.get(path, params.dict())
        if response.status_code != 200:
            raise HttpError(path)

        def _mapping(x: Dict[str, str]) -> WholeAccountSingleCompanyOutputDto:
            return WholeAccountSingleCompanyOutputDto(
                rcept_no=x["rcept_no"],
                reprt_code=x["reprt_code"],
                bsns_year=x["bsns_year"],
                corp_code=x["corp_code"],
                sj_div=x["sj_div"],
                sj_nm=x["sj_nm"],
                account_id=x["account_id"],
                account_nm=x["account_nm"],
                account_detail=x["account_detail"],
                thstrm_nm=x["thstrm_nm"],
                thstrm_amount=str_to_int(x["thstrm_amount"]),
                thstrm_add_amount=(
                    str_to_int(x["thstrm_add_amount"])
                    if "thstrm_add_amount" in x
                    else None
                ),
                frmtrm_nm=x["frmtrm_nm"],
                frmtrm_amount=str_to_int(x["frmtrm_amount"]),
                frmtrm_q_nm=x["frmtrm_q_nm"] if "frmtrm_q_nm" in x else None,
                frmtrm_q_amount=(
                    str_to_int(x["frmtrm_q_amount"])
                    if "frmtrm_q_amount" in x
                    else None
                ),
                frmtrm_add_amount=(
                    str_to_int(x["frmtrm_add_amount"])
                    if "frmtrm_add_amount" in x
                    else None
                ),
                bfefrmtrm_nm=x["bfefrmtrm_nm"],
                bfefrmtrm_amount=str_to_int(x["bfefrmtrm_amount"]),
                ord=str_to_int(x["ord"]),
                currency=x["currency"],
            )

        data = response.json()
        return BaseListDto[WholeAccountSingleCompanyOutputDto](
            status=data["status"],
            message=data["message"],
            list=list(map(_mapping, data["list"])),
        )

    def download_xbrl(self, rcept_no: str, reprt_code: str, file_path: str):
        """
        재무제표 원본파일(XBRL) 다운로드

        Args:
            rcept_no (str): 접수번호
            reprt_code (str): 보고서 코드 (11011: 사업보고서, 11012: 반기보고서, 11013: 1분기보고서, 11014: 3분기보고서)

        Returns:
            None
        """
        path = "/api/fnlttXbrl.xml"

        params = BaseParamDto(rcept_no=rcept_no, reprt_code=reprt_code)
        response = self.request.get(path, params.dict(), True)

        if response.status_code != 200:
            raise HttpError()

        file_name = extract_file_name(response)

        with open(f"{file_path}/{file_name}", mode="wb") as w:
            for chunk in response.iter_content(chunk_size=10 * 1024):
                w.write(chunk)

    def get_xbrl_taxanomy(
        self, sj_div: str
    ) -> BaseListDto[XbrlTaxanomyOutputDto]:
        """
        XBRL 텍사노미 재무제표양식 조회

        Args:
            sj_div (str): 재무제표 구분 (BS: 재무상태표, IS: 손익계산서, CIS: 포괄손익계산서, CF: 현금흐름표, SCE: 자본변동표

        Returns:
            XbrlTaxanomyOutputDto: XBRL 텍사노미 재무제표양식 결과
        """
        path = "/api/xbrlTaxonomy.json"
        params = BaseParamDto(sj_div=sj_div)

        response = self.request.get(path, params.dict())
        if response.status_code != 200:
            raise HttpError(path)

        def _mapping(x: Dict[str, str]) -> XbrlTaxanomyOutputDto:
            return XbrlTaxanomyOutputDto(
                sj_div=x["sj_div"],
                account_id=x["account_id"],
                account_nm=x["account_nm"],
                bsns_de=x["bsns_de"],
                label_kor=x["label_kor"],
                label_eng=x["label_eng"],
                data_tp=x["data_tp"] if "data_tp" in x else None,
                ifrs_ref=x["ifrs_ref"],
            )

        data = response.json()

        return BaseListDto[XbrlTaxanomyOutputDto](
            status=data["status"],
            message=data["message"],
            list=list(map(_mapping, data["list"])),
        )
