from dataclasses import asdict
from dataclasses import dataclass
from typing import Generic, List, Optional, TypeVar

T = TypeVar("T")


@dataclass
class BaseListDto(Generic[T]):
    """
    OpenDart 사용시 사용되는 default Response dto 클래스

    Attributes:
        status (str): 에러 및 정보 코드
        message (str): 에러 및 정보 메시지
        list (List[T]): Response
    """

    status: str
    message: str
    list: Optional[List[T]]


@dataclass
class BaseParamDto:
    """
    OpenDart에서 조회시 사용되는 default parameter

    Attributes:
        corp_code (Optional[str]): 고유번호
        bsns_year (Optional[str]): 사업연도
        reprt_code (Optional[str]): 보고서 코드 (1분기보고서: 11013, 반기보고서 : 11012, 3분기보고서 : 11014, 사업보고서 : 11011)
        rcept_no (Optional[str]): 접수번호
        idx_cl_code (Optional[str]): 지표구분 (수익성지표 : M210000 안정성지표 : M220000 성장성지표 : M230000 활동성지표 : M240000)
        fs_div (Optional[str]): 개별/연결 구분 (CFS:연결재무제표, OFS:재무제표)
        sj_div (Optional[str]):  재무제표 구분 (BS: 재무상태표, IS: 손익계산서, CIS: 포괄손익계산서, CF: 현금흐름표, SCE: 자본변동표)
        bgn_de (Optional[str]): 시작일 (YYYYMMDD)
        end_de (Optional[str]): 종료일 (YYYYMMDD)
    """

    corp_code: Optional[str] = None
    bsns_year: Optional[str] = None
    reprt_code: Optional[str] = None
    rcept_no: Optional[str] = None
    idx_cl_code: Optional[str] = None
    fs_div: Optional[str] = None
    sj_div: Optional[str] = None
    bgn_de: Optional[str] = None
    end_de: Optional[str] = None

    def dict(self):
        return {k: str(v) for k, v in asdict(self).items() if v is not None}
