"""사업보고서 주요정보 OpenDart 연동 Module"""

from typing import TYPE_CHECKING, Dict

from stock_clue.error import HttpError
from stock_clue.opendart.base_dto import BaseListDto
from stock_clue.opendart.base_dto import BaseParamDto
from stock_clue.opendart.business_report_info_dto import (
    ChangedLargestShareHoldersOutputDto,
)
from stock_clue.opendart.business_report_info_dto import (
    DirectorRemunerationAmountOutputDto,
)
from stock_clue.opendart.business_report_info_dto import (
    DirectorRemunerationApprovalOutputDto,
)
from stock_clue.opendart.business_report_info_dto import (
    LargestShareHoldersOutputDto,
)
from stock_clue.opendart.business_report_info_dto import (
    TotalStockQuantityOutputDto,
)
from stock_clue.opendart.business_report_info_dto import AuditOpinionOutputDto

if TYPE_CHECKING:
    from stock_clue.opendart.open_dart import OpenDart


# TODO 타입 변경시 잘못된 값 에러 처리
def str_to_int(v: str) -> int:
    """
    OpenDart에서 내려주는 문자열 형태의 숫자를 int로 변환

    param v: OpenDart에서 내려주는 문자열 형태의 숫자
    """
    if v == "-":
        return 0
    return int(v.replace(",", ""))


def str_to_float(v: str) -> float:
    """
    OpenDart에서 내려주는 문자열 형태의 실수를 float으로 변환

        param v: OpenDart에서 내려주는 문자열 형태의 숫자
    """
    if v == "-":
        return 0.0
    return float(v)


