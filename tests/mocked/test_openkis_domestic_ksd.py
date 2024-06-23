import unittest

import pytest
import responses

from finance_clue.openkis import OpenKisClient


class OpenKisKsdTestCase(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def setup(self, mock_openkis_client: OpenKisClient, mock_openkis_client_url: str):
        self.openkis_client = mock_openkis_client
        self.openkis_client_url = mock_openkis_client_url

    @responses.activate
    def test_ksd_dividend_info(self):
        expected = {
            "output1": [
                {
                    "record_date": "20231231",
                    "sht_cd": "005930",
                    "isin_name": "삼성전자",
                    "divi_kind": "결산",
                    "face_val": "100",
                    "per_sto_divi_amt": "361",
                    "divi_rate": "361.00",
                    "stk_divi_rate": "0.00",
                    "divi_pay_dt": "2024/04/19",
                    "stk_div_pay_dt": "",
                    "odd_pay_dt": "",
                    "stk_kind": "보통",
                    "high_divi_gb": "",
                }
            ],
            "rt_cd": "0",
            "msg_cd": "MCA00000",
            "msg1": "정상처리 되었습니다.",
        }

        responses.add(
            responses.GET,
            f"{self.openkis_client_url}/uapi/domestic-stock/v1/ksdinfo/dividend",
            json=expected,
            status=200,
        )
        resp = self.openkis_client.get_ksd_dividend_info(
            f_dt="20231201", t_dt="20240231", sht_cd="005930", high_gb="", gb1="0"
        )
        assert resp == expected

    @responses.activate
    def test_purchase_request(self):
        expected = {
            "output1": [
                {
                    "record_date": "20240531",
                    "sht_cd": "083790",
                    "isin_name": "씨지인바이츠",
                    "stk_kind": "보통",
                    "opp_opi_rcpt_term": "020240614",
                    "buy_req_rcpt_term": "",
                    "buy_req_price": "000000000000",
                    "buy_amt_pay_dt": "",
                    "get_meet_dt": "",
                },
                {
                    "record_date": "20240531",
                    "sht_cd": "08379K",
                    "isin_name": "씨지인바이츠1우",
                    "stk_kind": "우선",
                    "opp_opi_rcpt_term": "020240614",
                    "buy_req_rcpt_term": "",
                    "buy_req_price": "000000000000",
                    "buy_amt_pay_dt": "",
                    "get_meet_dt": "",
                },
            ],
            "rt_cd": "0",
            "msg_cd": "MCA00000",
            "msg1": "정상처리 되었습니다.",
        }

        responses.add(
            responses.GET,
            f"{self.openkis_client_url}/uapi/domestic-stock/v1/ksdinfo/purreq",
            json=expected,
            status=200,
        )
        resp = self.openkis_client.get_ksd_purchase_request(
            f_dt="20240501",
            t_dt="20240531",
            sht_cd="",
        )
        assert resp == expected

    @responses.activate
    def test_merger_split(self):
        expected = {
            "output1": [
                {
                    "record_date": "20240524",
                    "sht_cd": "405640",
                    "opp_cust_cd": "40564",
                    "opp_cust_nm": "신한제9호기업인수목적",
                    "cust_cd": "32335",
                    "cust_nm": "다원넥스뷰",
                    "merge_type": "흡수합병",
                    "merge_rate": "0.28",
                    "td_stop_dt": "2024/05/23 ~",
                    "list_dt": "20240611",
                    "odd_amt_pay_dt": "2024/06/18",
                    "tot_issue_stk_qty": "0",
                    "issue_stk_qty": "0",
                    "seq": "0",
                }
            ],
            "rt_cd": "0",
            "msg_cd": "MCA00000",
            "msg1": "정상처리 되었습니다.",
        }

        responses.add(
            responses.GET,
            f"{self.openkis_client_url}/uapi/domestic-stock/v1/ksdinfo/merger-split",
            json=expected,
            status=200,
        )
        resp = self.openkis_client.get_ksd_merger_and_split(
            f_dt="20240501",
            t_dt="20240531",
            sht_cd="",
        )
        assert resp == expected

    @responses.activate
    def test_change_par_value(self):
        expected = {
            "output1": [
                {
                    "record_date": "20240424",
                    "sht_cd": "457190",
                    "isin_name": "이수스페셜티케미컬",
                    "inter_bf_face_amt": "000005000",
                    "inter_af_face_amt": "000001000",
                    "td_stop_dt": "2024/04/23 ~ 2024/05/01",
                    "list_dt": "2024/05/02",
                }
            ],
            "rt_cd": "0",
            "msg_cd": "MCA00000",
            "msg1": "정상처리 되었습니다.",
        }

        responses.add(
            responses.GET,
            f"{self.openkis_client_url}/uapi/domestic-stock/v1/ksdinfo/rev-split",
            json=expected,
            status=200,
        )
        resp = self.openkis_client.get_ksd_change_par_value(
            f_dt="20231201",
            t_dt="20240531",
            sht_cd="",
            market_gb="1",
        )
        assert resp == expected

    @responses.activate
    def test_decrease_capital(self):
        expected = {
            "output1": [
                {
                    "record_date": "20240529",
                    "sht_cd": "046070",
                    "isin_name": "코다코",
                    "stk_kind": "보통",
                    "reduce_cap_type": "무상감자",
                    "reduce_cap_rate": "0.50",
                    "comp_way": "곱하기",
                    "td_stop_dt": "2024/05/28 ~",
                    "list_dt": "",
                }
            ],
            "rt_cd": "0",
            "msg_cd": "MCA00000",
            "msg1": "정상처리 되었습니다.",
        }
        responses.add(
            responses.GET,
            f"{self.openkis_client_url}/uapi/domestic-stock/v1/ksdinfo/cap-dcrs",
            json=expected,
            status=200,
        )
        resp = self.openkis_client.get_ksd_decrease_capital(
            f_dt="20240501",
            t_dt="20240531",
            sht_cd="",
        )
        assert resp == expected

    @responses.activate
    def test_list_info(self):
        expected = {
            "output1": [
                {
                    "list_dt": "20240531",
                    "sht_cd": "003580",
                    "isin_name": "에이치엘비글로벌",
                    "stk_kind": "보통",
                    "issue_type": "유상증자",
                    "issue_stk_qty": "      705219",
                    "tot_issue_stk_qty": "    47410892",
                    "issue_price": "     7090",
                }
            ],
            "rt_cd": "0",
            "msg_cd": "MCA00000",
            "msg1": "정상처리 되었습니다.",
        }
        responses.add(
            responses.GET,
            f"{self.openkis_client_url}/uapi/domestic-stock/v1/ksdinfo/list-info",
            json=expected,
            status=200,
        )
        resp = self.openkis_client.get_ksd_list_info(
            f_dt="20231201",
            t_dt="20240531",
            sht_cd="",
        )
        assert resp == expected

    @responses.activate
    def test_public_offer_subscription(self):
        expected = {
            "output1": [
                {
                    "record_date": "20240520",
                    "sht_cd": "477380",
                    "isin_name": "미래에셋비전기업인수목적4호",
                    "fix_subscr_pri": "        2000",
                    "face_value": "000000100",
                    "subscr_dt": "2024/05/20 ~ 2024/05/21",
                    "pay_dt": "2024/05/23",
                    "refund_dt": "2024/05/23",
                    "list_dt": "2024/05/29",
                    "lead_mgr": "미래에셋증권",
                    "pub_bf_cap": "      145000",
                    "pub_af_cap": "      166250",
                    "assign_stk_qty": "           0",
                }
            ],
            "rt_cd": "0",
            "msg_cd": "MCA00000",
            "msg1": "정상처리 되었습니다.",
        }
        responses.add(
            responses.GET,
            f"{self.openkis_client_url}/uapi/domestic-stock/v1/ksdinfo/pub-offer",
            json=expected,
            status=200,
        )
        resp = self.openkis_client.get_ksd_public_offer_subscription(
            f_dt="20231201",
            t_dt="20240531",
            sht_cd="",
        )
        assert resp == expected

    @responses.activate
    def test_forfeited_stock(self):
        expected = {
            "output1": [
                {
                    "record_date": "20240311",
                    "sht_cd": "032800",
                    "isin_name": "판타지오",
                    "subscr_dt": "2024/04/18 ~ 2024/04/19",
                    "subscr_price": "000000205",
                    "subscr_stk_qty": "   112000000",
                    "refund_dt": "2024/04/23",
                    "list_dt": "2024/05/07",
                    "lead_mgr": "하이투자증권㈜(대표) 인",
                }
            ],
            "rt_cd": "0",
            "msg_cd": "MCA00000",
            "msg1": "정상처리 되었습니다.",
        }
        responses.add(
            responses.GET,
            f"{self.openkis_client_url}/uapi/domestic-stock/v1/ksdinfo/forfeit",
            json=expected,
            status=200,
        )

        resp = self.openkis_client.get_ksd_forfeited_stock(
            f_dt="20231201",
            t_dt="20240531",
            sht_cd="",
        )
        assert resp == expected

    @responses.activate
    def test_mandatory_deposit(self):
        expected = {
            "output1": [
                {
                    "sht_cd": "003580",
                    "isin_name": "에이치엘비글로벌",
                    "stk_qty": "      705219",
                    "depo_date": "2024/05/31 ~ 2025/05/31",
                    "depo_reason": "모집매출",
                    "tot_issue_qty_per_rate": "148.7",
                }
            ],
            "rt_cd": "0",
            "msg_cd": "MCA00000",
            "msg1": "정상처리 되었습니다.",
        }
        responses.add(
            responses.GET,
            f"{self.openkis_client_url}/uapi/domestic-stock/v1/ksdinfo/mand-deposit",
            json=expected,
            status=200,
        )
        resp = self.openkis_client.get_ksd_mandatory_deposit(
            f_dt="20240501",
            t_dt="20240531",
            sht_cd="",
        )
        assert resp == expected

    @responses.activate
    def test_right_issue(self):
        expected = {
            "output1": [
                {
                    "record_date": "20240430",
                    "sht_cd": "190410",
                    "isin_name": "엘에스아이앤디",
                    "tot_issue_stk_qty": "14770262",
                    "issue_stk_qty": "884213",
                    "fix_rate": "6.29",
                    "disc_rate": "0.00",
                    "fix_price": "32252",
                    "right_dt": "20240429",
                    "sub_term_ft": "20240528",
                    "sub_term": "2024/05/28 ~ 2024/05/29",
                    "list_date": "2024/06/12",
                    "stk_kind": "01",
                }
            ],
            "rt_cd": "0",
            "msg_cd": "MCA00000",
            "msg1": "정상처리 되었습니다.",
        }
        responses.add(
            responses.GET,
            f"{self.openkis_client_url}/uapi/domestic-stock/v1/ksdinfo/paidin-capin",
            json=expected,
            status=200,
        )
        resp = self.openkis_client.get_ksd_right_issue(
            f_dt="20240501",
            t_dt="20240531",
            sht_cd="",
            gb1="1",
        )
        assert resp == expected

    @responses.activate
    def test_bonus_issue(self):
        expected = {
            "output1": [
                {
                    "record_date": "20240522",
                    "sht_cd": "199820",
                    "isin_name": "제일일렉트릭",
                    "fix_rate": "100.00",
                    "odd_rec_price": "0",
                    "right_dt": "20240521",
                    "odd_pay_dt": "",
                    "list_date": "20240611",
                    "tot_issue_stk_qty": "11110000",
                    "issue_stk_qty": "11110000",
                    "stk_kind": "01",
                }
            ],
            "rt_cd": "0",
            "msg_cd": "MCA00000",
            "msg1": "정상처리 되었습니다.",
        }
        responses.add(
            responses.GET,
            f"{self.openkis_client_url}/uapi/domestic-stock/v1/ksdinfo/bonus-issue",
            json=expected,
            status=200,
        )
        resp = self.openkis_client.get_ksd_bonus_issue(
            f_dt="20231201",
            t_dt="20240531",
            sht_cd="",
        )

        assert resp == expected

    @responses.activate
    def test_shareholder_meeting(self):
        expected = {
            "output1": [
                {
                    "record_date": "20240531",
                    "sht_cd": "001020",
                    "isin_name": "페이퍼코리아(주)",
                    "gen_meet_dt": "2024/06/28",
                    "gen_meet_type": "임시총회",
                    "agenda": "이사선임",
                    "vote_tot_qty": "   177983313",
                },
                {
                    "record_date": "20240531",
                    "sht_cd": "060240",
                    "isin_name": "(주)룽투코리아",
                    "gen_meet_dt": "2024/06/28",
                    "gen_meet_type": "임시총회",
                    "agenda": "사내이사 선임",
                    "vote_tot_qty": "    31136323",
                },
            ],
            "rt_cd": "0",
            "msg_cd": "MCA00000",
            "msg1": "정상처리 되었습니다.",
        }

        responses.add(
            responses.GET,
            f"{self.openkis_client_url}/uapi/domestic-stock/v1/ksdinfo/sharehld-meet",
            json=expected,
            status=200,
        )
        resp = self.openkis_client.get_ksd_shareholder_meeting(
            f_dt="20240501",
            t_dt="20240531",
            sht_cd="",
        )
        assert resp == expected


if __name__ == "__main__":
    unittest.main()
