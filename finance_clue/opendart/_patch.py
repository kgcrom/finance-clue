# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------
"""Customize generated code here.

Follow our quickstart for examples: https://aka.ms/azsdk/python/dpcodegen/python/customize
"""
import os
from typing import List, Union, Awaitable

from azure.core.credentials import AccessToken
from azure.core.pipeline import PipelineRequest
from azure.core.pipeline.policies import SansIOHTTPPolicy
from azure.core.pipeline.policies._base import HTTPRequestType

from finance_clue.opendart import GenOpenDartClient


class CustomCredentials:
    def __init__(self, token: str):
        self._token = token
        self._expires_on = 0

    def get_token(self, *args, **kwargs) -> AccessToken:
        return AccessToken(self._token, self._expires_on)


class CustomAuthenticationPolicy(SansIOHTTPPolicy):

    def __init__(self, credentials: CustomCredentials):
        self._credentials = credentials

    def on_request(self, request: PipelineRequest[HTTPRequestType]) -> Union[None, Awaitable[None]]:
        if "crtfc_key" not in request.http_request.url:
            request.http_request.url += f"&crtfc_key={self._credentials.get_token().token}"
        return super().on_request(request)


class OpenDartClient(GenOpenDartClient):

    def __init__(self, token: str, *, timeout: int = 120, **kwargs):
        credential = CustomCredentials(token)
        kwargs["authentication_policy"] = CustomAuthenticationPolicy(credential)
        super().__init__(credential=credential, timeout=timeout, **kwargs)


def patch_sdk():
    """Do not remove from this file.

    `patch_sdk` is a last resort escape hatch that allows you to do customizations
    you can't accomplish using the techniques described in
    https://aka.ms/azsdk/python/dpcodegen/python/customize
    """


__all__: List[str] = ["OpenDartClient"]  # Add all objects you want publicly available to users at this package level
