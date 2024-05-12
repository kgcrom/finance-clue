# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------
"""Customize generated code here.

Follow our quickstart for examples: https://aka.ms/azsdk/python/dpcodegen/python/customize
"""
from dataclasses import dataclass
from datetime import datetime
from typing import List

from azure.core.credentials import AccessToken

from stock_clue.openkis import GenOpenKisClient


@dataclass
class CredentialInfo:
    access_token: str
    access_token_token_expired: datetime
    expires_in: int


class CustomCredentials:
    def __init__(
            self, app_key: str, app_secret: str,
    ):
        self._app_key = app_key
        self._app_secret = app_secret
        self._grant_type = "client_credentials"
        self._access_token = ""
        self._access_token_token_expired = ""
        self._token_type = "Bearer"
        self._expires_in = 8600

    def get_token(self, *args, **kwargs) -> AccessToken:
        return AccessToken(self._access_token, self._expires_in)


class OpenKisClient(GenOpenKisClient):

    def __init__(self, app_key: str, app_secret: str, is_sandbox: bool = False, **kwargs):
        credential = CustomCredentials(app_key, app_secret)
        if not kwargs["endpoint"]:
            endpoint = "https://openapivts.koreainvestment.com:29443" if is_sandbox else "https://openapi.koreainvestment.com:9443"
            kwargs["endpoint"] = endpoint

        super().__init__(credential=credential, **kwargs)


def patch_sdk():
    """Do not remove from this file.

    `patch_sdk` is a last resort escape hatch that allows you to do customizations
    you can't accomplish using the techniques described in
    https://aka.ms/azsdk/python/dpcodegen/python/customize
    """


__all__: List[str] = ["OpenKisClient"]  # Add all objects you want publicly available to users at this package level
