from dataclasses import dataclass
from typing import Optional


@dataclass
class CapitalIncreaseOutputDto:
    """
    유상증자 결정 공시

    Attributes:
        rcept_no (str): 접수번호
        corp_cls (str): 법인구분
        corp_code (str): 고유번호
        corp_name (str): 회사명
        nstk_ostk_cnt (int): 신주의 종류와 수(보통주식 (주))
        nstk_estk_cnt (int): 신주의 종류와 수(기타주식 (주))
        fv_ps (int): 1주당 액면가액 (원)
        bfic_tisstk_ostk (int): 증자전 발행주식총수 (주)(보통주식 (주))
        bfic_tisstk_estk (int): 증자전 발행주식총수 (주)(기타주식 (주))
        fdpp_fclt (int): 자금조달의 목적(시설자금 (원))
        fdpp_bsninh (Optional[int]): 자금조달의 목적(영업양수자금 (원))
        fdpp_op (int): 자금조달의 목적(운영자금 (원))
        fdpp_dtrp (Optional[int]): 자금조달의 목적(채무상환자금 (원))
        fdpp_ocsa (int): 자금조달의 목적(타법인 증권 취득자금 (원))
        fdpp_etc (int): 자금조달의 목적(기타자금 (원))
        ic_mthn (str): 증자방식
        ssl_at (str): 공매도 해당여부
        ssl_bgd (str): 공매도 시작일
        ssl_edd (str): 공매도 종료일
    """
    
    rcept_no: str
    corp_cls: str
    corp_code: str
    corp_name: str
    nstk_ostk_cnt: int
    nstk_estk_cnt: int
    fv_ps: int
    bfic_tisstk_ostk: int
    bfic_tisstk_estk: int
    fdpp_fclt: int
    fdpp_bsninh: Optional[int]
    fdpp_op: int
    fdpp_dtrp: Optional[int]
    fdpp_ocsa: int
    fdpp_etc: int
    ic_mthn: str
    ssl_at: str
    ssl_bgd: str
    ssl_edd: str


@dataclass
class CaptitalDecreaseOutputDto:
    """
    무사증자 결정 공시

    Attributes:
        rcept_no (str): 접수번호
        corp_cls (str): 법인구분
        corp_code (str): 고유번호
        corp_name (str): 회사명
        nstk_ostk_cnt (int): 신주의 종류와 수(보통주식 (주))
        nstk_estk_cnt (int): 신주의 종류와 수(기타주식 (주))
        fv_ps (int): 1주당 액면가액 (원)
        bfic_tisstk_ostk (int): 증자전 발행주식총수 (주)(보통주식 (주))
        bfic_tisstk_estk (int): 증자전 발행주식총수 (주)(기타주식 (주))
        nstk_asstd (str): 신주배정기준일
        nstk_ascnt_ps_ostk (float): 1주당 신주배정 주식수(보통주식 (주))
        nstk_ascnt_ps_estk (float): 1주당 신주배정 주식수(기타주식 (주))
        nstk_dividrk (str): 신주의 배당기산일
        nstk_dlprd (str): 신주권교부예정일
        nstk_lstprd (str): 신주의 상장 예정일
        bddd (str): 이사회결의일(결정일)
        od_a_at_t (int): 사외이사 참석여부(참석(명))
        od_a_at_b (int): 사외이사 참석여부(불참(명))
        adt_a_atn (str): 감사(감사위원)참석 여부
    """
    
    rcept_no: str
    corp_cls: str
    corp_code: str
    corp_name: str
    nstk_ostk_cnt: int
    nstk_estk_cnt: int
    fv_ps: int
    bfic_tisstk_ostk: int
    bfic_tisstk_estk: int
    nstk_asstd: str
    nstk_ascnt_ps_ostk: float
    nstk_ascnt_ps_estk: float
    nstk_dividrk: str
    nstk_dlprd: str
    nstk_lstprd: str
    bddd: str
    od_a_at_t: int
    od_a_at_b: int
    adt_a_atn: str


