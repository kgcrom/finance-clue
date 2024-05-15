from finance_clue.openkrx import OpenKrxClient


def test_krx_daily_index_quotation(integration_openkrx_client: OpenKrxClient):
    resp = integration_openkrx_client.get_krx_daily_index_quotation(bas_dd="20240513")

    assert resp is not None
    assert len(resp["OutBlock_1"]) == 28
    assert resp["OutBlock_1"][0]["IDX_CLSS"] == "KRX"


def test_kospi_daily_index_quotation(integration_openkrx_client: OpenKrxClient):
    resp = integration_openkrx_client.get_kospi_daily_index_quotation(bas_dd="20240513")

    assert resp is not None
    assert len(resp["OutBlock_1"]) == 47
    assert resp["OutBlock_1"][0]["IDX_CLSS"] == "KOSPI"


def test_kosdaq_daily_index_quotation(integration_openkrx_client: OpenKrxClient):
    resp = integration_openkrx_client.get_kosdaq_daily_index_quotation(
        bas_dd="20240513"
    )

    assert resp is not None
    assert len(resp["OutBlock_1"]) == 52
    assert resp["OutBlock_1"][0]["IDX_CLSS"] == "KOSDAQ"


def test_bond_daily_index_quotation(integration_openkrx_client: OpenKrxClient):
    resp = integration_openkrx_client.get_bond_daily_index_quotation(bas_dd="20240513")

    assert resp is not None


def test_derivation_daily_index_quotation(integration_openkrx_client: OpenKrxClient):
    resp = integration_openkrx_client.get_derivatives_daily_index_quotation(
        bas_dd="20240513"
    )

    assert resp is not None
    assert len(resp["OutBlock_1"]) == 222
    assert resp["OutBlock_1"][0]["IDX_CLSS"] == "선물지수"
