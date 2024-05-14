from finance_clue.openkrx import OpenKrxClient


def test_krx_daily_index_quotation(integration_openkrx_client: OpenKrxClient):
    resp = integration_openkrx_client.get_krx_daily_index_quotation(bas_dd="20240513")

    assert resp is not None
    assert len(resp["OutBlock_1"]) == 28
