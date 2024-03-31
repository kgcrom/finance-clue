"""주요사항보고서 주요정보 OpenDart 연동 Module"""

from typing import Dict

from stock_clue.error import HttpError
from stock_clue.opendart import OpenDart
from stock_clue.opendart.base_dto import BaseListDto
from stock_clue.opendart.base_dto import BaseParamDto
from stock_clue.opendart.major_report_dto import (
    AcquisitionOfTreasuryStocksOutputDto,
)
from stock_clue.opendart.major_report_dto import (
    CapitalIncreaseAndDecreaseOutputDto,
)
from stock_clue.opendart.major_report_dto import (
    DisposalOfTreasuryStocksOutputDto,
)
from stock_clue.opendart.major_report_dto import BondWithWarrantsOutputDto
from stock_clue.opendart.major_report_dto import CapitalIncreaseOutputDto
from stock_clue.opendart.major_report_dto import CapitalReductionOutputDto
from stock_clue.opendart.major_report_dto import CaptitalDecreaseOutputDto
from stock_clue.opendart.major_report_dto import ConvertibleBondOutputDto
from stock_clue.opendart.major_report_dto import ExchangeableBondOutputDto
from stock_clue.opendart.request import Request
from stock_clue.opendart.utils import str_to_float
from stock_clue.opendart.utils import str_to_int


