import os
from typing import Callable, List, TypeVar

from stock_clue.opendart import OpenDart
from stock_clue.opendart.disclosure import Disclosure
from stock_clue.opendart.disclosure_dto import ListInputDto
from stock_clue.opendart.disclosure_type import DisclosureType

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
    def setup_class(self):
        self.disclosure = Disclosure(OpenDart(os.environ["OPENDART_API_KEY"]))

    def test_disclosure_list(self):
        params = ListInputDto(
            corp_code="01029394",
            bgn_de="20230717",
            end_de="20231017",
            pblntf_ty=DisclosureType.A,
            corp_cls="K",
        )
        results = self.disclosure.list(params)

        assert results is not None
        assert results.page_count == 10
        assert results.total_count == 1
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
        result = self.disclosure.get_company_overview(corp_code="01029394")

        assert result is not None
        assert result.corp_name == "(주)에코마케팅"

    def test_download_document(self):
        self.disclosure.download_document(
            rcept_no="20231024600472",
            file_path="./",
        )

    def test_corp_code(self):
        result = self.disclosure.get_corp_code_list()

        assert len(result) != 0
