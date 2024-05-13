"""배당 관련 공시 페이지 파싱 모듈"""

from typing import TYPE_CHECKING, List, Optional

from bs4 import element

from finance_clue.dartscrap.dart_scrap_dto import RevenueVolatilityDto
from finance_clue.dartscrap.table_parser import parse_html_table
from finance_clue.dartscrap.utils import str_to_int

if TYPE_CHECKING:
    from finance_clue.dartscrap import DartScrap


class RevenueVolatilityParser:
    """매출액 또는 손익30%(대규모법인은15%)이상 변경 공시 페이지 파싱 클래스"""

    def __init__(self, dart_scrap: "DartScrap"):
        self.dart_scrap = dart_scrap

    def parse_revenue_volatility(self, report_no: str) -> RevenueVolatilityDto:
        """
        매출액 또는 손익30%(대규모법인은15%)이상 변경 공시 페이지 파싱
        """
        from bs4 import BeautifulSoup

        url = f"https://dart.fss.or.kr/dsaf001/main.do?rcpNo={report_no}"
        contents = self.dart_scrap.get_html_content_no_side_menu(url)
        if contents is None:
            raise Exception("contents is None")

        soup = BeautifulSoup(contents, "html.parser")
        title = soup.find("div", {"class", "xforms_title"})
        # TODO 자회사인 경우 자회사 정보 스크랩 필요
        # https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20240126800861
        table: Optional[element.Tag | element.NavigableString] = None
        if title is not None:
            table = title.find_next_sibling("table")

        table_info: List[List[str]] = []
        if table is not None:
            table_info = parse_html_table(table, 6)

        begin_table_idx = 1 if "외부감사인" in table_info[0][0] else 0

        fs_kind = table_info[begin_table_idx + 0][2]
        table_headers = table_info[begin_table_idx + 1][2:]
        cause = next(filter(lambda x: "변동 주요원인" in x[0], table_info[:15]))[2]

        revenue = table_info[begin_table_idx + 2]
        op = table_info[begin_table_idx + 3]
        net_income = table_info[begin_table_idx + 5]

        return RevenueVolatilityDto(
            fs_kind=fs_kind,
            table_headers=table_headers,
            current_revenue=str_to_int(revenue[2]),
            previous_revenue=str_to_int(revenue[3]),
            diff_revenue_amount=str_to_int(revenue[4]),
            diff_revenue_ratio=revenue[5],
            current_op=str_to_int(op[2]),
            previous_op=str_to_int(op[3]),
            diff_op_amount=str_to_int(op[4]),
            diff_op_ratio=op[5],
            current_net_income=str_to_int(net_income[2]),
            previous_net_income=str_to_int(net_income[3]),
            diff_net_income_amount=str_to_int(net_income[4]),
            diff_net_income_ratio=net_income[5],
            cause=cause.replace("\n", " "),
        )
