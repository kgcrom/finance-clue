import unittest

import pytest

from finance_clue.openkis import OpenKisClient
from finance_clue.openkis import attach_headers


@pytest.mark.usefixtures("integration_openkis_client")
class MyTestCase(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def setup(self, integration_openkis_client: OpenKisClient):
        self.openkis_client = integration_openkis_client

    def test_index_price(self):
        resp = self.openkis_client.get_index_price(fid_input_iscd="0001")

        example = {
            "output": {
                "bstp_nmix_prpr": "2807.63",
                "bstp_nmix_prdy_vrss": "10.30",
                "prdy_vrss_sign": "2",
                "bstp_nmix_prdy_ctrt": "0.37",
                "acml_vol": "758166",
                "prdy_vol": "646706",
                "acml_tr_pbmn": "13576970",
                "prdy_tr_pbmn": "14069564",
                "bstp_nmix_oprc": "2802.10",
                "prdy_nmix_vrss_nmix_oprc": "4.77",
                "oprc_vrss_prpr_sign": "2",
                "bstp_nmix_oprc_prdy_ctrt": "0.17",
                "bstp_nmix_hgpr": "2812.62",
                "prdy_nmix_vrss_nmix_hgpr": "15.29",
                "hgpr_vrss_prpr_sign": "2",
                "bstp_nmix_hgpr_prdy_ctrt": "0.55",
                "bstp_nmix_lwpr": "2796.37",
                "prdy_clpr_vrss_lwpr": "-0.96",
                "lwpr_vrss_prpr_sign": "5",
                "prdy_clpr_vrss_lwpr_rate": "-0.03",
                "ascn_issu_cnt": "499",
                "uplm_issu_cnt": "4",
                "stnr_issu_cnt": "62",
                "down_issu_cnt": "371",
                "lslm_issu_cnt": "0",
                "dryy_bstp_nmix_hgpr": "2812.62",
                "dryy_hgpr_vrss_prpr_rate": "0.18",
                "dryy_bstp_nmix_hgpr_date": "20240620",
                "dryy_bstp_nmix_lwpr": "2429.12",
                "dryy_lwpr_vrss_prpr_rate": "-15.58",
                "dryy_bstp_nmix_lwpr_date": "20240118",
                "total_askp_rsqn": "21349106",
                "total_bidp_rsqn": "33251530",
                "seln_rsqn_rate": "39.10",
                "shnu_rsqn_rate": "60.90",
                "ntby_rsqn": "11902424",
            },
            "rt_cd": "0",
            "msg_cd": "MCA00000",
            "msg1": "정상처리 되었습니다.",
        }
        assert resp is not None

    def test_daily_index_price(self):
        resp = self.openkis_client.get_index_daily_price(
            fid_input_iscd="0001", fid_period_div_code="D", fid_input_date1="20240620"
        )
        example = {
            "output1": {
                "bstp_nmix_prpr": "2807.63",
                "bstp_nmix_prdy_vrss": "10.30",
                "prdy_vrss_sign": "2",
                "bstp_nmix_prdy_ctrt": "0.37",
                "acml_vol": "758166",
                "acml_tr_pbmn": "13576970",
                "bstp_nmix_oprc": "2802.10",
                "bstp_nmix_hgpr": "2812.62",
                "bstp_nmix_lwpr": "2796.37",
                "prdy_vol": "646706",
                "ascn_issu_cnt": "499",
                "down_issu_cnt": "371",
                "stnr_issu_cnt": "62",
                "uplm_issu_cnt": "4",
                "lslm_issu_cnt": "0",
                "prdy_tr_pbmn": "14069564",
                "dryy_bstp_nmix_hgpr_date": "20240620",
                "dryy_bstp_nmix_hgpr": "2812.62",
                "dryy_bstp_nmix_lwpr": "2429.12",
                "dryy_bstp_nmix_lwpr_date": "20240118",
            },
            "output2": [
                {
                    "stck_bsop_date": "20240620",
                    "bstp_nmix_prpr": "2807.63",
                    "prdy_vrss_sign": "2",
                    "bstp_nmix_prdy_vrss": "10.30",
                    "bstp_nmix_prdy_ctrt": "0.37",
                    "bstp_nmix_oprc": "2802.10",
                    "bstp_nmix_hgpr": "2812.62",
                    "bstp_nmix_lwpr": "2796.37",
                    "acml_vol_rlim": "100.00",
                    "acml_vol": "758166",
                    "acml_tr_pbmn": "13576970",
                    "invt_new_psdg": "61.12",
                    "d20_dsrt": "103.37",
                }
            ],
            "rt_cd": "0",
            "msg_cd": "MCA00000",
            "msg1": "정상처리 되었습니다.",
        }
        assert resp is not None

    def test_category_price(self):
        resp = self.openkis_client.get_index_category_price(
            fid_mrkt_cls_code="K", fid_blng_cls_code="0", fid_input_iscd="0001"
        )

        example = {
            "output1": {
                "bstp_nmix_prpr": "2807.63",
                "bstp_nmix_prdy_vrss": "10.30",
                "prdy_vrss_sign": "2",
                "bstp_nmix_prdy_ctrt": "0.37",
                "acml_vol": "758166",
                "acml_tr_pbmn": "13576970",
                "bstp_nmix_oprc": "2802.10",
                "bstp_nmix_hgpr": "2812.62",
                "bstp_nmix_lwpr": "2796.37",
                "prdy_vol": "646706",
                "ascn_issu_cnt": "499",
                "down_issu_cnt": "371",
                "stnr_issu_cnt": "62",
                "uplm_issu_cnt": "4",
                "lslm_issu_cnt": "0",
                "prdy_tr_pbmn": "14069564",
                "dryy_bstp_nmix_hgpr_date": "20240620",
                "dryy_bstp_nmix_hgpr": "2812.62",
                "dryy_bstp_nmix_lwpr": "2429.12",
                "dryy_bstp_nmix_lwpr_date": "20240118",
            },
            "output2": [
                {
                    "bstp_cls_code": "0001",
                    "hts_kor_isnm": "종합",
                    "bstp_nmix_prpr": "2807.63",
                    "bstp_nmix_prdy_vrss": "10.30",
                    "prdy_vrss_sign": "2",
                    "bstp_nmix_prdy_ctrt": "0.37",
                    "acml_vol": "758166",
                    "acml_tr_pbmn": "13576970",
                    "acml_vol_rlim": "100.00",
                    "acml_tr_pbmn_rlim": "",
                }
            ],
            "rt_cd": "0",
            "msg_cd": "MCA00000",
            "msg1": "정상처리 되었습니다.",
        }
        assert resp is not None

    def test_total_expected_conclusion(self):
        resp = self.openkis_client.get_index_total_exp(
            fid_mrkt_cls_code="O", fid_input_iscd="0001", fid_mkop_cls_code="1"
        )

        example = {
            "output1": {
                "bstp_nmix_prpr": "2800.06",
                "bstp_nmix_prdy_vrss": "2.73",
                "prdy_vrss_sign": "2",
                "prdy_ctrt": "0.10",
                "acml_vol": "6238",
                "ascn_issu_cnt": "383",
                "down_issu_cnt": "283",
                "stnr_issu_cnt": "221",
            },
            "output2": [
                {
                    "bstp_cls_code": "0001",
                    "hts_kor_isnm": "종합",
                    "bstp_nmix_prpr": "2800.06",
                    "bstp_nmix_prdy_vrss": "2.73",
                    "prdy_vrss_sign": "2",
                    "bstp_nmix_prdy_ctrt": "0.10",
                    "acml_vol": "6238",
                    "nmix_sdpr": "2797.33",
                    "ascn_issu_cnt": "383",
                    "stnr_issu_cnt": "221",
                    "down_issu_cnt": "283",
                }
            ],
            "rt_cd": "0",
            "msg_cd": "MCA00000",
            "msg1": "정상처리 되었습니다.",
        }
        assert resp is not None

    def test_tick_index_price(self):
        resp = self.openkis_client.get_index_tick_price(
            fid_input_iscd="0001", fid_input_hour1="60"
        )

        example = {
            "output": [
                {
                    "stck_cntg_hour": "999999",
                    "bstp_nmix_prpr": "2807.63",
                    "bstp_nmix_prdy_vrss": "10.30",
                    "prdy_vrss_sign": "2",
                    "bstp_nmix_prdy_ctrt": "0.37",
                    "acml_tr_pbmn": "13576970",
                    "acml_vol": "758166",
                    "cntg_vol": "12982",
                },
                {
                    "stck_cntg_hour": "888888",
                    "bstp_nmix_prpr": "2807.63",
                    "bstp_nmix_prdy_vrss": "10.30",
                    "prdy_vrss_sign": "2",
                    "bstp_nmix_prdy_ctrt": "0.37",
                    "acml_tr_pbmn": "13280842",
                    "acml_vol": "745184",
                    "cntg_vol": "153",
                },
            ],
            "rt_cd": "0",
            "msg_cd": "MCA00000",
            "msg1": "정상처리 되었습니다.",
        }
        assert resp is not None

    def test_minute_index_price(self):
        resp = self.openkis_client.get_index_minute_price(
            fid_input_iscd="0001", fid_input_hour1="60"
        )

        example = {
            "output": [
                {
                    "bsop_hour": "999999",
                    "bstp_nmix_prpr": "2807.63",
                    "bstp_nmix_prdy_vrss": "10.30",
                    "prdy_vrss_sign": "2",
                    "bstp_nmix_prdy_ctrt": "0.37",
                    "acml_tr_pbmn": "13576970",
                    "acml_vol": "758166",
                    "cntg_vol": "12982",
                },
                {
                    "bsop_hour": "888888",
                    "bstp_nmix_prpr": "2807.63",
                    "bstp_nmix_prdy_vrss": "10.30",
                    "prdy_vrss_sign": "2",
                    "bstp_nmix_prdy_ctrt": "0.37",
                    "acml_tr_pbmn": "13280842",
                    "acml_vol": "745184",
                    "cntg_vol": "153",
                },
            ],
            "rt_cd": "0",
            "msg_cd": "MCA00000",
            "msg1": "정상처리 되었습니다.",
        }
        assert resp is not None

    def test_expected_conclusion_index_trend(self):
        resp = self.openkis_client.get_index_expected_conclusion_trend(
            fid_mkop_cls_code="1", fid_input_hour1="60", fid_input_iscd="0001"
        )

        example = {
            "output": [
                {
                    "stck_cntg_hour": "666666",
                    "bstp_nmix_prpr": "2800.06",
                    "prdy_vrss_sign": "2",
                    "bstp_nmix_prdy_vrss": "2.73",
                    "prdy_ctrt": "0.10",
                    "acml_vol": "6238",
                    "acml_tr_pbmn": "164313",
                }
            ],
            "rt_cd": "0",
            "msg_cd": "MCA00000",
            "msg1": "정상처리 되었습니다.",
        }
        assert resp is not None

    def test_interest(self):
        resp = self.openkis_client.get_index_interest(
            fid_div_cls_code="1", fid_input_iscd="0001"
        )

        example = {
            "output1": [
                {
                    "bcdt_code": "Y0201",
                    "hts_kor_isnm": "미국 30년T-BOND",
                    "bond_mnrt_prpr": "4.3600",
                    "prdy_vrss_sign": "5",
                    "bond_mnrt_prdy_vrss": "-0.0400",
                    "prdy_ctrt": "-0.91",
                    "stck_bsop_date": "20240618",
                }
            ],
            "output2": [
                {
                    "bcdt_code": "Y0101",
                    "hts_kor_isnm": "국고채 3년",
                    "bond_mnrt_prpr": "3.1960",
                    "prdy_vrss_sign": "2",
                    "bond_mnrt_prdy_vrss": "0.0340",
                    "bstp_nmix_prdy_ctrt": "1.08",
                    "stck_bsop_date": "20240620",
                }
            ],
            "rt_cd": "0",
            "msg_cd": "MCA00000",
            "msg1": "정상처리 되었습니다.",
        }
        assert resp is not None

    def test_news_title(self):
        resp = self.openkis_client.get_index_news_title(
            fid_input_date1="20240620", fid_input_hour1="110100"
        )
        example = {
            "output": [
                {
                    "cntt_usiq_srno": "2024062011005138887",
                    "news_ofer_entp_code": "6",
                    "data_dt": "20240620",
                    "data_tm": "110051",
                    "hts_pbnt_titl_cntt": "서스틴베스트, 상반기 기업 ESG 성과평가…1위 네이버",
                    "news_lrdv_code": "02",
                    "dorg": "연합뉴스",
                    "iscd1": "010130",
                    "iscd2": "",
                    "iscd3": "",
                    "iscd4": "",
                    "iscd5": "",
                    "iscd6": "",
                    "iscd7": "",
                    "iscd8": "",
                    "iscd9": "",
                    "iscd10": "",
                    "kor_isnm1": "고려아연",
                    "kor_isnm2": "",
                    "kor_isnm3": "",
                    "kor_isnm4": "",
                    "kor_isnm5": "",
                    "kor_isnm6": "",
                    "kor_isnm7": "",
                    "kor_isnm8": "",
                    "kor_isnm9": "",
                    "kor_isnm10": "",
                }
            ],
            "rt_cd": "0",
            "msg_cd": "MCA00000",
            "msg1": "정상처리 되었습니다.",
        }
        assert resp is not None


if __name__ == "__main__":
    unittest.main()
