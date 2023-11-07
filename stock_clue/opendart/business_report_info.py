"""사업보고서 주요정보 OpenDart 연동 Module"""

from typing import TYPE_CHECKING, Dict

from stock_clue.error import HttpError
from stock_clue.opendart.base_dto import BaseListDto
from stock_clue.opendart.base_dto import BaseParamDto
from stock_clue.opendart.business_report_info_dto import (
    AcquisitionAndDisposalOfTreasuryStocksOutputDto,
)
from stock_clue.opendart.business_report_info_dto import (
    CapitalIncreaseAndReductionOutputDto,
)
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
    NonExecutiveDirectorOutputDto,
)
from stock_clue.opendart.business_report_info_dto import (
    TotalStockQuantityOutputDto,
)
from stock_clue.opendart.business_report_info_dto import AuditOpinionOutputDto
from stock_clue.opendart.business_report_info_dto import DividendOutputDto

if TYPE_CHECKING:
    from stock_clue.opendart.open_dart import OpenDart


# TODO 타입 변경시 잘못된 값 에러 처리
def str_to_int(v: str) -> int:
    """
    convert to int from string value

    param v: opendart에서 내려주는 문자열 타입의 숫자
    """

    if v == "-":
        return 0
    return int(v.replace(",", ""))


def str_to_float(v: str) -> float:
    """
    convert to float from string value

    param v: OpenDart에서 내려주는 문자열 타입의 숫자
    """
    if v == "-":
        return 0.0
    return float(v.replace(",", ""))


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
            list=list(map(_mapping, data["list"])) if "list" in data else None,
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
            list=list(map(_mapping, data["list"])) if "list" in data else None,
        )

    def get_dividend(
        self, corp_code: str, bsns_year: str, reprt_code: str
    ) -> BaseListDto[DividendOutputDto]:
        """
        배당에 관한 사항 조회
        """
        path = "/api/alotMatter.json"
        params = BaseParamDto(
            corp_code=corp_code,
            bsns_year=bsns_year,
            reprt_code=reprt_code,
        )
        response = self.open_dart.get(path, params.dict())
        if response.status_code != 200:
            raise HttpError(path)

        def _mapping(x: Dict[str, str]) -> DividendOutputDto:
            return DividendOutputDto(
                rcept_no=x["rcept_no"],
                corp_cls=x["corp_cls"],
                corp_code=x["corp_code"],
                corp_name=x["corp_name"],
                se=x["se"],
                stock_knd=x["stock_knd"] if "stock_knd" in x else None,
                thstrm=str_to_float(x["thstrm"]),
                frmtrm=str_to_float(x["frmtrm"]),
                lwfr=str_to_float(x["lwfr"]),
            )

        data = response.json()
        return BaseListDto[DividendOutputDto](
            status=data["status"],
            message=data["message"],
            list=list(map(_mapping, data["list"])) if "list" in data else None,
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
            list=list(map(_mapping, data["list"])) if "list" in data else None,
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
            list=list(map(_mapping, data["list"])) if "list" in data else None,
        )

    def get_non_executive_director(
        self, corp_code: str, bsns_year: str, reprt_code: str
    ) -> BaseListDto[NonExecutiveDirectorOutputDto]:
        """
        사외이사 및 그 변동사항 조회

        param corp_code: 고유번호
        param bsns_year: 사업연도
        param reprt_code: 보고서 코드 (11013: 사업보고서, 11012: 반기보고서, 11014: 분기보고서)
        """
        path = "/api/outcmpnyDrctrNdChangeSttus.json"
        params = BaseParamDto(
            corp_code=corp_code,
            bsns_year=bsns_year,
            reprt_code=reprt_code,
        )
        response = self.open_dart.get(path, params.dict())

        if response.status_code != 200:
            raise HttpError(path)

        def _mapping(x: Dict[str, str]) -> NonExecutiveDirectorOutputDto:
            return NonExecutiveDirectorOutputDto(
                rcept_no=x["rcept_no"],
                corp_cls=x["corp_cls"],
                corp_code=x["corp_code"],
                corp_name=x["corp_name"],
                drctr_co=str_to_int(x["drctr_co"]),
                otcmp_drctr_co=str_to_int(x["otcmp_drctr_co"]),
                apnt=str_to_int(x["apnt"]),
                rlsofc=str_to_int(x["rlsofc"]),
                mdstrm_resig=str_to_int(x["mdstrm_resig"]),
            )

        data = response.json()

        return BaseListDto[NonExecutiveDirectorOutputDto](
            status=data["status"],
            message=data["message"],
            list=list(map(_mapping, data["list"])) if "list" in data else None,
        )

    def get_acquisition_and_disposal_of_treasury_stocks(
        self, corp_code: str, bsns_year: str, reprt_code: str
    ):
        """
        자기주식 취득 및 처분 현황 조회

        param corp_code: 고유번호
        param bsns_year: 사업연도
        param reprt_code: 보고서 코드 (11013: 사업보고서, 11012: 반기보고서, 11014: 분기보고서)
        """
        path = "/api/tesstkAcqsDspsSttus.json"

        params = BaseParamDto(
            corp_code=corp_code,
            bsns_year=bsns_year,
            reprt_code=reprt_code,
        )
        response = self.open_dart.get(path, params.dict())

        if response.status_code != 200:
            raise HttpError(path)

        def _mapping(
            x: Dict[str, str]
        ) -> AcquisitionAndDisposalOfTreasuryStocksOutputDto:
            return AcquisitionAndDisposalOfTreasuryStocksOutputDto(
                rcept_no=x["rcept_no"],
                corp_cls=x["corp_cls"],
                corp_code=x["corp_code"],
                corp_name=x["corp_name"],
                acqs_mth1=x["acqs_mth1"],
                acqs_mth2=x["acqs_mth2"],
                acqs_mth3=x["acqs_mth3"],
                stock_knd=x["stock_knd"],
                bsis_qy=str_to_int(x["bsis_qy"]),
                change_qy_acqs=str_to_int(x["change_qy_acqs"]),
                change_qy_dsps=str_to_int(x["change_qy_dsps"]),
                change_qy_incnr=str_to_int(x["change_qy_incnr"]),
                trmend_qy=str_to_int(x["trmend_qy"]),
                rm=x["rm"],
            )

        data = response.json()

        return BaseListDto[AcquisitionAndDisposalOfTreasuryStocksOutputDto](
            status=data["status"],
            message=data["message"],
            list=list(map(_mapping, data["list"])) if "list" in data else None,
        )

    def get_capital_increase_and_reduction(
        self, corp_code: str, bsns_year: str, reprt_code: str
    ):
        """
        증자(감자) 현황 조회

        param corp_code: 고유번호
        param bsns_year: 사업연도
        param reprt_code: 보고서 코드 (11013: 사업보고서, 11012: 반기보고서, 11014: 분기보고서)
        """
        path = "/api/irdsSttus.json"
        params = BaseParamDto(
            corp_code=corp_code,
            bsns_year=bsns_year,
            reprt_code=reprt_code,
        )
        response = self.open_dart.get(path, params.dict())

        if response.status_code != 200:
            raise HttpError(path)

        def _mapping(x: Dict[str, str]) -> CapitalIncreaseAndReductionOutputDto:
            return CapitalIncreaseAndReductionOutputDto(
                rcept_no=x["rcept_no"],
                corp_cls=x["corp_cls"],
                corp_code=x["corp_code"],
                corp_name=x["corp_name"],
                isu_dcrs_de=x["isu_dcrs_de"],
                isu_dcrs_stle=x["isu_dcrs_stle"],
                isu_dcrs_stock_knd=x["isu_dcrs_stock_knd"],
                isu_dcrs_qy=str_to_int(x["isu_dcrs_qy"]),
                isu_dcrs_mstvdv_fval_amount=str_to_int(
                    x["isu_dcrs_mstvdv_fval_amount"]
                ),
                isu_dcrs_mstvdv_amount=str_to_int(x["isu_dcrs_mstvdv_amount"]),
            )

        data = response.json()

        return BaseListDto[CapitalIncreaseAndReductionOutputDto](
            status=data["status"],
            message=data["message"],
            list=list(map(_mapping, data["list"])) if "list" in data else None,
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
            list=list(map(_mapping, data["list"])) if "list" in data else None,
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
            list=list(map(_mapping, data["list"])) if "list" in data else None,
        )
