"""자기주식 소각 공시 페이지 파싱 모듈"""

from typing import TYPE_CHECKING, List, Optional

from bs4 import element

from stock_clue.dartscrap.dart_scrap_dto import RetirementTreasuryStockDto
from stock_clue.dartscrap.table_parser import parse_html_table
from stock_clue.dartscrap.utils import str_to_int

if TYPE_CHECKING:
    from stock_clue.dartscrap import DartScrap


class RetirementTreasuryStockParser:
    """자기주식 소각 공시 페이지 파싱 클래스"""

    def __init__(self, dart_scrap: "DartScrap"):
        self.dart_scrap = dart_scrap

    # TODO duck type 학습해서 parser 클래스 통일하기
    def parse_retirement_treasury_stock(
        self, report_no: str
    ) -> RetirementTreasuryStockDto:
        from bs4 import BeautifulSoup

        url = f"https://dart.fss.or.kr/dsaf001/main.do?rcpNo={report_no}"
        contents = self.dart_scrap.get_html_content_no_side_menu(url)
        if contents is None:
            raise Exception("contents is None")

        soup = BeautifulSoup(contents, "html.parser")

        title = soup.find("div", {"class", "xforms_title"})
        table: Optional[element.Tag | element.NavigableString] = None
        if title is not None:
            table = title.find_next_sibling("table")

        table_info: List[List[str]] = []
        if table is not None:
            table_info = parse_html_table(table, 3)

        return RetirementTreasuryStockDto(
            common_share_count=str_to_int(table_info[0][2]),
            preferred_share_count=str_to_int(table_info[1][2]),
            issued_common_share_count=str_to_int(table_info[2][2]),
            issued_preferred_share_count=str_to_int(table_info[3][2]),
            retirement_amount=str_to_int(table_info[5][2]),
            acquisition_start_date_for_retirement=table_info[6][2],
            acquisition_end_date_for_retirement=table_info[7][2],
            acquisition_method=table_info[8][2],
            acquisition_broker=table_info[10][2],
            retirement_date=table_info[9][2],
        )
