from dataclasses import dataclass
from typing import Optional


@dataclass
class MajorAccountCompanyOutputDto:
    """
    회사 주요계정 조회

    param rcept_no: 접수번호
    param bsns_year: 사업연도
    param stock_code: 종목코드
    param reprt_code: 보고서 코드 (1분기보고서 : 11013, 반기보고서 : 11012, 3분기보고서 : 11014, 사업보고서 : 11011)
    param account_nm: 계정명
    param fs_div: 개별/연결구분 (CFS:연결재무제표, OFS:재무제표)
    param fs_nm: 개별/연결명 (ex:연결재무제표)
    param sj_div: 재무제표구분 (BS:재무상태표, IS:손익계산서, CIS:포괄손익계산서, CF:현금흐름표, SCE:자본변동표)
    param sj_nm: 재무제표명 (ex:재무상태표)
    param thstrm_nm: 당기명 (ex:제 20 기 3분기말)
    param thstrm_dt: 당기일자 (ex:2018.09.30)
    param thstrm_amount: 당기금액 (ex:1000)
    param thstrm_add_amount: 당기누적금액 (ex:1000)
    param frmtrm_nm: 전기명 (ex:제 19 기말)
    param frmtrm_dt: 전기일자 (ex:2017.12.31)
    param frmtrm_amount: 전기금액 (ex:1000)
    param frmtrm_add_amount: 전기누적금액 (ex:1000)
    param bfefrmtrm_nm: 전전기명 (ex:제 18 기말)
    param bfefrmtrm_dt: 전전기일자 (ex:2016.12.31)
    param bfefrmtrm_amount: 전전기금액 (ex:1000)
    param ord: 계정과목 정렬순서 (ex: 1)
    param curr_cd: 통화 단위
    """

    rcept_no: str
    bsns_year: str
    stock_code: str
    reprt_code: str
    account_nm: str
    fs_div: str
    fs_nm: str
    sj_div: str
    sj_nm: str
    thstrm_nm: str
    thstrm_dt: str
    thstrm_amount: int
    thstrm_add_amount: Optional[int]
    frmtrm_nm: str
    frmtrm_dt: str
    frmtrm_amount: int
    frmtrm_add_amount: Optional[int]
    bfefrmtrm_nm: str
    bfe_frmtrm_dt: Optional[str]
    bfefrmtrm_amount: int
    ord: int
    currency: str


@dataclass
class WholeAccountSingleCompanyOutputDto:
    """
    단일회사 전체 재무제표 조회

    param
    """


@dataclass
class MajorAccountMultipleCompanyOutputDto:
    pass


@dataclass
class XbrlTaxanomyOutputDto:
    pass


@dataclass
class MajorIndexSingleCompanyOutputDto:
    pass


@dataclass
class MajorIndexMultipleCompanyOutputDto:
    pass
