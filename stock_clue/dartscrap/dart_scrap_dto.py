from dataclasses import asdict
from dataclasses import dataclass
from typing import Dict, List, Union


@dataclass
class DartScrapParamDto:
    """
    Data class representing the parameters for scraping DART (Data Analysis, Retrieval and Transfer System) data.

    param current_page: 현재 페이지
    param max_results: 페이지당 최대 건수
    param max_links: 최대 링크 수
    param sort: 정렬 기준    # time: 시간, crp: 회사명, rpt: 보고서명
    param series: 정렬 순서  # desc asc
    param page_grouping: 페이지 그룹
    param mday_cnt: 조회 기준일자 이전 몇일치 공시 조회
    param select_date: 조회 기준일자
    param text_crp_cik: 회사명 또는 종목코드
    """

    current_page: int
    max_results: int
    max_links: Union[str, None]
    sort: str
    series: str
    page_grouping: Union[str, None]
    mday_cnt: int
    select_date: str
    text_crp_cik: Union[str, None]

    def _snake_to_camel(self, snake_str: str) -> str:
        components = snake_str.split("_")
        return components[0] + "".join(x.title() for x in components[1:])

    def dict(self) -> Dict[str, Union[str, int]]:
        return {
            self._snake_to_camel(k): str(v) if v is not None else ""
            for k, v in asdict(self).items()
        }


@dataclass
class DisclosureInfoDto:
    market_name: str
    company_name: str
    report_name: str
    report_date: str
    report_time: str
    report_url: str


@dataclass
class DailyDisclosureListDto:
    def __init__(
        self, total: int, disclosures: List[Union[DisclosureInfoDto, None]]
    ):
        self.total = total
        self.disclosures = disclosures

    total: int
    list: List[Union[DisclosureInfoDto, None]]


@dataclass
class DividendClosingShareholders:
    """
    주주명부 폐쇄(기준일)결정 공시 페이지 파싱 결과를 담는 데이터 클래스

    param dividend_classification: 배당구분
    param start_date: 시작일
    param end_date: 종료일
    param base_date: 기준일
    """

    dividend_classification: str
    start_date: str
    end_date: str
    base_date: str


@dataclass
class DividendDecisionOnCash:
    """
    현금.현물배당 결정 공시 페이지 파싱 결과를 담는 데이터 클래스

    param dividend_classification: 배당구분
    param dividend_kind: 배당종류
    param dividend_amount: 배당금
    param dividend_rate: 배당율
    param total_dividend_amount: 배당금 총액(원)
    param dividend_date: 배당기준일

    """

    dividend_classification: str
    dividend_kind: str
    dividend_amount: int
    dividend_rate: float
    total_dividend_amount: int
    dividend_date: str
