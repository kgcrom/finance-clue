"""OpenDart API 연동을 관리하는 Module"""
from typing import TYPE_CHECKING, Dict, Optional

import requests

if TYPE_CHECKING:
    from stock_clue.opendart.business_report_info import BusinessReportInfo
    from stock_clue.opendart.disclosure import Disclosure
    from stock_clue.opendart.financial_info import FinancialInfo


class OpenDart(object):
    def __init__(self, api_key: str, timeout: Optional[int] = 5):
        super().__init__()
        self.api_key = api_key
        self.base_url = "https://opendart.fss.or.kr"
        self.timeout = timeout

    @property
    def disclosure(self) -> "Disclosure":
        from stock_clue.opendart import disclosure

        return disclosure.Disclosure(self)

    @property
    def business_report_info(self) -> "BusinessReportInfo":
        from stock_clue.opendart import business_report_info

        return business_report_info.BusinessReportInfo(self)

    @property
    def financial_info(self) -> "FinancialInfo":
        from stock_clue.opendart import financial_info

        return financial_info.FinancialInfo(self)

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
