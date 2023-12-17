"""OpenDart API 연동 관리 Module"""
from typing import Dict, Optional

import requests


class OpenDart(object):
    def __init__(self, api_key: str, timeout: Optional[int] = 5):
        super().__init__()
        self.api_key = api_key
        self.base_url = "https://opendart.fss.or.kr"
        self.timeout = timeout

    def get(
        self,
        path: str,
        params: Optional[Dict] = None,
        is_stream: Optional[bool] = False,
    ) -> requests.Response:
        """
        OpenDART API를 인증키와 함께 요청
        """
        if params is None:
            params = {}
        params["crtfc_key"] = self.api_key
        return requests.get(
            url=f"{self.base_url}{path}",
            params=params,
            stream=is_stream,
            timeout=self.timeout,
        )
