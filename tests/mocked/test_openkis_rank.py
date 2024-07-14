import unittest

import pytest
import responses

from finance_clue.openkis import OpenKisClient


class RankTestCase(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def setup(self, mock_openkis_client: OpenKisClient, mock_openkis_client_url: str):
        self.openkis_client = mock_openkis_client
        self.openkis_client_url = mock_openkis_client_url

    @responses.activate
    def test_volume_rank(self):
        expected = {
            "output": [
                {
                    "hts_kor_isnm": "KODEX 레버리지",
                    "mksc_shrn_iscd": "122630",
                    "data_rank": "2",
                    "stck_prpr": "20245",
                    "prdy_vrss_sign": "5",
                    "prdy_vrss": "-310",
                    "prdy_ctrt": "-1.51",
                    "acml_vol": "12429212",
                    "prdy_vol": "10230019",
                    "lstn_stcn": "106450000",
                    "avrg_vol": "3884",
                    "n_befr_clpr_vrss_prpr_rate": "0.00",
                    "vol_inrt": "9999.99",
                    "vol_tnrt": "11.68",
                    "nday_vol_tnrt": "73859.23",
                    "avrg_tr_pbmn": "54102317",
                    "tr_pbmn_tnrt": "11.65",
                    "nday_tr_pbmn_tnrt": "50813.18",
                    "acml_tr_pbmn": "251128667105",
                },
                {
                    "hts_kor_isnm": "미래산업",
                    "mksc_shrn_iscd": "025560",
                    "data_rank": "3",
                    "stck_prpr": "2100",
                    "prdy_vrss_sign": "5",
                    "prdy_vrss": "-260",
                    "prdy_ctrt": "-11.02",
                    "acml_vol": "2742115",
                    "prdy_vol": "19416876",
                    "lstn_stcn": "30429770",
                    "avrg_vol": "3729",
                    "n_befr_clpr_vrss_prpr_rate": "0.00",
                    "vol_inrt": "9999.99",
                    "vol_tnrt": "9.01",
                    "nday_vol_tnrt": "248097.92",
                    "avrg_tr_pbmn": "2575026",
                    "tr_pbmn_tnrt": "9.40",
                    "nday_tr_pbmn_tnrt": "81561.98",
                    "acml_tr_pbmn": "6009555145",
                },
            ],
            "rt_cd": "0",
            "msg_cd": "MCA00000",
            "msg1": "정상처리 되었습니다.",
        }

        responses.add(
            responses.GET,
            f"{self.openkis_client_url}/uapi/domestic-stock/v1/quotations/volume-rank",
            json=expected,
            status=200,
        )
        resp = self.openkis_client.get_ranking_volume(
            fid_input_iscd="0000",
            fid_div_cls_code="0",
            fid_blng_cls_code="0",
            fid_trgt_cls_code="111111111",
            fid_trgt_exls_cls_code="0000000000",
            fid_input_price1="1000",
            fid_input_price2="100000",
            fid_vol_cnt="",
            fid_input_date1="20240624",
        )
        assert resp == expected

    @responses.activate
    def test_rank_fluctuation_rate(self):
        expected = {
            "output": [
                {
                    "stck_shrn_iscd": "323280",
                    "data_rank": "1",
                    "hts_kor_isnm": "태성",
                    "stck_prpr": "12700",
                    "prdy_vrss": "70",
                    "prdy_vrss_sign": "2",
                    "prdy_ctrt": "0.55",
                    "acml_vol": "808418",
                    "stck_hgpr": "13830",
                    "hgpr_hour": "000000",
                    "acml_hgpr_date": "20240620",
                    "stck_lwpr": "5340",
                    "lwpr_hour": "000000",
                    "acml_lwpr_date": "20240524",
                    "lwpr_vrss_prpr_rate": "137.83",
                    "dsgt_date_clpr_vrss_prpr_rate": "128.83",
                    "cnnt_ascn_dynu": "2",
                    "hgpr_vrss_prpr_rate": "-8.17",
                    "cnnt_down_dynu": "0",
                    "oprc_vrss_prpr_sign": "2",
                    "oprc_vrss_prpr": "0",
                    "oprc_vrss_prpr_rate": "0.00",
                    "prd_rsfl": "0",
                    "prd_rsfl_rate": "0.00",
                }
            ],
            "rt_cd": "0",
            "msg_cd": "MCA00000",
            "msg1": "정상처리 되었습니다.",
        }

        responses.add(
            responses.GET,
            f"{self.openkis_client_url}/uapi/domestic-stock/v1/ranking/fluctuation",
            json=expected,
            status=200,
        )

        resp = self.openkis_client.get_ranking_fluctuation_rate(
            fid_input_iscd="0000",
            fid_rank_sort_cls_code="0",
            fid_prc_cls_code="0",
            fid_input_price1="",
            fid_input_price2="",
            fid_vol_cnt="",
            fid_rsfl_rate1="",
            fid_rsfl_rate2="",
            fid_input_cnt1="20",
        )

        assert resp == expected

    @responses.activate
    def test_profit_asset_index(self):
        expected = {
            "output": [
                {
                    "data_rank": "1",
                    "hts_kor_isnm": "삼성전자",
                    "mksc_shrn_iscd": "005930",
                    "stck_prpr": "80600",
                    "prdy_vrss": "600",
                    "prdy_vrss_sign": "2",
                    "prdy_ctrt": "0.75",
                    "acml_vol": "15454227",
                    "sale_totl_prfi": "785469.00",
                    "bsop_prti": "65670.00",
                    "op_prfi": "110063.00",
                    "thtr_ntin": "154871.00",
                    "total_aset": "4559060.00",
                    "total_lblt": "922281.00",
                    "total_cptl": "3636779.00",
                    "stac_month": "12",
                    "stac_month_cls_code": "0",
                    "iqry_csnu": "1762",
                },
                {
                    "data_rank": "30",
                    "hts_kor_isnm": "코리안리",
                    "mksc_shrn_iscd": "003690",
                    "stck_prpr": "7840",
                    "prdy_vrss": "-60",
                    "prdy_vrss_sign": "5",
                    "prdy_ctrt": "-0.76",
                    "acml_vol": "228769",
                    "sale_totl_prfi": "53385.00",
                    "bsop_prti": "3637.00",
                    "op_prfi": "3614.00",
                    "thtr_ntin": "2839.00",
                    "total_aset": "120663.00",
                    "total_lblt": "88134.00",
                    "total_cptl": "32529.00",
                    "stac_month": "12",
                    "stac_month_cls_code": "0",
                    "iqry_csnu": "1762",
                },
            ],
            "rt_cd": "0",
            "msg_cd": "MCA00000",
            "msg1": "정상처리 되었습니다.",
        }

        responses.add(
            responses.GET,
            f"{self.openkis_client_url}/uapi/domestic-stock/v1/ranking/profit-asset-index",
            json=expected,
            status=200,
        )
        resp = self.openkis_client.get_ranking_profit_asset_index(
            fid_input_iscd="0000",
            fid_input_price1="3000",
            fid_input_price2="",
            fid_vol_cnt="",
            fid_input_option1="2023",
            fid_input_option2="3",
            fid_rank_sort_cls_code="0",
        )
        assert resp == expected

    @responses.activate
    def test_market_cap(self):
        expected = {
            "output": [
                {
                    "mksc_shrn_iscd": "005930",
                    "data_rank": "1",
                    "hts_kor_isnm": "삼성전자",
                    "stck_prpr": "80600",
                    "prdy_vrss": "600",
                    "prdy_vrss_sign": "2",
                    "prdy_ctrt": "0.75",
                    "acml_vol": "15454227",
                    "lstn_stcn": "5969782550",
                    "stck_avls": "4811645",
                    "mrkt_whol_avls_rlim": "16.98",
                },
                {
                    "mksc_shrn_iscd": "000660",
                    "data_rank": "2",
                    "hts_kor_isnm": "SK하이닉스",
                    "stck_prpr": "223000",
                    "prdy_vrss": "-11000",
                    "prdy_vrss_sign": "5",
                    "prdy_ctrt": "-4.70",
                    "acml_vol": "5080726",
                    "lstn_stcn": "728002365",
                    "stck_avls": "1623445",
                    "mrkt_whol_avls_rlim": "5.73",
                },
            ],
            "rt_cd": "0",
            "msg_cd": "MCA00000",
            "msg1": "정상처리 되었습니다.",
        }

        responses.add(
            responses.GET,
            f"{self.openkis_client_url}/uapi/domestic-stock/v1/ranking/market-cap",
            json=expected,
            status=200,
        )

        resp = self.openkis_client.get_ranking_market_cap(
            fid_div_cls_code="0",
            fid_input_iscd="0000",
            fid_input_price1="",
            fid_input_price2="",
            fid_vol_cnt="10000",
        )
        assert resp == expected

    @responses.activate
    def test_financial_ratio(self):
        expected = {
            "output": [
                {
                    "data_rank": "1",
                    "hts_kor_isnm": "한진칼",
                    "mksc_shrn_iscd": "180640",
                    "stck_prpr": "66700",
                    "prdy_vrss": "-2800",
                    "prdy_vrss_sign": "5",
                    "prdy_ctrt": "-4.03",
                    "acml_vol": "40276",
                    "cptl_op_prfi": "140.84",
                    "cptl_ntin_rate": "10.09",
                    "sale_totl_rate": "40.03",
                    "sale_ntin_rate": "140.84",
                    "bis": "75.40",
                    "lblt_rate": "32.62",
                    "bram_depn": "16.28",
                    "rsrv_rate": "1541.21",
                    "grs": "37.63",
                    "op_prfi_inrt": "2.29",
                    "bsop_prfi_inrt": "195.73",
                    "ntin_inrt": "-41.12",
                    "equt_inrt": "10.78",
                    "cptl_tnrt": "0.10",
                    "sale_bond_tnrt": "10.72",
                    "totl_aset_inrt": "-3.32",
                    "stac_month": "12",
                    "stac_month_cls_code": "0",
                    "iqry_csnu": "935",
                },
                {
                    "data_rank": "30",
                    "hts_kor_isnm": "스톤브릿지벤처스",
                    "mksc_shrn_iscd": "330730",
                    "stck_prpr": "3920",
                    "prdy_vrss": "-55",
                    "prdy_vrss_sign": "5",
                    "prdy_ctrt": "-1.38",
                    "acml_vol": "39473",
                    "cptl_op_prfi": "32.56",
                    "cptl_ntin_rate": "6.30",
                    "sale_totl_rate": "87.21",
                    "sale_ntin_rate": "32.56",
                    "bis": "90.32",
                    "lblt_rate": "10.72",
                    "bram_depn": "0.00",
                    "rsrv_rate": "922.64",
                    "grs": "-35.76",
                    "op_prfi_inrt": "-17.37",
                    "bsop_prfi_inrt": "-17.28",
                    "ntin_inrt": "-13.35",
                    "equt_inrt": "3.46",
                    "cptl_tnrt": "0.22",
                    "sale_bond_tnrt": "0.00",
                    "totl_aset_inrt": "0.27",
                    "stac_month": "12",
                    "stac_month_cls_code": "0",
                    "iqry_csnu": "935",
                },
            ],
            "rt_cd": "0",
            "msg_cd": "MCA00000",
            "msg1": "정상처리 되었습니다.",
        }
        responses.add(
            responses.GET,
            f"{self.openkis_client_url}/uapi/domestic-stock/v1/ranking/finance-ratio",
            json=expected,
            status=200,
        )
        resp = self.openkis_client.get_ranking_financial_ratio(
            fid_input_iscd="0000",
            fid_input_price1="3000",
            fid_input_price2="120000",
            fid_vol_cnt="",
            fid_input_option1="2023",
            fid_input_option2="3",
            fid_rank_sort_cls_code="7",
        )
        assert resp == expected

    @responses.activate
    def test_prefer_disparate_ratio(self):
        expected = {
            "output": [
                {
                    "mksc_shrn_iscd": "336370",
                    "data_rank": "1",
                    "hts_kor_isnm": "솔루스첨단소재",
                    "stck_prpr": "16040",
                    "prdy_vrss": "-70",
                    "prdy_vrss_sign": "5",
                    "acml_vol": "157763",
                    "prst_iscd": "A33637K",
                    "prst_kor_isnm": "솔루스첨단소재1우",
                    "prst_prpr": "3035",
                    "prst_prdy_vrss": "-50",
                    "prst_prdy_vrss_sign": "5",
                    "prst_acml_vol": "33591",
                    "diff_prpr": "13005",
                    "dprt": "81.08",
                    "prdy_ctrt": "-0.43",
                    "prst_prdy_ctrt": "-1.62",
                }
            ],
            "rt_cd": "0",
            "msg_cd": "MCA00000",
            "msg1": "정상처리 되었습니다.",
        }
        responses.add(
            responses.GET,
            f"{self.openkis_client_url}/uapi/domestic-stock/v1/ranking/prefer-disparate-ratio",
            json=expected,
            status=200,
        )
        resp = self.openkis_client.get_ranking_prefer_disparate_ratio(
            fid_input_iscd="0000",
            fid_vol_cnt="",
            fid_input_price1="",
            fid_input_price2="",
        )
        assert resp == expected

    @responses.activate
    def test_quote_balance(self):
        expected = {
            "output": [
                {
                    "mksc_shrn_iscd": "Q530036",
                    "data_rank": "1",
                    "hts_kor_isnm": "삼성 인버스 2X WTI원유 선물 ETN",
                    "stck_prpr": "90",
                    "prdy_vrss": "1",
                    "prdy_vrss_sign": "2",
                    "prdy_ctrt": "1.12",
                    "acml_vol": "9166008",
                    "total_askp_rsqn": "38341265",
                    "total_bidp_rsqn": "84175817",
                    "total_ntsl_bidp_rsqn": "45834552",
                    "shnu_rsqn_rate": "68.71",
                    "seln_rsqn_rate": "31.29",
                },
                {
                    "mksc_shrn_iscd": "Q500027",
                    "data_rank": "2",
                    "hts_kor_isnm": "신한 인버스 2X WTI원유 선물 ETN(H)",
                    "stck_prpr": "76",
                    "prdy_vrss": "2",
                    "prdy_vrss_sign": "2",
                    "prdy_ctrt": "2.70",
                    "acml_vol": "1878757",
                    "total_askp_rsqn": "58970591",
                    "total_bidp_rsqn": "77725188",
                    "total_ntsl_bidp_rsqn": "18754597",
                    "shnu_rsqn_rate": "56.86",
                    "seln_rsqn_rate": "43.14",
                },
            ],
            "rt_cd": "0",
            "msg_cd": "MCA00000",
            "msg1": "정상처리 되었습니다.",
        }
        responses.add(
            responses.GET,
            f"{self.openkis_client_url}/uapi/domestic-stock/v1/ranking/quote-balance",
            json=expected,
            status=200,
        )
        resp = self.openkis_client.get_ranking_quote_balance(
            fid_vol_cnt="",
            fid_input_iscd="0000",
            fid_rank_sort_cls_code="0",
            fid_input_price1="",
            fid_input_price2="",
        )
        assert resp == expected

    @responses.activate
    def test_disparity(self):
        expected = {
            "output": [
                {
                    "mksc_shrn_iscd": "064090",
                    "data_rank": "1",
                    "hts_kor_isnm": "웨스트라이즈",
                    "stck_prpr": "6480",
                    "prdy_vrss": "1170",
                    "prdy_ctrt": "22.03",
                    "prdy_vrss_sign": "2",
                    "acml_vol": "2023407",
                    "d5_dsrt": "120.04",
                    "d10_dsrt": "149.21",
                    "d20_dsrt": "177.79",
                    "d60_dsrt": "198.34",
                    "d120_dsrt": "230.08",
                },
                {
                    "mksc_shrn_iscd": "101930",
                    "data_rank": "2",
                    "hts_kor_isnm": "인화정공",
                    "stck_prpr": "24300",
                    "prdy_vrss": "3600",
                    "prdy_ctrt": "17.39",
                    "prdy_vrss_sign": "2",
                    "acml_vol": "1049316",
                    "d5_dsrt": "120.98",
                    "d10_dsrt": "144.78",
                    "d20_dsrt": "163.45",
                    "d60_dsrt": "181.76",
                    "d120_dsrt": "197.30",
                },
            ],
            "rt_cd": "0",
            "msg_cd": "MCA00000",
            "msg1": "정상처리 되었습니다.",
        }
        responses.add(
            responses.GET,
            f"{self.openkis_client_url}/uapi/domestic-stock/v1/ranking/disparity",
            json=expected,
            status=200,
        )
        resp = self.openkis_client.get_ranking_disparity(
            fid_div_cls_code="0",
            fid_rank_sort_cls_code="0",
            fid_hour_cls_code="20",
            fid_input_iscd="0000",
            fid_input_price1="",
            fid_input_price2="",
            fid_vol_cnt="",
        )
        assert resp == expected

    @responses.activate
    def test_market_value(self):
        expected = {
            "output": [
                {
                    "data_rank": "1",
                    "hts_kor_isnm": "효성",
                    "mksc_shrn_iscd": "004800",
                    "stck_prpr": "57200",
                    "prdy_vrss": "-600",
                    "prdy_vrss_sign": "5",
                    "prdy_ctrt": "-1.04",
                    "acml_vol": "27304",
                    "per": "19066.67",
                    "pbr": "0.48",
                    "pcr": "11.08",
                    "psr": "0.35",
                    "eps": "300",
                    "eva": "-812.00",
                    "ebitda": "2031.00",
                    "pv_div_ebitda": "12.98",
                    "ebitda_div_fnnc_expn": "0.02",
                    "stac_month": "12",
                    "stac_month_cls_code": "0",
                    "iqry_csnu": "1703",
                }
            ],
            "rt_cd": "0",
            "msg_cd": "MCA00000",
            "msg1": "정상처리 되었습니다.",
        }
        responses.add(
            responses.GET,
            f"{self.openkis_client_url}/uapi/domestic-stock/v1/ranking/market-value",
            json=expected,
            status=200,
        )
        resp = self.openkis_client.get_ranking_market_value(
            fid_input_iscd="0000",
            fid_div_cls_code="0",
            fid_input_price1="",
            fid_input_price2="",
            fid_vol_cnt="",
            fid_input_option1="2023",
            fid_input_option2="3",
            fid_rank_sort_cls_code="23",
        )
        assert resp == expected

    @responses.activate
    def test_volume_power(self):
        expected = {
            "output": [
                {
                    "stck_shrn_iscd": "Q510035",
                    "data_rank": "1",
                    "hts_kor_isnm": "대신 3X 레버리지 국채10년 ETN",
                    "stck_prpr": "20955",
                    "prdy_vrss": "-15",
                    "prdy_vrss_sign": "5",
                    "prdy_ctrt": "-0.07",
                    "acml_vol": "2517",
                    "tday_rltv": "999.99",
                    "seln_cnqn_smtn": "0",
                    "shnu_cnqn_smtn": "2517",
                },
                {
                    "stck_shrn_iscd": "Q610063",
                    "data_rank": "2",
                    "hts_kor_isnm": "메리츠 KIS CD금리투자 ETN",
                    "stck_prpr": "52325",
                    "prdy_vrss": "5",
                    "prdy_vrss_sign": "2",
                    "prdy_ctrt": "0.01",
                    "acml_vol": "2000",
                    "tday_rltv": "999.99",
                    "seln_cnqn_smtn": "0",
                    "shnu_cnqn_smtn": "2000",
                },
            ],
            "rt_cd": "0",
            "msg_cd": "MCA00000",
            "msg1": "정상처리 되었습니다.",
        }

        responses.add(
            responses.GET,
            f"{self.openkis_client_url}/uapi/domestic-stock/v1/ranking/volume-power",
            json=expected,
            status=200,
        )
        resp = self.openkis_client.get_ranking_volume_power(
            fid_input_iscd="0000",
            fid_div_cls_code="0",
            fid_input_price1="",
            fid_input_price2="",
            fid_vol_cnt="",
        )
        assert resp == expected

    @responses.activate
    def test_top_interest_stock(self):
        expected = {
            "output": [
                {
                    "mrkt_div_cls_name": "코스피",
                    "mksc_shrn_iscd": "005930",
                    "hts_kor_isnm": "삼성전자",
                    "stck_prpr": "80600",
                    "prdy_vrss": "600",
                    "prdy_vrss_sign": "2",
                    "prdy_ctrt": "0.75",
                    "acml_vol": "15454227",
                    "acml_tr_pbmn": "1239803887850",
                    "askp": "80600",
                    "bidp": "80500",
                    "data_rank": "1",
                    "inter_issu_reg_csnu": "4775826",
                },
                {
                    "mrkt_div_cls_name": "코스피",
                    "mksc_shrn_iscd": "000660",
                    "hts_kor_isnm": "SK하이닉스",
                    "stck_prpr": "223000",
                    "prdy_vrss": "-11000",
                    "prdy_vrss_sign": "5",
                    "prdy_ctrt": "-4.70",
                    "acml_vol": "5080726",
                    "acml_tr_pbmn": "1136220620500",
                    "askp": "223500",
                    "bidp": "223000",
                    "data_rank": "2",
                    "inter_issu_reg_csnu": "1703526",
                },
            ],
            "rt_cd": "0",
            "msg_cd": "MCA00000",
            "msg1": "정상처리 되었습니다.",
        }
        responses.add(
            responses.GET,
            f"{self.openkis_client_url}/uapi/domestic-stock/v1/ranking/top-interest-stock",
            json=expected,
            status=200,
        )
        resp = self.openkis_client.get_ranking_top_interest_stock(
            fid_input_iscd="0000",
            fid_div_cls_code="0",
            fid_input_price1="",
            fid_input_price2="",
            fid_vol_cnt="",
            fid_input_cnt1="1",
        )
        assert resp == expected

    @responses.activate
    def test_expected_conclusion_up_down(self):
        expected = {
            "output": [
                {
                    "stck_shrn_iscd": "478440",
                    "hts_kor_isnm": "미래에셋비전스팩6호",
                    "stck_prpr": "3085",
                    "prdy_vrss": "1085",
                    "prdy_vrss_sign": "2",
                    "prdy_ctrt": "54.25",
                    "stck_sdpr": "2000",
                    "seln_rsqn": "147",
                    "askp": "3090",
                    "bidp": "3085",
                    "shnu_rsqn": "15332",
                    "cntg_vol": "2287817",
                    "antc_tr_pbmn": "261402894",
                    "total_askp_rsqn": "12873",
                    "total_bidp_rsqn": "260963",
                }
            ],
            "rt_cd": "0",
            "msg_cd": "MCA00000",
            "msg1": "정상처리 되었습니다.",
        }
        responses.add(
            responses.GET,
            f"{self.openkis_client_url}/uapi/domestic-stock/v1/ranking/exp-trans-updown",
            json=expected,
            status=200,
        )
        resp = self.openkis_client.get_ranking_expected_conclusion_up_down(
            fid_rank_sort_cls_code="0",
            fid_input_iscd="0000",
            fid_div_cls_code="1",
            fid_aply_rang_prc1="10000",
            fid_vol_cnt="",
            fid_pbmn="",
            fid_blng_cls_code="0",
            fid_mkop_cls_code="0",
        )
        assert resp == expected

    @responses.activate
    def test_trade_by_company(self):
        expected = {
            "output": [
                {
                    "data_rank": "1",
                    "mksc_shrn_iscd": "300640",
                    "hts_kor_isnm": "KBSTAR 게임테마",
                    "stck_prpr": "8805",
                    "prdy_vrss_sign": "5",
                    "prdy_vrss": "-175",
                    "prdy_ctrt": "-1.95",
                    "acml_vol": "52193",
                    "acml_tr_pbmn": "462581085",
                    "seln_cnqn_smtn": "5991402",
                    "shnu_cnqn_smtn": "1385180",
                    "ntby_cnqn": "-4606222",
                },
                {
                    "data_rank": "2",
                    "mksc_shrn_iscd": "099430",
                    "hts_kor_isnm": "바이오플러스",
                    "stck_prpr": "5050",
                    "prdy_vrss_sign": "5",
                    "prdy_vrss": "-30",
                    "prdy_ctrt": "-0.59",
                    "acml_vol": "470168",
                    "acml_tr_pbmn": "2339894360",
                    "seln_cnqn_smtn": "3522629",
                    "shnu_cnqn_smtn": "2144959",
                    "ntby_cnqn": "-1377670",
                },
                {
                    "data_rank": "3",
                    "mksc_shrn_iscd": "025320",
                    "hts_kor_isnm": "시노펙스",
                    "stck_prpr": "9800",
                    "prdy_vrss_sign": "5",
                    "prdy_vrss": "-220",
                    "prdy_ctrt": "-2.20",
                    "acml_vol": "1617124",
                    "acml_tr_pbmn": "15958697930",
                    "seln_cnqn_smtn": "25661140",
                    "shnu_cnqn_smtn": "24526494",
                    "ntby_cnqn": "-1134646",
                },
            ],
            "rt_cd": "0",
            "msg_cd": "MCA00000",
            "msg1": "정상처리 되었습니다.",
        }
        responses.add(
            responses.GET,
            f"{self.openkis_client_url}/uapi/domestic-stock/v1/ranking/traded-by-company",
            json=expected,
            status=200,
        )
        resp = self.openkis_client.get_ranking_trade_by_company(
            fid_div_cls_code="0",
            fid_rank_sort_cls_code="0",
            fid_input_date1="20240501",
            fid_input_date2="20240624",
            fid_input_iscd="0000",
            fid_aply_rang_vol="52194",
            fid_aply_rang_prc1="5000",
            fid_aply_rang_prc2="10000",
        )
        assert resp == expected

    @responses.activate
    def test_near_new_high_low(self):
        expected = {
            "output": [
                {
                    "hts_kor_isnm": "KOSEF 인도Nifty50(합성)",
                    "mksc_shrn_iscd": "200250",
                    "stck_prpr": "25345",
                    "prdy_vrss_sign": "2",
                    "prdy_vrss": "315",
                    "prdy_ctrt": "1.26",
                    "askp": "25345",
                    "askp_rsqn1": "1174",
                    "bidp": "25330",
                    "bidp_rsqn1": "478",
                    "acml_vol": "116278",
                    "new_hgpr": "25345",
                    "hprc_near_rate": "0.00",
                    "new_lwpr": "18995",
                    "lwpr_near_rate": "-25.05",
                    "stck_sdpr": "25030",
                }
            ],
            "rt_cd": "0",
            "msg_cd": "MCA00000",
            "msg1": "정상처리 되었습니다.",
        }
        responses.add(
            responses.GET,
            f"{self.openkis_client_url}/uapi/domestic-stock/v1/ranking/near-new-highlow",
            json=expected,
            status=200,
        )
        resp = self.openkis_client.get_ranking_near_new_high_low(
            fid_aply_rang_vol="3000",
            fid_div_cls_code="0",
            fid_input_cnt1="0.00",
            fid_input_cnt2="0.95",
            fid_prc_cls_code="0",
            fid_input_iscd="0000",
            fid_trgt_cls_code="2",
            fid_trgt_exls_cls_code="0",
            fid_aply_rang_prc1="1000",
            fid_aply_rang_prc2="100000",
        )
        assert resp == expected

    @responses.activate
    def test_bulk_trans_num(self):
        expected = {
            "output": [
                {
                    "mksc_shrn_iscd": "005420",
                    "data_rank": "1",
                    "hts_kor_isnm": "코스모화학",
                    "stck_prpr": "28000",
                    "prdy_vrss_sign": "5",
                    "prdy_vrss": "-50",
                    "prdy_ctrt": "-0.18",
                    "acml_vol": "86370",
                    "shnu_cntg_csnu": "39",
                    "seln_cntg_csnu": "39",
                    "ntby_cnqn": "0",
                },
                {
                    "mksc_shrn_iscd": "270810",
                    "data_rank": "2",
                    "hts_kor_isnm": "KBSTAR 코스닥150",
                    "stck_prpr": "13515",
                    "prdy_vrss_sign": "2",
                    "prdy_vrss": "35",
                    "prdy_ctrt": "0.26",
                    "acml_vol": "30585",
                    "shnu_cntg_csnu": "11",
                    "seln_cntg_csnu": "11",
                    "ntby_cnqn": "0",
                },
            ],
            "rt_cd": "0",
            "msg_cd": "MCA00000",
            "msg1": "정상처리 되었습니다.",
        }
        responses.add(
            responses.GET,
            f"{self.openkis_client_url}/uapi/domestic-stock/v1/ranking/bulk-trans-num",
            json=expected,
            status=200,
        )
        resp = self.openkis_client.get_ranking_bulk_trans_num(
            fid_aply_rang_prc1="10000",
            fid_aply_rang_prc2="100000",
            fid_input_iscd="0000",
            fid_rank_sort_cls_code="0",
            fid_div_cls_code="0",
            fid_input_price1="",
            fid_input_iscd2="",
            fid_trgt_cls_code="0",
            fid_trgt_exls_cls_code="0",
            fid_vol_cnt="",
        )
        assert resp == expected

    @responses.activate
    def test_short_sale(self):
        expected = {
            "output": [
                {
                    "mksc_shrn_iscd": "005930",
                    "hts_kor_isnm": "삼성전자",
                    "stck_prpr": "81300",
                    "prdy_vrss": "500",
                    "prdy_vrss_sign": "2",
                    "prdy_ctrt": "0.62",
                    "acml_vol": "297211074",
                    "acml_tr_pbmn": "23401356654068",
                    "ssts_cntg_qty": "1140742",
                    "ssts_vol_rlim": "0.38",
                    "ssts_tr_pbmn": "89937102700",
                    "ssts_tr_pbmn_rlim": "0.38",
                    "stnd_date1": "20240604",
                    "stnd_date2": "20240625",
                    "avrg_prc": "78840",
                },
                {
                    "mksc_shrn_iscd": "025320",
                    "hts_kor_isnm": "시노펙스",
                    "stck_prpr": "10960",
                    "prdy_vrss": "570",
                    "prdy_vrss_sign": "2",
                    "prdy_ctrt": "5.49",
                    "acml_vol": "136600711",
                    "acml_tr_pbmn": "1580802450140",
                    "ssts_cntg_qty": "1082704",
                    "ssts_vol_rlim": "0.79",
                    "ssts_tr_pbmn": "11619843010",
                    "ssts_tr_pbmn_rlim": "0.74",
                    "stnd_date1": "0",
                    "stnd_date2": "0",
                    "avrg_prc": "10732",
                },
            ],
            "rt_cd": "0",
            "msg_cd": "MCA00000",
            "msg1": "정상처리 되었습니다.",
        }
        responses.add(
            responses.GET,
            f"{self.openkis_client_url}/uapi/domestic-stock/v1/ranking/short-sale",
            json=expected,
            status=200,
        )
        resp = self.openkis_client.get_ranking_short_sale(
            fid_input_iscd="0000",
            fid_aply_rang_vol="1000",
            fid_period_div_code="D",
            fid_input_cnt1="14",
            fid_trgt_cls_code="0",
            fid_trgt_exls_cls_code="0",
            fid_aply_rang_prc1="1000",
            fid_aply_rang_prc2="100000",
        )
        assert resp == expected

    @responses.activate
    def test_credit_balance(self):
        expected = {
            "output1": [
                {
                    "bstp_cls_code": "1001",
                    "hts_kor_isnm": "종합",
                    "stnd_date1": "20240126",
                    "stnd_date2": "20240625",
                }
            ],
            "output2": [
                {
                    "mksc_shrn_iscd": "105740",
                    "hts_kor_isnm": "디케이락",
                    "stck_prpr": "9830",
                    "prdy_vrss": "-160",
                    "prdy_vrss_sign": "5",
                    "prdy_ctrt": "-1.60",
                    "acml_vol": "391065",
                    "whol_loan_rmnd_stcn": "944426",
                    "whol_loan_rmnd_amt": "883688",
                    "whol_loan_rmnd_rate": "9.29",
                    "whol_stln_rmnd_stcn": "0",
                    "whol_stln_rmnd_amt": "0",
                    "whol_stln_rmnd_rate": "0.00",
                    "nday_vrss_loan_rmnd_inrt": "3.63",
                    "nday_vrss_stln_rmnd_inrt": "0.00",
                }
            ],
            "rt_cd": "0",
            "msg_cd": "MCA00000",
            "msg1": "정상처리 되었습니다.",
        }
        responses.add(
            responses.GET,
            f"{self.openkis_client_url}/uapi/domestic-stock/v1/ranking/credit-balance",
            json=expected,
            status=200,
        )
        resp = self.openkis_client.get_ranking_credit_balance(
            fid_input_iscd="0000",
            fid_option="30",
            fid_rank_sort_cls_code="0",
        )
        assert resp == expected

    @responses.activate
    def test_dividend_rate(self):
        expected = {
            "output": [
                {
                    "rank": "2",
                    "sht_cd": "000810",
                    "isin_name": "삼성화재해상보험",
                    "record_date": "20240327",
                    "per_sto_divi_amt": "16000",
                    "divi_rate": "3200.00",
                    "divi_kind": "결산",
                },
                {
                    "rank": "3",
                    "sht_cd": "03473K",
                    "isin_name": "SK1우",
                    "record_date": "20240401",
                    "per_sto_divi_amt": "3550",
                    "divi_rate": "1775.00",
                    "divi_kind": "결산",
                },
            ],
            "rt_cd": "0",
            "msg_cd": "MCA00000",
            "msg1": "정상처리 되었습니다.",
        }

        responses.add(
            responses.GET,
            f"{self.openkis_client_url}/uapi/domestic-stock/v1/ranking/dividend-rate",
            json=expected,
            status=200,
        )
        resp = self.openkis_client.get_ranking_dividend_rate(
            upjong="002",
            gb1="0",
            gb2="0",
            gb3="2",
            gb4="0",
            f_dt="20240101",
            t_dt="20240620",
        )
        assert resp == expected

    @responses.activate
    def test_overtime_balance(self):
        expected = {
            "output": [
                {
                    "stck_shrn_iscd": "005930",
                    "data_rank": "1",
                    "hts_kor_isnm": "삼성전자",
                    "stck_prpr": "81300",
                    "prdy_vrss": "500",
                    "prdy_vrss_sign": "2",
                    "prdy_ctrt": "0.62",
                    "ovtm_total_askp_rsqn": "9674",
                    "ovtm_total_bidp_rsqn": "0",
                    "mkob_otcp_vol": "85854",
                    "mkfa_otcp_vol": "46143",
                },
                {
                    "stck_shrn_iscd": "005880",
                    "data_rank": "2",
                    "hts_kor_isnm": "대한해운",
                    "stck_prpr": "2470",
                    "prdy_vrss": "15",
                    "prdy_vrss_sign": "2",
                    "prdy_ctrt": "0.61",
                    "ovtm_total_askp_rsqn": "0",
                    "ovtm_total_bidp_rsqn": "8579",
                    "mkob_otcp_vol": "78421",
                    "mkfa_otcp_vol": "30717",
                },
                {
                    "stck_shrn_iscd": "001250",
                    "data_rank": "3",
                    "hts_kor_isnm": "GS글로벌",
                    "stck_prpr": "3945",
                    "prdy_vrss": "0",
                    "prdy_vrss_sign": "3",
                    "prdy_ctrt": "0.00",
                    "ovtm_total_askp_rsqn": "8882",
                    "ovtm_total_bidp_rsqn": "0",
                    "mkob_otcp_vol": "67080",
                    "mkfa_otcp_vol": "61210",
                },
            ],
            "rt_cd": "0",
            "msg_cd": "MCA00000",
            "msg1": "정상처리 되었습니다.",
        }
        responses.add(
            responses.GET,
            f"{self.openkis_client_url}/uapi/domestic-stock/v1/ranking/after-hour-balance",
            json=expected,
            status=200,
        )
        resp = self.openkis_client.get_ranking_overtime_balance(
            fid_rank_sort_cls_code="1",
            fid_input_iscd="0000",
            fid_input_price1="1000",
            fid_input_price2="100000",
            fid_vol_cnt="",
        )
        assert resp == expected

    @responses.activate
    def test_overtime_fluctuation_rate(self):
        expected = {
            "output1": {
                "ovtm_untp_uplm_issu_cnt": "4",
                "ovtm_untp_ascn_issu_cnt": "804",
                "ovtm_untp_stnr_issu_cnt": "747",
                "ovtm_untp_lslm_issu_cnt": "1",
                "ovtm_untp_down_issu_cnt": "830",
                "ovtm_untp_acml_vol": "19444288",
                "ovtm_untp_acml_tr_pbmn": "216809272912",
                "ovtm_untp_exch_vol": "9384600",
                "ovtm_untp_exch_tr_pbmn": "108985413417",
                "ovtm_untp_kosdaq_vol": "10059688",
                "ovtm_untp_kosdaq_tr_pbmn": "107823859495",
            },
            "output2": [
                {
                    "mksc_shrn_iscd": "298770",
                    "hts_kor_isnm": "KODEX 한국대만IT프리미어",
                    "ovtm_untp_prpr": "29295",
                    "ovtm_untp_prdy_vrss": "2660",
                    "ovtm_untp_prdy_vrss_sign": "1",
                    "ovtm_untp_prdy_ctrt": "9.99",
                    "ovtm_untp_askp1": "29290",
                    "ovtm_untp_seln_rsqn": "17",
                    "ovtm_untp_bidp1": "24000",
                    "ovtm_untp_shnu_rsqn": "17",
                    "ovtm_untp_vol": "4",
                    "ovtm_vrss_acml_vol_rlim": "0.03",
                    "stck_prpr": "26635",
                    "acml_vol": "14651",
                    "bidp": "26550",
                    "askp": "26635",
                }
            ],
            "rt_cd": "0",
            "msg_cd": "MCA00000",
            "msg1": "정상처리 되었습니다.",
        }

        responses.add(
            responses.GET,
            f"{self.openkis_client_url}/uapi/domestic-stock/v1/ranking/overtime-fluctuation",
            json=expected,
            status=200,
        )
        resp = self.openkis_client.get_ranking_over_time_fluctuation_rate(
            fid_input_iscd="0000",
            fid_div_cls_code="2",
            fid_input_price1="1000",
            fid_input_price2="100000",
            fid_vol_cnt="",
        )
        assert resp == expected

    @responses.activate
    def test_overtime_volume(self):
        expected = {
            "output1": {
                "ovtm_untp_exch_vol": "9384600",
                "ovtm_untp_exch_tr_pbmn": "108985413417",
                "ovtm_untp_kosdaq_vol": "10059688",
                "ovtm_untp_kosdaq_tr_pbmn": "107823859495",
            },
            "output2": [
                {
                    "stck_shrn_iscd": "240600",
                    "hts_kor_isnm": "유진테크놀로지",
                    "ovtm_untp_prpr": "10980",
                    "ovtm_untp_prdy_vrss": "990",
                    "ovtm_untp_prdy_vrss_sign": "1",
                    "ovtm_untp_prdy_ctrt": "9.91",
                    "ovtm_untp_seln_rsqn": "0",
                    "ovtm_untp_shnu_rsqn": "665006",
                    "ovtm_untp_vol": "158870",
                    "ovtm_vrss_acml_vol_rlim": "6.03",
                    "stck_prpr": "9990",
                    "acml_vol": "2633554",
                    "bidp": "9990",
                    "askp": "10000",
                }
            ],
            "rt_cd": "0",
            "msg_cd": "MCA00000",
            "msg1": "정상처리 되었습니다.",
        }
        responses.add(
            responses.GET,
            f"{self.openkis_client_url}/uapi/domestic-stock/v1/ranking/overtime-volume",
            json=expected,
            status=200,
        )
        resp = self.openkis_client.get_ranking_over_time_volume(
            fid_input_iscd="0000",
            fid_rank_sort_cls_code="0",
            fid_input_price1="1000",
            fid_input_price2="100000",
            fid_vol_cnt="",
        )
        assert resp == expected


if __name__ == "__main__":
    unittest.main()
