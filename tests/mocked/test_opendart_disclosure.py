import time
import unittest

import pytest
import responses

from finance_clue.opendart import OpenDartClient


class OpenDartDisclosureCase(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def setup(
        self, mock_opendart_client: OpenDartClient, mock_opendart_client_url: str
    ):
        self.opendart_client = mock_opendart_client
        self.opendart_client_url = mock_opendart_client_url

    @responses.activate
    def test_list(self):
        expected = {
            "status": "000",
            "message": "정상",
            "page_no": 1,
            "page_count": 10,
            "total_count": 2302,
            "total_page": 231,
            "list": [
                {
                    "corp_code": "00989619",
                    "corp_name": "알테오젠",
                    "stock_code": "196170",
                    "corp_cls": "K",
                    "report_nm": "투자판단관련주요경영사항              (ALT-BB4(Tergase)테르가제주 품목 허가 승인)",
                    "rcept_no": "20240705900656",
                    "flr_nm": "알테오젠",
                    "rcept_dt": "20240705",
                    "rm": "코",
                }
            ],
        }
        responses.add(
            responses.GET,
            f"{self.opendart_client_url}/api/list.json",
            json=expected,
            status=200,
        )
        resp = self.opendart_client.get_corporate_list(
            bgn_de="20240702",
            end_de="20240705",
        )
        assert resp == expected

    @responses.activate
    def test_company(self):
        expected = {
            "status": "000",
            "message": "정상",
            "corp_code": "00258999",
            "corp_name": "삼성전자 서비스주식회사",
            "corp_name_eng": "SAMSUNNG ELECTRONICS SERVICE CO., LTD",
            "stock_name": "삼성전자서비스",
            "stock_code": "",
            "ceo_nm": "송봉섭",
            "corp_cls": "E",
            "jurir_no": "1301110049139",
            "bizr_no": "1248158485",
            "adres": "경기도 수원시 영통구 삼성로 290 (원천동)",
            "hm_url": "www.samsungsvc.co.kr",
            "ir_url": "",
            "phn_no": "031-270-2177",
            "fax_no": "031-270-2106",
            "induty_code": "95",
            "est_dt": "19981027",
            "acc_mt": "12",
        }

        responses.add(
            responses.GET,
            f"{self.opendart_client_url}/api/company.json",
            json=expected,
            status=200,
        )
        resp = self.opendart_client.get_corporate_company(corp_code="00258999")
        assert resp == expected


if __name__ == "__main__":
    unittest.main()
