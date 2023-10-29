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
    param se_: 구분
    param nmpr: 인원수
    param gmtsck_confm_amount: 주주총회 승인금액
    param rm: 비고
    """

    rcept_no: str
    corp_cls: str
    corp_code: str
    corp_name: str
    nmpr: int
    gmtsck_confm_amount: int
    rm: str
