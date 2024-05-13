import pytest
import responses

from finance_clue.openkis import OpenKisClient


def test_domestic_quotation_inquiry_price(integration_openkis_client: OpenKisClient):
    """국내 주식 시세 조회 integration test"""
    resp = integration_openkis_client.get_domestic_stock_quotations_price(
        fid_cond_mrkt_div_code="J", fid_input_iscd="161390"
    )

    assert resp["rt_cd"] == "0"
    assert resp["msg_cd"] == "MCA00000"
    assert resp["output"]["bstp_kor_isnm"] == "화학"


def test_domestic_quotation_inquiry_daily_price(
    integration_openkis_client: OpenKisClient,
):
    """국내 주식 현재가 일자별 조회 integration test"""
    resp = integration_openkis_client.get_domestic_stock_quotations_daily_price(
        fid_cond_mrkt_div_code="J",
        fid_input_iscd="161390",
        fid_period_div_code="D",
        fid_org_adj_prc="0",
    )

    assert resp["rt_cd"] == "0"
    assert resp["msg_cd"] == "MCA00000"
    output = resp["output"]
    assert len(output) == 30
    assert output[0]["acml_prtt_rate"] == "1.00"