class MajorReport:
    def __init__(self, open_dart: OpenDart):
        self.request = Request(open_dart.api_key, open_dart.timeout)

    def get_capital_increase(
        self, corp_code: str, bgn_de: str, end_de: str
    ) -> BaseListDto[CapitalIncreaseOutputDto]:
        """
        유상증자 결정 공시 조회

        Args:
            corp_code (str): 고유번호
            bgn_de (str): 시작일(최초접수일)
            end_de (str): 종료일(최초접수일)

        Returns:
            BaseListDto[CapitalIncrease]: 유상증자 결정 조회 결과
        """
        path = "/api/piicDecsn.json"
        params = BaseParamDto(corp_code=corp_code, bgn_de=bgn_de, end_de=end_de)

        response = self.request.get(path=path, params=params.dict())
        if response.status_code != 200:
            raise HttpError(path)

        def _mapping(x: Dict[str, str]) -> CapitalIncreaseOutputDto:
            return CapitalIncreaseOutputDto(
                rcept_no=x["rcept_no"],
                corp_cls=x["corp_cls"],
                corp_code=x["corp_code"],
                corp_name=x["corp_name"],
                nstk_ostk_cnt=str_to_int(x["nstk_ostk_cnt"]),
                nstk_estk_cnt=str_to_int(x["nstk_estk_cnt"]),
                fv_ps=str_to_int(x["fv_ps"]),
                bfic_tisstk_ostk=str_to_int(x["bfic_tisstk_ostk"]),
                bfic_tisstk_estk=str_to_int(x["bfic_tisstk_estk"]),
                fdpp_fclt=str_to_int(x["fdpp_fclt"]),
                fdpp_bsninh=str_to_int(x["fdpp_bsninh"]),
                fdpp_op=str_to_int(x["fdpp_op"]),
                fdpp_dtrp=str_to_int(x["fdpp_dtrp"]),
                fdpp_ocsa=str_to_int(x["fdpp_ocsa"]),
                fdpp_etc=str_to_int(x["fdpp_etc"]),
                ic_mthn=x["ic_mthn"],
                ssl_at=x["ssl_at"],
                ssl_bgd=x["ssl_bgd"],
                ssl_edd=x["ssl_edd"],
            )

        data = response.json()

        return BaseListDto[CapitalIncreaseOutputDto](
            status=data["status"],
            message=data["message"],
            list=list(map(_mapping, data["list"])) if "list" in data else None,
        )

    def get_capital_decrease(
        self, corp_code: str, bgn_de: str, end_de: str
    ) -> BaseListDto[CaptitalDecreaseOutputDto]:
        """
        무상증자 결정 공시 조회

        Args:
            corp_code (str): 고유번호
            bgn_de (str): 시작일(최초접수일)
            end_de (str): 종료일(최초접수일)

        Returns:
            BaseListDto[CaptitalDecreaseOutputDto]: 무상증자 결정 DTO
        """
        path = "/api/fricDecsn.json"
        params = BaseParamDto(corp_code=corp_code, bgn_de=bgn_de, end_de=end_de)

        response = self.request.get(path=path, params=params.dict())
        if response.status_code != 200:
            raise HttpError(path)

        def _mapping(x: Dict[str, str]) -> CaptitalDecreaseOutputDto:
            return CaptitalDecreaseOutputDto(
                rcept_no=x["rcept_no"],
                corp_cls=x["corp_cls"],
                corp_code=x["corp_code"],
                corp_name=x["corp_name"],
                nstk_ostk_cnt=str_to_int(x["nstk_ostk_cnt"]),
                nstk_estk_cnt=str_to_int(x["nstk_estk_cnt"]),
                fv_ps=str_to_int(x["fv_ps"]),
                bfic_tisstk_ostk=str_to_int(x["bfic_tisstk_ostk"]),
                bfic_tisstk_estk=str_to_int(x["bfic_tisstk_estk"]),
                nstk_asstd=x["nstk_asstd"],
                nstk_ascnt_ps_ostk=str_to_float(x["nstk_ascnt_ps_ostk"]),
                nstk_ascnt_ps_estk=str_to_float(x["nstk_ascnt_ps_estk"]),
                nstk_dividrk=x["nstk_dividrk"],
                nstk_dlprd=x["nstk_dlprd"],
                nstk_lstprd=x["nstk_lstprd"],
                bddd=x["bddd"],
                od_a_at_t=str_to_int(x["od_a_at_t"]),
                od_a_at_b=str_to_int(x["od_a_at_b"]),
                adt_a_atn=x["adt_a_atn"],
            )

        data = response.json()

        return BaseListDto[CaptitalDecreaseOutputDto](
            status=data["status"],
            message=data["message"],
            list=list(map(_mapping, data["list"])) if "list" in data else None,
        )

    def get_capital_increase_and_decrease(
        self, corp_code: str, bgn_de: str, end_de: str
    ) -> BaseListDto[CapitalIncreaseAndDecreaseOutputDto]:
        """
        유무상증자 결정 공시 조회

        Args:
            corp_code (str): 고유번호
            bgn_de (str): 시작일(최초접수일)
            end_de (str): 종료일(최초접수일)

        Returns:
            BaseListDto[CapitalIncreaseAndDecreaseOutputDto]: 유무상증자 결정 조회 결과
        """
        path = "/api/pifricDecsn.json"
        params = BaseParamDto(corp_code=corp_code, bgn_de=bgn_de, end_de=end_de)

        response = self.request.get(path=path, params=params.dict())
        if response.status_code != 200:
            raise HttpError(path)

        def _mapping(x: Dict[str, str]) -> CapitalIncreaseAndDecreaseOutputDto:
            return CapitalIncreaseAndDecreaseOutputDto(
                rcept_no=x["rcept_no"],
                corp_cls=x["corp_cls"],
                corp_code=x["corp_code"],
                corp_name=x["corp_name"],
                piic_nstk_ostk_cnt=str_to_int(x["piic_nstk_ostk_cnt"]),
                piic_nstk_estk_cnt=str_to_int(x["piic_nstk_estk_cnt"]),
                piic_fv_ps=str_to_int(x["piic_fv_ps"]),
                piic_bfic_tisstk_ostk=str_to_int(x["piic_bfic_tisstk_ostk"]),
                piic_bfic_tisstk_estk=str_to_int(x["piic_bfic_tisstk_estk"]),
                piic_fdpp_fclt=str_to_int(x["piic_fdpp_fclt"]),
                piic_fdpp_bsninh=(
                    str_to_int(x["piic_fdpp_bsninh"])
                    if x["piic_fdpp_bsninh"]
                    else None
                ),
                piic_fdpp_op=str_to_int(x["piic_fdpp_op"]),
                piic_fdpp_dtrp=(
                    str_to_int(x["piic_fdpp_dtrp"])
                    if x["piic_fdpp_dtrp"]
                    else None
                ),
                piic_fdpp_ocsa=str_to_int(x["piic_fdpp_ocsa"]),
                piic_fdpp_etc=str_to_int(x["piic_fdpp_etc"]),
                piic_ic_mthn=x["piic_ic_mthn"],
                fric_nstk_ostk_cnt=str_to_int(x["fric_nstk_ostk_cnt"]),
                fric_nstk_estk_cnt=str_to_int(x["fric_nstk_estk_cnt"]),
                fric_fv_ps=str_to_int(x["fric_fv_ps"]),
                fric_bfic_tisstk_ostk=str_to_int(x["fric_bfic_tisstk_ostk"]),
                fric_bfic_tisstk_estk=str_to_int(x["fric_bfic_tisstk_estk"]),
                fric_nstk_asstd=x["fric_nstk_asstd"],
                fric_nstk_ascnt_ps_ostk=str_to_float(
                    x["fric_nstk_ascnt_ps_ostk"]
                ),
                fric_nstk_ascnt_ps_estk=str_to_float(
                    x["fric_nstk_ascnt_ps_estk"]
                ),
                fric_nstk_dividrk=x["fric_nstk_dividrk"],
                fric_nstk_dlprd=x["fric_nstk_dlprd"],
                fric_nstk_lstprd=x["fric_nstk_lstprd"],
                fric_bddd=x["fric_bddd"],
                fric_od_a_at_t=str_to_int(x["fric_od_a_at_t"]),
                fric_od_a_at_b=str_to_int(x["fric_od_a_at_b"]),
                fric_adt_a_atn=x["fric_adt_a_atn"],
                ssl_at=x["ssl_at"],
                ssl_bgd=x["ssl_bgd"],
                ssl_edd=x["ssl_edd"],
            )

        data = response.json()

        return BaseListDto[CapitalIncreaseAndDecreaseOutputDto](
            status=data["status"],
            message=data["message"],
            list=list(map(_mapping, data["list"])) if "list" in data else None,
        )

    def get_capital_reduction(
        self, corp_code: str, bgn_de: str, end_de: str
    ) -> BaseListDto[CapitalReductionOutputDto]:
        """
        감자 결정 공시 조회

        Args:
            corp_code (str): 고유번호
            bgn_de (str): 시작일(최초접수일)
            end_de (str): 종료일(최초접수일)

        Returns:
            BaseListDto[CapitalReductionOutputDto]: 감자 결정 조회 결과
        """
        path = "/api/crDecsn.json"

        params = BaseParamDto(corp_code=corp_code, bgn_de=bgn_de, end_de=end_de)

        response = self.request.get(path=path, params=params.dict())
        if response.status_code != 200:
            raise HttpError(path)

        def _mapping(x: Dict[str, str]) -> CapitalReductionOutputDto:
            return CapitalReductionOutputDto(
                rcept_no=x["rcept_no"],
                corp_cls=x["corp_cls"],
                corp_code=x["corp_code"],
                corp_name=x["corp_name"],
                crstk_ostk_cnt=str_to_int(x["crstk_ostk_cnt"]),
                crstk_estk_cnt=str_to_int(x["crstk_estk_cnt"]),
                fv_ps=str_to_int(x["fv_ps"]),
                bfcr_cpt=str_to_int(x["bfcr_cpt"]),
                atcr_cpt=str_to_int(x["atcr_cpt"]),
                bfcr_tisstk_ostk=str_to_int(x["bfcr_tisstk_ostk"]),
                atcr_tisstk_ostk=str_to_int(x["atcr_tisstk_ostk"]),
                bfcr_tisstk_estk=str_to_int(x["bfcr_tisstk_estk"]),
                atcr_tisstk_estk=str_to_int(x["atcr_tisstk_estk"]),
                cr_rt_ostk=x["cr_rt_ostk"],
                cr_rt_estk=x["cr_rt_estk"],
                cr_std=x["cr_std"],
                cr_mth=x["cr_mth"],
                cr_rs=x["cr_rs"],
                crsc_gmtsck_prd=x["crsc_gmtsck_prd"],
                crsc_trnmsppd=x["crsc_trnmsppd"],
                crsc_osprpd=x["crsc_osprpd"],
                crsc_trspprpd=x["crsc_trspprpd"],
                crsc_osprpd_bgd=x["crsc_osprpd_bgd"],
                crsc_osprpd_edd=x["crsc_osprpd_edd"],
                crsc_trspprpd_bgd=x["crsc_trspprpd_bgd"],
                crsc_trspprpd_edd=x["crsc_trspprpd_edd"],
                crsc_nstkdlprd=x["crsc_nstkdlprd"],
                crsc_nstklstprd=x["crsc_nstklstprd"],
                cdobprpd_bgd=x["cdobprpd_bgd"],
                cdobprpd_edd=x["cdobprpd_edd"],
                ospr_nstkdl_pl=x["ospr_nstkdl_pl"],
                bddd=x["bddd"],
                od_a_at_t=str_to_int(x["od_a_at_t"]),
                od_a_at_b=str_to_int(x["od_a_at_b"]),
                adt_a_atn=x["adt_a_atn"],
                ftc_stt_atn=x["ftc_stt_atn"],
            )

        data = response.json()

        return BaseListDto[CapitalReductionOutputDto](
            status=data["status"],
            message=data["message"],
            list=list(map(_mapping, data["list"])) if "list" in data else None,
        )

    def get_convertible_bond(
        self, corp_code: str, bgn_de: str, end_de: str
    ) -> BaseListDto[ConvertibleBondOutputDto]:
        """
        전환사채 결정 공시 조회

        Args:
            corp_code (str): 고유번호
            bgn_de (str): 시작일(최초접수일)
            end_de (str): 종료일(최초접수일)

        Returns:
            BaseListDto[ConvertibleBondOutputDto]: 전환사채 결정 조회 결과
        """
        path = "/api/cvbdIsDecsn.json"

        params = BaseParamDto(corp_code=corp_code, bgn_de=bgn_de, end_de=end_de)
        response = self.request.get(path=path, params=params.dict())
        if response.status_code != 200:
            raise HttpError(path)

        def _mapping(x: Dict[str, str]) -> ConvertibleBondOutputDto:
            return ConvertibleBondOutputDto(
                rcept_no=x["rcept_no"],
                corp_cls=x["corp_cls"],
                corp_code=x["corp_code"],
                corp_name=x["corp_name"],
                bd_tm=x["bd_tm"],
                bd_knd=x["bd_knd"],
                bd_fta=str_to_int(x["bd_fta"]),
                atcsc_rmislmt=(
                    str_to_int(x["atcsc_rmislmt"])
                    if "atcsc_rmislmt" in x
                    else None if "atcsc_rmislmt" in x else None
                ),
                ovis_fta=str_to_int(x["ovis_fta"]),
                ovis_fta_crn=x["ovis_fta_crn"],
                ovis_ster=x["ovis_ster"],
                ovis_isar=x["ovis_isar"],
                ovis_mktnm=x["ovis_mktnm"],
                fdpp_fclt=str_to_int(x["fdpp_fclt"]),
                fdpp_bsninh=str_to_int(x["fdpp_bsninh"]),
                fdpp_op=str_to_int(x["fdpp_op"]),
                fdpp_dtrp=str_to_int(x["fdpp_dtrp"]),
                fdpp_ocsa=str_to_int(x["fdpp_ocsa"]),
                fdpp_etc=str_to_int(x["fdpp_etc"]),
                bd_intr_ex=x["bd_intr_ex"],
                bd_intr_sf=x["bd_intr_sf"],
                bd_mtd=x["bd_mtd"],
                bdis_mthn=x["bdis_mthn"],
                cv_rt=x["cv_rt"],
                cv_prc=str_to_int(x["cv_prc"]),
                cvisstk_knd=x["cvisstk_knd"],
                cvisstk_cnt=str_to_int(x["cvisstk_cnt"]),
                cvisstk_tisstk_vs=x["cvisstk_tisstk_vs"],
                cvrqpd_bgd=x["cvrqpd_bgd"],
                cvrqpd_edd=x["cvrqpd_edd"],
                act_mktprcfl_cvprc_lwtrsprc=(
                    str_to_int(x["act_mktprcfl_cvprc_lwtrsprc"])
                    if "act_mktprcfl_cvprc_lwtrsprc" in x
                    else None if "act_mktprcfl_cvprc_lwtrsprc" in x else None
                ),
                act_mktprcfl_cvprc_lwtrsprc_bs=(
                    x["act_mktprcfl_cvprc_lwtrsprc_bs"]
                    if "act_mktprcfl_cvprc_lwtrsprc_bs" in x
                    else None
                ),
                rmislmt_lt70p=(
                    str_to_int(x["rmislmt_lt70p"])
                    if "rmislmt_lt70p" in x
                    else None
                ),
                abmg=x["abmg"],
                sbd=x["sbd"],
                pymd=x["pymd"],
                rpmcmp=x["rpmcmp"],
                grint=x["grint"],
                bddd=x["bddd"],
                od_a_at_t=str_to_int(x["od_a_at_t"]),
                od_a_at_b=str_to_int(x["od_a_at_b"]),
                adt_a_atn=x["adt_a_atn"],
                rs_sm_atn=x["rs_sm_atn"],
                ex_sm_r=x["ex_sm_r"],
                ovis_ltdtl=x["ovis_ltdtl"],
                ftc_stt_atn=x["ftc_stt_atn"],
            )

        data = response.json()

        return BaseListDto[ConvertibleBondOutputDto](
            status=data["status"],
            message=data["message"],
            list=list(map(_mapping, data["list"])) if "list" in data else None,
        )

    def get_bond_with_warrants(
        self, corp_code: str, bgn_de: str, end_de: str
    ) -> BaseListDto[BondWithWarrantsOutputDto]:
        """
        신주인수권부사채권 발행결정 공시 조회

        Args:
            corp_code (str): 고유번호
            bgn_de (str): 시작일(최초접수일)
            end_de (str): 종료일(최초접수일)

        Returns:
            BaseListDto[BondWithWarrantsOutputDto]: 신주인수권부사채권 발행결정 조회 결과
        """
        path = "/api/bdwtIsDecsn.json"

        params = BaseParamDto(corp_code=corp_code, bgn_de=bgn_de, end_de=end_de)
        response = self.request.get(path=path, params=params.dict())
        if response.status_code != 200:
            raise HttpError(path)

        def _mapping(x: Dict[str, str]) -> BondWithWarrantsOutputDto:
            return BondWithWarrantsOutputDto(
                rcept_no=x["rcept_no"],
                corp_cls=x["corp_cls"],
                corp_code=x["corp_code"],
                corp_name=x["corp_name"],
                bd_tm=x["bd_tm"],
                bd_knd=x["bd_knd"],
                bd_fta=str_to_int(x["bd_fta"]),
                atcsc_rmislmt=(
                    str_to_int(x["atcsc_rmislmt"])
                    if "atcsc_rmislmt" in x
                    else None if "atcsc_rmislmt" in x else None
                ),
                ovis_fta=str_to_int(x["ovis_fta"]),
                ovis_fta_crn=x["ovis_fta_crn"],
                ovis_ster=x["ovis_ster"],
                ovis_isar=x["ovis_isar"],
                ovis_mktnm=x["ovis_mktnm"],
                fdpp_fclt=str_to_int(x["fdpp_fclt"]),
                fdpp_bsninh=str_to_int(x["fdpp_bsninh"]),
                fdpp_op=str_to_int(x["fdpp_op"]),
                fdpp_dtrp=str_to_int(x["fdpp_dtrp"]),
                fdpp_ocsa=str_to_int(x["fdpp_ocsa"]),
                fdpp_etc=str_to_int(x["fdpp_etc"]),
                bd_intr_ex=x["bd_intr_ex"],
                bd_intr_sf=x["bd_intr_sf"],
                bd_mtd=x["bd_mtd"],
                bdis_mthn=x["bdis_mthn"],
                ex_rt=x["ex_rt"],
                ex_prc=str_to_int(x["ex_prc"]),
                ex_prc_dmth=x["ex_prc_dmth"],
                bdwt_div_atn=x["bdwt_div_atn"],
                nstk_pym_mth=x["nstk_pym_mth"],
                nstk_isstk_knd=x["nstk_isstk_knd"],
                nstk_isstk_cnt=str_to_int(x["nstk_isstk_cnt"]),
                nstk_isstk_tisstk_vs=x["nstk_isstk_tisstk_vs"],
                expd_bgd=x["expd_bgd"],
                expd_edd=x["expd_edd"],
                act_mktprcfl_cvprc_lwtrsprc=(
                    str_to_int(x["act_mktprcfl_cvprc_lwtrsprc"])
                    if "act_mktprcfl_cvprc_lwtrsprc" in x
                    else None if "act_mktprcfl_cvprc_lwtrsprc" in x else None
                ),
                act_mktprcfl_cvprc_lwtrsprc_bs=(
                    x["act_mktprcfl_cvprc_lwtrsprc_bs"]
                    if "act_mktprcfl_cvprc_lwtrsprc_bs" in x
                    else None
                ),
                rmislmt_lt70p=(
                    str_to_int(x["rmislmt_lt70p"])
                    if "rmislmt_lt70p" in x
                    else None
                ),
                abmg=x["abmg"],
                sbd=x["sbd"],
                pymd=x["pymd"],
                rpmcmp=x["rpmcmp"],
                grint=x["grint"],
                bddd=x["bddd"],
                od_a_at_t=str_to_int(x["od_a_at_t"]),
                od_a_at_b=str_to_int(x["od_a_at_b"]),
                adt_a_atn=x["adt_a_atn"],
                rs_sm_atn=x["rs_sm_atn"],
                ex_sm_r=x["ex_sm_r"],
                ovis_ltdtl=x["ovis_ltdtl"],
                ftc_stt_atn=x["ftc_stt_atn"],
            )

        data = response.json()

        return BaseListDto[BondWithWarrantsOutputDto](
            status=data["status"],
            message=data["message"],
            list=list(map(_mapping, data["list"])) if "list" in data else None,
        )

    def get_exchangeable_bond(
        self, corp_code: str, bgn_de: str, end_de: str
    ) -> BaseListDto[ExchangeableBondOutputDto]:
        """
        교환사채권 발행결정 공시 조회

        Args:
            corp_code (str): 고유번호
            bgn_de (str): 시작일(최초접수일)
            end_de (str): 종료일(최초접수일)

        Returns:
            BaseListDto[ExchangeableBondOutputDto]: 교환사채권 발행결정 조회 결과
        """
        path = "/api/exbdIsDecsn.json"

        params = BaseParamDto(corp_code=corp_code, bgn_de=bgn_de, end_de=end_de)
        response = self.request.get(path=path, params=params.dict())
        if response.status_code != 200:
            raise HttpError(path)

        def _mapping(x: Dict[str, str]) -> ExchangeableBondOutputDto:
            return ExchangeableBondOutputDto(
                rcept_no=x["rcept_no"],
                corp_cls=x["corp_cls"],
                corp_code=x["corp_code"],
                corp_name=x["corp_name"],
                bd_tm=x["bd_tm"],
                bd_knd=x["bd_knd"],
                bd_fta=x["bd_fta"],
                ovis_fta=x["ovis_fta"],
                ovis_fta_crn=x["ovis_fta_crn"],
                ovis_ster=x["ovis_ster"],
                ovis_isar=x["ovis_isar"],
                ovis_mktnm=x["ovis_mktnm"],
                fdpp_fclt=str_to_int(x["fdpp_fclt"]),
                fdpp_bsninh=str_to_int(x["fdpp_bsninh"]),
                fdpp_op=str_to_int(x["fdpp_op"]),
                fdpp_dtrp=str_to_int(x["fdpp_dtrp"]),
                fdpp_ocsa=str_to_int(x["fdpp_ocsa"]),
                fdpp_etc=str_to_int(x["fdpp_etc"]),
                bd_intr_ex=x["bd_intr_ex"],
                bd_intr_sf=x["bd_intr_sf"],
                bd_mtd=x["bd_mtd"],
                bdis_mthn=x["bdis_mthn"],
                ex_rt=x["ex_rt"],
                ex_prc=str_to_int(x["ex_prc"]),
                ex_prc_dmth=x["ex_prc_dmth"],
                extg=x["extg"],
                extg_stkcnt=str_to_int(x["extg_stkcnt"]),
                extg_tisstk_vs=x["extg_tisstk_vs"],
                exrqpd_bgd=x["exrqpd_bgd"],
                exrqpd_edd=x["exrqpd_edd"],
                sbd=x["sbd"],
                pymd=x["pymd"],
                rpmcmp=x["rpmcmp"],
                grint=x["grint"],
                bddd=x["bddd"],
                od_a_at_t=str_to_int(x["od_a_at_t"]),
                od_a_at_b=str_to_int(x["od_a_at_b"]),
                adt_a_atn=x["adt_a_atn"],
                rs_sm_atn=x["rs_sm_atn"],
                ex_sm_r=x["ex_sm_r"],
                ovis_ltdtl=x["ovis_ltdtl"],
                ftc_stt_atn=x["ftc_stt_atn"],
            )

        data = response.json()
        return BaseListDto[ExchangeableBondOutputDto](
            status=data["status"],
            message=data["message"],
            list=list(map(_mapping, data["list"])) if "list" in data else None,
        )

    def get_disposal_of_treasury_stocks(
        self, corp_code: str, bgn_de: str, end_de: str
    ) -> BaseListDto[DisposalOfTreasuryStocksOutputDto]:
        """
        자기주식 처분 결정 공시 조회

        Args:
            corp_code (str): 고유번호
            bgn_de (str): 시작일(최초접수일)
            end_de (str): 종료일(최초접수일)

        Returns:
            BaseListDto[DisposalOfTreasuryStocksOutputDto]: 자기주식 처분 결정 조회 결과
        """
        path = "/api/tsstkDpDecsn.json"
        params = BaseParamDto(corp_code=corp_code, bgn_de=bgn_de, end_de=end_de)

        response = self.request.get(path=path, params=params.dict())
        if response.status_code != 200:
            raise HttpError(path)

        def _mapping(x: Dict[str, str]) -> DisposalOfTreasuryStocksOutputDto:
            return DisposalOfTreasuryStocksOutputDto(
                rcept_no=x["rcept_no"],
                corp_cls=x["corp_cls"],
                corp_code=x["corp_code"],
                corp_name=x["corp_name"],
                dppln_stk_ostk=str_to_int(x["dppln_stk_ostk"]),
                dppln_stk_estk=str_to_int(x["dppln_stk_estk"]),
                dpstk_prc_ostk=str_to_int(x["dpstk_prc_ostk"]),
                dpstk_prc_estk=str_to_int(x["dpstk_prc_estk"]),
                dppln_prc_ostk=str_to_int(x["dppln_prc_ostk"]),
                dppln_prc_estk=str_to_int(x["dppln_prc_estk"]),
                dpprpd_bgd=x["dpprpd_bgd"],
                dpprpd_edd=x["dpprpd_edd"],
                dp_pp=x["dp_pp"],
                dp_m_mkt=x["dp_m_mkt"],
                dp_m_ovtm=x["dp_m_ovtm"],
                dp_m_otc=x["dp_m_otc"],
                dp_m_etc=x["dp_m_etc"],
                cs_iv_bk=x["cs_iv_bk"],
                aq_wtn_div_ostk=str_to_int(x["aq_wtn_div_ostk"]),
                aq_wtn_div_ostk_rt=x["aq_wtn_div_ostk_rt"],
                aq_wtn_div_estk=str_to_int(x["aq_wtn_div_estk"]),
                aq_wtn_div_estk_rt=x["aq_wtn_div_estk_rt"],
                eaq_ostk=str_to_int(x["eaq_ostk"]),
                eaq_ostk_rt=x["eaq_ostk_rt"],
                eaq_estk=str_to_int(x["eaq_estk"]),
                eaq_estk_rt=x["eaq_estk_rt"],
                dp_dd=x["dp_dd"],
                od_a_at_t=str_to_int(x["od_a_at_t"]),
                od_a_at_b=str_to_int(x["od_a_at_b"]),
                adt_a_atn=x["adt_a_atn"],
                d1_slodlm_ostk=str_to_int(x["d1_slodlm_ostk"]),
                d1_slodlm_estk=str_to_int(x["d1_slodlm_estk"]),
            )

        data = response.json()
        return BaseListDto[DisposalOfTreasuryStocksOutputDto](
            status=data["status"],
            message=data["message"],
            list=list(map(_mapping, data["list"])) if "list" in data else None,
        )

    def get_acquisition_of_treasury_stocks(
        self, corp_code: str, bgn_de: str, end_de: str
    ) -> BaseListDto[AcquisitionOfTreasuryStocksOutputDto]:
        """
        자기주식 취득 결정 공시 조회

        Args:
            corp_code (str): 고유번호
            bgn_de (str): 시작일(최초접수일)
            end_de (str): 종료일(최초접수일)

        Returns:
            BaseListDto[AcquisitionOfTreasuryStocksOutputDto]: 자기주식 취득 결정 조회 결과
        """
        path = "/api/tsstkAqDecsn.json"
        params = BaseParamDto(corp_code=corp_code, bgn_de=bgn_de, end_de=end_de)

        response = self.request.get(path=path, params=params.dict())
        if response.status_code != 200:
            raise HttpError(path)

        def _mapping(x: Dict[str, str]) -> AcquisitionOfTreasuryStocksOutputDto:
            return AcquisitionOfTreasuryStocksOutputDto(
                rcept_no=x["rcept_no"],
                corp_cls=x["corp_cls"],
                corp_code=x["corp_code"],
                corp_name=x["corp_name"],
                aqpln_stk_ostk=str_to_int(x["aqpln_stk_ostk"]),
                aqpln_stk_estk=str_to_int(x["aqpln_stk_estk"]),
                aqpln_prc_ostk=str_to_int(x["aqpln_prc_ostk"]),
                aqpln_prc_estk=str_to_int(x["aqpln_prc_estk"]),
                aqexpd_bgd=x["aqexpd_bgd"],
                aqexpd_edd=x["aqexpd_edd"],
                hdexpd_bgd=x["hdexpd_bgd"],
                hdexpd_edd=x["hdexpd_edd"],
                aq_pp=x["aq_pp"],
                aq_mth=x["aq_mth"],
                cs_iv_bk=x["cs_iv_bk"],
                aq_wtn_div_ostk=str_to_int(x["aq_wtn_div_ostk"]),
                aq_wtn_div_ostk_rt=x["aq_wtn_div_ostk_rt"],
                aq_wtn_div_estk=str_to_int(x["aq_wtn_div_estk"]),
                aq_wtn_div_estk_rt=x["aq_wtn_div_estk_rt"],
                eaq_ostk=str_to_int(x["eaq_ostk"]),
                eaq_ostk_rt=x["eaq_ostk_rt"],
                eaq_estk=str_to_int(x["eaq_estk"]),
                eaq_estk_rt=x["eaq_estk_rt"],
                aq_dd=x["aq_dd"],
                od_a_at_t=str_to_int(x["od_a_at_t"]),
                od_a_at_b=str_to_int(x["od_a_at_b"]),
                adt_a_atn=x["adt_a_atn"],
                d1_prodlm_ostk=str_to_int(x["d1_prodlm_ostk"]),
                d1_prodlm_estk=str_to_int(x["d1_prodlm_estk"]),
            )

        data = response.json()
        return BaseListDto[AcquisitionOfTreasuryStocksOutputDto](
            status=data["status"],
            message=data["message"],
            list=list(map(_mapping, data["list"])) if "list" in data else None,
        )
