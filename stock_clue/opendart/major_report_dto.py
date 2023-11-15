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
    """
    Data Transfer Object for Convertible Bond Output

    Attributes:
        rcept_no (str): 접수번호
        corp_cls (str): 법인구분
        corp_code (str): 고유번호
        corp_name (str): 회사명
        bd_tm (str): 사채의 종류(회차)
        bd_knd (str): 사채의 종류(종류)
        bd_fta (int): 사채의 권면(전자등록)총액 (원)
        atcsc_rmislmt (Optional[int]): 정관상 잔여 발행한도 (원)
        ovis_fta (int): 해외발행(권면(전자등록)총액)
        ovis_fta_crn (str): 해외발행(권면(전자등록)총액(통화단위))
        ovis_ster (str): 해외발행(기준환율등)
        ovis_isar (str): 해외발행(발행지역)
        ovis_mktnm (str): 해외발행(해외상장시 시장의 명칭)
        fdpp_fclt (int): 자금조달의 목적(시설자금 (원))
        fdpp_bsninh (Optional[int]): 자금조달의 목적(영업양수자금 (원))
        fdpp_op (int): 자금조달의 목적(운영자금 (원))
        fdpp_dtrp (Optional[int]): 자금조달의 목적(채무상환자금 (원))
        fdpp_ocsa (int): 자금조달의 목적(타법인 증권 취득자금 (원))
        fdpp_etc (int): 자금조달의 목적(기타자금 (원))
        bd_intr_ex (str): 사채의 이율(표면이자율 (%))
        bd_intr_sf (str): 사채의 이율(만기이자율 (%))
        bd_mtd (str): 사채만기일
        bdis_mthn (str): 사채발행방법
        cv_rt (str): 전환에 관한 사항(전환비율 (%))
        cv_prc (int): 전환에 관한 사항(전환가액 (원/주))
        cvisstk_knd (str): 전환에 관한 사항(전환에 따라 발행할 주식(종류))
        cvisstk_cnt (int): 전환에 관한 사항(전환에 따라 발행할 주식(주식수))
        cvisstk_tisstk_vs (str): 전환에 관한 사항(전환에 따라 발행할 주식(주식총수 대비 비율(%)))
        cvrqpd_bgd (str): 전환에 관한 사항(전환청구기간(시작일))
        cvrqpd_edd (str): 전환에 관한 사항(전환청구기간(종료일))
        act_mktprcfl_cvprc_lwtrsprc (Optional[int]): 전환에 관한 사항(시가하락에 따른 전환가액 조정(최저 조정가액 (원)))
        act_mktprcfl_cvprc_lwtrsprc_bs (Optional[str]): 전환에 관한 사항(시가하락에 따른 전환가액 조정(최저 조정가액 근거))
        rmislmt_lt70p (Optional[int]): 전환에 관한 사항(시가하락에 따른 전환가액 조정(발행당시 전환가액의 70% 미만으로 조정가능한 잔여 발행한도 (원)))
        abmg (str): 합병 관련 사항
        sbd (str): 청약일
        pymd (str): 납입일
        rpmcmp (str): 대표주관회사
        grint (str): 보증기관
        bddd (str): 이사회결의일(결정일)
        od_a_at_t (int): 사외이사 참석여부(참석(명))
        od_a_at_b (int): 사외이사 참석여부(불참(명))
        adt_a_atn (str): 감사(감사위원)참석 여부
        rs_sm_atn (str): 증권신고서 제출대상 여부
        ex_sm_r (str): 제출을 면제받은 경우 그 사유
        ovis_ltdtl (str): 당해 사채의 해외발행과 연계된 대차거래 내역
        ftc_stt_atn (str): 공정거래위원회 신고대상 여부
    """

    rcept_no: str
    corp_cls: str
    corp_code: str
    corp_name: str
    bd_tm: str
    bd_knd: str
    bd_fta: int
    atcsc_rmislmt: Optional[int]
    ovis_fta: int
    ovis_fta_crn: str
    ovis_ster: str
    ovis_isar: str
    ovis_mktnm: str
    fdpp_fclt: int
    fdpp_bsninh: Optional[int]
    fdpp_op: int
    fdpp_dtrp: Optional[int]
    fdpp_ocsa: int
    fdpp_etc: int
    bd_intr_ex: str
    bd_intr_sf: str
    bd_mtd: str
    bdis_mthn: str
    cv_rt: str
    cv_prc: int
    cvisstk_knd: str
    cvisstk_cnt: int
    cvisstk_tisstk_vs: str
    cvrqpd_bgd: str
    cvrqpd_edd: str
    act_mktprcfl_cvprc_lwtrsprc: Optional[int]
    act_mktprcfl_cvprc_lwtrsprc_bs: Optional[str]
    rmislmt_lt70p: Optional[int]
    abmg: str
    sbd: str
    pymd: str
    rpmcmp: str
    grint: str
    bddd: str
    od_a_at_t: int
    od_a_at_b: int
    adt_a_atn: str
    rs_sm_atn: str
    ex_sm_r: str
    ovis_ltdtl: str
    ftc_stt_atn: str


