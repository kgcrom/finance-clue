"""pytest tests for openkis auth"""

import responses

from finance_clue.openkis import OpenKisClient


@responses.activate
def test_get_access_token(
    mock_openkis_client: OpenKisClient, mock_openkis_client_url: str
):
    expected = {
        "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJ0b2tlbiIsImF1ZCI6ImMwNzM1NTYzLTA1MjctNDNhZS05ODRiLTJiNWI1ZWZmOWYyMyIsImlzcyI6InVub2d3IiwiZXhwIjoxNjQ5NzUxMTAwLCJpYXQiOjE2NDE5NzUxMDAsImp0aSI6IkJTZlM0QUtSSnpRVGpmdHRtdXZlenVQUTlKajc3cHZGdjBZVyJ9.Oyt_C639yUjWmRhymlszgt6jDo8fvIKkkxH1mMngunV1T15SCC4I3Xe6MXxcY23DXunzBfR1uI0KXXXXXXXXXX",
        "access_token_token_expired": "2023-12-22 08:16:59",
        "token_type": "Bearer",
        "expires_in": 86400,
    }

    responses.add(
        responses.POST,
        f"{mock_openkis_client_url}/oauth2/tokenP",
        json=expected,
        status=200,
    )

    resp = mock_openkis_client.get_access_token(
        {
            "appkey": "test",
            "appsecret": "test",
        }
    )

    assert resp == expected


@responses.activate
def test_revoke_access_token(
    mock_openkis_client: OpenKisClient,
    mock_openkis_client_url: str,
):
    expected = {"code": 200, "message": "접근토큰 폐기에 성공하였습니다"}

    responses.add(
        responses.POST,
        f"{mock_openkis_client_url}/oauth2/revokeP",
        json=expected,
        status=200,
    )

    resp = mock_openkis_client.revoke_access_token(
        {
            "appkey": "test",
            "appsecret": "test",
            "token": "token",
        }
    )

    assert resp == expected


@responses.activate
def test_hash_key(
    mock_openkis_client: OpenKisClient,
    mock_openkis_client_url: str,
):
    expected = {
        "BODY": {
            "ORD_PRCS_DVSN_CD": "02",
            "CANO": "계좌번호",
            "ACNT_PRDT_CD": "03",
            "SLL_BUY_DVSN_CD": "02",
            "SHTN_PDNO": "101S06",
            "ORD_QTY": "1",
            "UNIT_PRICE": "370",
            "NMPR_TYPE_CD": "",
            "KRX_NMPR_CNDT_CD": "",
            "CTAC_TLNO": "",
            "FUOP_ITEM_DVSN_CD": "",
            "ORD_DVSN_CD": "02",
        },
        "HASH": "8b84068222a49302f7ef58226d90403f62e216828f8103465f900de0e7be2f0f",
    }

    responses.add(
        responses.POST,
        f"{mock_openkis_client_url}/uapi/hashkey",
        json=expected,
        status=200,
    )

    data = {
        "ORD_PRCS_DVSN_CD": "02",
        "CANO": "계좌번호",
        "ACNT_PRDT_CD": "03",
        "SLL_BUY_DVSN_CD": "02",
        "SHTN_PDNO": "101S06",
        "ORD_QTY": "1",
        "UNIT_PRICE": "370",
        "NMPR_TYPE_CD": "",
        "KRX_NMPR_CNDT_CD": "",
        "CTAC_TLNO": "",
        "FUOP_ITEM_DVSN_CD": "",
        "ORD_DVSN_CD": "02",
    }

    resp = mock_openkis_client.get_hash_key(data)

    assert resp == expected
