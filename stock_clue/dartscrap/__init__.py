"""DART 공시정보 스크래핑"""
import threading
from typing import Dict

from playwright.sync_api import sync_playwright


# TODO DartScrap() 한 프로세스에 두번이상 호출하면 오류난다.
class DartScrap:
    def __init__(self, headless: bool = True) -> None:
        self.playwright_context = sync_playwright().start()
        self.browser = self.playwright_context.chromium.launch(
            headless=headless
        )

        with self.browser.new_page() as page:
            page.goto("https://dart.fss.or.kr/main.do")
            self.cookies = page.context.cookies()

    def __del__(self):
        self.browser.close()
        self.playwright_context.stop()

    # TODO 동시성 처리하기, circular queue 사용하고 모두 사용하면 두배 늘리는것도 괜찮은 듯?
    def _next_page(self):
        with self.page_index_lock:
            self.page_index += 1
            if self.page_index == len(self.pages):
                self.page_index = 0

        print(self.page_index)
        return self.pages[self.page_index]

    @property
    def headers_for_request(self) -> Dict[str, str]:
        jsession = [
            cookie for cookie in self.cookies if cookie["name"] == "JSESSIONID"
        ][0]
        wmonid = [
            cookie for cookie in self.cookies if cookie["name"] == "WMONID"
        ][0]
        return {
            "Accept": "text/html, */*; q=0.01",
            "Accept-Language": "en-US,en;q=0.9,ko;q=0.8",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "Host": "dart.fss.or.kr",
            "Origin": "https://dart.fss.or.kr",
            "Referer": "https://dart.fss.or.kr/dsac001/mainY.do",
            "Cookie": f"{wmonid['name']}={wmonid['value']}; {jsession['name']}={jsession['value']}",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36",
        }

    def get_html_content_no_side_menu(self, url: str) -> str | None:
        """dart.fss.or.kr의 사이드 메뉴가 없는 페이지의 html을 가져온다."""
        with self.browser.new_page() as p:
            p.goto(url)
            mf = p.wait_for_selector("#ifrm").content_frame()
            # mf.wait_for_timeout(1000)

            contents: str | None = mf.content() if mf is not None else None
            return contents

    @property
    def list_disclosure(self):
        from stock_clue.dartscrap.list_disclosure import ListDisclosure

        return ListDisclosure(self)

    @property
    def dividend_parser(self):
        from stock_clue.dartscrap.dividend_parser import DividendParser

        return DividendParser(self)

    @property
    def preliminary_parser(self):
        from stock_clue.dartscrap.preliminary_parser import PreliminaryParser

        return PreliminaryParser(self)
