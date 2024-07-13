import time
import unittest

import pytest

from finance_clue.opendart import OpenDartClient


@pytest.mark.usefixtures("integration_opendart_client")
class OpenDartShareDisclosureCase(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def setup(self, integration_opendart_client: OpenDartClient):
        self.opendart_client = integration_opendart_client
        time.sleep(1)

    def test_largest_shareholder_stock(self):
        resp = self.opendart_client.get_largest_shareholder_stock(corp_code="00126380")

        example = {
            "status": "000",
            "message": "정상",
            "list": [
                {
                    "rcept_no": "20220722000492",
                    "rcept_dt": "2022-07-22",
                    "corp_code": "00126380",
                    "corp_name": "삼성전자",
                    "report_tp": "일반",
                    "repror": "삼성물산",
                    "stkqy": "1,241,273,657",
                    "stkqy_irds": "142,632",
                    "stkrt": "20.79",
                    "stkrt_irds": "0.00",
                    "ctr_stkqy": "98,282,587",
                    "ctr_stkrt": "1.65",
                    "report_resn": "- 보유주식수 변동\n- 보유주식등에 관한 계약의 변경",
                }
            ],
        }
        assert resp is not None

    def test_executive_stock(self):
        resp = self.opendart_client.get_executive_major_stock(corp_code="00126380")

        example = {
            "status": "000",
            "message": "정상",
            "list": [
                {
                    "rcept_no": "20220719000004",
                    "rcept_dt": "2022-07-19",
                    "corp_code": "00126380",
                    "corp_name": "삼성전자",
                    "repror": "박상훈",
                    "isu_exctv_rgist_at": "비등기임원",
                    "isu_exctv_ofcps": "상무",
                    "isu_main_shrholdr": "-",
                    "sp_stock_lmp_cnt": "563",
                    "sp_stock_lmp_irds_cnt": "563",
                    "sp_stock_lmp_rate": "0.00",
                    "sp_stock_lmp_irds_rate": "0.00",
                }
            ],
        }
        assert resp is not None
