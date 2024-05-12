import pytest
import responses

from stock_clue.openkis import OpenKisClient


def test_domestic_quotation_inquiry_price(integration_openkis_client: OpenKisClient):
    resp = integration_openkis_client.get_domestic_stock_quotations_price(
        fid_cond_mrkt_div_code="J", fid_input_iscd="161390"
    )

    assert resp["rt_cd"] == "0"
    assert resp["msg_cd"] == "MCA00000"
    assert resp["output"]["bstp_kor_isnm"] == "화학"
