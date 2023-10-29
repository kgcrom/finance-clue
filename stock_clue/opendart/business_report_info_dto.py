"""사업보고서 주요정보 OpenDart 연동 dto Module"""
from dataclasses import asdict
from dataclasses import dataclass
from typing import Optional


@dataclass
class DirectorRemunerationApprovalOutputDto:
    """
    이사·감사 전체의 보수현황(주주총회 승인금액) 조회 response dto

    param rcept_no: 접수번호
    param corp_cls: 법인구분 (Y: 유가, K: 코스닥, N: 코넥스, E: 기타)
    param corp_code: 고유번호
    param corp_name: 회사명
    param se: 구분
    param nmpr: 인원수
    param gmtsck_confm_amount: 주주총회 승인금액
    param rm: 비고
    """

    rcept_no: str
    corp_cls: str
    corp_code: str
    corp_name: str
    se: str
    nmpr: int
    gmtsck_confm_amount: int
    rm: str


@dataclass
class DirectorRemunerationAmountOutputDto:
    """
    이사·감사 전체의 보수현황(보수지급금액 - 유형별)) 조회 response dto

    param rcept_no: 접수번호
    param corp_cls: 법인구분 (Y: 유가, K: 코스닥, N: 코넥스, E: 기타)
    param corp_code: 고유번호
    param corp_name: 회사명
    param se: 구분
    param nmpr: 인원수
    param pymnt_totamt: 보수총액
    param psn1_avrg_pymntamt: 1인당 평균보수액
    param rm: 비고
    """

    rcept_no: str
    corp_cls: str
    corp_code: str
    corp_name: str
    se: str
    nmpr: int
    pymnt_totamt: int
    psn1_avrg_pymntamt: int
    rm: str


@dataclass
class TotalStockQuantityOutputDto:
    """
    주식의 총수 현황 조회 response dto

    param rcept_no: 접수번호
    param corp_cls: 법인구분 (Y: 유가, K: 코스닥, N: 코넥스, E: 기타)
    param corp_code: 고유번호
    param corp_name: 회사명
    param se: 구분
    param isu_stock_totqy: 발행한 주식의 총수
    param now_to_isu_stock_totqy: 현재까지 발행한 주식의 총수
    param now_to_dcrs_stock_totqy: 현재까지 감소한 주식의 총수
    param redc: 감자
    param profit_incnr: 이익소각
    param rdmstk_repy: 상환주식의 상환
    param etc: 기타
    param istc_totqy: 발행주식의 총수
    param tesstk_co: 자기주식수
    param distb_stock_co: 유통주식수
    """

    rcept_no: str
    corp_cls: str
    corp_code: str
    corp_name: str
    se: str
    isu_stock_totqy: int
    now_to_isu_stock_totqy: int
    now_to_dcrs_stock_totqy: int
    redc: int
    profit_incnr: int
    rdmstk_repy: int
    etc: int
    istc_totqy: int
    tesstk_co: int
    distb_stock_co: int


@dataclass
class AuditOpinionInputDto:
    """
    회계감사인의 명칭 및 감사의견 조회 params dto

    param corp_code: 고유번호
    param bsns_year: 사업연도
    param reprt_code: 보고서 코드 (1분기보고서: 11013, 반기보고서 : 11012, 3분기보고서 : 11014, 사업보고서 : 11011)
    """

    corp_code: str
    bsns_year: str
    reprt_code: str

    def dict(self):
        return {k: str(v) for k, v in asdict(self).items()}


@dataclass
class AuditOpinionOutputDto:
    """
    회계감사인의 명칭 및 감사의견 조회 response dto

    param rcept_no:	접수번호
    param corp_cls: 법인구분 (Y: 유가, K: 코스닥, N: 코넥스, E: 기타)
    param corp_code: 고유번호
    param corp_name: 회사명
    param bsns_year: 사업연도
    param adtor: 감사인
    param adt_opinion: 감사의견
    param adt_reprt_spcmnt_matter: 감사보고서 특기사항 (2019년 12월 8일까지 사용됨)
    param emphs_matter:	강조사항 등 (2019년 12월 9일부터 추가됨)
    param core_adt_matter: 핵심감사사항 (2019년 12월 9일부터 추가됨)
    """

    rcept_no: str
    corp_cls: str
    corp_code: str
    corp_name: str
    bsns_year: str
    adtor: str
    adt_opinion: Optional[str]
    adt_reprt_spcmnt_matter: Optional[str]
    emphs_matter: Optional[str]
    core_adt_matter: Optional[str]


@dataclass
class LargestShareHoldersOutputDto:
    """
    최대주주 현황 조회 response dto

    param rcept_no: 접수번호
    param corp_cls: 법인구분
    param corp_code: 고유번호
    param corp_name: 법인명
    param nm: 성명
    param relate: 관계
    param stock_knd: 주식 종류
    param bsis_posesn_stock_co: 기초 소유 주식 수
    param bsis_posesn_stock_qota_rt: 기초 소유 주식 지분율
    param trmend_posesn_stock_co: 기말 소유 주식 수
    param trmend_posesn_stock_qota_rt: 기말 소유 주식 지분 율
    param rm: 비고
    """

    rcept_no: str
    corp_cls: str
    corp_code: str
    corp_name: str
    nm: str
    relate: Optional[str]
    stock_knd: str
    bsis_posesn_stock_co: int
    bsis_posesn_stock_qota_rt: float
    trmend_posesn_stock_co: int
    trmend_posesn_stock_qota_rt: float
    rm: str
