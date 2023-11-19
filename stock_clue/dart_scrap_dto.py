from dataclasses import asdict
from dataclasses import dataclass
from typing import Dict, List, Union


@dataclass
class DartScrapParamDto:
    """
    Data class representing the parameters for scraping DART (Data Analysis, Retrieval and Transfer System) data.

    Attributes:
        currentPage (int): The current page number.
        maxResults (int): The maximum number of results per page.
        maxLinks (Union[str, None]): The maximum number of links to scrape. None if unlimited.
        sort (str): The sorting criteria for the scraped data. Options: 'time' (시간), 'crp' (회사명), 'rpt' (보고서명).
        series (str): The sorting order for the scraped data. Options: 'desc', 'asc'.
        pageGrouping (Union[str, None]): The page grouping criteria. (Y: 유가증권시장, K: 코스닥, None: 전체)
        mdayCnt (int): The number of days to include in the scraped data.
        selectDate (str): The date to select for scraping.
        textCrpCik (Union[str, None]): The CIK (Central Index Key) of the company to filter by. None if not filtering by CIK.
    """

    currentPage: int
    maxResults: int
    maxLinks: Union[str, None]
    sort: str  # time: 시간, crp: 회사명, rpt: 보고서명
    series: str  # desc asc
    pageGrouping: Union[str, None]
    mdayCnt: int
    selectDate: str
    textCrpCik: Union[str, None]

    def dict(self) -> Dict[str, Union[str, int]]:
        return {
            k: str(v) if v is not None else "" for k, v in asdict(self).items()
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
class DailyDisclosureInfoDto:
    def __init__(
        self, total: int, disclosures: List[Union[DisclosureInfoDto, None]]
    ):
        self.total = total
        self.disclosures = disclosures

    total: int
    list: List[Union[DisclosureInfoDto, None]]
