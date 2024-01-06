import os

from stock_clue.opendart import OpenDart
from stock_clue.opendart.base_dto import BaseListDto
from stock_clue.opendart.financial_info import FinancialInfo
from stock_clue.opendart.financial_info_dto import MajorAccountCompanyOutputDto
from stock_clue.opendart.financial_info_dto import XbrlTaxanomyOutputDto


class TestFinancialInfo:
    def test_get_major_account_single_company(self):
        financial_info = FinancialInfo(OpenDart(os.environ["OPENDART_API_KEY"]))
        result = financial_info.get_major_account_single_company(
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
        financial_info = FinancialInfo(OpenDart(os.environ["OPENDART_API_KEY"]))

        result = financial_info.get_major_account_multiple_company(
            corp_code="01029394",
            bsns_year="2020",
            reprt_code="11011",
        )
        assert result.status == "000"
        assert result.message == "정상"
        assert len(result.list) > 0
        assert isinstance(result.list[0], MajorAccountCompanyOutputDto)

    def test_get_whole_account_single_company(self):
        financial_info = FinancialInfo(OpenDart(os.environ["OPENDART_API_KEY"]))

        result = financial_info.get_whole_account_single_company(
            corp_code="00126380",
            bsns_year="2020",
            reprt_code="11011",
            fs_div="CFS",
        )
        assert result.status == "000"
        assert result.message == "정상"
        assert len(result.list) > 0

    def test_get_xbrl_taxanomy(self):
        financial_info = FinancialInfo(OpenDart(os.environ["OPENDART_API_KEY"]))

        result = financial_info.get_xbrl_taxanomy(
            sj_div="BS1",
        )
        assert result.status == "000"
        assert result.message == "정상"
        assert len(result.list) > 0
        assert isinstance(result.list[0], XbrlTaxanomyOutputDto)

    def test_download_xbrl(self):
        financial_info = FinancialInfo(OpenDart(os.environ["OPENDART_API_KEY"]))

        financial_info.download_xbrl(
            rcept_no="20230814000595",
            reprt_code="11012",
            file_path="./",
        )
