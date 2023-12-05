"""배당 관련 공시 페이지 파싱 모듈"""

from typing import TYPE_CHECKING

from stock_clue.dartscrap.dart_scrap import parse_html_table
from stock_clue.dartscrap.dart_scrap_dto import DividendClosingShareholders
from stock_clue.dartscrap.dart_scrap_dto import DividendDecisionOnCash
from stock_clue.opendart.utils import str_to_float
from stock_clue.opendart.utils import str_to_int

if TYPE_CHECKING:
    from stock_clue.dartscrap.dart_scrap import DartScrap


class DividendParser:
    """배당 관련 공시 페이지 파싱 클래스"""

    def __init__(self, dart_scrap: "DartScrap"):
        self.dart_scrap = dart_scrap

    def parse_closing_shareholders(
        self, report_no: str
    ) -> DividendClosingShareholders:
        """현금.현물배당을 위한 최종주주명부 폐쇄(기준일)결정 공시 페이지 파싱"""
        url = f"https://dart.fss.or.kr/dsaf001/main.do?rcpNo={report_no}"

        contents = self.dart_scrap.get_html_content_no_side_menu(url)
        table_info = parse_html_table(contents, 4)

        # 칼럼이 자유인 경우 문자열 필터
        return DividendClosingShareholders(
            dividend_classification=table_info[0][2],
            start_date=table_info[1][2],
            end_date=table_info[2][2],
            base_date=table_info[3][2],
        )

    def parse_decision_on_cash(self, report_no: str) -> DividendDecisionOnCash:
        """현금.현물배당 결정 공시 페이지 파싱"""
        url = f"https://dart.fss.or.kr/dsaf001/main.do?rcpNo={report_no}"

        contents = self.dart_scrap.get_html_content_no_side_menu(url)
        table_info = parse_html_table(contents, 4)

        return DividendDecisionOnCash(
            dividend_classification=table_info[0][2],
            dividend_kind=table_info[1][2],
            dividend_amount=str_to_int(table_info[3][2]),
            dividend_rate=str_to_float(table_info[6][2]),
            total_dividend_amount=str_to_int(table_info[8][2]),
            dividend_date=table_info[9][2],
        )
