"""공시정보 관련된 API 연동을 제공하는 Module"""
from typing import TYPE_CHECKING, Any, List
import logging

from stock_clue.error import HttpError
from stock_clue.opendart.disclosure_dto import ListInputDto
from stock_clue.opendart.disclosure_dto import ListOutputDto

if TYPE_CHECKING:
    from stock_clue.opendart.open_dart import OpenDart


def _mapping_list(d: Any) -> ListOutputDto:
    return ListOutputDto(
        d["corp_cls"],
        d["corp_name"],
        d["corp_code"],
        d["stock_code"],
        d["report_nm"],
        d["rcept_no"],
        d["flr_nm"],
        d["rcept_dt"],
        d["rm"],
    )


class Disclosure(object):
    def __init__(self, open_dart: "OpenDart"):
        super().__init__()
        self.open_dart = open_dart

    def list(self, input_dto: ListInputDto) -> List[ListOutputDto]:
        path = "/api/list.json"
        response = self.open_dart.get(path, input_dto.dict())
        # TODO status, message 까지 포함한 클래스 리턴하도록
        # TODO python generic 이용 가능? https://medium.com/@steveYeah/using-generics-in-python-99010e5056eb

        if response.status_code != 200:
            raise HttpError()

        data = response.json()

        # TODO status error message와 응답 정보 로깅
        # TODO open dart 오류는 별도 class가 관리
        if data["status"] != '000':
            logging.error(f"status: {data['status']}, message: {data['message']}")
            return []

        return list(map(_mapping_list, data["list"]))
