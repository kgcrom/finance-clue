from dataclasses import asdict
from dataclasses import dataclass
from typing import Dict, List, Union


@dataclass
class DartScrapParamDto:
    """
    Data class representing the parameters for scraping DART (Data Analysis, Retrieval and Transfer System) data.

    Attributes:
        current_page (int): The current page number.
        max_results (int): The maximum number of results per page.
        max_links (Union[str, None]): The maximum number of links to scrape. None if unlimited.
        sort (str): The sorting criteria for the scraped data. Options: 'time' (시간), 'crp' (회사명), 'rpt' (보고서명).
        series (str): The sorting order for the scraped data. Options: 'desc', 'asc'.
        page_grouping (Union[str, None]): The page grouping criteria. (Y: 유가증권시장, K: 코스닥, None: 전체)
        mday_cnt (int): The number of days to include in the scraped data.
        select_date (str): The date to select for scraping.
        text_crp_cik (Union[str, None]): The CIK (Central Index Key) of the company to filter by. None if not filtering by CIK.
    """

    current_page: int
    max_results: int
    max_links: Union[str, None]
    sort: str  # time: 시간, crp: 회사명, rpt: 보고서명
    series: str  # desc asc
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
