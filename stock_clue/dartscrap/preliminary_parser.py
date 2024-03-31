"""배당 관련 공시 페이지 파싱 모듈"""

from typing import TYPE_CHECKING, List, Optional

from bs4 import element

from stock_clue.dartscrap.dart_scrap_dto import PreliminaryEstimateDto
from stock_clue.dartscrap.table_parser import parse_html_table
from stock_clue.opendart.utils import str_to_int

if TYPE_CHECKING:
    from stock_clue.dartscrap import DartScrap


class PreliminaryParser:
    """영업(잠정) 실적 공시 페이지 파싱 클래스"""

    def __init__(self, dart_scrap: "DartScrap"):
        self.dart_scrap = dart_scrap

    def parse_preliminary_estimate(
        self, report_no: str
    ) -> PreliminaryEstimateDto:
        """
        영업(잠정)실적(공정공시) 페이지 파싱
        """
        from bs4 import BeautifulSoup

        url = f"https://dart.fss.or.kr/dsaf001/main.do?rcpNo={report_no}"
        contents = self.dart_scrap.get_html_content_no_side_menu(url)
        if contents is None:
            raise Exception("contents is None")

        soup = BeautifulSoup(contents, "html.parser")
        title = soup.find("div", {"class", "xforms_title"})
        table: Optional[element.Tag | element.NavigableString] = None
        if title is not None and "잠정" in title.text:
            table = title.find_next_sibling("table")

        if table is None:
            raise Exception(f"this content is not preliminary, {url}")
        table_info = parse_html_table(table, 7)

        unit = self.extract_unit_from_preliminary(table_info)

        # 영업이익, 당기순이익의 당기실적에 값이 있는 경우
        if table_info[6][2] != "-" and table_info[10][2] != "-":
            return PreliminaryEstimateDto(
                unit=unit,
                revenue_current_quarter=str_to_int(table_info[4][2], True),
                revenue_previous_quarter=str_to_int(table_info[4][3], True),
                revenue_qoq=table_info[4][4],
                revenue_previous_year=str_to_int(table_info[4][5], True),
                revenue_yoy=table_info[4][6],
                op_current_quarter=str_to_int(table_info[6][2], True),
                op_previous_quarter=str_to_int(table_info[6][3], True),
                op_qoq=table_info[6][4],
                op_previous_year=str_to_int(table_info[6][5], True),
                op_yoy=table_info[6][6],
                net_income_current_quarter=str_to_int(table_info[10][2], True),
                net_income_previous_quarter=str_to_int(table_info[10][3], True),
                net_income_qoq=table_info[10][4],
                net_income_previous_year=str_to_int(table_info[10][5], True),
                net_income_yoy=table_info[10][6],
            )
        else:
            results: List[List[str]] = []
            for i in range(12, len(table_info)):
                if "정보제공" in table_info[i][0]:
                    break
                if "구분" in table_info[i][0].replace("\xa0", "").replace(
                    " ", ""
                ):
                    continue

                results.append(table_info[i])

            return PreliminaryEstimateDto(
                unit=unit,
                etc_info=results,
            )

    def extract_unit_from_preliminary(
        self, table_info: List[List[Optional[str]]]
    ) -> str:
        """
        잠정실적 페이지에서 단위 추출하는 함수
        """
        for sub_list in table_info[0:13]:
            for item in sub_list:
                if item is not None and item.find("단위") != -1:
                    if item.startswith("구분"):
                        return item[3:-1]
                    else:
                        return item
                    break
        return ""
