from dataclasses import asdict
from dataclasses import dataclass
from typing import Generic, List, Optional, TypeVar

T = TypeVar("T")


@dataclass
class BaseListDto(Generic[T]):
    """

    param status
    param message
    param list
    """

    status: str
    message: str
    list: Optional[List[T]]


@dataclass
class BaseParamDto:
    """
    OpenDart 사용시 사용되는 parameter

    param corp_code: 고유번호
    param bsns_year: 사업연도
    param reprt_code: 보고서 코드 (1분기보고서: 11013, 반기보고서 : 11012, 3분기보고서 : 11014, 사업보고서 : 11011)
    param rcept_no: 접수번호
    param idx_cl_code: 지표구분 (수익성지표 : M210000 안정성지표 : M220000 성장성지표 : M230000 활동성지표 : M240000)
    param fs_div: 개별/연결 구분 (CFS:연결재무제표, OFS:재무제표)
    param sj_div: 재무제표 구분 (BS: 재무상태표, IS: 손익계산서, CIS: 포괄손익계산서, CF: 현금흐름표, SCE: 자본변동표)
    """

    corp_code: Optional[str] = None
    bsns_year: Optional[str] = None
    reprt_code: Optional[str] = None
    rcept_no: Optional[str] = None
    idx_cl_code: Optional[str] = None
    fs_div: Optional[str] = None
    sj_div: Optional[str] = None

    def dict(self):
        return {k: str(v) for k, v in asdict(self).items() if v is not None}
