# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------
"""Customize generated code here.

Follow our quickstart for examples: https://aka.ms/azsdk/python/dpcodegen/python/customize
"""
from typing import List, Union, Awaitable

from azure.core.credentials import AccessToken
from azure.core.pipeline import PipelineRequest
from azure.core.pipeline.policies import SansIOHTTPPolicy
from azure.core.pipeline.policies._base import HTTPRequestType

from finance_clue.openkrx import GenOpenKrxClient


class CustomCredentials:

    def __init__(self, token: str):
        self._token = token
        self._expires_on = 0

    def get_token(self, *args, **kwargs) -> AccessToken:
        return AccessToken(self._token, self._expires_on)


class CustomProxyPolicy(SansIOHTTPPolicy):

    def __init__(self, proxies: dict):
        self._proxies = proxies
        super().__init__()

    def on_request(self, request: PipelineRequest[HTTPRequestType]) -> Union[None, Awaitable[None]]:
        ctxt = request.context.options

        if self._proxies and "proxies" not in ctxt:
            # Change the protocol from https to http in the proxy settings
            modified_proxies = {k if not k.startswith("https") else "http" + k[5:]: v for k, v in self._proxies.items()}
            ctxt["proxies"] = modified_proxies
        return super().on_request(request)


class OpenKrxClient(GenOpenKrxClient):

    def __init__(self, token: str, *, timeout: int = 120, **kwargs):
        credential = CustomCredentials(token)
        custom_proxy = CustomProxyPolicy(
            proxies=kwargs.pop("proxies", {"https://data-dbg.krx.co.kr": "http://data-dbg.krx.co.kr"})
        )
        kwargs["proxy_policy"] = custom_proxy
        super().__init__(credential=credential, timeout=timeout, **kwargs)


def patch_sdk():
    """Do not remove from this file.

    `patch_sdk` is a last resort escape hatch that allows you to do customizations
    you can't accomplish using the techniques described in
    https://aka.ms/azsdk/python/dpcodegen/python/customize
    """


__all__: List[str] = ["OpenKrxClient"]  # Add all objects you want publicly available to users at this package level
