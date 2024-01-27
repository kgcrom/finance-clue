from dataclasses import asdict
from dataclasses import dataclass
from enum import Enum
from typing import Dict, List, Optional


def _snake_to_camel(snake_str: str) -> str:
    components = snake_str.split("_")
    return components[0] + "".join(x.title() for x in components[1:])


@dataclass
class DartScrapParamDto:
    """
    Data class representing the parameters for scraping DART (Data Analysis, Retrieval and Transfer System) data.

    Attributes:
        current_page (int): 현재 페이지
        max_results (int): 페이지당 최대 건수
        max_links (Optional[str]): 최대 링크 수
        sort (str): 정렬 기준    # time: 시간, crp: 회사명, rpt: 보고서명
        series (str): 정렬 순서  # desc asc
        page_grouping (Optional[str]): 페이지 그룹
        mday_cnt (int): 조회 기준일자 이전 몇일치 공시 조회
        select_date (str): 조회 기준일자
        text_crp_cik (Optional[str]): 회사명 또는 종목코드
    """

    current_page: int
    max_results: int
    max_links: Optional[str]
    sort: str
    series: str
    page_grouping: Optional[str]
    mday_cnt: int
    select_date: str
    text_crp_cik: Optional[str]

    def dict(self) -> Dict[str, str | int]:
        return {
            _snake_to_camel(k): str(v) if v is not None else ""
            for k, v in asdict(self).items()
        }


@dataclass
class DisclosureInfoDto:
    """
    공시 리스트 정보 담는 dto 클래스

    Attributes:
        market_name (str): 시장구분
        company_name (str): 회사명
        report_name (str): 보고서명
        report_date (str): 보고서 접수일자
        report_time (str): 보고서 접수시간
        report_url (str): 보고서 url
    """

    market_name: str
    company_name: str
    report_name: str
    report_date: str
    report_time: str
    report_url: str


@dataclass
class DailyDisclosureListDto:
    """
    최근공시 보고서 목록 조회 결과를 담는 dto 클래스

    Attributes:
        total (int): 총 건수
        disclosures (List[Optional[DisclosureInfoDto]]): 최근 공시 리스트 정보
    """

    total: int
    disclosures: List[Optional[DisclosureInfoDto]]


@dataclass
class DividendClosingShareholders:
    """
    주주명부 폐쇄(기준일)결정 공시 페이지 파싱 결과를 담는 dto 클래스

    Attributes:
        dividend_classification (str): 배당구분
        start_date (str): 시작일
        end_date (str): 종료일
        base_date (str): 기준일
    """

    dividend_classification: str
    start_date: str
    end_date: str
    base_date: str


@dataclass
class DividendDecisionOnCash:
    """
    현금.현물배당 결정 공시 페이지 파싱 결과를 담는 dto 클래스

    Attributes:
        dividend_classification (str): 배당구분
        dividend_kind (str): 배당종류
        dividend_amount (int): 배당금
        dividend_rate (float): 배당율
        total_dividend_amount (int): 배당금 총액(원)
        dividend_date (str): 배당기준일
    """

    dividend_classification: str
    dividend_kind: str
    dividend_amount: float
    dividend_rate: float
    total_dividend_amount: int
    dividend_date: str


@dataclass
class DartScrapSearchParamDto:
    """
    통합 검색할 때 사용되는 parameter dto
    """

    current_page: int
    max_results: int
    sort: str
    series: str
    start_date: str
    end_date: str
    max_links: Optional[str] = None
    text_crp_cik: Optional[str] = None
    late_keyword: Optional[str] = None
    keyword: Optional[str] = None
    report_name_pop_yn: Optional[str] = None
    textkeyword: Optional[str] = None
    business_code: Optional[str] = None
    auto_search: Optional[str] = None
    option: Optional[str] = None
    report_name: Optional[str] = None
    text_crp_nm: Optional[str] = None
    text_crp_nm2: Optional[str] = None
    text_presenter_nm: Optional[str] = None
    final_report: Optional[str] = None
    business_nm: Optional[str] = None
    corporation_type: Optional[str] = None
    closing_accounts_month: Optional[str] = None
    toc_srch: Optional[str] = None
    toc_srch2: Optional[str] = None

    def dict(self) -> Dict[str, str | int]:
        return {
            _snake_to_camel(k): str(v) if v is not None else ""
            for k, v in asdict(self).items()
        }


@dataclass
class PreliminaryEstimateDto:
    """
    영업(잠정)실적(공정공시) 페이지 파싱 결과를 담는 dto 클래스
    누적은 저장하지 않는다.

    Attributes:
        unit (str): 단위
        name (str): 항목명
        table_headers (List[str]): 테이블 헤더
        header_date (List[str]): 헤더에 표시된 날짜
        current_q_earnings (Optional[int]): 당기실적
        previous_q_earnings (Optional[int]): 전기실적
        qoq (str): 전기대비증감율
        previous_y_earnings (Optional[int]): 전년동기실적
        yoy (str): 전년동기대비증감율
    """

    unit: str
    name: str
    table_headers: List[str]
    header_date: List[str]

    current_q_earnings: Optional[int]
    previous_q_earnings: Optional[int]
    qoq: str
    previous_y_earnings: Optional[int]
    yoy: str


@dataclass
class RevenueVolatilityDto:
    """
    매출액 또는 손익30%(대규모법인은15%)이상 페이지 파싱 결과를 담는 dto 클래스
    누적은 저장하지 않는다.

    Attribute:
        fs_kind (str): 재무제표 종류
        table_headers (List[str]): 테이블 헤더

        current_revenue (int): 매출액 당기실적
        previous_value (int): 매출액 전기실적
        diff_revenue_amount (int): 매출액 증감금액
        diff_revenue_ratio (str): 매출액 증감비율(%)

        current_op (int): 영업이익 당기실적
        previous_op (int): 영업이익 전기실적
        diff_op_amount (int): 영업이익 증감금액
        diff_op_ratio (str): 영업이익 증감비율(%)

        current_net_income (int): 순이익 당기실적
        previous_net_income (int): 순이익 전기실적
        diff_net_income_amount (int): 순이익 증감금액
        diff_net_income_ratio (str): 순이익 증감비율(%)

        cause (str): 사유
    """

    fs_kind: str
    table_headers: List[str]

    current_revenue: int
    previous_revenue: int
    diff_revenue_amount: int
    diff_revenue_ratio: str

    current_op: int
    previous_op: int
    diff_op_amount: int
    diff_op_ratio: str

    current_net_income: int
    previous_net_income: int
    diff_net_income_amount: int
    diff_net_income_ratio: str

    cause: str


@dataclass
class DartScrapSearchResultDto:
    """
    통합 검색 결과 dto
    """

    pass


class SearchOption(Enum):
    """
    통합 검색 옵션
    """

    REPORT = "report"
    CORP = "corp"


class SearchKeyword(Enum):
    """
    통합 검색 키워드
    """

    DIVIDEND_DECISION_ON_CASH = "현금ㆍ현물배당결정//현금배당결정"
    PRELIMINARY_ESTIMATE = "연결재무제표기준영업(잠정)실적(공정공시)//영업(잠정)실적(공정공시)"
    REVENUE_VOLATILITY = "매출액또는손익30%(대규모법인은15%)이상변경//매출액또는손익구조30%(대규모법인15%)미만변경(자율공시)//매출액또는손익구조30%(대규모법인은15%)미만변동(자율공시)//매출액또는손익구조30%(대규모법인은15%)이상변경//매출액또는손익구조30%(대규모법인은15%)이상변동"