@dataclass
class BondWithWarrantsOutputDto:
    """
    Data Transfer Object for Bond With Warrants Output

    Attributes:
        rcept_no (str): 접수번호
        corp_cls (str): 법인구분
        corp_code (str): 고유번호
        corp_name (str): 회사명
        bd_tm (str): 사채의 종류(회차)
        bd_knd (str): 사채의 종류(종류)
        bd_fta (int): 사채의 권면(전자등록)총액 (원)
        atcsc_rmislmt (Optional[int]): 정관상 잔여 발행한도 (원)
        ovis_fta (int): 해외발행(권면(전자등록)총액)
        ovis_fta_crn (str): 해외발행(권면(전자등록)총액(통화단위))
        ovis_ster (str): 해외발행(기준환율등)
        ovis_isar (str): 해외발행(발행지역)
        ovis_mktnm (str): 해외발행(해외상장시 시장의 명칭)
        fdpp_fclt (int): 자금조달의 목적(시설자금 (원))
        fdpp_bsninh (Optional[int]): 자금조달의 목적(영업양수자금 (원))
        fdpp_op (int): 자금조달의 목적(운영자금 (원))
        fdpp_dtrp (Optional[int]): 자금조달의 목적(채무상환자금 (원))
        fdpp_ocsa (int): 자금조달의 목적(타법인 증권 취득자금 (원))
        fdpp_etc (int): 자금조달의 목적(기타자금 (원))
        bd_intr_ex (str): 사채의 이율(표면이자율 (%))
        bd_intr_sf (str): 사채의 이율(만기이자율 (%))
        bd_mtd (str): 사채만기일
        bdis_mthn (str): 사채발행방법
        ex_rt (str): 신주인수권에 관한 사항(행사비율 (%))
        ex_prc: (int): 신주인수권에 관한 사항(행사가액 (원/주))
        ex_prc_dmth (str): 신주인수권에 관한 사항(행사가액 결정방법)
        bdwt_div_atn (str): 신주인수권에 관한 사항(사채와 인수권의 분리여부)
        nstk_pym_mth (str): 신주인수권에 관한 사항(신주대금 납입방법)
        nstk_isstk_knd (str): 신주인수권에 관한 사항(신주인수권 행사에 따라 발행할 주식(종류))
        nstk_isstk_cnt (int): 신주인수권에 관한 사항(신주인수권 행사에 따라 발행할 주식(주식수))
        expd_bgd (str): 신주인수권에 관한 사항(권리행사기간(시작일))
        expd_edd (str): 신주인수권에 관한 사항(권리행사기간(종료일))
        act_mktprcfl_cvprc_lwtrsprc (Optional[int]): 전환에 관한 사항(시가하락에 따른 전환가액 조정(최저 조정가액 (원)))
        act_mktprcfl_cvprc_lwtrsprc_bs (Optional[str]): 전환에 관한 사항(시가하락에 따른 전환가액 조정(최저 조정가액 근거))
        rmislmt_lt70p (Optional[int]): 전환에 관한 사항(시가하락에 따른 전환가액 조정(발행당시 전환가액의 70% 미만으로 조정가능한 잔여 발행한도 (원)))
        abmg (str): 합병 관련 사항
        sbd (str): 청약일
        pymd (str): 납입일
        rpmcmp (str): 대표주관회사
        grint (str): 보증기관
        bddd (str): 이사회결의일(결정일)
        od_a_at_t (int): 사외이사 참석여부(참석(명))
        od_a_at_b (int): 사외이사 참석여부(불참(명))
        adt_a_atn (str): 감사(감사위원)참석 여부
        rs_sm_atn (str): 증권신고서 제출대상 여부
        ex_sm_r (str): 제출을 면제받은 경우 그 사유
        ovis_ltdtl (str): 당해 사채의 해외발행과 연계된 대차거래 내역
        ftc_stt_atn (str): 공정거래위원회 신고대상 여부
    """

    rcept_no: str
    corp_cls: str
    corp_code: str
    corp_name: str
    bd_tm: str
    bd_knd: str
    bd_fta: int
    atcsc_rmislmt: Optional[int]
    ovis_fta: int
    ovis_fta_crn: str
    ovis_ster: str
    ovis_isar: str
    ovis_mktnm: str
    fdpp_fclt: int
    fdpp_bsninh: Optional[int]
    fdpp_op: int
    fdpp_dtrp: Optional[int]
    fdpp_ocsa: int
    fdpp_etc: int
    bd_intr_ex: str
    bd_intr_sf: str
    bd_mtd: str
    bdis_mthn: str
    ex_rt: str
    ex_prc: int
    ex_prc_dmth: str
    bdwt_div_atn: str
    nstk_pym_mth: str
    nstk_isstk_knd: str
    nstk_isstk_cnt: int
    nstk_isstk_tisstk_vs: str
    expd_bgd: str
    expd_edd: str
    act_mktprcfl_cvprc_lwtrsprc: Optional[int]
    act_mktprcfl_cvprc_lwtrsprc_bs: Optional[str]
    rmislmt_lt70p: Optional[int]
    abmg: str
    sbd: str
    pymd: str
    rpmcmp: str
    grint: str
    bddd: str
    od_a_at_t: int
    od_a_at_b: int
    adt_a_atn: str
    rs_sm_atn: str
    ex_sm_r: str
    ovis_ltdtl: str
    ftc_stt_atn: str


