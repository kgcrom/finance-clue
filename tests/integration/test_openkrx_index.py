import time
import unittest

import pytest

from finance_clue.openkrx import OpenKrxClient


@pytest.mark.usefixtures("integration_openkrx_client")
class OpenKrxIndexTestCase(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def setup(self, integration_openkrx_client: OpenKrxClient):
        self.openkrx_client = integration_openkrx_client
        time.sleep(1)

    def test_krx_daily_index(self):
        resp = self.openkrx_client.get_krx_daily_index(bas_dd="20240513")

        assert resp is not None
        assert len(resp["OutBlock_1"]) == 28
        assert resp["OutBlock_1"][0]["IDX_CLSS"] == "KRX"

    def test_kospi_daily_index(self):
        resp = self.openkrx_client.get_kospi_daily_index(bas_dd="20240513")

        assert resp is not None
        assert len(resp["OutBlock_1"]) == 47
        assert resp["OutBlock_1"][0]["IDX_CLSS"] == "KOSPI"

    def test_kosdaq_daily_index(self):
        resp = self.openkrx_client.get_kosdaq_daily_index(bas_dd="20240513")

        assert resp is not None
        assert resp["OutBlock_1"] is not None
        assert type(resp["OutBlock_1"]) == list

    def test_bond_daily_index(self):
        resp = self.openkrx_client.get_bond_daily_index(bas_dd="20240513")

        assert resp is not None

    def test_derivation_daily_index(self):
        resp = self.openkrx_client.get_derivatives_daily_index(bas_dd="20240513")

        assert resp is not None
        assert resp["OutBlock_1"] is not None
        assert type(resp["OutBlock_1"]) == list
