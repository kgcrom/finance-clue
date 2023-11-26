"""배당 관련 공시 페이지 파싱 모듈"""

from typing import TYPE_CHECKING

from playwright.sync_api import sync_playwright
import requests

from stock_clue.dartscrap.dart_scrap import parse_html_table
from stock_clue.error import HttpError

if TYPE_CHECKING:
    from stock_clue.dartscrap.dart_scrap import DartScrap


class DividendParser:
    """배당 관련 공시 페이지 파싱 클래스"""

    def __init__(self, dart_scrap: "DartScrap"):
        self.dart_scrap = dart_scrap

    def parse_closing_shareholders(self, report_no: str):
        """현금.현물배당을 위한 최종주주명부 폐쇄(기준일)결정 공시 페이지 파싱"""
        url = f"https://dart.fss.or.kr/dsaf001/main.do?rcpNo={report_no}"
        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page()
            page.goto(url)

            target_frame = None
            for frame in page.frames:
                if frame.name == "ifrm":
                    target_frame = frame

            if target_frame is None:
                raise HttpError(f"iframe not found: {url}")

            result = parse_html_table(target_frame.content(), 4)
            browser.close()

            return result

    def parse_decision_on_cash(self, report_no: str):
        """현금.현물배당 결정 공시 페이지 파싱"""
        url = f"https://dart.fss.or.kr/dsaf001/main.do?rcpNo={report_no}"
        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page()
            page.goto(url)

            target_frame = None
            for frame in page.frames:
                if frame.name == "ifrm":
                    target_frame = frame

            if target_frame is None:
                raise HttpError(f"iframe not found: {url}")

            result = parse_html_table(target_frame.content(), 4)
            browser.close()

            return result
