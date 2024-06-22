import unittest

import pytest
import responses

from finance_clue.openkis import OpenKisClient


class OpenKisFinancialTestCase(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def setup(self, mock_openkis_client: OpenKisClient, mock_openkis_client_url: str):
        self.openkis_client = mock_openkis_client
        self.openkis_client_url = mock_openkis_client_url

    @responses.activate
    def test_balance_sheet(self):
        expected = {
            "output": [
                {
                    "stac_yymm": "202403",
                    "cras": "2085443.00",
                    "fxas": "2623555.00",
                    "total_aset": "4708998.00",
                    "flow_lblt": "817704.00",
                    "fix_lblt": "172133.00",
                    "total_lblt": "989837.00",
                    "cpfn": "8975",
                    "cfp_surp": "99.99",
                    "prfi_surp": "99.99",
                    "total_cptl": "3719161.00",
                }
            ],
            "rt_cd": "0",
            "msg_cd": "MCA00000",
            "msg1": "정상처리 되었습니다.",
        }

        responses.add(
            responses.GET,
            f"{self.openkis_client_url}/uapi/domestic-stock/v1/finance/balance-sheet",
            json=expected,
            status=200,
        )

        resp = self.openkis_client.get_financial_balance_sheet(
            fid_div_cls_code="0", fid_input_iscd="005930"
        )

        assert resp == expected

    @responses.activate
    def test_income_statement(self):
        expected = {
            "output": [
                {
                    "stac_yymm": "202403",
                    "sale_account": "719156.00",
                    "sale_cost": "458863.00",
                    "sale_totl_prfi": "260293",
                    "depr_cost": "99.99",
                    "sell_mang": "99.99",
                    "bsop_prti": "66060.00",
                    "bsop_non_ernn": "99.99",
                    "bsop_non_expn": "99.99",
                    "op_prfi": "77067.00",
                    "spec_prfi": "99.99",
                    "spec_loss": "99.99",
                    "thtr_ntin": "67547.00",
                }
            ],
            "rt_cd": "0",
            "msg_cd": "MCA00000",
            "msg1": "정상처리 되었습니다.",
        }

        responses.add(
            responses.GET,
            f"{self.openkis_client_url}/uapi/domestic-stock/v1/finance/income-statement",
            json=expected,
            status=200,
        )
        resp = self.openkis_client.get_financial_income_statement(
            fid_div_cls_code="1", fid_input_iscd="005930"
        )

        assert resp == expected

    @responses.activate
    def test_financial_ratio(self):
        expected = {
            "output": [
                {
                    "stac_yymm": "202403",
                    "grs": "12.8200",
                    "bsop_prfi_inrt": "931.9000",
                    "ntin_inrt": "328.9800",
                    "roe_val": "7.40",
                    "eps": "975.00",
                    "sps": "42349",
                    "bps": "53339.00",
                    "rsrv_rate": "40268.7400",
                    "lblt_rate": "26.6100",
                },
                {
                    "stac_yymm": "202312",
                    "grs": "-14.3300",
                    "bsop_prfi_inrt": "-84.8600",
                    "ntin_inrt": "-72.1700",
                    "roe_val": "4.14",
                    "eps": "2131.00",
                    "sps": "38120",
                    "bps": "52002.00",
                    "rsrv_rate": "39256.9100",
                    "lblt_rate": "25.3600",
                },
                {
                    "stac_yymm": "202309",
                    "grs": "-17.5200",
                    "bsop_prfi_inrt": "-90.4200",
                    "ntin_inrt": "-71.2600",
                    "roe_val": "3.22",
                    "eps": "1244.00",
                    "sps": "37522",
                    "bps": "52068.00",
                    "rsrv_rate": "39306.6500",
                    "lblt_rate": "24.8900",
                },
                {
                    "stac_yymm": "202306",
                    "grs": "-20.1500",
                    "bsop_prfi_inrt": "-95.3600",
                    "ntin_inrt": "-85.2900",
                    "roe_val": "1.70",
                    "eps": "434.00",
                    "sps": "36437",
                    "bps": "51385.00",
                    "rsrv_rate": "38789.9100",
                    "lblt_rate": "24.8000",
                },
                {
                    "stac_yymm": "202303",
                    "grs": "-18.0500",
                    "bsop_prfi_inrt": "-95.4700",
                    "ntin_inrt": "-86.1000",
                    "roe_val": "1.61",
                    "eps": "206.00",
                    "sps": "37538",
                    "bps": "51529.00",
                    "rsrv_rate": "38898.8300",
                    "lblt_rate": "26.2100",
                },
                {
                    "stac_yymm": "202212",
                    "grs": "8.0900",
                    "bsop_prfi_inrt": "-15.9900",
                    "ntin_inrt": "39.4600",
                    "roe_val": "17.07",
                    "eps": "8057.00",
                    "sps": "44494",
                    "bps": "50817.00",
                    "rsrv_rate": "38360.2500",
                    "lblt_rate": "26.4100",
                },
            ],
            "rt_cd": "0",
            "msg_cd": "MCA00000",
            "msg1": "정상처리 되었습니다.",
        }

        responses.add(
            responses.GET,
            f"{self.openkis_client_url}/uapi/domestic-stock/v1/finance/financial-ratio",
            json=expected,
            status=200,
        )
        resp = self.openkis_client.get_financial_ratio(
            fid_div_cls_code="1", fid_input_iscd="005930"
        )

        assert resp == expected

    @responses.activate
    def test_profit_ratio(self):
        expected = {
            "output": [
                {
                    "stac_yymm": "202403",
                    "cptl_ntin_rate": "5.83",
                    "self_cptl_ntin_inrt": "7.40",
                    "sale_ntin_rate": "9.39",
                    "sale_totl_rate": "36.19",
                },
                {
                    "stac_yymm": "202312",
                    "cptl_ntin_rate": "3.43",
                    "self_cptl_ntin_inrt": "4.14",
                    "sale_ntin_rate": "5.98",
                    "sale_totl_rate": "30.33",
                },
            ],
            "rt_cd": "0",
            "msg_cd": "MCA00000",
            "msg1": "정상처리 되었습니다.",
        }

        responses.add(
            responses.GET,
            f"{self.openkis_client_url}/uapi/domestic-stock/v1/finance/profit-ratio",
            json=expected,
            status=200,
        )
        resp = self.openkis_client.get_financial_profit_ratio(
            fid_div_cls_code="0", fid_input_iscd="005930"
        )
        assert resp == expected

    @responses.activate
    def test_other_major_ratio(self):
        expected = {
            "output": [
                {
                    "stac_yymm": "202403",
                    "payout_rate": "0.00",
                    "eva": "0.00",
                    "ebitda": "165568.00",
                    "ev_ebitda": "0.00",
                },
                {
                    "stac_yymm": "202312",
                    "payout_rate": "0.01",
                    "eva": "-123150.00",
                    "ebitda": "452335.00",
                    "ev_ebitda": "11.72",
                },
                {
                    "stac_yymm": "202212",
                    "payout_rate": "0.00",
                    "eva": "332465.00",
                    "ebitda": "824843.00",
                    "ev_ebitda": "4.62",
                },
                {
                    "stac_yymm": "202112",
                    "payout_rate": "0.00",
                    "eva": "256689.00",
                    "ebitda": "858812.00",
                    "ev_ebitda": "6.23",
                },
                {
                    "stac_yymm": "202012",
                    "payout_rate": "0.01",
                    "eva": "154774.00",
                    "ebitda": "663295.00",
                    "ev_ebitda": "8.33",
                },
            ],
            "rt_cd": "0",
            "msg_cd": "MCA00000",
            "msg1": "정상처리 되었습니다.",
        }

        responses.add(
            responses.GET,
            f"{self.openkis_client_url}/uapi/domestic-stock/v1/finance/other-major-ratios",
            json=expected,
            status=200,
        )
        resp = self.openkis_client.get_financial_other_major_ratio(
            fid_div_cls_code="0", fid_input_iscd="005930"
        )

        assert resp == expected

    @responses.activate
    def test_stability_ratio(self):
        expected = {
            "output": [
                {
                    "stac_yymm": "202403",
                    "lblt_rate": "26.61",
                    "bram_depn": "3.29",
                    "crnt_rate": "255.04",
                    "quck_rate": "0.00",
                },
                {
                    "stac_yymm": "202312",
                    "lblt_rate": "25.36",
                    "bram_depn": "2.78",
                    "crnt_rate": "258.77",
                    "quck_rate": "190.59",
                },
                {
                    "stac_yymm": "202212",
                    "lblt_rate": "26.41",
                    "bram_depn": "2.30",
                    "crnt_rate": "278.86",
                    "quck_rate": "212.24",
                },
            ],
            "rt_cd": "0",
            "msg_cd": "MCA00000",
            "msg1": "정상처리 되었습니다.",
        }

        responses.add(
            responses.GET,
            f"{self.openkis_client_url}/uapi/domestic-stock/v1/finance/stability-ratio",
            json=expected,
            status=200,
        )

        resp = self.openkis_client.get_financial_stability_ratio(
            fid_div_cls_code="0", fid_input_iscd="005930"
        )

        assert resp == expected

    @responses.activate
    def test_growth_ratio(self):
        expected = {
            "output": [
                {
                    "stac_yymm": "202403",
                    "grs": "12.8200",
                    "bsop_prfi_inrt": "931.9000",
                    "equt_inrt": "3.37",
                    "totl_aset_inrt": "3.70",
                },
                {
                    "stac_yymm": "202312",
                    "grs": "-14.3300",
                    "bsop_prfi_inrt": "-84.8600",
                    "equt_inrt": "2.52",
                    "totl_aset_inrt": "1.67",
                },
                {
                    "stac_yymm": "202212",
                    "grs": "8.0900",
                    "bsop_prfi_inrt": "-15.9900",
                    "equt_inrt": "16.35",
                    "totl_aset_inrt": "5.11",
                },
                {
                    "stac_yymm": "202112",
                    "grs": "18.0700",
                    "bsop_prfi_inrt": "43.4500",
                    "equt_inrt": "10.49",
                    "totl_aset_inrt": "12.79",
                },
            ],
            "rt_cd": "0",
            "msg_cd": "MCA00000",
            "msg1": "정상처리 되었습니다.",
        }

        responses.add(
            responses.GET,
            f"{self.openkis_client_url}/uapi/domestic-stock/v1/finance/growth-ratio",
            json=expected,
            status=200,
        )

        resp = self.openkis_client.get_financial_growth_ratio(
            fid_div_cls_code="0", fid_input_iscd="005930"
        )
        assert resp == expected

    @responses.activate
    def test_estimate_perform(self):
        expected = {
            "output1": {
                "sht_cd": "A005930",
                "item_kor_nm": "삼성전자",
                "name1": "채민숙",
                "name2": "",
                "estdate": "20240109",
                "rcmd_name": "매수",
                "capital": "8975.0",
                "forn_item_lmtrt": "0.00",
            },
            "output2": [
                {
                    "data1": "2796048.0",
                    "data2": "3022314.0",
                    "data3": "2581509.0",
                    "data4": "3048945.0",
                    "data5": "3295675.0",
                },
                {
                    "data1": "181.0",
                    "data2": "81.0",
                    "data3": "-146.0",
                    "data4": "181.0",
                    "data5": "81.0",
                },
                {
                    "data1": "516339.0",
                    "data2": "433766.0",
                    "data3": "65405.0",
                    "data4": "330172.0",
                    "data5": "555410.0",
                },
                {
                    "data1": "435.0",
                    "data2": "-160.0",
                    "data3": "-849.0",
                    "data4": "4048.0",
                    "data5": "682.0",
                },
                {
                    "data1": "392438.0",
                    "data2": "547300.0",
                    "data3": "106144.0",
                    "data4": "253332.0",
                    "data5": "422055.0",
                },
                {
                    "data1": "504.0",
                    "data2": "395.0",
                    "data3": "-806.0",
                    "data4": "1387.0",
                    "data5": "666.0",
                },
            ],
            "output3": [
                {
                    "data1": "858812.0",
                    "data2": "824843.0",
                    "data3": "483199.0",
                    "data4": "792602.0",
                    "data5": "1043367.0",
                },
                {
                    "data1": "57770.0",
                    "data2": "80570.0",
                    "data3": "15609.0",
                    "data4": "36983.0",
                    "data5": "61483.0",
                },
                {
                    "data1": "504.0",
                    "data2": "395.0",
                    "data3": "-806.0",
                    "data4": "1369.0",
                    "data5": "662.0",
                },
                {
                    "data1": "136.0",
                    "data2": "69.0",
                    "data3": "503.0",
                    "data4": "207.0",
                    "data5": "124.0",
                },
                {
                    "data1": "50.0",
                    "data2": "34.0",
                    "data3": "95.0",
                    "data4": "53.0",
                    "data5": "39.0",
                },
                {
                    "data1": "139.0",
                    "data2": "171.0",
                    "data3": "31.0",
                    "data4": "70.0",
                    "data5": "109.0",
                },
                {
                    "data1": "399.0",
                    "data2": "264.0",
                    "data3": "255.0",
                    "data4": "226.0",
                    "data5": "163.0",
                },
                {
                    "data1": "1197.0",
                    "data2": "568.0",
                    "data3": "58.0",
                    "data4": "232.0",
                    "data5": "655.0",
                },
            ],
            "output4": [
                {"dt": "2021.12"},
                {"dt": "2022.12"},
                {"dt": "2023.12E"},
                {"dt": "2024.12E"},
                {"dt": "2025.12E"},
            ],
            "rt_cd": "0",
            "msg_cd": "MCA00000",
            "msg1": "정상처리 되었습니다.",
        }

        responses.add(
            responses.GET,
            f"{self.openkis_client_url}/uapi/domestic-stock/v1/quotations/estimate-perform",
            json=expected,
            status=200,
        )
        resp = self.openkis_client.get_financial_estimate_perform(sht_cd="005930")

        assert resp == expected


if __name__ == "__main__":
    unittest.main()
