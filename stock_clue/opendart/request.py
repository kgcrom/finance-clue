"""HTTP Request Module"""

from typing import Dict, Optional

import requests


class Request(object):
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

        Args:
            path (str): 요청할 API의 경로
            params (Optional[Dict]): 요청할 API의 쿼리 파라미터
            is_stream (Optional[bool]): 스트림으로 받을지 여부 (기본값: False)

        Returns:
            requests.Response: 요청 결과
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

    # TODO add logging
    # TODO handle response status code
    # TODO handle open_dart api limit
