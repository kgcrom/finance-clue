import time
import unittest

import pytest

from finance_clue.opendart import OpenDartClient


@pytest.mark.usefixtures("integration_opendart_client")
class OpenDartDisclosureCase(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def setup(self, integration_opendart_client: OpenDartClient):
        self.opendart_client = integration_opendart_client
        time.sleep(1)

    def test_list(self):
        resp = self.opendart_client.get_corporate_list(
            bgn_de="20240702",
            end_de="20240705",
        )

        example = {
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
        assert resp is not None

    def test_company(self):
        resp = self.opendart_client.get_corporate_company(corp_code="00258999")

        example = {
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
        assert resp is not None

    def test_document(self):
        resp = self.opendart_client.get_corporate_document(rcept_no="20240516001421")
        zip_file_path = "corp_code.zip"

        with open(zip_file_path, "wb") as zip_file:
            for chunk in resp:
                zip_file.write(chunk)

        assert resp is not None

    def test_corp_code(self):
        resp = self.opendart_client.download_corporate_code()
        zip_file_path = "corp_code.zip"

        with open(zip_file_path, "wb") as zip_file:
            for chunk in resp:
                zip_file.write(chunk)

        assert resp is not None


if __name__ == "__main__":
    unittest.main()
