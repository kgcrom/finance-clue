# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------
"""Customize generated code here.

Follow our quickstart for examples: https://aka.ms/azsdk/python/dpcodegen/python/customize
"""
import json
import os
from dataclasses import dataclass
from datetime import datetime
from typing import List, Union, Awaitable

from azure.core.credentials import AccessToken
from azure.core.pipeline import PipelineRequest
from azure.core.pipeline.policies import SansIOHTTPPolicy
from azure.core.pipeline.policies._base import HTTPRequestType

from stock_clue.openkis import GenOpenKisClient


@dataclass
class CredentialInfo:
    app_key: str
    app_secret: str
    grant_type: str

    access_token: str
    access_token_token_expired: datetime
    token_type: str
    expires_in: int


access_token_file = "stock_clue.json"


def _write_access_token(resp):
    write_obj = {}
    if os.path.exists(access_token_file):
        f = open(access_token_file, "r")
        write_obj = json.load(f)
        f.close()

    write_obj["open_kis"] = resp
    with open(access_token_file, "w") as f:
        json.dump(write_obj, f)


class CustomCredentials:
    def __init__(
            self,
            app_key: str,
            app_secret: str,
    ):
        self.app_key = app_key
        self.app_secret = app_secret
        self.grant_type = "client_credentials"
        self.access_token = None
        self.access_token_token_expired = None
        self.token_type = None
        self.expires_in = 0

    def get_token(self, *args, **kwargs) -> AccessToken:
        return AccessToken(self.access_token, self.expires_in)

    def get_credential_info(self, *args, **kwargs) -> CredentialInfo:
        return CredentialInfo(
            app_key=self.app_key,
            app_secret=self.app_secret,
            grant_type=self.grant_type,
            access_token=self.access_token,
            access_token_token_expired=self.access_token_token_expired,
            token_type=self.token_type,
            expires_in=self.expires_in,
        )

    def update_token(self, *args, **kwargs):
        """kwargs: access_token, access_token_token_expired, token_type, expires_in"""
        self.access_token = kwargs["access_token"]
        self.access_token_token_expired = kwargs["access_token_token_expired"]
        self.token_type = kwargs["token_type"]
        self.expires_in = kwargs["expires_in"]


class CustomAuthenticationPolicy(SansIOHTTPPolicy):

    def __init__(self, credentials: CustomCredentials):
        self._credentials = credentials

    def on_request(self, request: PipelineRequest[HTTPRequestType]) -> Union[None, Awaitable[None]]:
        credential_info = self._credentials.get_credential_info()
        request.http_request.headers[
            "authorization"] = f"{credential_info.token_type} {credential_info.access_token}"
        request.http_request.headers["appkey"] = f"{credential_info.app_key}"
        request.http_request.headers["appsecret"] = f"{credential_info.app_secret}"
        return super().on_request(request)


class OpenKisClient(GenOpenKisClient):

    def __init__(self, app_key: str, app_secret: str, is_sandbox: bool = False, **kwargs):
        self._credential = CustomCredentials(app_key, app_secret)
        if "endpoint" not in kwargs:
            endpoint = (
                "https://openapivts.koreainvestment.com:29443"
                if is_sandbox
                else "https://openapi.koreainvestment.com:9443"
            )
            kwargs["endpoint"] = endpoint

        kwargs["authentication_policy"] = CustomAuthenticationPolicy(self._credential)
        super().__init__(credential=self._credential, **kwargs)

    def init(self):
        if os.path.exists(access_token_file):
            with open(access_token_file, "r") as f:
                token_obj = json.load(f)
                access_token = token_obj["open_kis"]

                # TODO 시간 지났으면 갱신하기
                self._credential.update_token(access_token=access_token["access_token"],
                                              access_token_token_expired=datetime.fromisoformat(
                                                  access_token["access_token_token_expired"]),
                                              token_type=access_token["token_type"],
                                              expires_in=access_token["expires_in"])

        else:
            resp = self.get_access_token({
                "appkey": self._credential.app_key,
                "appsecret": self._credential.app_secret,
                "grant_type": self._credential.grant_type,
            })

            _write_access_token(resp)
            self._credential.update_token(access_token=resp["access_token"],
                                          access_token_token_expired=datetime.fromisoformat(
                                              resp["access_token_token_expired"]),
                                          token_type=resp["token_type"],
                                          expires_in=resp["expires_in"])


def patch_sdk():
    """Do not remove from this file.

    `patch_sdk` is a last resort escape hatch that allows you to do customizations
    you can't accomplish using the techniques described in
    https://aka.ms/azsdk/python/dpcodegen/python/customize
    """


__all__: List[str] = ["OpenKisClient"]  # Add all objects you want publicly available to users at this package level
