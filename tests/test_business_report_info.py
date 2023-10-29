import os
from typing import List

from stock_clue.opendart.business_report_info_dto import (
    DirectorRemunerationInputDto,
)
from stock_clue.opendart.business_report_info_dto import (
    DirectorRemunerationOutputDto,
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
        results: List[
            DirectorRemunerationOutputDto
        ] = open_dart.business_report_info.get_director_remuneration(params)

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
