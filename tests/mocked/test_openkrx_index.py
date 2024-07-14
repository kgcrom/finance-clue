"""mocked test for OpenKrxClient"""

import unittest

import pytest
import responses

from finance_clue.openkrx import OpenKrxClient


class OpenKrxIndexTestCase(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def setup(self, mock_openkrx_client: OpenKrxClient, mock_openkrx_client_url: str):
        self.openkrx_client = mock_openkrx_client
        self.openkrx_client_url = mock_openkrx_client_url

    @responses.activate
    def test_krx_daily_index_quotation(self):
        expected = self._generate_expected("KRX")

        responses.add(
            responses.GET,
            f"{self.openkrx_client_url}/svc/apis/idx/krx_dd_trd",
            json=expected,
            status=200,
        )

        resp = self.openkrx_client.get_krx_daily_index(
            bas_dd="20240514",
        )

        assert resp == expected

    @responses.activate
    def test_kospi_daily_index(self):
        expected = self._generate_expected("KOSPI")

        responses.add(
            responses.GET,
            f"{self.openkrx_client_url}/svc/apis/idx/kospi_dd_trd",
            json=expected,
            status=200,
        )

        resp = self.openkrx_client.get_kospi_daily_index(
            bas_dd="20240514",
        )

        assert resp == expected

    @responses.activate
    def test_kosdaq_daily_index(self):
        expected = self._generate_expected("KOSDAQ")

        responses.add(
            responses.GET,
            f"{self.openkrx_client_url}/svc/apis/idx/kosdaq_dd_trd",
            json=expected,
            status=200,
        )

        resp = self.openkrx_client.get_kosdaq_daily_index(
            bas_dd="20240514",
        )

        assert resp == expected

    @responses.activate
    def test_bond_daily_index(self):
        expected = {
            "OutBlock_1": [
                {
                    "BAS_DD": "20200414",
                    "BND_IDX_GRP_NM": "KRX 채권지수",
                    "TOT_EARNG_IDX": "189.02",
                    "TOT_EARNG_IDX_CMPPREVDD": "0.03",
                    "NETPRC_IDX": "110.03",
                    "NETPRC_IDX_CMPPREVDD": "0.01",
                    "ZERO_REINVST_IDX": "183.02",
                    "ZERO_REINVST_IDX_CMPPREVDD": "0.03",
                    "CALL_REINVST_IDX": "186.33",
                    "CALL_REINVST_IDX_CMPPREVDD": "0.03",
                    "MKT_PRC_IDX": "111.86",
                    "MKT_PRC_IDX_CMPPREVDD": "0.02",
                    "AVG_DURATION": "5.670",
                    "AVG_CONVEXITY_PRC": "87.205",
                    "BND_IDX_AVG_YD": "1.338",
                }
            ]
        }

        responses.add(
            responses.GET,
            f"{self.openkrx_client_url}/svc/apis/idx/bon_dd_trd",
            json=expected,
            status=200,
        )

        resp = self.openkrx_client.get_bond_daily_index(
            bas_dd="20240514",
        )

        assert resp == expected

    @responses.activate
    def test_derivatives_daily_index(self):
        expected = {
            "OutBlock_1": [
                {
                    "BAS_DD": "20200414",
                    "IDX_CLSS": "선물지수",
                    "IDX_NM": "코스피 200 선물지수",
                    "CLSPRC_IDX": "1212.67",
                    "CMPPREVDD_IDX": "23.59",
                    "FLUC_RT": "1.98",
                    "OPNPRC_IDX": "1202.10",
                    "HGPRC_IDX": "1219.55",
                    "LWPRC_IDX": "1195.96",
                }
            ]
        }

        responses.add(
            responses.GET,
            f"{self.openkrx_client_url}/svc/apis/idx/drvprod_dd_trd",
            json=expected,
            status=200,
        )

        resp = self.openkrx_client.get_derivatives_daily_index(
            bas_dd="20240514",
        )

        assert resp == expected

    def _generate_expected(self, idx_class: str):
        return {
            "OutBlock_1": [
                {
                    "BAS_DD": "20200414",
                    "IDX_CLSS": idx_class,
                    "IDX_NM": "KTOP 30",
                    "CLSPRC_IDX": "6250.82",
                    "CMPPREVDD_IDX": "113.20",
                    "FLUC_RT": "1.84",
                    "OPNPRC_IDX": "6225.70",
                    "HGPRC_IDX": "6271.00",
                    "LWPRC_IDX": "6182.54",
                    "ACC_TRDVOL": "38188565",
                    "ACC_TRDVAL": "2722079713896",
                    "MKTCAP": "676169353869620",
                }
            ]
        }
