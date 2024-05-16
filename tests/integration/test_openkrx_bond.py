from finance_clue.openkrx import OpenKrxClient


def test_kts_daily_trade(integration_openkrx_client: OpenKrxClient):
    resp = integration_openkrx_client.get_kts_daily_trade(bas_dd="20240514")
    assert resp is not None


def test_bond_daily_trade(integration_openkrx_client: OpenKrxClient):
    resp = integration_openkrx_client.get_bond_daily_trade(bas_dd="20240514")
    assert resp is not None


def test_small_bond_daily_trade(integration_openkrx_client: OpenKrxClient):
    resp = integration_openkrx_client.get_small_bond_daily_trade(bas_dd="20240514")
    assert resp is not None
