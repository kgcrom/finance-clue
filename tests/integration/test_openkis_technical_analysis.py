import time
import unittest

import pytest

from finance_clue.openkis import OpenKisClient
from finance_clue.openkis import attach_headers


@pytest.mark.usefixtures("integration_openkis_client")
class OpenKisTechnicalAnalysisTestCase(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def setup(self, integration_openkis_client: OpenKisClient):
        self.openkis_client = integration_openkis_client
        time.sleep(1)

    def test_foreign_institution_total(self):
        resp = self.openkis_client.get_technical_foreign_institution_total(
            fid_input_iscd="0000",
            fid_div_cls_code="0",
            fid_rank_sort_cls_code="1",
            fid_etc_cls_code="2",
        )

        example = {
            "output": [
                {
                    "hts_kor_isnm": "삼성전자",
                    "mksc_shrn_iscd": "005930",
                    "ntby_qty": "-903000",
                    "stck_prpr": "81800",
                    "prdy_vrss_sign": "3",
                    "prdy_vrss": "0",
                    "prdy_ctrt": "0.00",
                    "acml_vol": "14471904",
                    "frgn_ntby_qty": "2272000",
                    "orgn_ntby_qty": "-903000",
                    "ivtr_ntby_qty": "-804000",
                    "bank_ntby_qty": "0",
                    "insu_ntby_qty": "-26000",
                    "mrbn_ntby_qty": "0",
                    "fund_ntby_qty": "-73000",
                    "etc_orgt_ntby_vol": "0",
                    "etc_corp_ntby_vol": "29000",
                    "frgn_ntby_tr_pbmn": "185850",
                    "orgn_ntby_tr_pbmn": "-73865",
                    "ivtr_ntby_tr_pbmn": "-65767",
                    "bank_ntby_tr_pbmn": "0",
                    "insu_ntby_tr_pbmn": "-2127",
                    "mrbn_ntby_tr_pbmn": "0",
                    "fund_ntby_tr_pbmn": "-5971",
                    "etc_orgt_ntby_tr_pbmn": "0",
                    "etc_corp_ntby_tr_pbmn": "2372",
                }
            ],
            "rt_cd": "0",
            "msg_cd": "MCA00000",
            "msg1": "정상처리 되었습니다.",
        }
        assert resp is not None

    def test_program_trade_by_stock(self):
        resp = self.openkis_client.get_technical_program_trade_by_stock(
            fid_input_iscd="005930",
        )

        example = {
            "output": [
                {
                    "bsop_hour": "153004",
                    "stck_prpr": "81800",
                    "prdy_vrss": "0",
                    "prdy_vrss_sign": "3",
                    "prdy_ctrt": "0.00",
                    "acml_vol": "14370571",
                    "whol_smtn_seln_vol": "3464778",
                    "whol_smtn_shnu_vol": "3736261",
                    "whol_smtn_ntby_qty": "271483",
                    "whol_smtn_seln_tr_pbmn": "283874208800",
                    "whol_smtn_shnu_tr_pbmn": "306404815000",
                    "whol_smtn_ntby_tr_pbmn": "22530606200",
                    "whol_ntby_vol_icdc": "-1007",
                    "whol_ntby_tr_pbmn_icdc": "-82372600",
                }
            ],
            "rt_cd": "0",
            "msg_cd": "MCA00000",
            "msg1": "정상처리 되었습니다.",
        }
        assert resp is not None

    def test_investor_trend_estimate(self):
        resp = self.openkis_client.get_technical_investor_trend_estimate(
            mksc_shrn_iscd="005930",
        )

        example = {
            "output2": [
                {
                    "bsop_hour_gb": "5",
                    "frgn_fake_ntby_qty": "000000000002272000",
                    "orgn_fake_ntby_qty": "-00000000000903000",
                    "sum_fake_ntby_qty": "000000000001369000",
                }
            ],
            "rt_cd": "0",
            "msg_cd": "MCA00000",
            "msg1": "정상처리 되었습니다.",
        }
        assert resp is not None

    def test_trade_daily_volume(self):
        resp = self.openkis_client.get_technical_trade_daily_volume(
            fid_input_iscd="005930",
            fid_input_date1="20240601",
            fid_input_date2="20240701",
        )

        example = {
            "output1": {"shnu_cnqn_smtn": "5540756", "seln_cnqn_smtn": "6688312"},
            "output2": [
                {
                    "stck_bsop_date": "20240701",
                    "total_seln_qty": "4610063",
                    "total_shnu_qty": "5302002",
                }
            ],
            "rt_cd": "0",
            "msg_cd": "MCA00000",
            "msg1": "정상처리 되었습니다.",
        }
        assert resp is not None

    def test_investor_time_by_market(self):
        resp = self.openkis_client.get_technical_investor_trend_by_market(
            fid_input_iscd="KSP",
            fid_input_iscd2="0027",
        )

        example = {
            "output": [
                {
                    "frgn_seln_vol": "49021",
                    "frgn_shnu_vol": "45433",
                    "frgn_ntby_qty": "-3588",
                    "frgn_seln_tr_pbmn": "2110230",
                    "frgn_shnu_tr_pbmn": "2069138",
                    "frgn_ntby_tr_pbmn": "-41092",
                    "prsn_seln_vol": "210706",
                    "prsn_shnu_vol": "221274",
                    "prsn_ntby_qty": "10568",
                    "prsn_seln_tr_pbmn": "4501355",
                    "prsn_shnu_tr_pbmn": "4872445",
                    "prsn_ntby_tr_pbmn": "371090",
                    "orgn_seln_vol": "24518",
                    "orgn_shnu_vol": "17135",
                    "orgn_ntby_qty": "-7383",
                    "orgn_seln_tr_pbmn": "1757677",
                    "orgn_shnu_tr_pbmn": "1426382",
                    "orgn_ntby_tr_pbmn": "-331295",
                    "scrt_seln_vol": "8804",
                    "scrt_shnu_vol": "4442",
                    "scrt_ntby_qty": "-4362",
                    "scrt_seln_tr_pbmn": "425139",
                    "scrt_shnu_tr_pbmn": "240251",
                    "scrt_ntby_tr_pbmn": "-184888",
                    "ivtr_seln_vol": "2522",
                    "ivtr_shnu_vol": "1242",
                    "ivtr_ntby_qty": "-1280",
                    "ivtr_seln_tr_pbmn": "171189",
                    "ivtr_shnu_tr_pbmn": "114168",
                    "ivtr_ntby_tr_pbmn": "-57022",
                    "pe_fund_seln_tr_pbmn": "173254",
                    "pe_fund_seln_vol": "2445",
                    "pe_fund_ntby_vol": "-927",
                    "pe_fund_shnu_tr_pbmn": "109495",
                    "pe_fund_shnu_vol": "1517",
                    "pe_fund_ntby_tr_pbmn": "-63760",
                    "bank_seln_vol": "125",
                    "bank_shnu_vol": "39",
                    "bank_ntby_qty": "-86",
                    "bank_seln_tr_pbmn": "4317",
                    "bank_shnu_tr_pbmn": "3194",
                    "bank_ntby_tr_pbmn": "-1123",
                    "insu_seln_vol": "895",
                    "insu_shnu_vol": "691",
                    "insu_ntby_qty": "-204",
                    "insu_seln_tr_pbmn": "64411",
                    "insu_shnu_tr_pbmn": "56679",
                    "insu_ntby_tr_pbmn": "-7732",
                    "mrbn_seln_vol": "50",
                    "mrbn_shnu_vol": "30",
                    "mrbn_ntby_qty": "-20",
                    "mrbn_seln_tr_pbmn": "3434",
                    "mrbn_shnu_tr_pbmn": "2171",
                    "mrbn_ntby_tr_pbmn": "-1263",
                    "fund_seln_vol": "9677",
                    "fund_shnu_vol": "9175",
                    "fund_ntby_qty": "-503",
                    "fund_seln_tr_pbmn": "915932",
                    "fund_shnu_tr_pbmn": "900425",
                    "fund_ntby_tr_pbmn": "-15507",
                    "etc_orgt_seln_vol": "0",
                    "etc_orgt_shnu_vol": "0",
                    "etc_orgt_ntby_vol": "0",
                    "etc_orgt_seln_tr_pbmn": "0",
                    "etc_orgt_shnu_tr_pbmn": "0",
                    "etc_orgt_ntby_tr_pbmn": "0",
                    "etc_corp_seln_vol": "1937",
                    "etc_corp_shnu_vol": "2339",
                    "etc_corp_ntby_vol": "403",
                    "etc_corp_seln_tr_pbmn": "68119",
                    "etc_corp_shnu_tr_pbmn": "69416",
                    "etc_corp_ntby_tr_pbmn": "1297",
                }
            ],
            "rt_cd": "0",
            "msg_cd": "MCA00000",
            "msg1": "정상처리 되었습니다.",
        }
        assert resp is not None

    def test_credit_balance_daily(self):
        resp = self.openkis_client.get_technical_credit_balance_daily(
            fid_input_iscd="005930",
            fid_input_date1="20240601",
        )

        example = {
            "output": [
                {
                    "deal_date": "20240529",
                    "stck_prpr": "75200",
                    "prdy_vrss_sign": "5",
                    "prdy_vrss": "-2400",
                    "prdy_ctrt": "-3.09",
                    "acml_vol": "30244875",
                    "stlm_date": "20240531",
                    "whol_loan_new_stcn": "1448396",
                    "whol_loan_rdmp_stcn": "1304754",
                    "whol_loan_rmnd_stcn": "9668427",
                    "whol_loan_new_amt": "9848361",
                    "whol_loan_rdmp_amt": "8982782",
                    "whol_loan_rmnd_amt": "67053045",
                    "whol_loan_rmnd_rate": "0.16",
                    "whol_loan_gvrt": "4.78",
                    "whol_stln_new_stcn": "0",
                    "whol_stln_rdmp_stcn": "0",
                    "whol_stln_rmnd_stcn": "5865",
                    "whol_stln_new_amt": "0",
                    "whol_stln_rdmp_amt": "0",
                    "whol_stln_rmnd_amt": "36432",
                    "whol_stln_rmnd_rate": "0.00",
                    "whol_stln_gvrt": "0.00",
                    "stck_oprc": "77700",
                    "stck_hgpr": "78200",
                    "stck_lwpr": "75200",
                }
            ],
            "rt_cd": "0",
            "msg_cd": "MCA00000",
            "msg1": "정상처리 되었습니다.",
        }
        assert resp is not None

    def test_expected_conclusion_trend(self):
        resp = self.openkis_client.get_technical_expected_conclusion_trend(
            fid_input_iscd="005930",
            fid_mkop_cls_code="4",
        )

        example = {
            "output1": {
                "rprs_mrkt_kor_name": "KOSPI200",
                "antc_cnpr": "81800",
                "antc_cntg_vrss_sign": "3",
                "antc_cntg_vrss": "0",
                "antc_cntg_prdy_ctrt": "0.00",
                "antc_vol": "1050841",
                "antc_tr_pbmn": "85958793800",
            },
            "output2": [
                {
                    "stck_bsop_date": "20240702",
                    "stck_cntg_hour": "153002",
                    "stck_prpr": "81800",
                    "prdy_vrss_sign": "3",
                    "prdy_vrss": "0",
                    "prdy_ctrt": "0.00",
                    "acml_vol": "1050841",
                }
            ],
            "rt_cd": "0",
            "msg_cd": "MCA00000",
            "msg1": "정상처리 되었습니다.",
        }
        assert resp is not None

    def test_short_sale_daily(self):
        resp = self.openkis_client.get_technical_short_sale_daily(
            fid_input_iscd="005930",
            fid_input_date1="20240601",
            fid_input_date2="20240701",
        )

        example = {
            "output1": {
                "stck_prpr": "81800",
                "prdy_vrss": "0",
                "prdy_vrss_sign": "3",
                "prdy_ctrt": "0.00",
                "acml_vol": "14471904",
                "prdy_vol": "11317202",
            },
            "output2": [
                {
                    "stck_bsop_date": "20240701",
                    "stck_clpr": "81800",
                    "prdy_vrss": "300",
                    "prdy_vrss_sign": "2",
                    "prdy_ctrt": "0.37",
                    "acml_vol": "11317202",
                    "stnd_vol_smtn": "363213435",
                    "ssts_cntg_qty": "19329",
                    "ssts_vol_rlim": "0.17",
                    "acml_ssts_cntg_qty": "1292853",
                    "acml_ssts_cntg_qty_rlim": "0.36",
                    "acml_tr_pbmn": "925400917400",
                    "stnd_tr_pbmn_smtn": "28671550298770",
                    "ssts_tr_pbmn": "1580633900",
                    "ssts_tr_pbmn_rlim": "0.17",
                    "acml_ssts_tr_pbmn": "102222013200",
                    "acml_ssts_tr_pbmn_rlim": "0.36",
                    "stck_oprc": "81500",
                    "stck_hgpr": "82100",
                    "stck_lwpr": "81300",
                    "avrg_prc": "81775",
                }
            ],
            "rt_cd": "0",
            "msg_cd": "MCA00000",
            "msg1": "정상처리 되었습니다.",
        }
        assert resp is not None

    def test_program_trade_daily(self):
        resp = self.openkis_client.get_technical_program_trade_daily(
            fid_mrkt_cls_code="K",
            fid_input_date1="20240601",
            fid_input_date2="20240701",
        )

        example = {
            "output": [
                {
                    "stck_bsop_date": "20240701",
                    "arbt_entm_seln_vol": "492",
                    "arbt_entm_seln_vol_rate": "0.11",
                    "arbt_entm_seln_tr_pbmn": "32752",
                    "arbt_entm_seln_tr_pbmn_rate": "0.33",
                    "arbt_onsl_seln_tr_pbmn": "2048",
                    "arbt_onsl_seln_tr_pbmn_rate": "0.02",
                    "arbt_onsl_seln_vol": "31",
                    "arbt_onsl_seln_vol_rate": "0.01",
                    "arbt_smtn_seln_vol": "523",
                    "arbt_smtm_seln_vol_rate": "0.11",
                    "arbt_smtn_seln_tr_pbmn": "34800",
                    "arbt_smtm_seln_tr_pbmn_rate": "0.35",
                    "nabt_entm_seln_vol": "67992",
                    "nabt_entm_seln_tr_pbmn": "2040809",
                    "nabt_entm_seln_vol_rate": "14.81",
                    "nabt_entm_seln_tr_pbmn_rate": "20.52",
                    "nabt_onsl_seln_vol": "457",
                    "nabt_onsl_seln_vol_rate": "0.10",
                    "nabt_onsl_seln_tr_pbmn": "28737",
                    "nabt_onsl_seln_tr_pbmn_rate": "0.29",
                    "nabt_smtn_seln_vol": "68450",
                    "nabt_smtm_seln_vol_rate": "14.91",
                    "nabt_smtn_seln_tr_pbmn": "2069545",
                    "nabt_smtm_seln_tr_pbmn_rate": "20.81",
                    "whol_entm_seln_vol": "68484",
                    "whol_entm_seln_tr_pbmn": "2073561",
                    "whol_entm_seln_vol_rate": "14.91",
                    "whol_entm_seln_tr_pbmn_rate": "20.85",
                    "whol_onsl_seln_vol": "488",
                    "whol_onsl_seln_vol_rate": "0.11",
                    "whol_onsl_seln_tr_pbmn": "30785",
                    "whol_onsl_seln_tr_pbmn_rate": "0.31",
                    "whol_smtn_seln_vol": "68972",
                    "whol_seln_vol_rate": "15.02",
                    "whol_smtn_seln_tr_pbmn": "2104346",
                    "whol_seln_tr_pbmn_rate": "21.16",
                    "arbt_entm_shnu_vol": "492",
                    "arbt_entm_shnu_vol_rate": "0.11",
                    "arbt_entm_shnu_tr_pbmn": "32770",
                    "arbt_entm_shnu_tr_pbmn_rate": "0.33",
                    "arbt_onsl_shnu_vol": "816",
                    "arbt_onsl_shnu_vol_rate": "0.18",
                    "arbt_onsl_shnu_tr_pbmn": "54458",
                    "arbt_onsl_shnu_tr_pbmn_rate": "0.55",
                    "arbt_smtn_shnu_vol": "1308",
                    "arbt_smtm_shun_vol_rate": "0.28",
                    "arbt_smtn_shnu_tr_pbmn": "87228",
                    "arbt_smtm_shun_tr_pbmn_rate": "0.88",
                    "nabt_entm_shnu_vol": "58604",
                    "nabt_entm_shnu_vol_rate": "12.76",
                    "nabt_entm_shnu_tr_pbmn": "1883215",
                    "nabt_entm_shnu_tr_pbmn_rate": "18.94",
                    "nabt_onsl_shnu_vol": "145",
                    "nabt_onsl_shnu_vol_rate": "0.03",
                    "nabt_onsl_shnu_tr_pbmn": "3850",
                    "nabt_onsl_shnu_tr_pbmn_rate": "0.04",
                    "nabt_smtn_shnu_vol": "58749",
                    "nabt_smtm_shun_vol_rate": "12.79",
                    "nabt_smtn_shnu_tr_pbmn": "1887065",
                    "nabt_smtm_shun_tr_pbmn_rate": "18.97",
                    "whol_entm_shnu_vol": "59096",
                    "whol_entm_shnu_vol_rate": "12.87",
                    "whol_entm_shnu_tr_pbmn": "1915985",
                    "whol_entm_shnu_tr_pbmn_rate": "19.27",
                    "whol_onsl_shnu_vol": "961",
                    "whol_onsl_shnu_tr_pbmn": "58308",
                    "whol_onsl_shnu_tr_pbmn_rate": "0.59",
                    "whol_onsl_shnu_vol_rate": "0.21",
                    "whol_smtn_shnu_vol": "60057",
                    "whol_shun_vol_rate": "13.08",
                    "whol_smtn_shnu_tr_pbmn": "1974294",
                    "whol_shun_tr_pbmn_rate": "19.85",
                    "arbt_entm_ntby_qty": "0",
                    "arbt_entm_ntby_qty_rate": "0.00",
                    "arbt_entm_ntby_tr_pbmn": "18",
                    "arbt_entm_ntby_tr_pbmn_rate": "0.00",
                    "arbt_onsl_ntby_qty": "785",
                    "arbt_onsl_ntby_qty_rate": "0.17",
                    "arbt_onsl_ntby_tr_pbmn": "52410",
                    "arbt_onsl_ntby_tr_pbmn_rate": "0.53",
                    "arbt_smtn_ntby_qty": "785",
                    "arbt_smtm_ntby_qty_rate": "0.17",
                    "arbt_smtn_ntby_tr_pbmn": "52428",
                    "arbt_smtm_ntby_tr_pbmn_rate": "0.53",
                    "nabt_entm_ntby_qty": "-9388",
                    "nabt_entm_ntby_qty_rate": "-2.04",
                    "nabt_entm_ntby_tr_pbmn": "-157594",
                    "nabt_entm_ntby_tr_pbmn_rate": "-1.58",
                    "nabt_onsl_ntby_qty": "-312",
                    "nabt_onsl_ntby_qty_rate": "-0.07",
                    "nabt_onsl_ntby_tr_pbmn": "-24886",
                    "nabt_onsl_ntby_tr_pbmn_rate": "-0.25",
                    "nabt_smtn_ntby_qty": "-9700",
                    "nabt_smtm_ntby_qty_rate": "-2.11",
                    "nabt_smtn_ntby_tr_pbmn": "-182480",
                    "nabt_smtm_ntby_tr_pbmn_rate": "-1.83",
                    "whol_entm_ntby_qty": "-9388",
                    "whol_entm_ntby_qty_rate": "-2.04",
                    "whol_entm_ntby_tr_pbmn": "-157576",
                    "whol_entm_ntby_tr_pbmn_rate": "-1.58",
                    "whol_onsl_ntby_qty": "473",
                    "whol_onsl_ntby_qty_rate": "0.10",
                    "whol_onsl_ntby_tr_pbmn": "27523",
                    "whol_onsl_ntby_tr_pbmn_rate": "0.28",
                    "whol_smtn_ntby_qty": "-8915",
                    "whol_ntby_qty_rate": "-1.94",
                    "whol_smtn_ntby_tr_pbmn": "-130052",
                    "whol_ntby_tr_pbmn_rate": "-1.31",
                    "bstp_nmix_prpr": "",
                    "bstp_nmix_prdy_vrss": "",
                    "prdy_vrss_sign": "",
                },
                {
                    "stck_bsop_date": "20240628",
                    "arbt_entm_seln_vol": "0",
                    "arbt_entm_seln_vol_rate": "0.00",
                    "arbt_entm_seln_tr_pbmn": "0",
                    "arbt_entm_seln_tr_pbmn_rate": "0.00",
                    "arbt_onsl_seln_tr_pbmn": "3484",
                    "arbt_onsl_seln_tr_pbmn_rate": "0.03",
                    "arbt_onsl_seln_vol": "45",
                    "arbt_onsl_seln_vol_rate": "0.01",
                    "arbt_smtn_seln_vol": "45",
                    "arbt_smtm_seln_vol_rate": "0.01",
                    "arbt_smtn_seln_tr_pbmn": "3484",
                    "arbt_smtm_seln_tr_pbmn_rate": "0.03",
                    "nabt_entm_seln_vol": "88539",
                    "nabt_entm_seln_tr_pbmn": "2660770",
                    "nabt_entm_seln_vol_rate": "14.50",
                    "nabt_entm_seln_tr_pbmn_rate": "24.14",
                    "nabt_onsl_seln_vol": "234",
                    "nabt_onsl_seln_vol_rate": "0.04",
                    "nabt_onsl_seln_tr_pbmn": "13246",
                    "nabt_onsl_seln_tr_pbmn_rate": "0.12",
                    "nabt_smtn_seln_vol": "88772",
                    "nabt_smtm_seln_vol_rate": "14.54",
                    "nabt_smtn_seln_tr_pbmn": "2674016",
                    "nabt_smtm_seln_tr_pbmn_rate": "24.26",
                    "whol_entm_seln_vol": "88539",
                    "whol_entm_seln_tr_pbmn": "2660770",
                    "whol_entm_seln_vol_rate": "14.50",
                    "whol_entm_seln_tr_pbmn_rate": "24.14",
                    "whol_onsl_seln_vol": "278",
                    "whol_onsl_seln_vol_rate": "0.05",
                    "whol_onsl_seln_tr_pbmn": "16730",
                    "whol_onsl_seln_tr_pbmn_rate": "0.15",
                    "whol_smtn_seln_vol": "88817",
                    "whol_seln_vol_rate": "14.55",
                    "whol_smtn_seln_tr_pbmn": "2677500",
                    "whol_seln_tr_pbmn_rate": "24.30",
                    "arbt_entm_shnu_vol": "385",
                    "arbt_entm_shnu_vol_rate": "0.06",
                    "arbt_entm_shnu_tr_pbmn": "32608",
                    "arbt_entm_shnu_tr_pbmn_rate": "0.30",
                    "arbt_onsl_shnu_vol": "1375",
                    "arbt_onsl_shnu_vol_rate": "0.23",
                    "arbt_onsl_shnu_tr_pbmn": "91104",
                    "arbt_onsl_shnu_tr_pbmn_rate": "0.83",
                    "arbt_smtn_shnu_vol": "1760",
                    "arbt_smtm_shun_vol_rate": "0.29",
                    "arbt_smtn_shnu_tr_pbmn": "123712",
                    "arbt_smtm_shun_tr_pbmn_rate": "1.12",
                    "nabt_entm_shnu_vol": "99539",
                    "nabt_entm_shnu_vol_rate": "16.30",
                    "nabt_entm_shnu_tr_pbmn": "2798770",
                    "nabt_entm_shnu_tr_pbmn_rate": "25.40",
                    "nabt_onsl_shnu_vol": "468",
                    "nabt_onsl_shnu_vol_rate": "0.08",
                    "nabt_onsl_shnu_tr_pbmn": "30808",
                    "nabt_onsl_shnu_tr_pbmn_rate": "0.28",
                    "nabt_smtn_shnu_vol": "100007",
                    "nabt_smtm_shun_vol_rate": "16.38",
                    "nabt_smtn_shnu_tr_pbmn": "2829578",
                    "nabt_smtm_shun_tr_pbmn_rate": "25.68",
                    "whol_entm_shnu_vol": "99923",
                    "whol_entm_shnu_vol_rate": "16.37",
                    "whol_entm_shnu_tr_pbmn": "2831378",
                    "whol_entm_shnu_tr_pbmn_rate": "25.69",
                    "whol_onsl_shnu_vol": "1843",
                    "whol_onsl_shnu_tr_pbmn": "121912",
                    "whol_onsl_shnu_tr_pbmn_rate": "1.11",
                    "whol_onsl_shnu_vol_rate": "0.30",
                    "whol_smtn_shnu_vol": "101766",
                    "whol_shun_vol_rate": "16.67",
                    "whol_smtn_shnu_tr_pbmn": "2953290",
                    "whol_shun_tr_pbmn_rate": "26.80",
                    "arbt_entm_ntby_qty": "385",
                    "arbt_entm_ntby_qty_rate": "0.06",
                    "arbt_entm_ntby_tr_pbmn": "32608",
                    "arbt_entm_ntby_tr_pbmn_rate": "0.30",
                    "arbt_onsl_ntby_qty": "1330",
                    "arbt_onsl_ntby_qty_rate": "0.22",
                    "arbt_onsl_ntby_tr_pbmn": "87620",
                    "arbt_onsl_ntby_tr_pbmn_rate": "0.80",
                    "arbt_smtn_ntby_qty": "1715",
                    "arbt_smtm_ntby_qty_rate": "0.28",
                    "arbt_smtn_ntby_tr_pbmn": "120228",
                    "arbt_smtm_ntby_tr_pbmn_rate": "1.09",
                    "nabt_entm_ntby_qty": "11000",
                    "nabt_entm_ntby_qty_rate": "1.80",
                    "nabt_entm_ntby_tr_pbmn": "138000",
                    "nabt_entm_ntby_tr_pbmn_rate": "1.25",
                    "nabt_onsl_ntby_qty": "234",
                    "nabt_onsl_ntby_qty_rate": "0.04",
                    "nabt_onsl_ntby_tr_pbmn": "17562",
                    "nabt_onsl_ntby_tr_pbmn_rate": "0.16",
                    "nabt_smtn_ntby_qty": "11234",
                    "nabt_smtm_ntby_qty_rate": "1.84",
                    "nabt_smtn_ntby_tr_pbmn": "155562",
                    "nabt_smtm_ntby_tr_pbmn_rate": "1.41",
                    "whol_entm_ntby_qty": "11385",
                    "whol_entm_ntby_qty_rate": "1.86",
                    "whol_entm_ntby_tr_pbmn": "170608",
                    "whol_entm_ntby_tr_pbmn_rate": "1.55",
                    "whol_onsl_ntby_qty": "1565",
                    "whol_onsl_ntby_qty_rate": "0.26",
                    "whol_onsl_ntby_tr_pbmn": "105183",
                    "whol_onsl_ntby_tr_pbmn_rate": "0.95",
                    "whol_smtn_ntby_qty": "12949",
                    "whol_ntby_qty_rate": "2.12",
                    "whol_smtn_ntby_tr_pbmn": "275791",
                    "whol_ntby_tr_pbmn_rate": "2.50",
                    "bstp_nmix_prpr": "",
                    "bstp_nmix_prdy_vrss": "",
                    "prdy_vrss_sign": "",
                },
            ],
            "rt_cd": "0",
            "msg_cd": "MCA00000",
            "msg1": "정상처리 되었습니다.",
        }
        assert resp is not None

    def test_overtime_expected_trans_fluct(self):
        resp = self.openkis_client.get_technical_over_time_exp_fluctuation_rate(
            fid_input_iscd="0001",
            fid_rank_sort_cls_code="0",
            fid_div_cls_code="0",
            fid_input_price1="",
            fid_input_price2="",
            fid_input_vol1="",
        )

        example = {
            "msg1": "정상처리 되었습니다.",
            "msg_cd": "MCA00000",
            "output": [
                {
                    "data_rank": "1",
                    "iscd_stat_cls_code": "57",
                    "stck_shrn_iscd": "025820",
                    "hts_kor_isnm": "이구산업",
                    "ovtm_untp_antc_cnpr": "6270",
                    "ovtm_untp_antc_cntg_vrss": "570",
                    "ovtm_untp_antc_cntg_vrss_sign": "1",
                    "ovtm_untp_antc_cntg_ctrt": "10.00",
                    "ovtm_untp_askp_rsqn1": "231200",
                    "ovtm_untp_bidp_rsqn1": "394",
                    "ovtm_untp_antc_cnqn": "253267",
                    "itmt_vol": "14355442",
                    "stck_prpr": "5700",
                },
            ],
            "rt_cd": "0",
        }
        assert resp is not None

    def test_daily_loan_trans(self):
        resp = self.openkis_client.get_technical_daily_loan_trans(
            mrkt_div_cls_code="3",
            mksc_shrn_iscd="005930",
            start_date="20240601",
            end_date="20240701",
        )

        example = {
            "output1": [
                {
                    "bsop_date": "20240701",
                    "stck_prpr": "81800.00",
                    "prdy_vrss_sign": "2",
                    "prdy_vrss": "300.00",
                    "prdy_ctrt": "0.37",
                    "acml_vol": "11317202",
                    "new_stcn": "7441346",
                    "rdmp_stcn": "1431733",
                    "prdy_rmnd_vrss": "6009613",
                    "rmnd_stcn": "89029928",
                    "rmnd_amt": "7282648",
                }
            ],
            "rt_cd": "0",
            "msg_cd": "MCA00000",
            "msg1": "정상처리 되었습니다.",
        }
        assert resp is not None

    def test_program_trade_today(self):
        resp = self.openkis_client.get_technical_program_trade_today(
            fid_mrkt_cls_code="K",
        )

        example = {
            "output": [
                {
                    "bsop_hour": "180500",
                    "arbt_smtn_seln_tr_pbmn": "64011",
                    "arbt_smtm_seln_tr_pbmn_rate": "0.49",
                    "arbt_smtn_shnu_tr_pbmn": "501473",
                    "arbt_smtm_shun_tr_pbmn_rate": "3.88",
                    "nabt_smtn_seln_tr_pbmn": "2111474",
                    "nabt_smtm_seln_tr_pbmn_rate": "16.32",
                    "nabt_smtn_shnu_tr_pbmn": "3071257",
                    "nabt_smtm_shun_tr_pbmn_rate": "23.73",
                    "arbt_smtn_ntby_tr_pbmn": "437461",
                    "arbt_smtm_ntby_tr_pbmn_rate": "3.38",
                    "nabt_smtn_ntby_tr_pbmn": "959784",
                    "nabt_smtm_ntby_tr_pbmn_rate": "7.42",
                    "whol_smtn_ntby_tr_pbmn": "1397245",
                    "whol_ntby_tr_pbmn_rate": "10.80",
                },
                {
                    "bsop_hour": "180400",
                    "arbt_smtn_seln_tr_pbmn": "64011",
                    "arbt_smtm_seln_tr_pbmn_rate": "0.49",
                    "arbt_smtn_shnu_tr_pbmn": "501473",
                    "arbt_smtm_shun_tr_pbmn_rate": "3.88",
                    "nabt_smtn_seln_tr_pbmn": "2111474",
                    "nabt_smtm_seln_tr_pbmn_rate": "16.32",
                    "nabt_smtn_shnu_tr_pbmn": "3071257",
                    "nabt_smtm_shun_tr_pbmn_rate": "23.73",
                    "arbt_smtn_ntby_tr_pbmn": "437461",
                    "arbt_smtm_ntby_tr_pbmn_rate": "3.38",
                    "nabt_smtn_ntby_tr_pbmn": "959784",
                    "nabt_smtm_ntby_tr_pbmn_rate": "7.42",
                    "whol_smtn_ntby_tr_pbmn": "1397245",
                    "whol_ntby_tr_pbmn_rate": "10.80",
                },
            ],
            "rt_cd": "0",
            "msg_cd": "MCA00000",
            "msg1": "정상처리 되었습니다.",
        }
        assert resp is not None

    def test_foreign_trade_estimate(self):
        resp = self.openkis_client.get_technical_foreign_trade_estimate(
            fid_input_iscd="0000",
            fid_rank_sort_cls_code="0",
            fid_rank_sort_cls_code2="0",
        )

        example = {
            "output": [
                {
                    "stck_shrn_iscd": "005930",
                    "hts_kor_isnm": "삼성전자",
                    "glob_ntsl_qty": "10409817",
                    "stck_prpr": "87100",
                    "prdy_vrss": "2500",
                    "prdy_vrss_sign": "2",
                    "prdy_ctrt": "2.96",
                    "acml_vol": "45791193",
                    "glob_total_seln_qty": "0",
                    "glob_total_shnu_qty": "10409817",
                }
            ],
            "rt_cd": "0",
            "msg_cd": "MCA00000",
            "msg1": "정상처리 되었습니다.",
        }
        assert resp is not None

    def test_foreign_purchase_trend(self):
        resp = self.openkis_client.get_technical_foreign_purchase_trend(
            fid_input_iscd="005930",
        )

        example = {
            "output": [
                {
                    "bsop_hour": "153105",
                    "stck_prpr": "87100",
                    "prdy_vrss": "2500",
                    "prdy_vrss_sign": "2",
                    "prdy_ctrt": "2.96",
                    "acml_vol": "44922557",
                    "frgn_seln_vol": "0",
                    "frgn_shnu_vol": "10409817",
                    "glob_ntby_qty": "10409817",
                    "frgn_ntby_qty_icdc": "980225",
                }
            ],
            "rt_cd": "0",
            "msg_cd": "MCA00000",
            "msg1": "정상처리 되었습니다.",
        }
        assert resp is not None

    def test_trade_part_by_amount(self):
        resp = self.openkis_client.get_technical_trade_by_amount(
            fid_input_iscd="005930",
        )

        example = {
            "output": [
                {
                    "prpr_name": "3백 이하",
                    "smtn_avrg_prpr": "86237",
                    "acml_vol": "1577124",
                    "whol_ntby_qty_rate": "0.57",
                    "ntby_cntg_csnu": "32431",
                    "seln_cnqn_smtn": "660670",
                    "whol_seln_vol_rate": "1.47",
                    "seln_cntg_csnu": "81871",
                    "shnu_cnqn_smtn": "916454",
                    "whol_shun_vol_rate": "2.04",
                    "shnu_cntg_csnu": "114302",
                }
            ],
            "rt_cd": "0",
            "msg_cd": "MCA00000",
            "msg1": "정상처리 되었습니다.",
        }
        assert resp is not None

    def test_market_fund(self):
        # TODO tr_id, 거래ID 문서가 잘못되어있다. 시장별 투자매매동향과 동일. 예측도 어려움
        pass

    def test_investor_trend_by_market_daily(self):
        resp = self.openkis_client.get_technical_investor_trend_by_market_daily(
            fid_input_iscd="0001",
            fid_input_date1="20240610",
            fid_input_iscd1="KSP",
        )

        example = {
            "output": [
                {
                    "stck_bsop_date": "20240610",
                    "bstp_nmix_prpr": "2701.17",
                    "bstp_nmix_prdy_vrss": "-21.50",
                    "prdy_vrss_sign": "5",
                    "bstp_nmix_prdy_ctrt": "-0.79",
                    "bstp_nmix_oprc": "2698.71",
                    "bstp_nmix_hgpr": "2718.89",
                    "bstp_nmix_lwpr": "2689.19",
                    "stck_prdy_clpr": "2722.67",
                    "frgn_ntby_qty": "-4482",
                    "frgn_reg_ntby_qty": "-4465",
                    "frgn_nreg_ntby_qty": "-17",
                    "prsn_ntby_qty": "13862",
                    "orgn_ntby_qty": "-9895",
                    "scrt_ntby_qty": "-7233",
                    "ivtr_ntby_qty": "-210",
                    "pe_fund_ntby_vol": "-1198",
                    "bank_ntby_qty": "91",
                    "insu_ntby_qty": "-463",
                    "mrbn_ntby_qty": "-65",
                    "fund_ntby_qty": "-817",
                    "etc_ntby_qty": "516",
                    "etc_orgt_ntby_vol": "0",
                    "etc_corp_ntby_vol": "516",
                    "frgn_ntby_tr_pbmn": "17915",
                    "frgn_reg_ntby_pbmn": "16955",
                    "frgn_nreg_ntby_pbmn": "960",
                    "prsn_ntby_tr_pbmn": "556561",
                    "orgn_ntby_tr_pbmn": "-566989",
                    "scrt_ntby_tr_pbmn": "-469019",
                    "ivtr_ntby_tr_pbmn": "2816",
                    "pe_fund_ntby_tr_pbmn": "-39429",
                    "bank_ntby_tr_pbmn": "-1410",
                    "insu_ntby_tr_pbmn": "-8859",
                    "mrbn_ntby_tr_pbmn": "-9003",
                    "fund_ntby_tr_pbmn": "-42084",
                    "etc_ntby_tr_pbmn": "-7487",
                    "etc_orgt_ntby_tr_pbmn": "0",
                    "etc_corp_ntby_tr_pbmn": "-7487",
                }
            ],
            "rt_cd": "0",
            "msg_cd": "MCA00000",
            "msg1": "정상처리 되었습니다.",
        }
        assert resp is not None

    def test_program_trade_by_stock_daily(self):
        resp = self.openkis_client.get_technical_program_trade_by_stock_daily(
            fid_input_iscd="005930",
            fid_input_date1="20240601",
        )

        example = {
            "output": [
                {
                    "stck_bsop_date": "20240531",
                    "stck_clpr": "73500",
                    "prdy_vrss": "0",
                    "prdy_vrss_sign": "3",
                    "prdy_ctrt": "0.00",
                    "acml_vol": "26198776",
                    "acml_tr_pbmn": "1935963757832",
                    "whol_smtn_seln_vol": "13242141",
                    "whol_smtn_shnu_vol": "9690098",
                    "whol_smtn_ntby_qty": "-3552043",
                    "whol_smtn_seln_tr_pbmn": "976753206700",
                    "whol_smtn_shnu_tr_pbmn": "714977274500",
                    "whol_smtn_ntby_tr_pbmn": "-261775932200",
                    "whol_ntby_vol_icdc": "-336694",
                    "whol_ntby_tr_pbmn_icdc2": "-24156271800",
                },
                {
                    "stck_bsop_date": "20240530",
                    "stck_clpr": "73500",
                    "prdy_vrss": "-1700",
                    "prdy_vrss_sign": "5",
                    "prdy_ctrt": "-2.26",
                    "acml_vol": "28551272",
                    "acml_tr_pbmn": "2117784497387",
                    "whol_smtn_seln_vol": "8439709",
                    "whol_smtn_shnu_vol": "5224360",
                    "whol_smtn_ntby_qty": "-3215349",
                    "whol_smtn_seln_tr_pbmn": "625228165900",
                    "whol_smtn_shnu_tr_pbmn": "387608505500",
                    "whol_smtn_ntby_tr_pbmn": "-237619660400",
                    "whol_ntby_vol_icdc": "652137",
                    "whol_ntby_tr_pbmn_icdc2": "56673226600",
                },
            ],
            "rt_cd": "0",
            "msg_cd": "MCA00000",
            "msg1": "정상처리 되었습니다.",
        }
        assert resp is not None

    def test_investor_program_trade_today(self):
        resp = self.openkis_client.get_technical_program_trend_by_investor_today(
            mrkt_div_cls_code="1",
        )

        example = {
            "output1": [
                {
                    "invr_cls_code": "7100",
                    "invr_cls_name": "기 타",
                    "arbt_seln_qty": "0",
                    "arbt_shnu_qty": "0",
                    "arbt_ntby_qty": "0",
                    "arbt_seln_amt": "0",
                    "arbt_shnu_amt": "0",
                    "arbt_ntby_amt": "0",
                    "nabt_seln_qty": "146",
                    "nabt_shnu_qty": "153",
                    "nabt_ntby_qty": "7",
                    "nabt_seln_amt": "2687",
                    "nabt_shnu_amt": "4144",
                    "nabt_ntby_amt": "1456",
                    "all_seln_qty": "146",
                    "all_shnu_qty": "153",
                    "all_ntby_qty": "7",
                    "all_seln_amt": "2687",
                    "all_shnu_amt": "4144",
                    "all_ntby_amt": "1456",
                }
            ],
            "rt_cd": "0",
            "msg_cd": "MCA00000",
            "msg1": "정상처리 되었습니다.",
        }
        assert resp is not None

    def test_capture_up_low_price(self):
        resp = self.openkis_client.get_technical_capture_up_low_price(
            fid_prc_cls_code="0",
            fid_div_cls_code="6",
            fid_input_iscd="0001",
        )

        example = {
            "output": [
                {
                    "mksc_shrn_iscd": "000100",
                    "hts_kor_isnm": "유한양행",
                    "stck_prpr": "89500",
                    "prdy_vrss_sign": "2",
                    "prdy_vrss": "9600",
                    "prdy_ctrt": "12.02",
                    "acml_vol": "5652055",
                    "total_askp_rsqn": "48618",
                    "total_bidp_rsqn": "16645",
                    "askp_rsqn1": "4154",
                    "bidp_rsqn1": "1119",
                    "prdy_vol": "482253",
                    "seln_cnqn": "0",
                    "shnu_cnqn": "20",
                    "stck_llam": "56000",
                    "stck_mxpr": "103800",
                    "prdy_vrss_vol_rate": "1172.01",
                }
            ],
            "rt_cd": "0",
            "msg_cd": "MCA00000",
            "msg1": "정상처리 되었습니다.",
        }
        assert resp is not None

    def test_volume_profile_indicator(self):
        resp = self.openkis_client.get_technical_volume_profile_indicator(
            fid_input_iscd="005930",
        )

        example = {
            "output1": {
                "rprs_mrkt_kor_name": "KOSPI200",
                "stck_shrn_iscd": "005930",
                "hts_kor_isnm": "삼성전자",
                "stck_prpr": "87100",
                "prdy_vrss_sign": "2",
                "prdy_vrss": "2500",
                "prdy_ctrt": "2.96",
                "acml_vol": "45791193",
                "prdy_vol": "43857228",
                "wghn_avrg_stck_prc": "86280.34",
                "lstn_stcn": "5969782550",
            },
            "output2": [
                {
                    "data_rank": "1",
                    "stck_prpr": "86000",
                    "cntg_vol": "5120359",
                    "acml_vol_rlim": "11.18",
                }
            ],
            "rt_cd": "0",
            "msg_cd": "MCA00000",
            "msg1": "정상처리 되었습니다.",
        }
        assert resp is not None

    def test_member_trend_daily(self):
        resp = self.openkis_client.get_technical_member_trend_daily(
            fid_input_iscd="005930",
            fid_input_iscd2="00025",
            fid_input_date1="20240601",
            fid_input_date2="20240630",
        )

        example = {
            "output": [
                {
                    "stck_bsop_date": "20240628",
                    "total_seln_qty": "98986",
                    "total_shnu_qty": "55100",
                    "ntby_qty": "-43886",
                    "stck_prpr": "81500",
                    "prdy_vrss": "-100",
                    "prdy_vrss_sign": "5",
                    "prdy_ctrt": "-0.12",
                    "acml_vol": "9455929",
                },
                {
                    "stck_bsop_date": "20240627",
                    "total_seln_qty": "47368",
                    "total_shnu_qty": "29110",
                    "ntby_qty": "-18258",
                    "stck_prpr": "81600",
                    "prdy_vrss": "300",
                    "prdy_vrss_sign": "2",
                    "prdy_ctrt": "0.37",
                    "acml_vol": "11739720",
                },
                {
                    "stck_bsop_date": "20240626",
                    "total_seln_qty": "83795",
                    "total_shnu_qty": "34886",
                    "ntby_qty": "-48909",
                    "stck_prpr": "81300",
                    "prdy_vrss": "500",
                    "prdy_vrss_sign": "2",
                    "prdy_ctrt": "0.62",
                    "acml_vol": "17783242",
                },
            ],
            "rt_cd": "0",
            "msg_cd": "MCA00000",
            "msg1": "정상처리 되었습니다.",
        }
        assert resp is not None


if __name__ == "__main__":
    unittest.main()