@dataclass
class CapitalIncreaseAndDecreaseOutputDto:
    """
    DTO class for Capital Increase and Decrease information from OpenDART API.

    Attributes:
        rcept_no (str): 접수번호
        corp_cls (str): 법인구분
        corp_code (str): 고유번호
        corp_name (str): 법인명
        piic_nstk_ostk_cnt (int): 유상증자(신주의 종류와 수(보통주식 (주)))
        piic_nstk_estk_cnt (int): 유상증자(신주의 종류와 수(기타주식 (주)))
        piic_fv_ps (int): 유상증자(1주당 액면가액 (원))
        piic_bfic_tisstk_ostk (int): 유상증자(증자전 발행주식총수 (주)(보통주식 (주)))
        piic_bfic_tisstk_estk (int): 유상증자(증자전 발행주식총수 (주)(기타주식 (주)))
        piic_fdpp_fclt (int): 유상증자(자금조달의 목적(시설자금 (원)))
        piic_fdpp_bsninh (Optional[int]): 유상증자(자금조달의 목적(영업양수자금 (원)))
        piic_fdpp_op (int): 유상증자(자금조달의 목적(운영자금 (원)))
        piic_fdpp_dtrp (Optional[int]): 유상증자(자금조달의 목적(채무상환자금 (원)))
        piic_fdpp_ocsa (int): 유상증자(자금조달의 목적(타법인 증권 취득자금 (원)))
        piic_fdpp_etc (int): 유상증자(자금조달의 목적(기타자금 (원)))
        piic_ic_mthn (str): 유상증자(증자방식)
        fric_nstk_ostk_cnt (int): 무상증자(신주의 종류와 수(보통주식 (주)))
        fric_nstk_estk_cnt (int): 무상증자(신주의 종류와 수(기타주식 (주)))
        fric_fv_ps (int): 무상증자(1주당 액면가액 (원))
        fric_bfic_tisstk_ostk (int): 무상증자(증자전 발행주식총수(보통주식 (주)))
        fric_bfic_tisstk_estk (int): 무상증자(증자전 발행주식총수(기타주식 (주)))
        fric_nstk_asstd (str): 무상증자(신주배정기준일)
        fric_nstk_ascnt_ps_ostk (float): 무상증자(1주당 신주배정 주식수(보통주식 (주)))
        fric_nstk_ascnt_ps_estk (float): 무상증자(1주당 신주배정 주식수(기타주식 (주)))
        fric_nstk_dividrk (str): 무상증자(신주의 배당기산일)
        fric_nstk_dlprd (str): 무상증자(신주권교부예정일)
        fric_nstk_lstprd (str): 무상증자(신주의 상장 예정일)
        fric_bddd (str): 무상증자(이사회결의일(결정일))
        fric_od_a_at_t (int): 무상증자(사외이사 참석여부(참석(명)))
        fric_od_a_at_b (int): 무상증자(사외이사 참석여부(불참(명)))
        fric_adt_a_atn (str): 무상증자(감사(감사위원)참석 여부)
        ssl_at (str): 공매도 해당여부
        ssl_bgd (str): 공매도 시작일
        ssl_edd (str): 공매도 종료일
    """
    
    rcept_no: str
    corp_cls: str
    corp_code: str
    corp_name: str
    piic_nstk_ostk_cnt: int
    piic_nstk_estk_cnt: int
    piic_fv_ps: int
    piic_bfic_tisstk_ostk: int
    piic_bfic_tisstk_estk: int
    piic_fdpp_fclt: int
    piic_fdpp_bsninh: Optional[int]
    piic_fdpp_op: int
    piic_fdpp_dtrp: Optional[int]
    piic_fdpp_ocsa: int
    piic_fdpp_etc: int
    piic_ic_mthn: str
    fric_nstk_ostk_cnt: int
    fric_nstk_estk_cnt: int
    fric_fv_ps: int
    fric_bfic_tisstk_ostk: int
    fric_bfic_tisstk_estk: int
    fric_nstk_asstd: str
    fric_nstk_ascnt_ps_ostk: float
    fric_nstk_ascnt_ps_estk: float
    fric_nstk_dividrk: str
    fric_nstk_dlprd: str
    fric_nstk_lstprd: str
    fric_bddd: str
    fric_od_a_at_t: int
    fric_od_a_at_b: int
    fric_adt_a_atn: str
    ssl_at: str
    ssl_bgd: str
    ssl_edd: str