class BusinessReportInfo:
    def __init__(self, open_dart: "OpenDart"):
        super().__init__()
        self.open_dart = open_dart

    def get_director_remuneration_approval(
        self,
        corp_code: str,
        bsns_year: str,
        reprt_code: str,
    ) -> BaseListDto[DirectorRemunerationApprovalOutputDto]:
        path = "/api/drctrAdtAllMendngSttusGmtsckConfmAmount.json"
        params = BaseParamDto(
            corp_code=corp_code,
            bsns_year=bsns_year,
            reprt_code=reprt_code,
        )
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
                nmpr=str_to_int(x["nmpr"]),
                gmtsck_confm_amount=str_to_int(x["gmtsck_confm_amount"]),
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
        self,
        corp_code: str,
        bsns_year: str,
        reprt_code: str,
    ) -> BaseListDto[DirectorRemunerationAmountOutputDto]:
        path = "/api/drctrAdtAllMendngSttusMendngPymntamtTyCl.json"
        params = BaseParamDto(
            corp_code=corp_code,
            bsns_year=bsns_year,
            reprt_code=reprt_code,
        )
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
                nmpr=str_to_int(x["nmpr"]),
                pymnt_totamt=str_to_int(x["pymnt_totamt"]),
                psn1_avrg_pymntamt=str_to_int(x["psn1_avrg_pymntamt"]),
                rm=x["rm"],
            )

        data = resposne.json()

        return BaseListDto[DirectorRemunerationAmountOutputDto](
            status=data["status"],
            message=data["message"],
            list=list(map(_mapping, data["list"])),
        )

    # TODO 함수명 동사로 시작할건지 아닌지 동일하게 하기
    def total_stock_quantity(
        self,
        corp_code: str,
        bsns_year: str,
        reprt_code: str,
    ) -> BaseListDto[TotalStockQuantityOutputDto]:
        path = "/api/stockTotqySttus.json"
        params = BaseParamDto(
            corp_code=corp_code,
            bsns_year=bsns_year,
            reprt_code=reprt_code,
        )
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
                isu_stock_totqy=str_to_int(x["isu_stock_totqy"]),
                now_to_isu_stock_totqy=str_to_int(x["now_to_isu_stock_totqy"]),
                now_to_dcrs_stock_totqy=str_to_int(
                    x["now_to_dcrs_stock_totqy"]
                ),
                redc=str_to_int(x["redc"]),
                profit_incnr=str_to_int(x["profit_incnr"]),
                rdmstk_repy=str_to_int(x["rdmstk_repy"]),
                etc=str_to_int(x["etc"]),
                istc_totqy=str_to_int(x["istc_totqy"]),
                tesstk_co=str_to_int(x["tesstk_co"]),
                distb_stock_co=str_to_int(x["distb_stock_co"]),
            )

        data = response.json()
        return BaseListDto[TotalStockQuantityOutputDto](
            status=data["status"],
            message=data["message"],
            list=list(map(_mapping, data["list"])),
        )

    def audit_opinion(
        self,
        corp_code: str,
        bsns_year: str,
        reprt_code: str,
    ) -> BaseListDto[AuditOpinionOutputDto]:
        path = "/api/accnutAdtorNmNdAdtOpinion.json"
        params = BaseParamDto(
            corp_code=corp_code,
            bsns_year=bsns_year,
            reprt_code=reprt_code,
        )
        response = self.open_dart.get(path, params.dict())

        if response.status_code != 200:
            raise HttpError(path)

        def _mapping(x: Dict[str, str]) -> AuditOpinionOutputDto:
            return AuditOpinionOutputDto(
                rcept_no=x["rcept_no"],
                corp_cls=x["corp_cls"],
                corp_code=x["corp_code"],
                corp_name=x["corp_name"],
                bsns_year=x["bsns_year"],
                adtor=x["adtor"],
                adt_opinion=x["adt_opinion"] if "adt_opinion" in x else None,
                adt_reprt_spcmnt_matter=x["adt_reprt_spcmnt_matter"]
                if "adt_reprt_spcmnt_matter" in x
                else None,
                emphs_matter=x["emphs_matter"] if "emphs_matter" in x else None,
                core_adt_matter=x["core_adt_matter"]
                if "core_adt_matter" in x
                else None,
            )

        data = response.json()

        return BaseListDto[AuditOpinionOutputDto](
            status=data["status"],
            message=data["message"],
            list=list(map(_mapping, data["list"])),
        )

    def largest_shareholders(
        self,
        corp_code: str,
        bsns_year: str,
        reprt_code: str,
    ) -> BaseListDto[LargestShareHoldersOutputDto]:
        path = "/api/hyslrSttus.json"
        params = BaseParamDto(
            corp_code=corp_code,
            bsns_year=bsns_year,
            reprt_code=reprt_code,
        )
        response = self.open_dart.get(path, params.dict())

        if response.status_code != 200:
            raise HttpError(path)

        def _mapping(x: Dict[str, str]) -> LargestShareHoldersOutputDto:
            return LargestShareHoldersOutputDto(
                rcept_no=x["rcept_no"],
                corp_cls=x["corp_cls"],
                corp_code=x["corp_code"],
                corp_name=x["corp_name"],
                nm=x["nm"],
                relate=x["relate"] if "relate" in x else None,
                stock_knd=x["stock_knd"],
                bsis_posesn_stock_co=str_to_int(x["bsis_posesn_stock_co"]),
                bsis_posesn_stock_qota_rt=str_to_float(
                    x["bsis_posesn_stock_qota_rt"]
                ),
                trmend_posesn_stock_co=str_to_int(x["trmend_posesn_stock_co"]),
                trmend_posesn_stock_qota_rt=str_to_float(
                    x["trmend_posesn_stock_qota_rt"]
                ),
                rm=x["rm"],
            )

        data = response.json()

        return BaseListDto[LargestShareHoldersOutputDto](
            status=data["status"],
            message=data["message"],
            list=list(map(_mapping, data["list"])),
        )

    def changed_largest_shareholders(
        self,
        corp_code: str,
        bsns_year: str,
        reprt_code: str,
    ) -> BaseListDto[ChangedLargestShareHoldersOutputDto]:
        path = "/api/hyslrChgSttus.json"
        params = BaseParamDto(
            corp_code=corp_code,
            bsns_year=bsns_year,
            reprt_code=reprt_code,
        )
        response = self.open_dart.get(path, params.dict())

        if response.status_code != 200:
            raise HttpError(path)

        def _mapping(x: Dict[str, str]) -> ChangedLargestShareHoldersOutputDto:
            return ChangedLargestShareHoldersOutputDto(
                rcept_no=x["rcept_no"],
                corp_cls=x["corp_cls"],
                corp_code=x["corp_code"],
                corp_name=x["corp_name"],
                change_on=x["change_on"],
                mxmm_shrholdr_nm=x["mxmm_shrholdr_nm"],
                posesn_stock_co=str_to_int(x["posesn_stock_co"]),
                qota_rt=str_to_float(x["qota_rt"]),
                change_cause=x["qota_rt"],
                rm=x["rm"],
            )

        data = response.json()

        return BaseListDto[ChangedLargestShareHoldersOutputDto](
            status=data["status"],
            message=data["message"],
            list=list(map(_mapping, data["list"])),
        )
