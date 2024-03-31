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
    DirectorTotalRemunerationApprovalOutputDto,
)
from stock_clue.opendart.business_report_info_dto import (
    ExecutivesAndMajorShareholders,
)
from stock_clue.opendart.business_report_info_dto import (
    IndividualDirectorRemunerationOutputDto,
)
from stock_clue.opendart.business_report_info_dto import (
    IndividualRemunerationOver5OutputDto,
)
from stock_clue.opendart.business_report_info_dto import (
    LargestShareHoldersOutputDto,
)
from stock_clue.opendart.business_report_info_dto import (
    NonExecutiveDirectorOutputDto,
)
from stock_clue.opendart.business_report_info_dto import (
    TotalDirectorRemunerationOutputDto,
)
from stock_clue.opendart.business_report_info_dto import (
    TotalStockQuantityOutputDto,
)
from stock_clue.opendart.business_report_info_dto import AuditOpinionOutputDto
from stock_clue.opendart.business_report_info_dto import DividendOutputDto
from stock_clue.opendart.business_report_info_dto import EmployeeInfoOutputDto
from stock_clue.opendart.business_report_info_dto import ExecutiveInfoOutputDto
from stock_clue.opendart.business_report_info_dto import LargeScaleHolding
from stock_clue.opendart.request import Request
from stock_clue.opendart.utils import str_to_float
from stock_clue.opendart.utils import str_to_int

if TYPE_CHECKING:
    from stock_clue.opendart import OpenDart


