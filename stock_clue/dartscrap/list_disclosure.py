"""DART 공시 목록 스크래핑"""
from datetime import datetime
from datetime import timedelta
from enum import Enum
import re
from typing import TYPE_CHECKING, Dict, Optional, Union

from bs4 import BeautifulSoup
from bs4 import ResultSet
from bs4 import Tag
import requests

from stock_clue.dartscrap.dart_scrap_dto import DailyDisclosureListDto
from stock_clue.dartscrap.dart_scrap_dto import DartScrapParamDto
from stock_clue.dartscrap.dart_scrap_dto import DartScrapSearchParamDto
from stock_clue.dartscrap.dart_scrap_dto import DisclosureInfoDto
from stock_clue.dartscrap.dart_scrap_dto import SearchKeyword
from stock_clue.dartscrap.dart_scrap_dto import SearchOption
from stock_clue.error import HttpError

if TYPE_CHECKING:
    from stock_clue.dartscrap import DartScrap


class MarketGroup(Enum):
    KOSPI = "Y"
    KOSDAQ = "K"
    ALL = None


class SortField(Enum):
    """
    정렬 필드

    Attributes:
        DATE: 접수일자
        CRP: 회사명
    """

    DATE = "date"
    CRP = "crp"


class SortSeries(Enum):
    """
    정렬 순서

    Attributes:
        ASC: 오름차순
        DESC: 내림차순
    """

    ASC = "asc"
    DESC = "desc"


def parse_daily_disclosure(html_doc: str) -> DailyDisclosureListDto:
    """
    최근공시 1일치 공시보고서 html 파싱

    Args:
        html_doc (str): 공시 html 텍스트

    Returns:
        DailyDisclosureListDto: 공시 리스트 정보 파싱 결과

    """
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


def parse_search_disclosure(html_doc: str) -> DailyDisclosureListDto:
    """
    공시통합검색 공시보고서 html 파싱

    Args:
        html_doc (str): 공시 html 텍스트

    Returns:
        DailyDisclosureListDto: 공시 리스트 정보 파싱 결과

    """
    soup = BeautifulSoup(html_doc, "html.parser")

    page_info = soup.find("div", {"class": "pageInfo"})
    if not isinstance(page_info, Tag):
        return DailyDisclosureListDto(total=0, disclosures=[])

    total = int(re.findall("\d+", page_info.text)[2])

    table = soup.find("table")
    tbody = table.find("tbody")
    table_rows: ResultSet = tbody.find_all("tr")

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


def get_search_parameter(
    search_option: SearchOption,
    keyword: SearchKeyword,
    sort_field: str,
    sort_series: str,
    page: int,
    size: int,
    start_date: Optional[str],
    end_date: Optional[str],
) -> Optional[Dict[str, str | int]]:
    """
    공시통합검색 공시목록 조회 파라미터 생성

    Args:
        search_option (SearchOption): 검색 옵션
        keyword (SearchKeyword): 검색 키워드
        sort_field (str): 정렬 필드 (접수일자[date], 회사명[crp])
        sort_series (str): 정렬 순서 (오름차순[asc], 내림차순[desc])
        page (int): 페이지 번호 (1부터 시작)
        size (int): 페이지 사이즈 (기본값: 15)
        start_date (Optional[str]): 검색 시작 일자 (YYYYMMDD)
        end_date (Optional[str]): 검색 종료 일자 (YYYYMMDD)

    Returns:
        Optional[Dict[str, str | int]]: 검색 파라미터
    """
    now = datetime.now()
    if end_date is None:
        end_date = now.strftime("%Y%m%d")
    if start_date is None:
        start_date = (now - timedelta(weeks=52)).strftime("%Y%m%d")

    if search_option == SearchOption.REPORT:
        return DartScrapSearchParamDto(
            current_page=page,
            max_results=size,
            max_links=None,
            sort=sort_field,
            series=sort_series,
            report_name_pop_yn="Y",
            business_code="all",
            option=search_option.value,
            report_name=keyword.value,
            start_date=start_date,
            end_date=end_date,
            final_report="recent",
            business_nm="전체",
            corporation_type="all",
            closing_accounts_month="all",
        ).dict()
    elif search_option == SearchOption.CORP:
        # 회사명 option: "corp", textCrpNm / keyword
        return None
    else:
        raise ValueError(f"search_option: {search_option} is not supported")


class ListDisclosure:
    def __init__(self, dart_scrap: "DartScrap", time_out: int = 5):
        self._dart_scrap = dart_scrap
        self.time_out = time_out

    def get_daily_disclosure(
        self,
        selected_date: str,
        page: int,
        market_group: MarketGroup = MarketGroup.ALL,
    ) -> DailyDisclosureListDto:
        """
        최근공시 보고서 목록 조회

        Args:
            selected_date (str): 조회 일자
            page (int): 페이지 번호
            market_group (MarketGroup): 시장 구분 (Y: 유가증권시장, K: 코스닥, None: 전체)

        Returns:
            DailyDisclosureListDto: 공시 리스트 정보 파싱 결과
        """
        url = "https://dart.fss.or.kr/dsac001/search.ax"

        form_data = DartScrapParamDto(
            current_page=page,
            max_results=100,
            max_links=None,
            sort="time",
            series="desc",
            page_grouping=market_group.value,
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

    def search(
        self,
        search_option: SearchOption,
        keyword: SearchKeyword,
        start_date: Optional[str] = None,
        end_date: Optional[str] = None,
        sort_field: SortField = SortField.DATE,
        sort_series: SortSeries = SortSeries.DESC,
        page: int = 1,
        size: Union[15, 30, 50, 100] = 15,
    ) -> DailyDisclosureListDto:
        """
        공시통합검색 공시목록 조회
        """
        # TODO 검색 관련 파라미터 모두 확인해서 기능 구현 w/ parameter
        url = "https://dart.fss.or.kr/dsab007/detailSearch.ax"

        form_data = get_search_parameter(
            search_option,
            keyword,
            sort_field.value,
            sort_series.value,
            page,
            size,
            start_date,
            end_date,
        )

        headers = self._dart_scrap.headers_for_request
        response = requests.post(
            url=url, data=form_data, headers=headers, timeout=self.time_out
        )
        if response.status_code != 200:
            raise HttpError(f"HTTP Error: {response.status_code}")

        return parse_search_disclosure(response.text)
