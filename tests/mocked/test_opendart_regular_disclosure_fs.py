import unittest

import pytest
import responses

from finance_clue.opendart import OpenDartClient


class RegularDisclosureFsCase(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def setup(
        self, mock_opendart_client: OpenDartClient, mock_opendart_client_url: str
    ):
        self.opendart_client = mock_opendart_client
        self.opendart_client_url = mock_opendart_client_url

    @responses.activate
    def test_single_financial_account(self):
        expected = {
            "status": "000",
            "message": "정상",
            "list": [
                {
                    "rcept_no": "20210309000744",
                    "reprt_code": "11011",
                    "bsns_year": "2020",
                    "corp_code": "00126380",
                    "stock_code": "005930",
                    "fs_div": "CFS",
                    "fs_nm": "연결재무제표",
                    "sj_div": "BS",
                    "sj_nm": "재무상태표",
                    "account_nm": "유동자산",
                    "thstrm_nm": "제 52 기",
                    "thstrm_dt": "2020.12.31 현재",
                    "thstrm_amount": "198,215,579,000,000",
                    "frmtrm_nm": "제 51 기",
                    "frmtrm_dt": "2019.12.31 현재",
                    "frmtrm_amount": "181,385,260,000,000",
                    "bfefrmtrm_nm": "제 50 기",
                    "bfefrmtrm_dt": "2018.12.31 현재",
                    "bfefrmtrm_amount": "174,697,424,000,000",
                    "ord": "1",
                    "currency": "KRW",
                }
            ],
        }

        responses.add(
            responses.GET,
            f"{self.opendart_client_url}/api/fnlttSinglAcnt.json",
            json=expected,
            status=200,
        )
        resp = self.opendart_client.get_single_financial_account(
            corp_code="00126380",
            bsns_year="2020",
            reprt_code="11011",
        )
        assert resp == expected

    @responses.activate
    def test_multi_financial_account(self):
        expected = {
            "status": "000",
            "message": "정상",
            "list": [
                {
                    "rcept_no": "20210309000744",
                    "reprt_code": "11011",
                    "bsns_year": "2020",
                    "corp_code": "00126380",
                    "stock_code": "005930",
                    "fs_div": "CFS",
                    "fs_nm": "연결재무제표",
                    "sj_div": "BS",
                    "sj_nm": "재무상태표",
                    "account_nm": "유동자산",
                    "thstrm_nm": "제 52 기",
                    "thstrm_dt": "2020.12.31 현재",
                    "thstrm_amount": "198,215,579,000,000",
                    "frmtrm_nm": "제 51 기",
                    "frmtrm_dt": "2019.12.31 현재",
                    "frmtrm_amount": "181,385,260,000,000",
                    "bfefrmtrm_nm": "제 50 기",
                    "bfefrmtrm_dt": "2018.12.31 현재",
                    "bfefrmtrm_amount": "174,697,424,000,000",
                    "ord": "1",
                    "currency": "KRW",
                },
                {
                    "rcept_no": "20210309000744",
                    "reprt_code": "11011",
                    "bsns_year": "2020",
                    "corp_code": "00126380",
                    "stock_code": "005930",
                    "fs_div": "CFS",
                    "fs_nm": "연결재무제표",
                    "sj_div": "BS",
                    "sj_nm": "재무상태표",
                    "account_nm": "비유동자산",
                    "thstrm_nm": "제 52 기",
                    "thstrm_dt": "2020.12.31 현재",
                    "thstrm_amount": "180,020,139,000,000",
                    "frmtrm_nm": "제 51 기",
                    "frmtrm_dt": "2019.12.31 현재",
                    "frmtrm_amount": "171,179,237,000,000",
                    "bfefrmtrm_nm": "제 50 기",
                    "bfefrmtrm_dt": "2018.12.31 현재",
                    "bfefrmtrm_amount": "164,659,820,000,000",
                    "ord": "3",
                    "currency": "KRW",
                },
            ],
        }

        responses.add(
            responses.GET,
            f"{self.opendart_client_url}/api/fnlttMultiAcnt.json",
            json=expected,
            status=200,
        )
        resp = self.opendart_client.get_multi_financial_account(
            corp_code="00126380",
            bsns_year="2020",
            reprt_code="11011",
        )
        assert resp is not None

    @responses.activate
    def test_single_financial_account_all(self):
        expected = {
            "status": "000",
            "message": "정상",
            "list": [
                {
                    "rcept_no": "20210309000744",
                    "reprt_code": "11011",
                    "bsns_year": "2020",
                    "corp_code": "00126380",
                    "sj_div": "BS",
                    "sj_nm": "재무상태표",
                    "account_id": "ifrs-full_CurrentAssets",
                    "account_nm": "유동자산",
                    "account_detail": "-",
                    "thstrm_nm": "제 52 기",
                    "thstrm_amount": "198215579000000",
                    "frmtrm_nm": "제 51 기",
                    "frmtrm_amount": "181385260000000",
                    "bfefrmtrm_nm": "제 50 기",
                    "bfefrmtrm_amount": "174697424000000",
                    "ord": "1",
                    "currency": "KRW",
                }
            ],
        }

        responses.add(
            responses.GET,
            f"{self.opendart_client_url}/api/fnlttSinglAcntAll.json",
            json=expected,
            status=200,
        )
        resp = self.opendart_client.get_single_financial_account_all(
            corp_code="00126380",
            bsns_year="2020",
            reprt_code="11011",
            fs_div="CFS",
        )
        assert resp is not None

    @responses.activate
    def test_xbrl_taxonomy(self):
        expected = {
            "status": "000",
            "message": "정상",
            "list": [
                {
                    "sj_div": "BS1",
                    "bsns_de": "20180701",
                    "account_id": "ifrs_StatementOfFinancialPositionAbstract",
                    "account_nm": "StatementOfFinancialPositionAbstract",
                    "label_kor": "재무상태표 [abstract]",
                    "label_eng": "Statement of financial position [abstract]",
                    "ifrs_ref": " ",
                },
                {
                    "sj_div": "BS1",
                    "bsns_de": "20180701",
                    "account_id": "ifrs_AssetsAbstract",
                    "account_nm": "AssetsAbstract",
                    "label_kor": "자산 [abstract]",
                    "label_eng": "Assets [abstract]",
                    "ifrs_ref": " ",
                },
            ],
        }

        responses.add(
            responses.GET,
            f"{self.opendart_client_url}/api/xbrlTaxonomy.json",
            json=expected,
            status=200,
        )
        resp = self.opendart_client.get_xbrl_taxonomy(
            sj_div="BS1",
        )
        assert resp is not None

    @responses.activate
    def test_single_financial_index(self):
        expected = {
            "status": "000",
            "message": "정상",
            "list": [
                {
                    "reprt_code": "11014",
                    "bsns_year": "2023",
                    "corp_code": "00164742",
                    "stock_code": "005380",
                    "idx_cl_code": "M210000",
                    "idx_cl_nm": "수익성지표",
                    "idx_code": "M211100",
                    "idx_nm": "세전계속사업이익률",
                }
            ],
        }

        responses.add(
            responses.GET,
            f"{self.opendart_client_url}/api/fnlttSinglIndx.json",
            json=expected,
            status=200,
        )
        resp = self.opendart_client.get_single_financial_index(
            corp_code="00164742",
            bsns_year="2023",
            reprt_code="11014",
            idx_cl_code="M210000",
        )
        assert resp is not None

    @responses.activate
    def test_multi_financial_index(self):
        expected = {
            "status": "000",
            "message": "정상",
            "list": [
                {
                    "reprt_code": "11014",
                    "bsns_year": "2023",
                    "corp_code": "00164742",
                    "stock_code": "005380",
                    "idx_cl_code": "M210000",
                    "idx_cl_nm": "수익성지표",
                    "idx_code": "M211100",
                    "idx_nm": "세전계속사업이익률",
                }
            ],
        }

        responses.add(
            responses.GET,
            f"{self.opendart_client_url}/api/fnlttCmpnyIndx.json",
            json=expected,
            status=200,
        )
        resp = self.opendart_client.get_multi_financial_index(
            corp_code="00164742",
            bsns_year="2023",
            reprt_code="11014",
            idx_cl_code="M210000",
        )
        assert resp is not None
