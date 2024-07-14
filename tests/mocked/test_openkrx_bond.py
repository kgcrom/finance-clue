import unittest

import pytest
import responses

from finance_clue.openkrx import OpenKrxClient


class OpenKrxBondTestCase(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def setup(self, mock_openkrx_client: OpenKrxClient, mock_openkrx_client_url: str):
        self.openkrx_client = mock_openkrx_client
        self.openkrx_client_url = mock_openkrx_client_url

    @responses.activate
    def test_kts_daily_trade(self):
        expected = {
            "OutBlock_1": [
                {
                    "BAS_DD": "20240514",
                    "MKT_NM": "국채전문유통시장",
                    "ISU_CD": "KR103503GE39",
                    "ISU_NM": "국고03250-2603(24-3)",
                    "BND_EXP_TP_NM": "2",
                    "GOVBND_ISU_TP_NM": "지표",
                    "CLSPRC": "10018.5",
                    "CMPPREVDD_PRC": "2.5",
                    "CLSPRC_YD": "3.478",
                    "OPNPRC": "10017.5",
                    "OPNPRC_YD": "3.484",
                    "HGPRC": "10019.5",
                    "HGPRC_YD": "3.473",
                    "LWPRC": "10016.5",
                    "LWPRC_YD": "3.490",
                    "ACC_TRDVOL": "95000000000",
                    "ACC_TRDVAL": "95172500000",
                }
            ]
        }

        responses.add(
            responses.GET,
            f"{self.openkrx_client_url}/svc/apis/bon/kts_bydd_trd",
            json=expected,
            status=200,
        )

        resp = self.openkrx_client.get_kts_daily_trade(bas_dd="20240514")

        assert resp == expected

    @responses.activate
    def test_bond_daily_trade(self):
        expected = {
            "OutBlock_1": [
                {
                    "BAS_DD": "20240514",
                    "MKT_NM": "일반채권시장",
                    "ISU_CD": "KR101501D967",
                    "ISU_NM": "국민주택1종19-06",
                    "CLSPRC": "10863.5",
                    "CMPPREVDD_PRC": "2.4",
                    "CLSPRC_YD": "3.046",
                    "OPNPRC": "10861.8",
                    "OPNPRC_YD": "3.168",
                    "HGPRC": "10863.5",
                    "HGPRC_YD": "3.046",
                    "LWPRC": "10861.8",
                    "LWPRC_YD": "3.168",
                    "ACC_TRDVOL": "17549000",
                    "ACC_TRDVAL": "19061516",
                }
            ]
        }

        responses.add(
            responses.GET,
            f"{self.openkrx_client_url}/svc/apis/bon/bnd_bydd_trd",
            json=expected,
            status=200,
        )

        resp = self.openkrx_client.get_bond_daily_trade(bas_dd="20240514")

        assert resp == expected

    @responses.activate
    def test_small_bond_daily_trade(self):
        expected = {
            "OutBlock_1": [
                {
                    "BAS_DD": "20240514",
                    "MKT_NM": "소액채권시장",
                    "ISU_CD": "KR101501DE46",
                    "ISU_NM": "국민주택1종24-04",
                    "CLSPRC": "8937.0",
                    "CMPPREVDD_PRC": "-5.0",
                    "CLSPRC_YD": "3.630",
                    "OPNPRC": "8943.0",
                    "OPNPRC_YD": "3.616",
                    "HGPRC": "8945.0",
                    "HGPRC_YD": "3.611",
                    "LWPRC": "8931.5",
                    "LWPRC_YD": "3.643",
                    "ACC_TRDVOL": "17968188000",
                    "ACC_TRDVAL": "16068916648",
                }
            ]
        }

        responses.add(
            responses.GET,
            f"{self.openkrx_client_url}/svc/apis/bon/smb_bydd_trd",
            json=expected,
            status=200,
        )

        resp = self.openkrx_client.get_small_bond_daily_trade(bas_dd="20240514")

        assert resp == expected
