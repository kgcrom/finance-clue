from finance_clue.openkrx import OpenKrxClient


def test_instrument_etf(integration_openkrx_client: OpenKrxClient):
    resp = integration_openkrx_client.get_etf_daily_trade(bas_dd="20240514")

    assert resp is not None
    assert len(resp["OutBlock_1"]) == 860


def test_instrument_etn(integration_openkrx_client: OpenKrxClient):
    resp = integration_openkrx_client.get_etn_daily_trade(bas_dd="20240514")

    assert resp is not None
    assert len(resp["OutBlock_1"]) == 382


def test_instrument_elw(integration_openkrx_client: OpenKrxClient):
    resp = integration_openkrx_client.get_elw_daily_trade(bas_dd="20240514")

    assert resp is not None
    assert len(resp["OutBlock_1"]) == 3992
