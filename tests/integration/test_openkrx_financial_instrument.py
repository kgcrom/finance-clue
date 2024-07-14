import time
import unittest

import pytest

from finance_clue.openkrx import OpenKrxClient


@pytest.mark.usefixtures("integration_openkrx_client")
class OpenKrxFinancialInstrumentTestCase(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def setup(self, integration_openkrx_client: OpenKrxClient):
        self.openkrx_client = integration_openkrx_client
        time.sleep(1)

    def test_instrument_etf(self):
        resp = self.openkrx_client.get_etf_daily_trade(bas_dd="20240514")

        assert resp is not None
        assert len(resp["OutBlock_1"]) == 860

    def test_instrument_etn(self):
        resp = self.openkrx_client.get_etn_daily_trade(bas_dd="20240514")

        assert resp is not None
        assert len(resp["OutBlock_1"]) == 382

    def test_instrument_elw(self):
        resp = self.openkrx_client.get_elw_daily_trade(bas_dd="20240514")

        assert resp is not None
        assert len(resp["OutBlock_1"]) == 3992