class BusinessReportInfo:
    def __init__(self, open_dart: "OpenDart"):
        self.request = Request(open_dart.api_key, open_dart.timeout)

    def get_director_total_remuneration_approval(
        self,
        corp_code: str,
        bsns_year: str,
        reprt_code: str,
    ) -> BaseListDto[DirectorTotalRemunerationApprovalOutputDto]:
        """
        이사·감사 전체의 보수현황(주주총회 승인금액) 조회

        Args:
            corp_code (str): 고유번호
            bsns_year (str): 사업연도
            reprt_code (str): 보고서 코드 (11011: 사업보고서, 11012: 반기보고서, 11013: 1분기보고서, 11014: 3분기보고서)

        Returns:
            BaseListDto[DirectorTotalRemunerationApprovalOutputDto]: 이사·감사 전체의 보수현황(주주총회 승인금액) 정보
        """
        path = "/api/drctrAdtAllMendngSttusGmtsckConfmAmount.json"
        params = BaseParamDto(
            corp_code=corp_code,
            bsns_year=bsns_year,
            reprt_code=reprt_code,
        )
        response = self.request.get(path, params.dict())

        def _mapping(
            x: Dict[str, str]
        ) -> DirectorTotalRemunerationApprovalOutputDto:
            return DirectorTotalRemunerationApprovalOutputDto(
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
        return BaseListDto[DirectorTotalRemunerationApprovalOutputDto](
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
        """
        이사·감사 전체의 보수현황(보수지급금액) 조회

        Args:
            corp_code (str): 고유번호
            bsns_year (str): 사업연도
            reprt_code (str): 보고서 코드 (11011: 사업보고서, 11012: 반기보고서, 11013: 1분기보고서, 11014: 3분기보고서)

        Returns:
            BaseListDto[DirectorRemunerationAmountOutputDto]: 이사·감사 전체의 보수현황(보수지급금액) 정보
        """
        path = "/api/drctrAdtAllMendngSttusMendngPymntamtTyCl.json"
        params = BaseParamDto(
            corp_code=corp_code,
            bsns_year=bsns_year,
            reprt_code=reprt_code,
        )
        resposne = self.request.get(path, params.dict())

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

        Args:
            corp_code (str): 고유번호
            bsns_year (str): 사업연도
            reprt_code (str): 보고서 코드 (11011: 사업보고서, 11012: 반기보고서, 11013: 1분기보고서, 11014: 3분기보고서)

        Returns:
            BaseListDto[DividendOutputDto]: 배당에 관한 사항 정보
        """
        path = "/api/alotMatter.json"
        params = BaseParamDto(
            corp_code=corp_code,
            bsns_year=bsns_year,
            reprt_code=reprt_code,
        )
        response = self.request.get(path, params.dict())
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
        """
        주식의 총수 현황 조회

        Args:
            corp_code (str): 고유번호
            bsns_year (str): 사업연도
            reprt_code (str): 보고서 코드 (11011: 사업보고서, 11012: 반기보고서, 11013: 1분기보고서, 11014: 3분기보고서)

        Returns:
            BaseListDto[TotalStockQuantityOutputDto]: 주식의 총수 현황 정보
        """
        path = "/api/stockTotqySttus.json"
        params = BaseParamDto(
            corp_code=corp_code,
            bsns_year=bsns_year,
            reprt_code=reprt_code,
        )
        response = self.request.get(path, params.dict())
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
        """
        회계감사인의 명칭 및 감사의견 조회

        Args:
            corp_code (str): 고유번호
            bsns_year (str): 사업연도
            reprt_code (str): 보고서 코드 (11011: 사업보고서, 11012: 반기보고서, 11013: 1분기보고서, 11014: 3분기보고서)

        Returns:
            BaseListDto[AuditOpinionOutputDto]: 회계감사인의 명칭 및 감사의견 정보
        """
        path = "/api/accnutAdtorNmNdAdtOpinion.json"
        params = BaseParamDto(
            corp_code=corp_code,
            bsns_year=bsns_year,
            reprt_code=reprt_code,
        )
        response = self.request.get(path, params.dict())

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
                adt_reprt_spcmnt_matter=(
                    x["adt_reprt_spcmnt_matter"]
                    if "adt_reprt_spcmnt_matter" in x
                    else None
                ),
                emphs_matter=x["emphs_matter"] if "emphs_matter" in x else None,
                core_adt_matter=(
                    x["core_adt_matter"] if "core_adt_matter" in x else None
                ),
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

        Args:
            corp_code (str): 고유번호
            bsns_year (str): 사업연도
            reprt_code (str): 보고서 코드 (11011: 사업보고서, 11012: 반기보고서, 11013: 1분기보고서, 11014: 3분기보고서

        Returns:
            BaseListDto[NonExecutiveDirectorOutputDto]: 사외이사 및 그 변동사항 정보

        """
        path = "/api/outcmpnyDrctrNdChangeSttus.json"
        params = BaseParamDto(
            corp_code=corp_code,
            bsns_year=bsns_year,
            reprt_code=reprt_code,
        )
        response = self.request.get(path, params.dict())

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

        Args:
            corp_code (str): 고유번호
            bsns_year (str): 사업연도
            reprt_code (str): 보고서 코드 (11011: 사업보고서, 11012: 반기보고서, 11013: 1분기보고서, 11014: 3분기보고서)

        Returns:
            BaseListDto[AcquisitionAndDisposalOfTreasuryStocksOutputDto]: 자기주식 취득 및 처분 현황 정보
        """
        path = "/api/tesstkAcqsDspsSttus.json"

        params = BaseParamDto(
            corp_code=corp_code,
            bsns_year=bsns_year,
            reprt_code=reprt_code,
        )
        response = self.request.get(path, params.dict())

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

        Args:
            corp_code (str): Corporation code
            bsns_year (str): Business year
            reprt_code (str): Report code

        Returns:
            BaseListDto[CapitalIncreaseAndReductionOutputDto]: 증자(감자) 현황 조회 정보
        """

        path = "/api/irdsSttus.json"
        params = BaseParamDto(
            corp_code=corp_code,
            bsns_year=bsns_year,
            reprt_code=reprt_code,
        )
        response = self.request.get(path, params.dict())

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
        """
        최대주주 현황 조회

        Args:
            corp_code (str): 고유번호
            bsns_year (str): 사업연도
            reprt_code (str): 보고서 코드 (11011: 사업보고서, 11012: 반기보고서, 11013: 1분기보고서, 11014: 3분기보고서)

        Returns:
            BaseListDto[LargestShareHoldersOutputDto]: 최대주주 현황 정보
        """
        path = "/api/hyslrSttus.json"
        params = BaseParamDto(
            corp_code=corp_code,
            bsns_year=bsns_year,
            reprt_code=reprt_code,
        )
        response = self.request.get(path, params.dict())

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
        """
        최대주주 변동 현황 조회

        Args:
            corp_code (str): 고유번호
            bsns_year (str): 사업연도
            reprt_code (str): 보고서 코드 (11011: 사업보고서, 11012: 반기보고서, 11013: 1분기보고서, 11014: 3분기보고서)

        Returns:
            BaseListDto[ChangedLargestShareHoldersOutputDto]: 최대주주 변동 현황 정보
        """
        path = "/api/hyslrChgSttus.json"
        params = BaseParamDto(
            corp_code=corp_code,
            bsns_year=bsns_year,
            reprt_code=reprt_code,
        )
        response = self.request.get(path, params.dict())

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

    def get_executive_info(
        self, corp_code: str, bsns_year: str, reprt_code: str
    ) -> BaseListDto[ExecutiveInfoOutputDto]:
        """
        임원 현황 조회

        Args:
            corp_code (str): 고유번호
            bsns_year (str): 사업연도
            reprt_code (str): 보고서 코드 (11011: 사업보고서, 11012: 반기보고서, 11013: 1분기보고서, 11014: 3분기보고서)

        Returns:
            BaseListDto[ExecutiveInfoOutputDto]: 임원 현황 정보
        """
        path = "/api/exctvSttus.json"
        params = BaseParamDto(
            corp_code=corp_code,
            bsns_year=bsns_year,
            reprt_code=reprt_code,
        )
        response = self.request.get(path, params.dict())
        if response.status_code != 200:
            raise HttpError(path)

        def _mapping(x: Dict[str, str]) -> ExecutiveInfoOutputDto:
            return ExecutiveInfoOutputDto(
                rcept_no=x["rcept_no"],
                corp_cls=x["corp_cls"],
                corp_code=x["corp_code"],
                corp_name=x["corp_name"],
                nm=x["nm"],
                sexdstn=x["sexdstn"],
                birth_ym=x["birth_ym"],
                ofcps=x["ofcps"],
                rgit_exctv_at=(
                    x["rgit_exctv_at"] if "rgit_exctv_at" in x else None
                ),
                fte_at=x["fte_at"],
                chrg_job=x["chrg_job"],
                main_career=x["main_career"],
                maxmm_shrholdr_relate=(
                    x["maxmm_shrholdr_relate"]
                    if "maxmm_shrholdr_relate" in x
                    else None
                ),
                hffc_pd=x["hffc_pd"],
                tenure_end_on=x["tenure_end_on"],
            )

        data = response.json()
        return BaseListDto[ExecutiveInfoOutputDto](
            status=data["status"],
            message=data["message"],
            list=list(map(_mapping, data["list"])) if "list" in data else None,
        )

    def get_employee_info(
        self, corp_code: str, bsns_year: str, reprt_code: str
    ) -> BaseListDto[EmployeeInfoOutputDto]:
        """
        직원 현황 조회

        Args:
            corp_code (str): 고유번호
            bsns_year (str): 사업연도
            reprt_code (str): 보고서 코드 (11011: 사업보고서, 11012: 반기보고서, 11013: 1분기보고서, 11014: 3분기보고서

        Returns:
            BaseListDto[EmployeeInfoOutputDto]: 직원 현황 정보
        """
        path = "/api/empSttus.json"
        param = BaseParamDto(
            corp_code=corp_code, bsns_year=bsns_year, reprt_code=reprt_code
        )
        response = self.request.get(path, param.dict())

        if response.status_code != 200:
            raise HttpError(path)

        def _mapping(x: Dict[str, str]) -> EmployeeInfoOutputDto:
            return EmployeeInfoOutputDto(
                rcept_no=x["rcept_no"],
                corp_cls=x["corp_cls"],
                corp_code=x["corp_code"],
                corp_name=x["corp_name"],
                fo_bbm=x["fo_bbm"],
                sexdstn=x["sexdstn"],
                reform_bfe_emp_co_rgllbr=str_to_int(
                    x["reform_bfe_emp_co_rgllbr"]
                ),
                reform_bfe_emp_co_cnttk=str_to_int(
                    x["reform_bfe_emp_co_cnttk"]
                ),
                reform_bfe_emp_co_etc=str_to_int(x["reform_bfe_emp_co_etc"]),
                rgllbr_co=str_to_int(x["rgllbr_co"]),
                rgllbr_abacpt_labrr_co=str_to_int(x["rgllbr_abacpt_labrr_co"]),
                cnttk_co=str_to_int(x["cnttk_co"]),
                cnttk_abacpt_labrr_co=str_to_int(x["cnttk_abacpt_labrr_co"]),
                sm=str_to_int(x["sm"]),
                avrg_cnwk_sdytrn=x["avrg_cnwk_sdytrn"],
                fyer_salary_totamt=str_to_int(x["fyer_salary_totamt"]),
                jan_salary_am=str_to_int(x["jan_salary_am"]),
                rm=x["rm"],
            )

        data = response.json()
        return BaseListDto[EmployeeInfoOutputDto](
            status=data["status"],
            message=data["message"],
            list=list(map(_mapping, data["list"])) if "list" in data else None,
        )

    def get_individual_director_remuneration(
        self, corp_code: str, bsns_year: str, reprt_code: str
    ) -> BaseListDto[IndividualDirectorRemunerationOutputDto]:
        """
        이사·감사의 개인별 보수 현황 조회

        Args:
            corp_code (str): 고유번호
            bsns_year (str): 사업연도
            reprt_code (str): 보고서 코드 (11011: 사업보고서, 11012: 반기보고서, 11013: 1분기보고서, 11014: 3분기보고서

        Returns:
            BaseListDto[IndividualDirectorRemunerationOutputDto]: 이사·감사의 개인별 보수 현황 정보
        """
        path = "/api/hmvAuditIndvdlBySttus.json"
        param = BaseParamDto(
            corp_code=corp_code, bsns_year=bsns_year, reprt_code=reprt_code
        )

        response = self.request.get(path, param.dict())
        if response.status_code != 200:
            raise HttpError(path)

        def _mapping(
            x: Dict[str, str]
        ) -> IndividualDirectorRemunerationOutputDto:
            return IndividualDirectorRemunerationOutputDto(
                rcept_no=x["rcept_no"],
                corp_cls=x["corp_cls"],
                corp_code=x["corp_code"],
                corp_name=x["corp_name"],
                nm=x["nm"],
                ofcps=x["ofcps"],
                mendng_totamt=str_to_int(x["mendng_totamt"]),
                mendng_totamt_ct_incls_mendng=str_to_int(
                    x["mendng_totamt_ct_incls_mendng"]
                ),
            )

        data = response.json()
        return BaseListDto[IndividualDirectorRemunerationOutputDto](
            status=data["status"],
            message=data["message"],
            list=list(map(_mapping, data["list"])) if "list" in data else None,
        )

    def get_total_director_remuneration(
        self, corp_code: str, bsns_year: str, reprt_code: str
    ) -> BaseListDto[TotalDirectorRemunerationOutputDto]:
        """
        이사·감사의 전체의 보수 현황 조회

        Args:
            corp_code (str): 고유번호
            bsns_year (str): 사업연도
            reprt_code (str): 보고서 코드 (11011: 사업보고서, 11012: 반기보고서, 11013: 1분기보고서, 11014: 3분기보고서

        Returns:
            BaseListDto[TotalDirectorRemunerationOutputDto]: 이사·감사의 전체의 보수 현황 정보
        """
        path = "/api/hmvAuditAllSttus.json"
        params = BaseParamDto(
            corp_code=corp_code, bsns_year=bsns_year, reprt_code=reprt_code
        )
        response = self.request.get(path, params.dict())

        if response.status_code != 200:
            raise HttpError(path)

        def _mapping(x: Dict[str, str]) -> TotalDirectorRemunerationOutputDto:
            return TotalDirectorRemunerationOutputDto(
                rcept_no=x["rcept_no"],
                corp_cls=x["corp_cls"],
                corp_code=x["corp_code"],
                corp_name=x["corp_name"],
                nmpr=str_to_int(x["nmpr"]),
                mendng_totamt=str_to_int(x["mendng_totamt"]),
                jan_avrg_mendng_am=str_to_int(x["jan_avrg_mendng_am"]),
                rm=x["rm"],
            )

        data = response.json()

        return BaseListDto[TotalDirectorRemunerationOutputDto](
            status=data["status"],
            message=data["message"],
            list=list(map(_mapping, data["list"])) if "list" in data else None,
        )

    def get_individual_remuneration_over5(
        self, corp_code: str, bsns_year: str, reprt_code: str
    ) -> BaseListDto[IndividualRemunerationOver5OutputDto]:
        """
        개인별 보수지급 금액(5억이상 상위5인) 조회

        Args:
            corp_code (str): 고유번호
            bsns_year (str): 사업년도
            reprt_code (str): 보고서 코드 (11011: 사업보고서, 11012: 반기보고서, 11013: 1분기보고서

        Returns:
            BaseListDto[IndividualRemunerationOver5OutputDto]: 개인별 보수지급 금액(5억이상 상위5인) 정보
        """
        path = "/api/indvdlByPay.json"
        params = BaseParamDto(
            corp_code=corp_code, bsns_year=bsns_year, reprt_code=reprt_code
        )
        response = self.request.get(path, params.dict())

        if response.status_code != 200:
            raise HttpError(path)

        def _mapping(x: Dict[str, str]) -> IndividualRemunerationOver5OutputDto:
            return IndividualRemunerationOver5OutputDto(
                rcept_no=x["rcept_no"],
                corp_cls=x["corp_cls"],
                corp_code=x["corp_code"],
                corp_name=x["corp_name"],
                nm=x["nm"],
                ofcps=x["ofcps"],
                mendng_totamt=str_to_int(x["mendng_totamt"]),
                mendng_totamt_ct_incls_mendng=str_to_int(
                    x["mendng_totamt_ct_incls_mendng"]
                ),
            )

        data = response.json()

        return BaseListDto[IndividualRemunerationOver5OutputDto](
            status=data["status"],
            message=data["message"],
            list=list(map(_mapping, data["list"])) if "list" in data else None,
        )

    def get_large_scale_holding(
        self, corp_code: str
    ) -> BaseListDto[LargeScaleHolding]:
        """
        지분공시 종합정보 - 대량보유상황 보고 조회

        Args:
            corp_code (str): 고유번호

        Returns:
            BaseListDto[LargeScaleHolding]: 지분공시 종합정보 - 대량보유상황 보고 정보
        """
        path = "/api/majorstock.json"
        param = BaseParamDto(corp_code=corp_code)
        response = self.request.get(path, param.dict())
        if response.status_code != 200:
            raise HttpError(path)

        def _mapping(x: Dict[str, str]) -> LargeScaleHolding:
            return LargeScaleHolding(
                rcept_no=x["rcept_no"],
                rcept_dt=x["rcept_dt"],
                corp_code=x["corp_code"],
                corp_name=x["corp_name"],
                report_tp=x["report_tp"],
                repror=x["repror"],
                stkqy=str_to_int(x["stkqy"]),
                stkqy_irds=str_to_int(x["stkqy_irds"]),
                stkrt=str_to_float(x["stkrt"]),
                stkrt_irds=str_to_float(x["stkrt_irds"]),
                ctr_stkqy=str_to_int(x["ctr_stkqy"]),
                ctr_stkrt=str_to_float(x["ctr_stkrt"]),
                report_resn=x["report_resn"],
            )

        data = response.json()
        return BaseListDto[LargeScaleHolding](
            status=data["status"],
            message=data["message"],
            list=list(map(_mapping, data["list"])) if "list" in data else None,
        )

    def get_executives_and_major_shareholders(
        self, corp_code: str
    ) -> BaseListDto[ExecutivesAndMajorShareholders]:
        """
        지분공시 종합정보 - 임원 . 주요주주 소유보고 조회

        Args:
            corp_code (str): 고유번호

        Returns:
            BaseListDto[ExecutivesAndMajorShareholders]: 지분공시 종합정보 - 임원 . 주요주주 소유보고 정보
        """
        path = "/api/elestock.json"
        params = BaseParamDto(corp_code=corp_code)

        response = self.request.get(path, params.dict())
        if response.status_code != 200:
            raise HttpError(path)

        def _mapping(x: Dict[str, str]) -> ExecutivesAndMajorShareholders:
            return ExecutivesAndMajorShareholders(
                rcept_no=x["rcept_no"],
                rcept_dt=x["rcept_dt"],
                corp_code=x["corp_code"],
                corp_name=x["corp_name"],
                repror=x["repror"],
                isu_exctv_rgist_at=x["isu_exctv_rgist_at"],
                isu_exctv_ofcps=x["isu_exctv_ofcps"],
                isu_main_shrholdr=x["isu_main_shrholdr"],
                sp_stock_lmp_cnt=str_to_int(x["sp_stock_lmp_cnt"]),
                sp_stock_lmp_irds_cnt=str_to_int(x["sp_stock_lmp_irds_cnt"]),
                sp_stock_lmp_rate=str_to_float(x["sp_stock_lmp_rate"]),
                sp_stock_lmp_irds_rate=str_to_float(
                    x["sp_stock_lmp_irds_rate"]
                ),
            )

        data = response.json()
        return BaseListDto[ExecutivesAndMajorShareholders](
            status=data["status"],
            message=data["message"],
            list=list(map(_mapping, data["list"])) if "list" in data else None,
        )
