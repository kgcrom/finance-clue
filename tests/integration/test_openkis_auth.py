"""Integration tests OpenKIS 권한"""

from os import environ
import time

from finance_clue.openkis import OpenKisClient


# OpenKIS token 재생성은 1분에 1회 호출만 가능하다.
# OpenKis 인스턴스 만들면 내부적으로 토큰 생성
def test_get_access_and_revoke_token(integration_openkis_client: OpenKisClient):
    app_key = environ.get("OPENKIS_APP_KEY", None)
    app_secret = environ.get("OPENKIS_APP_SECRET", None)
    resp = integration_openkis_client.get_access_token(
        {
            "appkey": app_key,
            "appsecret": app_secret,
            "grant_type": "client_credentials",
        }
    )

    assert resp["token_type"] == "Bearer"
    assert resp["expires_in"] == 86400

    time.sleep(3)
    access_token = resp["access_token"]
    revoke_resp = integration_openkis_client.revoke_access_token(
        {
            "appkey": app_key,
            "appsecret": app_secret,
            "token": access_token,
        }
    )

    assert revoke_resp["code"] == 200
    assert revoke_resp["message"] == "접근토큰 폐기에 성공하였습니다."


def test_get_hash_key(integration_openkis_client: OpenKisClient):
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

    resp = integration_openkis_client.get_hash_key(data)

    assert resp["HASH"] is not None
    assert resp["BODY"] is not None
