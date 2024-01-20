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
    ) -> List[PreliminaryEstimateDto]:
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
        if title is not None:
            table = title.find_next_sibling("table")

        table_info: List[List[str]] = []
        if table is not None:
            table_info = parse_html_table(table, 7)

        results: List[PreliminaryEstimateDto] = []
        unit = ""
        for sub_list in table_info[0:13]:
            for item in sub_list:
                if item is not None and item.find("단위") != -1:
                    if item.startswith("구분"):
                        unit = item[3:-1]
                    else:
                        unit = item
                    break
            if unit is not None:
                break

        # 영업이익, 당기순이익의 당기실적에 값이 있는 경우
        if table_info[6][2] != "-" and table_info[10][2] != "-":
            for i in range(4, 12, 2):
                results.append(
                    PreliminaryEstimateDto(
                        unit=unit,
                        name=table_info[i][0],
                        table_headers=table_info[2],
                        header_date=table_info[3],
                        current_q_earnings=str_to_int(table_info[i][2]),
                        previous_q_earnings=str_to_int(table_info[i][3]),
                        qoq=table_info[i][4],
                        previous_y_earnings=str_to_int(table_info[i][5]),
                        yoy=table_info[i][6],
                    )
                )
        else:
            for i in range(12, len(table_info)):
                if "정보제공" in table_info[i][0]:
                    break
                if "구분" in table_info[i][0].replace("\xa0", "").replace(
                    " ", ""
                ):
                    continue

                results.append(
                    PreliminaryEstimateDto(
                        unit=unit,
                        name=table_info[i][0].replace("\xa0", ""),
                        table_headers=table_info[2],
                        header_date=table_info[3],
                        current_q_earnings=str_to_int(table_info[i][2]),
                        previous_q_earnings=str_to_int(table_info[i][3]),
                        qoq=table_info[i][4],
                        previous_y_earnings=str_to_int(table_info[i][5]),
                        yoy=table_info[i][6],
                    )
                )

        return results
