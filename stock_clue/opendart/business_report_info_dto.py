from dataclasses import asdict
from dataclasses import dataclass


@dataclass
class DirectorRemunerationInputDto:
    """
    이사·감사 전체의 보수현황(주주총회 승인금액) 조회 param dto

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
class DirectorRemunerationOutputDto:
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
class TotalStockQuantityInputDto:
    """
    주식의 총수 현황 조회 params dto

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
