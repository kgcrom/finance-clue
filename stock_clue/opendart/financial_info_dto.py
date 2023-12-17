from dataclasses import dataclass
from typing import Optional


@dataclass
class MajorAccountCompanyOutputDto:
    """
    단일회사 주요계정 재무정보 조회 결과를 담는 DTO 클래스

    Attributes:
        rcept_no (str): 접수번호
        bsns_year (str): 사업연도
        stock_code (str): 종목 코드
        reprt_code (str): 보고서 코드 (11011: 사업보고서, 11012: 반기보고서, 11013: 1분기보고서, 11014: 3분기보고서)
        account_nm (str): 계정명
        fs_div (str): 개별/연결구분 (CFS: 연결재무제표, OFS: 재무제표)
        fs_nm (str): 개별/연결명 (연결재무제표, 재무제표)
        sj_div (str): 재무제표 구분 (BS: 재무상태표, IS: 손익계산서, CIS: 포괄손익계산서, CF: 현금흐름표, SCE: 자본변동표)
        sj_nm (str): 재무제표명
        thstrm_nm (str): 당기명
        thstrm_dt (str): 당기일자
        thstrm_amount (int): 당기금액
        thstrm_add_amount (Optional[int]): 당기누적금액
        frmtrm_nm (str): 전기명
        frmtrm_dt (str): 전기일자
        frmtrm_amount (int): 전기금액
        frmtrm_add_amount (Optional[int]): 전기누적금액
        bfefrmtrm_nm (str): 전전기명
        bfe_frmtrm_dt (Optional[str]): 전전기일자
        bfefrmtrm_amount (int): 전전기금액
        ord (int): 계정과목 정렬순서
        currency (str): 통화 단위
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
    단일회사 전체 재무제표 조회 결과를 담는 DTO 클래스

    Attributes:
        rcept_no (str): 접수번호
        reprt_code (str): 보고서 코드
        bsns_year (str): 사업 연도
        corp_code (str): 고유번호
        sj_div (str): 재무제표 구분 (BS: 재무상태표, IS: 손익계산서, CIS: 포괄손익계산서, CF: 현금흐름표, SCE: 자본변동표)
        sj_nm (str): 재무제표명
        account_id (str): 계정 ID
        account_nm (str): 계정명
        account_detail (str): 계정상세
        thstrm_nm (str): 당기명
        thstrm_amount (int): 당기금액
        thstrm_add_amount (Optional[int]): 당기누적금액
        frmtrm_nm (str): 전기명
        frmtrm_amount (int): 전기금액
        frmtrm_q_nm (Optional[str]): 전기명(분/반기)
        frmtrm_q_amount (Optional[int]): 전기금액(분/반기)
        frmtrm_add_amount (Optional[int]): 전기누적금액
        bfefrmtrm_nm (str): 전전기명
        bfefrmtrm_amount (int): 전전기금액
        ord (int): 계정과목 정렬순서
        currency (str): 통화 단위
    """

    rcept_no: str
    reprt_code: str
    bsns_year: str
    corp_code: str
    sj_div: str
    sj_nm: str
    account_id: str
    account_nm: str
    account_detail: str
    thstrm_nm: str
    thstrm_amount: int
    thstrm_add_amount: Optional[int]
    frmtrm_nm: str
    frmtrm_amount: int
    frmtrm_q_nm: Optional[str]
    frmtrm_q_amount: Optional[int]
    frmtrm_add_amount: Optional[int]
    bfefrmtrm_nm: str
    bfefrmtrm_amount: int
    ord: int
    currency: str


@dataclass
class XbrlTaxanomyOutputDto:
    """
    XBRL taxanomy 재무제표 양식 조회 결과를 담는 dto 클래스
    sj_div talbe: https://opendart.fss.or.kr/guide/detail.do?apiGrpCd=DS003&apiId=2020001

    Attributes:
        sj_div (str): 재무제표 구분 (BS: 재무상태표, IS: 손익계산서, CIS: 포괄손익계산서, CF: 현금흐름표, SCE: 자본변동표)
        account_id (str): 계정 ID
        account_nm (str): 계정명
        bsns_de (str): 기준일
        label_kor (str): 한글 출력명
        label_eng (str): 영문 출력명
        data_tp (Optional[str]): 데이터 유형
        ifrs_ref (str): IRS 참조
    """

    sj_div: str
    account_id: str
    account_nm: str
    bsns_de: str
    label_kor: str
    label_eng: str
    data_tp: Optional[str]
    ifrs_ref: str


# TODO: implement 단일회사 주요 재무지표 API
