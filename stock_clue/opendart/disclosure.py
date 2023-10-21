from typing import TYPE_CHECKING, List, Any

from stock_clue.error import HttpError
from stock_clue.opendart.disclosure_dto import ListInputDto, ListOutputDto

if TYPE_CHECKING:
    from stock_clue.opendart.open_dart import OpenDart


def _mapping_list(d: Any) -> ListOutputDto:
    return ListOutputDto(
        d['corp_cls'],
        d['corp_name'],
        d['corp_code'],
        d['stock_code'],
        d['report_nm'],
        d['rcept_no'],
        d['flr_nm'],
        d['rcept_dt'],
        d['rm'],
    )


class Disclosure(object):

    def __init__(self, open_dart: "OpenDart"):
        super().__init__()
        self.open_dart = open_dart

    def list(self, input_dto: ListInputDto) -> List[ListOutputDto]:
        path = '/api/list.json'
        response = self.open_dart.get(path, input_dto.dict())
        # TODO status, message 까지 포함한 클래스 리턴하도록
        # TODO python generic 이용 가능? https://medium.com/@steveYeah/using-generics-in-python-99010e5056eb

        if response.status_code != 200:
            raise HttpError()

        data = response.json()
        return list(map(_mapping_list, data['list']))
