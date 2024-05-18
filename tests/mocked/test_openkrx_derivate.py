import responses

from finance_clue.openkrx import OpenKrxClient


@responses.activate
def test_exclude_stock_futures(
    mock_openkrx_client: OpenKrxClient, mock_openkrx_client_url: str
):
    expected = {
        "OutBlock_1": [
            {
                "BAS_DD": "20200414",
                "PROD_NM": "코스피200 선물",
                "MKT_NM": "야간",
                "ISU_CD": "101Q6000",
                "ISU_NM": "코스피200 F 202006 (야간)",
                "TDD_CLSPRC": "-",
                "CMPPREVDD_PRC": "-",
                "TDD_OPNPRC": "-",
                "TDD_HGPRC": "-",
                "TDD_LWPRC": "-",
                "SPOT_PRC": "247.45",
                "SETL_PRC": "0.00",
                "ACC_TRDVOL": "0",
                "ACC_TRDVAL": "0",
                "ACC_OPNINT_QTY": "324159",
            }
        ]
    }

    responses.add(
        responses.GET,
        f"{mock_openkrx_client_url}/svc/apis/drv/fut_bydd_trd",
        json=expected,
        status=200,
    )

    resp = mock_openkrx_client.get_exclude_stock_futures(bas_dd="20240514")
    assert resp == expected


@responses.activate
def test_kospi_futures(
    mock_openkrx_client: OpenKrxClient, mock_openkrx_client_url: str
):
    expected = {
        "OutBlock_1": [
            {
                "BAS_DD": "20200414",
                "PROD_NM": "코스피200 선물",
                "MKT_NM": "야간",
                "ISU_CD": "101Q6000",
                "ISU_NM": "코스피200 F 202006 (야간)",
                "TDD_CLSPRC": "-",
                "CMPPREVDD_PRC": "-",
                "TDD_OPNPRC": "-",
                "TDD_HGPRC": "-",
                "TDD_LWPRC": "-",
                "SPOT_PRC": "247.45",
                "SETL_PRC": "0.00",
                "ACC_TRDVOL": "0",
                "ACC_TRDVAL": "0",
                "ACC_OPNINT_QTY": "324159",
            }
        ]
    }

    responses.add(
        responses.GET,
        f"{mock_openkrx_client_url}/svc/apis/drv/eqsfu_stk_bydd_trd",
        json=expected,
        status=200,
    )

    resp = mock_openkrx_client.get_kospi_futures(bas_dd="20240514")
    assert resp == expected


@responses.activate
def test_kosdaq_futures(
    mock_openkrx_client: OpenKrxClient, mock_openkrx_client_url: str
):
    expected = {
        "OutBlock_1": [
            {
                "BAS_DD": "20200414",
                "PROD_NM": "코스피200 선물",
                "MKT_NM": "야간",
                "ISU_CD": "101Q6000",
                "ISU_NM": "코스피200 F 202006 (야간)",
                "TDD_CLSPRC": "-",
                "CMPPREVDD_PRC": "-",
                "TDD_OPNPRC": "-",
                "TDD_HGPRC": "-",
                "TDD_LWPRC": "-",
                "SPOT_PRC": "247.45",
                "SETL_PRC": "0.00",
                "ACC_TRDVOL": "0",
                "ACC_TRDVAL": "0",
                "ACC_OPNINT_QTY": "324159",
            }
        ]
    }

    responses.add(
        responses.GET,
        f"{mock_openkrx_client_url}/svc/apis/drv/eqkfu_ksq_bydd_trd",
        json=expected,
        status=200,
    )

    resp = mock_openkrx_client.get_kosdaq_futures(bas_dd="20240514")
    assert resp == expected


@responses.activate
def test_exclude_stock_option(
    mock_openkrx_client: OpenKrxClient, mock_openkrx_client_url: str
):
    expected = {
        "OutBlock_1": [
            {
                "BAS_DD": "20200414",
                "PROD_NM": "코스피200 옵션",
                "RGHT_TP_NM": "CALL",
                "ISU_CD": "201Q5160",
                "ISU_NM": "코스피200 C 202005 160.0",
                "TDD_CLSPRC": "84.75",
                "CMPPREVDD_PRC": "1.20",
                "TDD_OPNPRC": "84.85",
                "TDD_HGPRC": "84.85",
                "TDD_LWPRC": "84.75",
                "IMP_VOLT": "3.00",
                "NXTDD_BAS_PRC": "84.75",
                "ACC_TRDVOL": "4",
                "ACC_TRDVAL": "84812500",
                "ACC_OPNINT_QTY": "67",
            }
        ]
    }

    responses.add(
        responses.GET,
        f"{mock_openkrx_client_url}/svc/apis/drv/opt_bydd_trd",
        json=expected,
        status=200,
    )

    resp = mock_openkrx_client.get_exclude_stock_option(bas_dd="20240514")
    assert resp == expected


@responses.activate
def test_kospi_option(mock_openkrx_client: OpenKrxClient, mock_openkrx_client_url: str):
    expected = {
        "OutBlock_1": [
            {
                "BAS_DD": "20200414",
                "PROD_NM": "코스피200 옵션",
                "RGHT_TP_NM": "CALL",
                "ISU_CD": "201Q5160",
                "ISU_NM": "코스피200 C 202005 160.0",
                "TDD_CLSPRC": "84.75",
                "CMPPREVDD_PRC": "1.20",
                "TDD_OPNPRC": "84.85",
                "TDD_HGPRC": "84.85",
                "TDD_LWPRC": "84.75",
                "IMP_VOLT": "3.00",
                "NXTDD_BAS_PRC": "84.75",
                "ACC_TRDVOL": "4",
                "ACC_TRDVAL": "84812500",
                "ACC_OPNINT_QTY": "67",
            }
        ]
    }

    responses.add(
        responses.GET,
        f"{mock_openkrx_client_url}/svc/apis/drv/eqsop_bydd_trd",
        json=expected,
        status=200,
    )

    resp = mock_openkrx_client.get_kospi_option(bas_dd="20240514")
    assert resp == expected


@responses.activate
def test_kosdaq_option(
    mock_openkrx_client: OpenKrxClient, mock_openkrx_client_url: str
):
    expected = {
        "OutBlock_1": [
            {
                "BAS_DD": "20200414",
                "PROD_NM": "코스피200 옵션",
                "RGHT_TP_NM": "CALL",
                "ISU_CD": "201Q5160",
                "ISU_NM": "코스피200 C 202005 160.0",
                "TDD_CLSPRC": "84.75",
                "CMPPREVDD_PRC": "1.20",
                "TDD_OPNPRC": "84.85",
                "TDD_HGPRC": "84.85",
                "TDD_LWPRC": "84.75",
                "IMP_VOLT": "3.00",
                "NXTDD_BAS_PRC": "84.75",
                "ACC_TRDVOL": "4",
                "ACC_TRDVAL": "84812500",
                "ACC_OPNINT_QTY": "67",
            }
        ]
    }

    responses.add(
        responses.GET,
        f"{mock_openkrx_client_url}/svc/apis/drv/eqkop_bydd_trd",
        json=expected,
        status=200,
    )

    resp = mock_openkrx_client.get_kosdaq_option(bas_dd="20240514")
    assert resp == expected
