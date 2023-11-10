import os

from stock_clue.opendart.base_dto import BaseListDto
from stock_clue.opendart.financial_info_dto import MajorAccountCompanyOutputDto
from stock_clue.opendart.open_dart import OpenDart


class TestFinancialInfo:
    def test_get_major_account_single_company(self):
        open_dart = OpenDart(os.environ["OPENDART_API_KEY"])
        result = open_dart.financial_info.get_major_account_single_company(
            corp_code="01029394",
            bsns_year="2020",
            reprt_code="11011",
        )
        assert result is not None
        assert isinstance(result, BaseListDto)
        assert result.status == "000"
        assert result.message == "정상"
        assert len(result.list) != 0
        assert isinstance(result.list[0], MajorAccountCompanyOutputDto)

    def test_get_major_account_multiple_company(self):
        open_dart = OpenDart(os.environ["OPENDART_API_KEY"])

        result = open_dart.financial_info.get_major_account_multiple_company(
            corp_code="01029394",
            bsns_year="2020",
            reprt_code="11011",
        )
        assert result.status == "000"
        assert result.message == "정상"
        assert len(result.list) > 0
        assert isinstance(result.list[0], MajorAccountCompanyOutputDto)
