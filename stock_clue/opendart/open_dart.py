"""OpenDart API 연동을 관리하는 Module"""
from typing import TYPE_CHECKING, Dict, Optional

import requests

if TYPE_CHECKING:
    from stock_clue.opendart.disclosure import Disclosure


class OpenDart(object):
    def __init__(self, api_key: str):
        super().__init__()
        self.api_key = api_key
        self.base_url = "https://opendart.fss.or.kr"

    @property
    def disclosure(self) -> "Disclosure":
        from stock_clue.opendart import disclosure

        return disclosure.Disclosure(self)

    def get(
        self,
        path: str,
        params: Optional[Dict] = None,
        is_stream: Optional[bool] = False,
    ) -> requests.Response:
        if params is None:
            params = {}
        params["crtfc_key"] = self.api_key
        return requests.get(
            f"{self.base_url}{path}", params=params, stream=is_stream
        )
