import unittest

import pytest
import responses

from finance_clue.openkis import OpenKisClient


class MyTestCase(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def setup(self, mock_openkis_client: OpenKisClient, mock_openkis_client_url: str):
        self.openkis_client = mock_openkis_client
        self.openkis_client_url = mock_openkis_client_url

    @responses.activate
    def test_domestic_etf_price(self):
        expected = {
            "stck_prpr": "19020",
            "prdy_vrss_sign": "3",
            "prdy_vrss": "0",
            "prdy_ctrt": "0.00",
            "acml_vol": "0",
            "prdy_vol": "1733827",
            "stck_mxpr": "24725",
            "stck_llam": "13315",
            "stck_prdy_clpr": "19020",
            "stck_oprc": "0",
            "prdy_clpr_vrss_oprc_rate": "0.00",
            "stck_hgpr": "0",
            "prdy_clpr_vrss_hgpr_rate": "0.00",
            "stck_lwpr": "0",
            "prdy_clpr_vrss_lwpr_rate": "0.00",
            "prdy_last_nav": "19028.18",
            "nav": "19028.18",
            "nav_prdy_vrss": "0.00",
            "nav_prdy_vrss_sign": "3",
            "nav_prdy_ctrt": "0.00",
            "trc_errt": "0.44",
            "stck_sdpr": "19020",
            "stck_sspr": "14070",
            "etf_crcl_stcn": "62400000",
            "etf_ntas_ttam": "11873",
            "etf_frcr_ntas_ttam": "0",
            "frgn_limt_rate": "100.0000",
            "frgn_oder_able_qty": "62247678",
            "etf_cu_unit_scrt_cnt": "100000",
            "etf_cnfg_issu_cnt": "26",
            "etf_dvdn_cycl": "2",
            "crcd": "KRW",
            "etf_crcl_ntas_ttam": "0",
            "etf_frcr_crcl_ntas_ttam": "0",
            "etf_frcr_last_ntas_wrth_val": "0",
            "lp_oder_able_cls_code": "N",
            "stck_dryy_hgpr": "23523",
            "dryy_hgpr_vrss_prpr_rate": "-19.14",
            "dryy_hgpr_date": "20240102",
            "stck_dryy_lwpr": "17910",
            "dryy_lwpr_vrss_prpr_rate": "6.20",
            "dryy_lwpr_date": "20240530",
            "bstp_kor_isnm": "ETF(실물복제/수익증권)",
            "vi_cls_code": "N",
            "lstn_stcn": "62400000",
            "frgn_hldn_qty": "152322",
            "frgn_hldn_qty_rate": "0.24",
            "etf_trc_ert_mltp": "1.00",
            "dprt": "-0.04",
            "mbcr_name": "삼성자산운용(ETF)",
            "stck_lstn_date": "20180912",
            "mtrt_date": "0",
            "shrg_type_code": "  ",
            "lp_hldn_rate": "0.00",
            "etf_trgt_nmix_bstp_code": "9999",
            "etf_div_name": "수익증권형",
            "etf_rprs_bstp_kor_isnm": "FnGuide 2차전지 산업 지수",
            "lp_hldn_vol": "0",
        }

        responses.add(
            responses.GET,
            f"{self.openkis_client_url}/uapi/etfetn/v1/quotations/inquire-price",
            json=expected,
            status=200,
        )

        resp = self.openkis_client.get_etf_n_etn_price(fid_input_iscd="305720")

        assert resp == expected

    @responses.activate
    def test_domestic_etf_nav_comparison_trend(self):
        expected = {
            "output1": {
                "stck_prpr": "19020",
                "prdy_vrss": "0",
                "prdy_vrss_sign": "3",
                "prdy_ctrt": "0.00",
                "acml_vol": "0",
                "acml_tr_pbmn": "0",
                "stck_prdy_clpr": "19020",
                "stck_oprc": "0",
                "stck_hgpr": "0",
                "stck_lwpr": "0",
                "stck_mxpr": "24725",
                "stck_llam": "13315",
            },
            "output2": {
                "nav": "19028.18",
                "nav_prdy_vrss_sign": "3",
                "nav_prdy_vrss": "0.00",
                "nav_prdy_ctrt": "0.00",
                "prdy_clpr_nav": "19028.18",
                "oprc_nav": "0.00",
                "hprc_nav": "0.00",
                "lprc_nav": "0.00",
            },
            "rt_cd": "0",
            "msg_cd": "MCA00000",
            "msg1": "정상처리 되었습니다.",
        }

        responses.add(
            responses.GET,
            f"{self.openkis_client_url}/uapi/etfetn/v1/quotations/nav-comparison-trend",
            json=expected,
            status=200,
        )
        resp = self.openkis_client.get_etf_n_etn_nav_comparison_trend(
            fid_input_iscd="305720"
        )

        assert resp == expected

    @responses.activate
    def test_domestic_etf_nav_comparison_minute_trend(self):
        expected = {
            "output": [
                {
                    "bsop_hour": "153000",
                    "nav": "37922.77",
                    "nav_prdy_vrss_sign": "2",
                    "nav_prdy_vrss": "389.11",
                    "nav_prdy_ctrt": "1.03",
                    "nav_vrss_prpr": "-77.77",
                    "dprt": "-0.21",
                    "stck_prpr": "37845",
                    "prdy_vrss": "395",
                    "prdy_vrss_sign": "2",
                    "prdy_ctrt": "1.05",
                    "acml_vol": "2806771",
                    "cntg_vol": "46085",
                }
            ],
            "rt_cd": "0",
            "msg_cd": "MCA00000",
            "msg1": "정상처리 되었습니다.",
        }

        responses.add(
            responses.GET,
            f"{self.openkis_client_url}/uapi/etfetn/v1/quotations/nav-comparison-time-trend",
            json=expected,
            status=200,
        )
        resp = self.openkis_client.get_etf_n_etn_nav_minute_trend(
            fid_input_iscd="069500", fid_hour_cls_code="60"
        )
        assert resp == expected

    @responses.activate
    def test_domestic_etf_nav_comparison_daily_trend(self):
        expected = {
            "output": [
                {
                    "stck_bsop_date": "20210615",
                    "stck_clpr": "40751",
                    "prdy_vrss": "94",
                    "prdy_vrss_sign": "2",
                    "prdy_ctrt": "0.23",
                    "acml_vol": "3267790",
                    "cntg_vol": "",
                    "dprt": "-0.22",
                    "nav_vrss_prpr": "-2671.04",
                    "nav": "43422.04",
                    "nav_prdy_vrss_sign": "2",
                    "nav_prdy_vrss": "90.07",
                    "nav_prdy_ctrt": "0.21",
                },
                {
                    "stck_bsop_date": "20210614",
                    "stck_clpr": "40657",
                    "prdy_vrss": "-18",
                    "prdy_vrss_sign": "5",
                    "prdy_ctrt": "-0.05",
                    "acml_vol": "3292736",
                    "cntg_vol": "",
                    "dprt": "-0.25",
                    "nav_vrss_prpr": "-2674.97",
                    "nav": "43331.97",
                    "nav_prdy_vrss_sign": "2",
                    "nav_prdy_vrss": "44.59",
                    "nav_prdy_ctrt": "0.10",
                },
            ],
            "rt_cd": "0",
            "msg_cd": "MCA00000",
            "msg1": "정상처리 되었습니다.",
        }

        responses.add(
            responses.GET,
            f"{self.openkis_client_url}/uapi/etfetn/v1/quotations/nav-comparison-daily-trend",
            json=expected,
            status=200,
        )

        resp = self.openkis_client.get_etf_n_etn_nav_daily_trend(
            fid_input_iscd="069500",
            fid_input_date1="20210601",
            fid_input_date2="20210615",
        )

        assert resp == expected

    @responses.activate
    def test_domestic_etf_component_stock_price(self):
        expected = {
            "output1": {
                "stck_prpr": "37845",
                "prdy_vrss": "395",
                "prdy_vrss_sign": "2",
                "prdy_ctrt": "1.05",
                "etf_cnfg_issu_avls": "189514",
                "nav": "37922.77",
                "nav_prdy_vrss_sign": "2",
                "nav_prdy_vrss": "389.11",
                "nav_prdy_ctrt": "1.04",
                "etf_ntas_ttam": "61724",
                "prdy_clpr_nav": "37533.66",
                "oprc_nav": "37586.69",
                "hprc_nav": "38022.14",
                "lprc_nav": "37586.69",
                "etf_cu_unit_scrt_cnt": "50000",
                "etf_cnfg_issu_cnt": "201",
            },
            "output2": [
                {
                    "stck_shrn_iscd": "005930",
                    "hts_kor_isnm": "삼성전자",
                    "stck_prpr": "79800",
                    "prdy_vrss": "1700",
                    "prdy_vrss_sign": "2",
                    "prdy_ctrt": "2.18",
                    "acml_vol": "18207598",
                    "acml_tr_pbmn": "1451893499146",
                    "tday_rsfl_rate": "2.05",
                    "prdy_vrss_vol": "2084547",
                    "tr_pbmn_tnrt": "0.30",
                    "hts_avls": "4763886",
                    "etf_cnfg_issu_avls": "570011400",
                    "etf_cnfg_issu_rlim": "30.08",
                    "etf_vltn_amt": "557868300",
                }
            ],
            "rt_cd": "0",
            "msg_cd": "MCA00000",
            "msg1": "정상처리 되었습니다.",
        }

        responses.add(
            responses.GET,
            f"{self.openkis_client_url}/uapi/etfetn/v1/quotations/inquire-component-stock-price",
            json=expected,
            status=200,
        )
        resp = self.openkis_client.get_etf_n_etn_component_stock_price(
            fid_input_iscd="069500"
        )

        assert resp == expected


if __name__ == "__main__":
    unittest.main()
