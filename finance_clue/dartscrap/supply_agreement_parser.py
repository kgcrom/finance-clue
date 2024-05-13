"""배당 관련 공시 페이지 파싱 모듈"""

from dataclasses import dataclass
from typing import TYPE_CHECKING, List, Optional

from bs4 import element

from finance_clue.dartscrap.dart_scrap_dto import SupplyAgreementDto
from finance_clue.dartscrap.table_parser import parse_html_table
from finance_clue.dartscrap.utils import str_to_float
from finance_clue.dartscrap.utils import str_to_int

if TYPE_CHECKING:
    from finance_clue.dartscrap import DartScrap


@dataclass
class ContractDetailsDto:
    """
    2. 계약 내역

    Attributes:
        contract_amount: 계약금액
        recent_revenue: 최근 매출액
        revenue_ratio: 매출액 대비(%)
    """

    contract_amount: int
    recent_revenue: int
    revenue_ratio: float


def extract_contract_details(table_info) -> ContractDetailsDto:
    d = list(filter(lambda x: "계약내역" in x[0], table_info[:7]))

    return ContractDetailsDto(
        contract_amount=str_to_int(
            next(filter(lambda x: x[1].startswith("계약금액"), d))[2]
        ),
        recent_revenue=str_to_int(
            next(filter(lambda x: x[1].endswith("매출액(원)"), d))[2]
        ),
        revenue_ratio=str_to_float(
            next(filter(lambda x: x[1].startswith("매출액"), d))[2]
        ),
    )


class SupplyAgreementParser:
    """단일판매 공급계약 체결 공시 페이지 파싱 클래스"""

    def __init__(self, dart_scrap: "DartScrap"):
        self.dart_scrap = dart_scrap

    def parse_supply_agreement(self, report_no: str) -> SupplyAgreementDto:
        """
        단일판매 공급계약 체결 공시 페이지 파싱
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
        else:
            d = None

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
            table_info = parse_html_table(table, 4)

        invest_judgment_note = None
        # 계약 내역
        contract_details = extract_contract_details(table_info)
        # 계약 상대
        contractual_partner = next(
            filter(lambda x: "3. 계약상대" in x[0], table_info[4:])
        )[2]

        supply_area = next(
            filter(lambda x: x[0].startswith("4. 판매"), table_info[6:])
        )[2]
        contract_durations = filter(
            lambda x: x[0].startswith("5. 계약기간"), table_info[6:]
        )
        # assert len(list(contract_durations)) == 2
        contract_condition = next(
            filter(lambda x: x[0].startswith("6. 주요 계약조건"), table_info[6:])
        )[2]
        contract_date = next(filter(lambda x: "계약(수주)일" in x[0], table_info[6:]))[
            2
        ]

        for i, v in enumerate(table_info[12:]):
            if "투자판단" in v[0]:
                invest_judgment_note = table_info[i + 1 + 13][0]
                break

        return SupplyAgreementDto(
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
                correction_table_info[5] if correction_table_info is not None else None
            ),
            correction_note2=(
                correction_table_info[6]
                if correction_table_info is not None and len(correction_table_info) > 6
                else None
            ),
            contract_name=table_info[0][2],
            contract_name_detail=(
                table_info[1][2] if table_info[1][0].startswith("- 세부내용") else None
            ),
            contract_amount=contract_details.contract_amount,
            recent_revenue=contract_details.recent_revenue,
            revenue_ratio=contract_details.revenue_ratio,
            contractual_partner=contractual_partner,
            supply_area=supply_area,
            contract_start_date=next(contract_durations)[2],
            contract_end_date=next(contract_durations)[2],
            contract_condition=contract_condition,
            contract_date=contract_date,
            invest_judgment_note=invest_judgment_note,
        )
