import os

from stock_clue.opendart.business_report_info_dto import (
    DirectorRemunerationInputDto,
)
from stock_clue.opendart.business_report_info_dto import (
    TotalStockQuantityInputDto,
)
from stock_clue.opendart.open_dart import OpenDart


class TestBusinessReportInfo:
    def test_get_director_remuneration(self):
        open_dart = OpenDart(os.environ["OPENDART_API_KEY"])
        params = DirectorRemunerationInputDto(
            corp_code="01029394",
            bsns_year="2020",
            reprt_code="11013",
        )
        results = open_dart.business_report_info.get_director_remuneration(
            params
        )

        assert results is not None
        assert len(list(filter(lambda x: x.corp_cls == "K", results))) == 2
        assert (
            len(
                list(
                    filter(
                        lambda x: x.gmtsck_confm_amount >= 100000000, results
                    )
                )
            )
            == 2
        )

    def test_total_stock(self):
        open_dart = OpenDart(os.environ["OPENDART_API_KEY"])
        params = TotalStockQuantityInputDto(
            corp_code="01029394",
            bsns_year="2020",
            reprt_code="11013",
        )
        results = open_dart.business_report_info.total_stock_quantity(params)

        assert results is not None
        assert len(results) == 4