@dataclass
class ExchangeableBondOutputDto:
    """
    DTO class for exchangeable bond output data from Open DART API.

    Attributes:
        rcept_no (str): 접수번호
        corp_cls (str): 법인구분
        corp_code (str): 고유번호
        corp_name (str): 회사명
        bd_tm (str): 사채의 종류(회차)
        bd_knd (str): 사채의 종류(종류)
        bd_fta (str): 사채의 권면(전자등록)총액 (원)
        ovis_fta (str): 해외발행(권면(전자등록)총액)
        ovis_fta_crn (str): 해외발행(권면(전자등록)총액(통화단위))
        ovis_ster (str): 해외발행(기준환율등)
        ovis_isar (str): 해외발행(발행지역)
        ovis_mktnm (str): 해외발행(해외상장시 시장의 명칭)
        fdpp_fclt (int): 자금조달의 목적(시설자금 (원))
        fdpp_bsninh (Optional[int]): 자금조달의 목적(영업양수자금 (원))
        fdpp_op (int): 자금조달의 목적(운영자금 (원))
        fdpp_dtrp (Optional[int]): 자금조달의 목적(채무상환자금 (원))
        fdpp_ocsa (int): 자금조달의 목적(타법인 증권 취득자금 (원))
        fdpp_etc (int): 자금조달의 목적(기타자금 (원))
        bd_intr_ex (str): 사채의 이율(표면이자율 (%))
        bd_intr_sf (str): 사채의 이율(만기이자율 (%))
        bd_mtd (str): 사채만기일
        bdis_mthn (str): 사채발행방법
        ex_rt (str): 교환권에 관한 사항(교환비율 (%))
        ex_prc (int): 교환권에 관한 사항(교환가액 (원/주))
        ex_prc_dmth (str): 교환권에 관한 사항(교환가액 결정방법)
        extg (str): 교환권에 관한 사항(교환대상 (종류))
        extg_stkcnt (int): 교환권에 관한 사항(교환대상 (주식수))
        extg_tisstk_vs (str): 교환권에 관한 사항(교환대상 (주식총수 대비 비율(%)))
        exrqpd_bgd (str): 교환권에 관한 사항(교환청구기간(시작일))
        exrqpd_edd (str): 교환권에 관한 사항(교환청구기간(종료일))
        sbd (str): 청약일
        pymd (str): 납입일
        rpmcmp (str): 대표주관회사
        grint (str): 보증기관
        bddd (str): 이사회결의일(결정일)
        od_a_at_t (int): 사외이사 참석여부(참석(명))
        od_a_at_b (int): 사외이사 참석여부(불참(명))
        adt_a_atn (str): 감사(감사위원)참석 여부
        rs_sm_atn (str): 증권신고서 제출대상 여부
        ex_sm_r (str): 제출을 면제받은 경우 그 사유
        ovis_ltdtl (str): 당해 사채의 해외발행과 연계된 대차거래 내역
        ftc_stt_atn (str): 공정거래위원회 신고대상 여부
    """

    rcept_no: str
    corp_cls: str
    corp_code: str
    corp_name: str
    bd_tm: str
    bd_knd: str
    bd_fta: str
    ovis_fta: str
    ovis_fta_crn: str
    ovis_ster: str
    ovis_isar: str
    ovis_mktnm: str
    fdpp_fclt: int
    fdpp_bsninh: Optional[int]
    fdpp_op: int
    fdpp_dtrp: Optional[int]
    fdpp_ocsa: int
    fdpp_etc: int
    bd_intr_ex: str
    bd_intr_sf: str
    bd_mtd: str
    bdis_mthn: str
    ex_rt: str
    ex_prc: int
    ex_prc_dmth: str
    extg: str
    extg_stkcnt: int
    extg_tisstk_vs: str
    exrqpd_bgd: str
    exrqpd_edd: str
    sbd: str
    pymd: str
    rpmcmp: str
    grint: str
    bddd: str
    od_a_at_t: int
    od_a_at_b: int
    adt_a_atn: str
    rs_sm_atn: str
    ex_sm_r: str
    ovis_ltdtl: str
    ftc_stt_atn: str
    ovis_ltdtl: str
    ftc_stt_atn: str


@dataclass
class DisposalOfTreasuryStocksOutputDto:
    pass


@dataclass
class AcquisitionOfTreasuryStocksOutputDto:
    pass
