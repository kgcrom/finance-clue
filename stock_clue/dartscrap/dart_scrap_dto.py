from dataclasses import asdict
from dataclasses import dataclass
from typing import Dict, List


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
        max_links (str | None): 최대 링크 수
        sort (str): 정렬 기준    # time: 시간, crp: 회사명, rpt: 보고서명
        series (str): 정렬 순서  # desc asc
        page_grouping (str | None): 페이지 그룹
        mday_cnt (int): 조회 기준일자 이전 몇일치 공시 조회
        select_date (str): 조회 기준일자
        text_crp_cik (str | None): 회사명 또는 종목코드
    """

    current_page: int
    max_results: int
    max_links: str | None
    sort: str
    series: str
    page_grouping: str | None
    mday_cnt: int
    select_date: str
    text_crp_cik: str | None

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
    """

    total: int
    disclosures: List[DisclosureInfoDto | None]


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
    max_links: str | None = None
    text_crp_cik: str | None = None
    late_keyword: str | None = None
    keyword: str | None = None
    report_name_pop_yn: str | None = None
    textkeyword: str | None = None
    business_code: str | None = None
    auto_search: str | None = None
    option: str | None = None
    report_name: str | None = None
    text_crp_nm: str | None = None
    text_crp_nm2: str | None = None
    text_presenter_nm: str | None = None
    final_report: str | None = None
    business_nm: str | None = None
    corporation_type: str | None = None
    closing_accounts_month: str | None = None
    toc_srch: str | None = None
    toc_srch2: str | None = None

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
    """

    unit: str
    name: str
    table_headers: List[str]
    header_date: List[str]

    current_q_earnings: int | None
    previous_q_earnings: int | None
    qoq: str
    previous_y_earnings: int | None
    yoy: str


@dataclass
class DartScrapSearchResultDto:
    """
    통합 검색 결과 dto
    """

    pass
