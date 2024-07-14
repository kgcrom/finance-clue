import time
import unittest

import pytest

from finance_clue.openkrx import OpenKrxClient


@pytest.mark.usefixtures("integration_openkrx_client")
class OpenKrxStockTestCase(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def setup(self, integration_openkrx_client: OpenKrxClient):
        self.openkrx_client = integration_openkrx_client
        time.sleep(1)

    def test_kospi_daily_stock(self):
        resp = self.openkrx_client.get_kospi_stock_daily(bas_dd="20240514")

        assert resp is not None
        assert len(resp["OutBlock_1"]) == 953

    def test_kosdaq_daily_stock(self):
        resp = self.openkrx_client.get_kosdaq_stock_daily(bas_dd="20240514")

        assert resp is not None
        assert len(resp["OutBlock_1"]) == 1728

    def test_konex_daily_stock(self):
        resp = self.openkrx_client.get_konex_stock_daily(bas_dd="20240514")

        assert resp is not None
        assert len(resp["OutBlock_1"]) == 125

    def test_kospi_base_info(self):
        resp = self.openkrx_client.get_kospi_base_info(bas_dd="20240514")

        assert resp is not None
        assert len(resp["OutBlock_1"]) == 953

    def test_kosdaq_base_info(self):
        resp = self.openkrx_client.get_kosdaq_base_info(bas_dd="20240514")

        assert resp is not None
        assert len(resp["OutBlock_1"]) == 1728

    def test_konex_base_info(self):
        resp = self.openkrx_client.get_konex_base_info(bas_dd="20240514")

        assert resp is not None
        assert len(resp["OutBlock_1"]) == 1
