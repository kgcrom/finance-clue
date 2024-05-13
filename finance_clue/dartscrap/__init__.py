"""DART 공시정보 스크래핑"""

from typing import Dict, Optional

from playwright.sync_api import sync_playwright


# TODO DartScrap() 한 프로세스에 두번이상 호출하면 오류난다.
class DartScrap:
    def __init__(self, headless: bool = True) -> None:
        self.playwright_context = sync_playwright().start()
        self.browser = self.playwright_context.chromium.launch(headless=headless)

        with self.browser.new_page() as page:
            page.goto("https://dart.fss.or.kr/main.do")
            self.cookies = page.context.cookies()

    def __del__(self):
        self.browser.close()
        self.playwright_context.stop()

    @property
    def headers_for_request(self) -> Dict[str, str]:
        jsession = [
            cookie for cookie in self.cookies if cookie["name"] == "JSESSIONID"
        ][0]
        wmonid = [cookie for cookie in self.cookies if cookie["name"] == "WMONID"][0]
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

    def get_html_content_no_side_menu(self, url: str) -> Optional[str]:
        """dart.fss.or.kr의 사이드 메뉴가 없는 페이지의 html을 가져온다."""
        with self.browser.new_page() as p:
            p.goto(url)
            ifrm = next(filter(lambda f: f.name == "ifrm", p.main_frame.child_frames))
            ifrm.wait_for_timeout(timeout=3000)

            return ifrm.content()

    @property
    def list_disclosure(self):
        from finance_clue.dartscrap.list_disclosure import ListDisclosure

        return ListDisclosure(self)

    @property
    def dividend_parser(self):
        from finance_clue.dartscrap.dividend_parser import DividendParser

        return DividendParser(self)

    @property
    def preliminary_parser(self):
        from finance_clue.dartscrap.preliminary_parser import PreliminaryParser

        return PreliminaryParser(self)

    @property
    def revenue_volatility_parser(self):
        from finance_clue.dartscrap.revenue_volatility_parser import (
            RevenueVolatilityParser,
        )

        return RevenueVolatilityParser(self)

    @property
    def facility_invest_parser(self):
        from finance_clue.dartscrap.facility_invest_parser import FacilityInvestParser

        return FacilityInvestParser(self)

    @property
    def supply_agreement_parser(self):
        from finance_clue.dartscrap.supply_agreement_parser import SupplyAgreementParser

        return SupplyAgreementParser(self)

    @property
    def retirement_treasury_stock_parser(self):
        from finance_clue.dartscrap.retirement_treasury_stock_parser import (
            RetirementTreasuryStockParser,
        )

        return RetirementTreasuryStockParser(self)
