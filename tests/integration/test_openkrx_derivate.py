"""test openkrx 파생상품 API"""

from finance_clue.openkrx import OpenKrxClient


def test_exclude_stock_futures(integration_openkrx_client: OpenKrxClient):
    resp = integration_openkrx_client.get_exclude_stock_futures(bas_dd="20240514")

    assert resp is not None


def test_kospi_futures(integration_openkrx_client: OpenKrxClient):
    resp = integration_openkrx_client.get_kospi_futures(bas_dd="20240514")

    assert resp is not None


def test_kosdaq_futures(integration_openkrx_client: OpenKrxClient):
    resp = integration_openkrx_client.get_kosdaq_futures(bas_dd="20240514")

    assert resp is not None


def test_exclude_stock_option(integration_openkrx_client: OpenKrxClient):
    resp = integration_openkrx_client.get_exclude_stock_option(bas_dd="20240514")

    assert resp is not None


def test_kospi_option(integration_openkrx_client: OpenKrxClient):
    resp = integration_openkrx_client.get_kospi_option(bas_dd="20240514")

    assert resp is not None


def test_kosdaq_option(integration_openkrx_client: OpenKrxClient):
    resp = integration_openkrx_client.get_kosdaq_option(bas_dd="20240514")

    assert resp is not None
