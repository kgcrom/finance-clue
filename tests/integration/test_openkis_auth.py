"""Integration tests OpenKIS 권한"""

from os import environ

from stock_clue.openkis import OpenKisClient


def test_get_access_token(integration_openkis_client: OpenKisClient):
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
