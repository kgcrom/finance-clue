"""DART 공시 목록 스크래핑"""

from typing import TYPE_CHECKING, Union

from bs4 import BeautifulSoup
from bs4 import ResultSet
from bs4 import Tag
import requests

from stock_clue.dartscrap.dart_scrap_dto import DailyDisclosureListDto
from stock_clue.dartscrap.dart_scrap_dto import DartScrapParamDto
from stock_clue.dartscrap.dart_scrap_dto import DisclosureInfoDto
from stock_clue.error import HttpError

if TYPE_CHECKING:
    from stock_clue.dartscrap.dart_scrap import DartScrap


def parse_daily_disclosure(html_doc: str) -> DailyDisclosureListDto:
    """1일치 공시보고서 html 파싱"""
    soup = BeautifulSoup(html_doc, "html.parser")

    total_values = soup.find("input", {"name": "totalCnt"})
    if isinstance(total_values, Tag) and "value" in total_values.attrs:
        total = int(total_values.attrs["value"])
    else:
        return DailyDisclosureListDto(total=0, disclosures=[])

    table_rows: ResultSet = soup.find_all("tr")

    def _mapping(tr: Tag) -> Union[DisclosureInfoDto, None]:
        td = tr.find_all("td")
        if len(td) == 0:
            return None
        report_time = td[0].text.strip()
        company_info = td[1]
        market_name = company_info.find("span").find("span").attrs["title"]
        company_name = company_info.a.text.strip()
        report_info = td[2]
        report_name = (
            report_info.text.strip()
            .replace("\r", "")
            .replace("\t", "")
            .replace("\n", " ")
        )
        report_path = report_info.a["href"]
        report_date = td[4].text

        return DisclosureInfoDto(
            market_name=market_name,
            company_name=company_name,
            report_name=report_name,
            report_date=report_date,
            report_time=report_time,
            report_url=f"https://dart.fss.or.kr{report_path}",
        )

    disclosures = list(
        filter(lambda x: x is not None, map(_mapping, table_rows))
    )

    return DailyDisclosureListDto(total=total, disclosures=disclosures)


class DailyDisclosure:
    def __init__(self, dart_scrap: "DartScrap", time_out: int = 5):
        self._dart_scrap = dart_scrap
        self.time_out = time_out

    def get_kospi_daily_disclosure(
        self, selected_date: str, page: int
    ) -> DailyDisclosureListDto:
        """유가증권시장 1일치 공시보고서"""
        url = "https://dart.fss.or.kr/dsac001/search.ax"

        form_data = DartScrapParamDto(
            current_page=page,
            max_results=100,
            max_links=None,
            sort="time",
            series="desc",
            page_grouping="Y",
            mday_cnt=0,
            select_date=selected_date,
            text_crp_cik=None,
        ).dict()

        headers = self._dart_scrap.headers_for_request
        response = requests.post(
            url=url, data=form_data, headers=headers, timeout=self.time_out
        )
        if response.status_code != 200:
            raise HttpError(f"HTTP Error: {response.status_code}")

        return parse_daily_disclosure(response.text)

    def get_kosdaq_daily_disclosure(self, selected_date: str, page: int):
        """코스닥 1일치 공시보고서"""
        url = "https://dart.fss.or.kr/dsac001/search.ax"
        form_data = DartScrapParamDto(
            current_page=page,
            max_results=100,
            max_links=None,
            sort="time",
            series="desc",
            page_grouping="K",
            mday_cnt=0,
            select_date=selected_date,
            text_crp_cik=None,
        ).dict()

        headers = self._dart_scrap.headers_for_request
        response = requests.post(
            url=url, data=form_data, headers=headers, timeout=self.time_out
        )
        if response.status_code != 200:
            raise HttpError(f"HTTP Error: {response.status_code}")

        return parse_daily_disclosure(response.text)

    def get_all_daily_disclosure(self, selected_date: str, page: int):
        """1일치 전제 공시 정보 조회"""
        url = "https://dart.fss.or.kr/dsac001/search.ax"
        form_data = DartScrapParamDto(
            current_page=page,
            max_results=100,
            max_links=None,
            sort="time",
            series="desc",
            page_grouping=None,
            mday_cnt=0,
            select_date=selected_date,
            text_crp_cik=None,
        ).dict()

        headers = self._dart_scrap.headers_for_request
        response = requests.post(
            url=url, data=form_data, headers=headers, timeout=self.time_out
        )
        if response.status_code != 200:
            raise HttpError(f"HTTP Error: {response.status_code}")

        return parse_daily_disclosure(response.text)
