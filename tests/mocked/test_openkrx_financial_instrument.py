import responses

from finance_clue.openkrx import OpenKrxClient


@responses.activate
def test_instrument_etf(
    mock_openkrx_client: OpenKrxClient, mock_openkrx_client_url: str
):
    expected = {
        "OutBlock_1": [
            {
                "BAS_DD": "20240514",
                "ISU_CD": "580048",
                "ISU_NM": "KB CSI 300 ETN",
                "TDD_CLSPRC": "8880",
                "CMPPREVDD_PRC": "-10",
                "FLUC_RT": "-0.11",
                "PER1SECU_INDIC_VAL": "8868.86",
                "TDD_OPNPRC": "0",
                "TDD_HGPRC": "0",
                "TDD_LWPRC": "0",
                "ACC_TRDVOL": "0",
                "ACC_TRDVAL": "0",
                "MKTCAP": "17760000000",
                "INDIC_VAL_AMT": "17737720000",
                "LIST_SHRS": "2000000",
                "IDX_IND_NM": "CSI 300 NTR",
                "OBJ_STKPRC_IDX": "4937.52",
                "CMPPREVDD_IDX": "-9.82",
                "FLUC_RT_IDX": "-0.20",
            }
        ]
    }

    responses.add(
        responses.GET,
        f"{mock_openkrx_client_url}/svc/apis/etp/etf_bydd_trd",
        json=expected,
        status=200,
    )

    resp = mock_openkrx_client.get_etf_daily_trade(bas_dd="20240514")

    assert resp == expected


@responses.activate
def test_instrument_etn(
    mock_openkrx_client: OpenKrxClient, mock_openkrx_client_url: str
):
    expected = {
        "OutBlock_1": [
            {
                "BAS_DD": "20200414",
                "ISU_CD": "500052",
                "ISU_NM": "신한 FnGuide 5G 테마주 ETN",
                "TDD_CLSPRC": "9470",
                "CMPPREVDD_PRC": "495",
                "FLUC_RT": "5.52",
                "PER1SECU_INDIC_VAL": "9520.12",
                "TDD_OPNPRC": "8975",
                "TDD_HGPRC": "9525",
                "TDD_LWPRC": "8975",
                "ACC_TRDVOL": "14966",
                "ACC_TRDVAL": "140777645",
                "MKTCAP": "9470000000",
                "INDIC_VAL_AMT": "9520120000",
                "LIST_SHRS": "1000000",
                "IDX_IND_NM": "FnGuide 5G 테마주 지수",
                "OBJ_STKPRC_IDX": "-",
                "CMPPREVDD_IDX": "-",
                "FLUC_RT_IDX": "-",
            }
        ]
    }

    responses.add(
        responses.GET,
        f"{mock_openkrx_client_url}/svc/apis/etp/etn_bydd_trd",
        json=expected,
        status=200,
    )

    resp = mock_openkrx_client.get_etn_daily_trade(bas_dd="20240514")

    assert resp == expected


@responses.activate
def test_instrument_elw(
    mock_openkrx_client: OpenKrxClient, mock_openkrx_client_url: str
):
    expected = {
        "OutBlock_1": [
            {
                "BAS_DD": "20240514",
                "ISU_CD": "58J684",
                "ISU_NM": "KBJ684네이버콜",
                "TDD_CLSPRC": "10",
                "CMPPREVDD_PRC": "0",
                "TDD_OPNPRC": "0",
                "TDD_HGPRC": "0",
                "TDD_LWPRC": "0",
                "ACC_TRDVOL": "0",
                "ACC_TRDVAL": "0",
                "MKTCAP": "135000000",
                "LIST_SHRS": "13500000",
                "ULY_NM": "NAVER",
                "ULY_PRC": "184,400",
                "CMPPREVDD_PRC_ULY": "100",
                "FLUC_RT_ULY": "0.05",
            }
        ]
    }

    responses.add(
        responses.GET,
        f"{mock_openkrx_client_url}/svc/apis/etp/elw_bydd_trd",
        json=expected,
        status=200,
    )

    resp = mock_openkrx_client.get_elw_daily_trade(bas_dd="20240514")

    assert resp == expected
