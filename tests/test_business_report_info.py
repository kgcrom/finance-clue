import os

from stock_clue.opendart.business_report_info_dto import (
    DirectorRemunerationAmountInputDto,
)
from stock_clue.opendart.business_report_info_dto import (
    DirectorRemunerationApprovalInputDto,
)
from stock_clue.opendart.business_report_info_dto import (
    TotalStockQuantityInputDto,
)
from stock_clue.opendart.business_report_info_dto import AuditOpinionInputDto
from stock_clue.opendart.open_dart import OpenDart


class TestBusinessReportInfo:
    def test_get_director_remuneration_approval(self):
        """
        이사·감사 전체의 보수현황(주주총회 승인금액) 조회 테스트
        """
        open_dart = OpenDart(os.environ["OPENDART_API_KEY"])
        params = DirectorRemunerationApprovalInputDto(
            corp_code="01029394",
            bsns_year="2020",
            reprt_code="11013",
        )
        result = (
            open_dart.business_report_info.get_director_remuneration_approval(
                params
            )
        )

        assert result is not None
        assert result.status == "000"
        assert len(list(filter(lambda x: x.corp_cls == "K", result.list))) == 2
        assert (
            len(
                list(
                    filter(
                        lambda x: x.gmtsck_confm_amount >= 100000000,
                        result.list,
                    )
                )
            )
            == 2
        )

    def test_get_director_remuneration_amount(self):
        open_dart = OpenDart(os.environ["OPENDART_API_KEY"])
        params = DirectorRemunerationAmountInputDto(
            corp_code="01029394",
            bsns_year="2020",
            reprt_code="11013",
        )
        result = (
            open_dart.business_report_info.get_director_remuneration_amount(
                params
            )
        )

        assert result is not None
        assert result.status == "000"
        assert len(result.list) != 0

    def test_total_stock(self):
        """
        주식의 총수 현황 조회 테스트
        """
        open_dart = OpenDart(os.environ["OPENDART_API_KEY"])
        params = TotalStockQuantityInputDto(
            corp_code="01029394",
            bsns_year="2020",
            reprt_code="11013",
        )
        result = open_dart.business_report_info.total_stock_quantity(params)

        assert result is not None
        assert len(result.list) == 4

    def test_audit_opinion(self):
        """
        회계감사인의 명칭 및 감사의견 조회 테스트
        """
        open_dart = OpenDart(os.environ["OPENDART_API_KEY"])
        params = AuditOpinionInputDto(
            corp_code="01029394",
            bsns_year="2020",
            reprt_code="11013",
        )

        result = open_dart.business_report_info.audit_opinion(params)

        assert result is not None
