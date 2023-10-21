import os
from collections.abc import Callable
from typing import TypeVar

from stock_clue.opendart.disclosure_dto import ListInputDto
from stock_clue.opendart.open_dart import OpenDart

T = TypeVar('T')
R = TypeVar('R')


def typehint_map(
        fn: Callable[[T], R],
        items: list[T],
) -> list[R]:
    return [fn(i) for i in items]


def typehint_filter(
        fn: Callable[[T], R],
        items: list[T],
) -> list[R]:
    return [i for i in items if fn(i)]


class TestDisclosure:
    def test_disclosure_list(self):
        open_dart = OpenDart(os.environ['OPENDART_API_KEY'])
        params = ListInputDto(
            corp_code='01029394',
            bgn_de='20230717',
            end_de='20231017',
            corp_cls='K'
        )
        results = open_dart.disclosure.list(params)

        assert len(list(typehint_filter(lambda x: x.corp_name == '에코마케팅', results))) != 0
        assert results is not None
