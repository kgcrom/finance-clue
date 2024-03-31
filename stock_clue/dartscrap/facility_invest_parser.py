"""배당 관련 공시 페이지 파싱 모듈"""

from typing import TYPE_CHECKING, List, Optional

from bs4 import element

from stock_clue.dartscrap.dart_scrap_dto import FacilityInvestDto
from stock_clue.dartscrap.table_parser import parse_html_table
from stock_clue.opendart.utils import str_to_float
from stock_clue.opendart.utils import str_to_int

if TYPE_CHECKING:
    from stock_clue.dartscrap import DartScrap


class FacilityInvestParser:
    """신규시설 투자 공시 페이지 파싱 클래스"""

    def __init__(self, dart_scrap: "DartScrap"):
        self.dart_scrap = dart_scrap

    def parse_facility_invest(self, report_no: str) -> FacilityInvestDto:
        """
        신규시설 투자 공시 페이지 파싱
        """
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

        d = title.find_previous_sibling("div")
        correction_tables = d.find_all("table") if d is not None else None
        correction_publish_info = (
            parse_html_table(correction_tables[0], 2)
            if correction_tables is not None and len(correction_tables) != 1
            else None
        )
        correction_table_info = (
            parse_html_table(correction_tables[1], 3)
            if correction_tables is not None and len(correction_tables) != 1
            else None
        )
        correction_table_info2 = (
            parse_html_table(correction_tables[2], 1)
            if correction_tables is not None and len(correction_tables) >= 3
            else None
        )

        table_info: List[List[str]] = []
        if table is not None:
            table_info = parse_html_table(table, 3)

        # 투자대상을 추가 정보로 적는 보고서 존재
        begin_idx = 1 if "투자대상" in table_info[1][0] else 0
        investment_note = next(
            filter(lambda x: "기타 투자판단" in x[0], table_info[10:])
        )
        return FacilityInvestDto(
            correction_publish_date=(
                correction_publish_info[0][1]
                if correction_publish_info is not None
                else None
            ),
            correction_submit_date=(
                correction_table_info[1][1]
                if correction_table_info is not None
                else None
            ),
            correction_cause=(
                correction_table_info[2][1]
                if correction_table_info is not None
                else None
            ),
            correction_cause_detail=(
                correction_table_info2[0][0].replace("\xa0", "")
                if correction_table_info2 is not None
                else None
            ),
            correction_note1=(
                correction_table_info[5]
                if correction_table_info is not None
                and len(correction_table_info) > 5
                else None
            ),
            correction_note2=(
                correction_table_info[6]
                if correction_table_info is not None
                and len(correction_table_info) > 6
                else None
            ),
            invest_amount=str_to_int(table_info[begin_idx + 1][2]),
            equity_amount=str_to_int(table_info[begin_idx + 2][2]),
            equity_ratio=str_to_float(table_info[begin_idx + 3][2]),
            is_large_scale_corporation=table_info[begin_idx + 4][2] == "해당",
            investment_purpose=table_info[begin_idx + 5][2].replace("\n", " "),
            investment_start_date=table_info[begin_idx + 6][2],
            investment_end_date=table_info[begin_idx + 7][2],
            investment_decision_date=table_info[begin_idx + 8][2],
            investment_note=investment_note[2],
        )
