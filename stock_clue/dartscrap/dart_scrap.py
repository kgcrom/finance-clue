"""DART 공시정보 스크래핑"""
from typing import Dict, List, Optional

from playwright.sync_api import sync_playwright


class TdInfo(object):
    def __init__(self, idx: int, rowspan: int, colspan: int, text: str):
        self.idx = idx
        self.rowspan = rowspan
        self.colspan = colspan
        self.used_count = rowspan * colspan
        self.text = text

    def mark_used(self, used_count: int = 1) -> bool:
        self.used_count -= self.colspan * used_count
        if self.used_count == 0:
            return True
        return False


def parse_html_table(html_doc: str, col_count: int):
    from bs4 import BeautifulSoup

    soup = BeautifulSoup(html_doc, "html.parser")
    table = soup.find_all("table")[-1]

    table_rows = table.find_all("tr")

    span_info: List[Optional[TdInfo]] = [None] * col_count
    results: List[List[Optional[str]]] = [[] for _ in range(len(table_rows))]
    for tr_idx, row in enumerate(table_rows):
        td_list = row.find_all("td")
        if len(td_list) == 0:
            continue

        td_idx = 0
        for col_idx in range(col_count):
            if len(results[tr_idx]) > col_idx:
                continue

            span = span_info[col_idx]
            if span is not None:
                value: List[Optional[str]] = []
                value.insert(0, span.text.strip())
                value.extend([None] * (span.colspan - 1))
                results[tr_idx].extend(value)
                if span.mark_used():
                    span_info[col_idx] = None
            else:
                td = td_list[td_idx]
                row_span: int = (
                    int(td.attrs["rowspan"]) if td.has_attr("rowspan") else 1
                )
                col_span: int = (
                    int(td.attrs["colspan"]) if td.has_attr("colspan") else 1
                )

                span_info[col_idx] = TdInfo(
                    col_idx, row_span, col_span, td.text.strip()
                )

                new_span: Optional[TdInfo] = span_info[col_idx]
                if new_span is not None:
                    new_value: List[Optional[str]] = [new_span.text.strip()]
                    new_value.extend([None] * (new_span.colspan - 1))
                    results[tr_idx].extend(new_value)
                    td_idx += 1
                    if new_span.mark_used():
                        span_info[col_idx] = None
                else:
                    raise Exception("span is None")

    return results


class DartScrap:
    def __init__(self, headless: bool = True) -> None:
        self.playwright_context = sync_playwright().start()
        self.browser = self.playwright_context.chromium.launch(
            headless=headless
        )

        page = self.browser.new_page()
        page.goto("https://dart.fss.or.kr/main.do")
        self.cookies = page.context.cookies()
        page.close()

    def __del__(self):
        self.browser.close()
        self.playwright_context.stop()

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
        context = self.browser.new_context()
        page = context.new_page()
        page.goto(url)

        page.locator("iframe").wait_for(state="attached")
        mf = page.frame("ifrm")
        
        contents: Optional[str] = mf.content() if mf is not None else None

        page.close()
        context.close()
        return contents
