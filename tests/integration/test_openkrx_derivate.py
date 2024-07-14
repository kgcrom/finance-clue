import time
import unittest

import pytest

from finance_clue.openkrx import OpenKrxClient


@pytest.mark.usefixtures("integration_openkrx_client")
class OpenKrxDerivateTestCase(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def setup(self, integration_openkrx_client: OpenKrxClient):
        self.openkrx_client = integration_openkrx_client
        time.sleep(1)

    def test_exclude_stock_futures(self):
        resp = self.openkrx_client.get_exclude_stock_futures(bas_dd="20240514")

        assert resp is not None

    def test_kospi_futures(self):
        resp = self.openkrx_client.get_kospi_futures(bas_dd="20240514")

        assert resp is not None

    def test_kosdaq_futures(self):
        resp = self.openkrx_client.get_kosdaq_futures(bas_dd="20240514")

        assert resp is not None

    def test_exclude_stock_option(self):
        resp = self.openkrx_client.get_exclude_stock_option(bas_dd="20240514")

        assert resp is not None

    def test_kospi_option(self):
        resp = self.openkrx_client.get_kospi_option(bas_dd="20240514")

        assert resp is not None

    def test_kosdaq_option(self):
        resp = self.openkrx_client.get_kosdaq_option(bas_dd="20240514")

        assert resp is not None
