"""자기주식 취득 공시 페이지 파싱 모듈"""

from dataclasses import dataclass
from typing import TYPE_CHECKING, List, Optional

from bs4 import element

from stock_clue.dartscrap.dart_scrap_dto import AcquisitionSharesDto
from stock_clue.dartscrap.dart_scrap_dto import SupplyAgreementDto
from stock_clue.dartscrap.table_parser import parse_html_table
from stock_clue.opendart.utils import str_to_float
from stock_clue.opendart.utils import str_to_int

if TYPE_CHECKING:
    from stock_clue.dartscrap import DartScrap


class AcquisitionSharesParser:
    """자기주식 취득 공시 페이지 파싱 클래스"""

    def __init__(self, dart_scrap: "DartScrap"):
        self.dart_scrap = dart_scrap

    def parse_acquisition_shares(self, report_no: str) -> AcquisitionSharesDto:
        from bs4 import BeautifulSoup

        url = f"https://dart.fss.or.kr/dsaf001/main.do?rcpNo={report_no}"
        contents = self.dart_scrap.get_html_content_no_side_menu(url)
        if contents is None:
            raise Exception("contents is None")

        soup = BeautifulSoup(contents, "html.parser")

        title = soup.find_all("p", {"class", "section-1"})
        table: Optional[element.Tag | element.NavigableString] = None
        if title is not None:
            table = title[1].find_next_sibling("table")

        table_info: List[List[str]] = []
        if table is not None:
            table_info = parse_html_table(table, 5)

        if title[1].text == "자기주식 취득 결정":
            return self.__generate_acquisition_decision(table_info)
        if title[1].text == "자기주식취득 신탁계약 체결 결정":
            return self.__generate_acquisition_contract(table_info)

    def __generate_acquisition_decision(
        self, table_info: List[List[str]]
    ) -> AcquisitionSharesDto:
        """
        주요사항보고서(자기주식취득결정) 공시
        """
        return AcquisitionSharesDto(
            acquisition_common_shares_count=str_to_int(table_info[0][3]),
            acquisition_preferred_shares_count=str_to_int(table_info[1][3]),
            acquisition_common_shares_amount=str_to_int(table_info[2][3]),
            acquisition_preferred_shares_amount=str_to_int(table_info[3][3]),
            acquisition_start_date=table_info[4][3],
            acquisition_end_date=table_info[5][3],
            acquisition_purpose=table_info[8][3],
            acquisition_method=table_info[9][3],
            acquisition_broker=table_info[10][3],
        )

    def __generate_acquisition_contract(
        self, table_info: List[List[str]]
    ) -> AcquisitionSharesDto:
        """
        주요사항보고서(자기주식취득신탁계약체결결정) 공시
        """
        return AcquisitionSharesDto(
            acquisition_common_shares_count=str_to_int(table_info[0][3]),
            acquisition_preferred_shares_count=0,
            acquisition_common_shares_amount=0,
            acquisition_preferred_shares_amount=0,
            acquisition_start_date=table_info[1][3],
            acquisition_end_date=table_info[2][3],
            acquisition_purpose=table_info[3][3],
            acquisition_method="",
            acquisition_broker=table_info[4][3],
        )
