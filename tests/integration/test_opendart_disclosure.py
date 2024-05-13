"""Integration tests OpenDartClient 공시정보"""

from finance_clue.opendart import OpenDartClient


def test_list_disclosure(integration_opendart_client: OpenDartClient):
    resp = integration_opendart_client.list_disclosure_info(
        bgn_de="20210101",
        end_de="20210131",
        page_no="1",
        page_count="10",
    )

    assert resp["status"] == "000"
    assert len(resp["list"]) == 10
