from finance_clue.openkrx import OpenKrxClient


def test_kospi_daily_stock(integration_openkrx_client: OpenKrxClient):
    resp = integration_openkrx_client.get_kospi_stock_daily(bas_dd=20240514)

    assert resp is not None
    assert len(resp["OutBlock_1"]) == 953


def test_kosdaq_daily_stock(integration_openkrx_client: OpenKrxClient):
    resp = integration_openkrx_client.get_kosdaq_stock_daily(bas_dd=20240514)

    assert resp is not None
    assert len(resp["OutBlock_1"]) == 1728


def test_konex_daily_stock(integration_openkrx_client: OpenKrxClient):
    resp = integration_openkrx_client.get_konex_stock_daily(bas_dd=20240514)

    assert resp is not None
    assert len(resp["OutBlock_1"]) == 125