@dataclass
class CapitalReductionOutputDto:
    """
    Data class for holding the output of the Capital Reduction API.

    Attributes:
        rcept_no (str): 접수번호
        corp_cls (str): 법인구분
        corp_code (str): 고유번호
        corp_name (str): 회사명
        crstk_ostk_cnt (int): 감자전 주식의 종류와 수(보통주식 (주))
        crstk_estk_cnt (int): 감자전 주식의 종류와 수(기타주식 (주))
        fv_ps (int): 1주당 액면가액 (원)
        bfcr_cpt (int): 감자전후 자본금(감자전 (원))
        atcr_cpt (int): 감자전후 자본금(감자후 (원))
        bfcr_tisstk_ostk (int): 감자전후 발행주식수(보통주식 (주)(감자전 (원)))
        atcr_tisstk_ostk (int): 감자전후 발행주식수(보통주식 (주)(감자후 (원)))
        bfcr_tisstk_estk (int): 감자전후 발행주식수(기타주식 (주)(감자전 (원)))
        atcr_tisstk_estk (int): 감자전후 발행주식수(기타주식 (주)(감자후 (원)))
        cr_rt_ostk (str): 감자비율(보통주식 (%))
        cr_rt_estk (str): 감자비율(기타주식 (%))
        cr_std (str): 감자기준일
        cr_mth (str): 감자방법
        cr_rs (str): 감자사유
        crsc_gmtsck_prd (str): 감자일정(주주총회 예정일)
        crsc_trnmsppd (str): 감자일정(명의개서정지기간)
        crsc_osprpd (Optional[str]): 감자일정(구주권 제출기간)
        crsc_trspprpd (Optional[str]): 감자일정(매매거래 정지예정기간)
        crsc_osprpd_bgd (Optional[str]): 감자일정(구주권 제출기간(시작일))
        crsc_osprpd_edd (Optional[str]): 감자일정(구주권 제출기간(종료일))
        crsc_trspprpd_bgd (Optional[str]): 감자일정(매매거래 정지예정기간(시작일))
        crsc_trspprpd_edd (Optional[str]): 감자일정(매매거래 정지예정기간(종료일))
        crsc_nstkdlprd (str): 감자일정(신주권교부예정일)
        crsc_nstklstprd (str): 감자일정(신주상장예정일)
        cdobprpd_bgd (str): 채권자 이의제출기간(시작일)
        cdobprpd_edd (str): 채권자 이의제출기간(종료일)
        ospr_nstkdl_pl (str): 구주권제출 및 신주권교부장소
        bddd (str): 이사회결의일(결정일)
        od_a_at_t (int): 사외이사 참석여부(참석(명))
        od_a_at_b (int): 사외이사 참석여부(불참(명))
        adt_a_atn (str): 감사(감사위원) 참석여부
        ftc_stt_atn (str): 공정거래위원회 신고대상 여부
    """
    rcept_no: str
    corp_cls: str
    corp_code: str
    corp_name: str
    crstk_ostk_cnt: int
    crstk_estk_cnt: int
    fv_ps: int
    bfcr_cpt: int
    atcr_cpt: int
    bfcr_tisstk_ostk: int
    atcr_tisstk_ostk: int
    bfcr_tisstk_estk: int
    atcr_tisstk_estk: int
    cr_rt_ostk: str
    cr_rt_estk: str
    cr_std: str
    cr_mth: str
    cr_rs: str
    crsc_gmtsck_prd: str
    crsc_trnmsppd: str
    crsc_osprpd: Optional[str]
    crsc_trspprpd: Optional[str]
    crsc_osprpd_bgd: Optional[str]
    crsc_osprpd_edd: Optional[str]
    crsc_trspprpd_bgd: Optional[str]
    crsc_trspprpd_edd: Optional[str]
    crsc_nstkdlprd: str
    crsc_nstklstprd: str
    cdobprpd_bgd: str
    cdobprpd_edd: str
    ospr_nstkdl_pl: str
    bddd: str
    od_a_at_t: int
    od_a_at_b: int
    adt_a_atn: str
    ftc_stt_atn: str


@dataclass
class ConvertibleBondOutputDto:
    pass


@dataclass
class BondWithWarrantsOutputDto:
    pass


@dataclass
class ExchangeableBondOutputDto:
    pass


@dataclass
class DisposalOfTreasuryStocksOutputDto:
    pass


@dataclass
class AcquisitionOfTreasuryStocksOutputDto:
    pass
