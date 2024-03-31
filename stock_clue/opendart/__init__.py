"""OpenDart API 연동 관리 Module"""

from typing import Optional


class OpenDart(object):
    def __init__(self, api_key: str, timeout: Optional[int] = 5):
        super().__init__()
        self.api_key = api_key
        self.base_url = "https://opendart.fss.or.kr"
        self.timeout = timeout

    @property
    def major_report(self):
        from stock_clue.opendart import major_report

        return major_report.MajorReport(self)

    @property
    def disclosure(self):
        from stock_clue.opendart import disclosure

        return disclosure.Disclosure(self)
