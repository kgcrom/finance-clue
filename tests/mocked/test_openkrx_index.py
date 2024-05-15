"""mocked test for OpenKrxClient"""

import responses

from finance_clue.openkrx import OpenKrxClient


@responses.activate
def test_krx_daily_index_quotation(
        mock_openkrx_client: OpenKrxClient, mock_openkrx_client_url: str
):
    expected = _generate_expected("KRX")

    responses.add(
        responses.GET,
        f"{mock_openkrx_client_url}/svc/apis/idx/krx_dd_trd",
        json=expected,
        status=200,
    )

    resp = mock_openkrx_client.get_krx_daily_index_quotation(
        bas_dd="20240514",
    )

    assert resp == expected


@responses.activate
def test_kospi_daily_index_quotation(
        mock_openkrx_client: OpenKrxClient, mock_openkrx_client_url: str
):
    expected = _generate_expected("KRX")

    responses.add(
        responses.GET,
        f"{mock_openkrx_client_url}/svc/apis/idx/kospi_dd_trd",
        json=expected,
        status=200,
    )

    resp = mock_openkrx_client.get_kospi_daily_index_quotation(
        bas_dd="20240514",
    )

    assert resp == expected


@responses.activate
def test_kosdaq_daily_index_quotation(
        mock_openkrx_client: OpenKrxClient, mock_openkrx_client_url: str
):
    expected = _generate_expected("KRX")

    responses.add(
        responses.GET,
        f"{mock_openkrx_client_url}/svc/apis/idx/kosdaq_dd_trd",
        json=expected,
        status=200,
    )

    resp = mock_openkrx_client.get_kosdaq_daily_index_quotation(
        bas_dd="20240514",
    )

    assert resp == expected


def _generate_expected(idx_class: str):
    return {
        "OutBlock_1": [
            {
                "BAS_DD": "20200414",
                "IDX_CLSS": idx_class,
                "IDX_NM": "KTOP 30",
                "CLSPRC_IDX": "6250.82",
                "CMPPREVDD_IDX": "113.20",
                "FLUC_RT": "1.84",
                "OPNPRC_IDX": "6225.70",
                "HGPRC_IDX": "6271.00",
                "LWPRC_IDX": "6182.54",
                "ACC_TRDVOL": "38188565",
                "ACC_TRDVAL": "2722079713896",
                "MKTCAP": "676169353869620",
            }
        ]
    }
