"""사업보고서 주요정보 OpenDart 연동 Module"""

from typing import TYPE_CHECKING, Dict

from stock_clue.error import HttpError
from stock_clue.opendart.base_list_dto import BaseListDto
from stock_clue.opendart.business_report_info_dto import (
    DirectorRemunerationAmountInputDto,
)
from stock_clue.opendart.business_report_info_dto import (
    DirectorRemunerationAmountOutputDto,
)
from stock_clue.opendart.business_report_info_dto import (
    DirectorRemunerationApprovalInputDto,
)
from stock_clue.opendart.business_report_info_dto import (
    DirectorRemunerationApprovalOutputDto,
)
from stock_clue.opendart.business_report_info_dto import (
    TotalStockQuantityInputDto,
)
from stock_clue.opendart.business_report_info_dto import (
    TotalStockQuantityOutputDto,
)

if TYPE_CHECKING:
    from stock_clue.opendart.open_dart import OpenDart


def str_to_number(v: str) -> int:
    """
    OpenDart에서 내려주는 문자열 형태의 숫자를 숫자형으로 변환

    param v: OpenDart에서 내려주는 문자열 형태의 숫자
    """
    if v == "-":
        return 0
    return int(v.replace(",", ""))


class BusinessReportInfo:
    def __init__(self, open_dart: "OpenDart"):
        super().__init__()
        self.open_dart = open_dart

    def get_director_remuneration_approval(
        self, params: DirectorRemunerationApprovalInputDto
    ) -> BaseListDto[DirectorRemunerationApprovalOutputDto]:
        path = "/api/drctrAdtAllMendngSttusGmtsckConfmAmount.json"
        response = self.open_dart.get(path, params.dict())

        def _mapping(
            x: Dict[str, str]
        ) -> DirectorRemunerationApprovalOutputDto:
            return DirectorRemunerationApprovalOutputDto(
                rcept_no=x["rcept_no"],
                corp_cls=x["corp_cls"],
                corp_code=x["corp_code"],
                corp_name=x["corp_name"],
                se=x["se"],
                nmpr=str_to_number(x["nmpr"]),
                gmtsck_confm_amount=str_to_number(x["gmtsck_confm_amount"]),
                rm=x["rm"],
            )

        if response.status_code != 200:
            raise HttpError(path)

        data = response.json()
        return BaseListDto[DirectorRemunerationApprovalOutputDto](
            status=data["status"],
            message=data["message"],
            list=list(map(_mapping, data["list"])),
        )

    def get_director_remuneration_amount(
        self, params: DirectorRemunerationAmountInputDto
    ) -> BaseListDto[DirectorRemunerationAmountOutputDto]:
        path = "/api/drctrAdtAllMendngSttusMendngPymntamtTyCl.json"
        resposne = self.open_dart.get(path, params.dict())

        if resposne.status_code != 200:
            raise HttpError(path)

        def _mapping(x: Dict[str, str]) -> DirectorRemunerationAmountOutputDto:
            return DirectorRemunerationAmountOutputDto(
                rcept_no=x["rcept_no"],
                corp_cls=x["corp_cls"],
                corp_code=x["corp_code"],
                corp_name=x["corp_name"],
                se=x["se"],
                nmpr=str_to_number(x["nmpr"]),
                pymnt_totamt=str_to_number(x["pymnt_totamt"]),
                psn1_avrg_pymntamt=str_to_number(x["psn1_avrg_pymntamt"]),
                rm=x["rm"],
            )

        data = resposne.json()

        return BaseListDto[DirectorRemunerationAmountOutputDto](
            status=data["status"],
            message=data["message"],
            list=list(map(_mapping, data["list"])),
        )

    def total_stock_quantity(
        self, params: TotalStockQuantityInputDto
    ) -> BaseListDto[TotalStockQuantityOutputDto]:
        path = "/api/stockTotqySttus.json"
        response = self.open_dart.get(path, params.dict())
        if response.status_code != 200:
            raise HttpError(path)

        def _mapping(x: Dict[str, str]) -> TotalStockQuantityOutputDto:
            return TotalStockQuantityOutputDto(
                rcept_no=x["rcept_no"],
                corp_cls=x["corp_cls"],
                corp_code=x["corp_code"],
                corp_name=x["corp_name"],
                se=x["se"],
                isu_stock_totqy=str_to_number(x["isu_stock_totqy"]),
                now_to_isu_stock_totqy=str_to_number(
                    x["now_to_isu_stock_totqy"]
                ),
                now_to_dcrs_stock_totqy=str_to_number(
                    x["now_to_dcrs_stock_totqy"]
                ),
                redc=str_to_number(x["redc"]),
                profit_incnr=str_to_number(x["profit_incnr"]),
                rdmstk_repy=str_to_number(x["rdmstk_repy"]),
                etc=str_to_number(x["etc"]),
                istc_totqy=str_to_number(x["istc_totqy"]),
                tesstk_co=str_to_number(x["tesstk_co"]),
                distb_stock_co=str_to_number(x["distb_stock_co"]),
            )

        data = response.json()
        return BaseListDto[TotalStockQuantityOutputDto](
            status=data["status"],
            message=data["message"],
            list=list(map(_mapping, data["list"])),
        )
