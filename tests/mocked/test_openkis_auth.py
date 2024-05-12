"""pytest tests for openkis auth"""
import responses

from stock_clue.openkis import OpenKisClient


@responses.activate
def test_get_access_token(mock_openkis_client: OpenKisClient, mock_openkis_client_url: str):
    expected = {
        "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJ0b2tlbiIsImF1ZCI6ImMwNzM1NTYzLTA1MjctNDNhZS05ODRiLTJiNWI1ZWZmOWYyMyIsImlzcyI6InVub2d3IiwiZXhwIjoxNjQ5NzUxMTAwLCJpYXQiOjE2NDE5NzUxMDAsImp0aSI6IkJTZlM0QUtSSnpRVGpmdHRtdXZlenVQUTlKajc3cHZGdjBZVyJ9.Oyt_C639yUjWmRhymlszgt6jDo8fvIKkkxH1mMngunV1T15SCC4I3Xe6MXxcY23DXunzBfR1uI0KXXXXXXXXXX",
        "access_token_token_expired": "2023-12-22 08:16:59",
        "token_type": "Bearer",
        "expires_in": 86400
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
        })

    assert resp == expected
