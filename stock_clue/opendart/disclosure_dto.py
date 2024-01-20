from dataclasses import asdict
from dataclasses import dataclass
from enum import Enum
from typing import List, Optional, Any

from stock_clue.opendart.disclosure_type import DisclosureType


def __to_str(value: Any) -> str:
    if isinstance(value, Enum):
        return value.name
    return str(value)


@dataclass
class ListInputDto:
    """
    공시 검색 조회를 위한 Input DTO

    Attributes:
        corp_code (Optional[str]): 고유번호 (8자리)
        bgn_de (Optional[str]): 시작일 (YYYYMMDD)
        end_de (Optional[str]): 종료일 (YYYYMMDD)
        last_reprt_at (Optional[str]): 최종보고서 검색여부 (Y or N)
        pblntf_ty (Optional[DisclosureType]): 공시 유형
        pblntf_detail_ty ((Optional[str])): 공시상세유형
        corp_cls (Optional[str]): 법인구분 (Y: 유가, K: 코스닥, N: 코넥스, E: 기타)
        sort (Optional[str]): 정렬(date: 접수일자, crp: 회사명, rpt: 보고서명 ※ 기본값 date)
        sort_mth (Optional[str]): 정렬방법 (asc: 오름차순, desc: 내림차순)
        page_no (Optional[int]): 페이지 번호 (1~n, ※ 기본값 1)
        page_count (Optional[int]): 페이지 건수 (1~100, ※ 기본값: 10, 최대값: 100)
    """

    corp_code: Optional[str] = None
    bgn_de: Optional[str] = None
    end_de: Optional[str] = None
    last_reprt_at: Optional[str] = None
    pblntf_ty: Optional[DisclosureType] = None
    pblntf_detail_ty: Optional[str] = None
    corp_cls: Optional[str] = "Y"
    sort: Optional[str] = None
    sort_mth: Optional[str] = None
    page_no: Optional[int] = 1
    page_count: Optional[int] = 10

    def dict(self):
        return {
            k: __to_str(v) for k, v in asdict(self).items() if v is not None
        }


@dataclass
class ListOutputDto:
    """
    공시 정보 조회 결과를 담는 dto 클래스

    Attributes:
        corp_cls (str):	법인구분 Y(유가), K(코스닥), N(코넥스), E(기타)
        corp_name (str): 종목명(법인명)	공시대상회사의 종목명(상장사) 또는 법인명(기타법인)
        corp_code (str): 고유번호(8자리)
        stock_code (str): 종목코드(6자리)
        report_nm (str): 보고서명 (공시구분+보고서명+기타정보)
        rcept_no (str): 접수번호(14자리)
        flr_nm (str): 공시 제출인명
        rcept_dt (str):	공시 접수일자 (YYYYMMDD)
        rm (str): 비고
    """

    corp_cls: str
    corp_name: str
    corp_code: str
    stock_code: str
    report_nm: str
    rcept_no: str
    flr_nm: str
    rcept_dt: str
    rm: str


@dataclass
class DisclosureSearchResultDto:
    """
    공시검색 정보 조회 메타 정보를 담는 dto 클래스

    Attributes:
        status (str): 에러 및 정보 코드
        message (str): 에러 및 정보 메시지
        page_no (int): 페이지 번호
        page_count (int): 페이지 별 건수
        total_count (int): 총 건수
        total_page (int): 총 페이지 수
        list (List[ListOutputDto]): 공시 정보 결과 DTO 리스트
    """

    status: str
    message: str
    page_no: int
    page_count: int
    total_count: int
    total_page: int
    list: List[ListOutputDto]


@dataclass
class CompanyOverviewOutputDto:
    """
    기업개황 조회 결과를 담는 dto 클래스

    Attributes:
        status (str): 에러 및 정보 코드
        message (str): 에러 및 정보 메시지
        corp_name (str): 정식명칭
        corp_name_eng (str): 영문명칭
        stock_name (str): 종목명(상장사) 또는 약식명칭(기타법인)
        stock_code (str): 상장회사의 종목코드(6자리)
        ceo_nm (str): 대표자명
        corp_cls (str): 법인구분 (Y: 유가, K: 코스닥, N: 코넥스, E:기타)
        jurir_no (str): 법인등록번호
        bizr_no (str): 사업자등록번호
        adres (str): 주소
        hmurl (str): 홈페이지
        ir_url (str): IR홈페이지
        phn_no (str): 전화번호
        fax_no (str): 팩스번호
        induty_code (str): 업종코드
        est_dt (str): 설립일 (YYYYMMDD)
        acc_mt (str): 결산월 (MM)
    """

    status: str
    message: str
    corp_name: str
    corp_name_eng: str
    stock_name: str
    stock_code: str
    ceo_nm: str
    corp_cls: str
    jurir_no: str
    bizr_no: str
    adres: str
    hm_url: str
    ir_url: str
    phn_no: str
    fax_no: str
    induty_code: str
    est_dt: str
    acc_mt: str


@dataclass
class CorpCodeDto:
    """
    고유번호 조회 결과를 담는 dto 클래스

    Attributes:
        corp_code (str): 고유번호
        corp_name (str): 정식명칭
        stock_code (Optional[str]): 종목코드
        modify_date (str): 최종변경일자
    """

    corp_code: str
    corp_name: str
    stock_code: Optional[str]
    modify_date: str
