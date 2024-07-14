import time
import unittest

import pytest

from finance_clue.openkrx import OpenKrxClient


@pytest.mark.usefixtures("integration_openkrx_client")
class OpenKrxBondTestCase(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def setup(self, integration_openkrx_client: OpenKrxClient):
        self.openkrx_client = integration_openkrx_client
        time.sleep(1)

    def test_kts_daily_trade(self):
        resp = self.openkrx_client.get_kts_daily_trade(bas_dd="20240514")
        assert resp is not None

    def test_bond_daily_trade(self):
        resp = self.openkrx_client.get_bond_daily_trade(bas_dd="20240514")
        assert resp is not None

    def test_small_bond_daily_trade(self):
        resp = self.openkrx_client.get_small_bond_daily_trade(bas_dd="20240514")
        assert resp is not None
