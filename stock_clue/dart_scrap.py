"""DART 공시정보 스크래핑"""
from typing import Dict, Union

from bs4 import BeautifulSoup
from bs4 import ResultSet
from bs4 import Tag
from playwright.sync_api import sync_playwright
import requests

from stock_clue.dart_scrap_dto import DailyDisclosureInfoDto
from stock_clue.dart_scrap_dto import DartScrapParamDto
from stock_clue.dart_scrap_dto import DisclosureInfoDto
from stock_clue.error import HttpError


def parse_daily_disclosure(html_doc: str) -> DailyDisclosureInfoDto:
    """1일치 공시보고서 html 파싱"""
    soup = BeautifulSoup(html_doc, "html.parser")

    total_values = soup.find("input", {"name": "totalCnt"})
    if isinstance(total_values, Tag) and "value" in total_values.attrs:
        total = int(total_values.attrs["value"])
    else:
        return DailyDisclosureInfoDto(total=0, disclosures=[])

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

    return DailyDisclosureInfoDto(total=total, disclosures=disclosures)


class DartScrap:
    def __init__(self) -> None:
        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page()
            page.goto("https://dart.fss.or.kr/main.do")
            self.cookies = page.context.cookies()
            browser.close()

    def get_kospi_daily_disclosure(
        self, selected_date: str, page: int
    ) -> DailyDisclosureInfoDto:
        """유가증권시장 1일치 공시보고서"""
        url = "https://dart.fss.or.kr/dsac001/search.ax"

        form_data = DartScrapParamDto(
            currentPage=page,
            maxResults=100,
            maxLinks=None,
            sort="time",
            series="desc",
            pageGrouping="Y",
            mdayCnt=0,
            selectDate=selected_date,
            textCrpCik=None,
        ).dict()

        headers = self._headers_for_request
        response = requests.post(url=url, data=form_data, headers=headers)
        if response.status_code != 200:
            raise HttpError(f"HTTP Error: {response.status_code}")

        return parse_daily_disclosure(response.text)

    def get_kosdaq_daily_disclosure(self, selected_date: str, page: int):
        """코스닥 1일치 공시보고서"""
        url = "https://dart.fss.or.kr/dsac001/search.ax"
        form_data = DartScrapParamDto(
            currentPage=page,
            maxResults=100,
            maxLinks=None,
            sort="time",
            series="desc",
            pageGrouping="K",
            mdayCnt=0,
            selectDate=selected_date,
            textCrpCik=None,
        ).dict()

        headers = self._headers_for_request
        response = requests.post(url=url, data=form_data, headers=headers)
        if response.status_code != 200:
            raise HttpError(f"HTTP Error: {response.status_code}")

        return parse_daily_disclosure(response.text)

    def get_all_daily_disclosure(self, selected_date: str, page: int):
        """1일치 전제 공시 정보 조회"""
        url = "https://dart.fss.or.kr/dsac001/search.ax"
        form_data = DartScrapParamDto(
            currentPage=page,
            maxResults=100,
            maxLinks=None,
            sort="time",
            series="desc",
            pageGrouping=None,
            mdayCnt=0,
            selectDate=selected_date,
            textCrpCik=None,
        ).dict()

        headers = self._headers_for_request
        response = requests.post(url=url, data=form_data, headers=headers)
        if response.status_code != 200:
            raise HttpError(f"HTTP Error: {response.status_code}")

        return parse_daily_disclosure(response.text)

    def search_disclosure_report_list(self):
        """공시 통합검색"""

        # body = {
        #     currentPage: 1,
        #     maxResults: 15,
        #     maxLinks: 10,
        #     sort: date,
        #     series: desc,
        #     textCrpCik: None,
        #     lateKeyword: None,
        #     keyword: None,
        #     reportNamePopYn: "Y",
        #     textkeyword: None,
        #     businessCode: "all",
        #     autoSearch: "N",
        #     option: "report",
        #     textCrpNm: None,
        #     reportName: "조회공시요구(풍문또는보도)에대한답변(미확정)//조회공시요구(풍문또는보도등)에대한답변(미확정)//조회공시요구(현저한시황변동)에대한답변(미확정)//풍문또는보도에대한해명(미확정)",
        #     tocSrch: None,
        #     textCrpNm2: None,
        #     textPresenterNm: None,
        #     startDate: 20221116,
        #     endDate: 20231116,
        #     decadeType: None,
        #     finalReport: "recent",
        #     businessNm: "전체",
        #     corporationType: "all",
        #     closingAccountsMonth: "all",
        #     tocSrch2: None,
        # }
        pass

    def _generate_cookie_for_request(self) -> Dict[str, str]:
        """쿠키값 생성"""
        cookies: Dict[str, str] = {}
        for cookie in self.cookies:
            cookies[cookie["name"]] = cookie["value"]
        return cookies

    @property
    def _headers_for_request(self) -> Dict[str, str]:
        jsession = [
            cookie for cookie in self.cookies if cookie["name"] == "JSESSIONID"
        ][0]
        wmonid = [
            cookie for cookie in self.cookies if cookie["name"] == "WMONID"
        ][0]
        return {
            "Accept": "text/html, */*; q=0.01",
            "Accept-Language": "en-US,en;q=0.9,ko;q=0.8",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "Host": "dart.fss.or.kr",
            "Origin": "https://dart.fss.or.kr",
            "Referer": "https://dart.fss.or.kr/dsac001/mainY.do",
            "Cookie": f"{wmonid['name']}={wmonid['value']}; {jsession['name']}={jsession['value']}",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36",
        }
