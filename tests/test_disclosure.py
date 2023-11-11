"""disclosure Module 테스트"""
import os
from typing import Callable, TypeVar, List

from stock_clue.opendart.disclosure_dto import CompanyOverviewInputDto
from stock_clue.opendart.disclosure_dto import DownloadDocumentInputDto
from stock_clue.opendart.disclosure_dto import ListInputDto
from stock_clue.opendart.open_dart import OpenDart

T = TypeVar("T")
R = TypeVar("R")


def typehint_map(
    fn: Callable[[T], R],
    items: List[T],
) -> List[R]:
    return [fn(i) for i in items]


def typehint_filter(
    fn: Callable[[T], T],
    items: List[T],
) -> List[T]:
    return [i for i in items if fn(i)]


class TestDisclosure:
    def test_disclosure_list(self):
        open_dart = OpenDart(os.environ["OPENDART_API_KEY"])
        params = ListInputDto(
            corp_code="01029394",
            bgn_de="20230717",
            end_de="20231017",
            corp_cls="K",
        )
        results = open_dart.disclosure.list(params)

        assert results is not None
        assert results.page_count == 10
        assert results.total_count == 7
        assert results.total_page == 1
        assert len(results.list) != 0
        assert (
            len(
                list(
                    typehint_filter(
                        lambda x: x.corp_name == "에코마케팅", results.list
                    )
                )
            )
            != 0
        )

    def test_company_overview(self):
        open_dart = OpenDart(os.environ["OPENDART_API_KEY"])
        params = CompanyOverviewInputDto(
            corp_code="01029394",
        )
        result = open_dart.disclosure.get_company_overview(params)

        assert result is not None
        assert result.corp_name == "(주)에코마케팅"

    def test_download_document(self):
        open_dart = OpenDart(os.environ["OPENDART_API_KEY"])
        params = DownloadDocumentInputDto(
            rcept_no="20231024600472",
            file_path="./",
        )

        open_dart.disclosure.download_document(params)

    def test_corp_code(self):
        open_dart = OpenDart(os.environ["OPENDART_API_KEY"])
        result = open_dart.disclosure.get_corp_code_list()

        assert len(result) != 0
