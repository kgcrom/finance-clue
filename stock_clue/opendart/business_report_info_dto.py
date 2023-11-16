"""사업보고서 주요정보 OpenDart 연동 dto Module"""
from dataclasses import asdict
from dataclasses import dataclass
from typing import Optional


@dataclass
class DirectorTotalRemunerationApprovalOutputDto:
    """
    이사·감사 전체의 보수현황(주주총회 승인금액) 조회 response dto

    param rcept_no (str): 접수번호
    param corp_cls (str): 법인구분 (Y: 유가, K: 코스닥, N: 코넥스, E: 기타)
    param corp_code (str): 고유번호
    param corp_name (str): 회사명
    param se (str): 구분
    param nmpr (str): 인원수
    param gmtsck_confm_amount (str): 주주총회 승인금액
    param rm (str): 비고
    """

    rcept_no: str
    corp_cls: str
    corp_code: str
    corp_name: str
    se: str
    nmpr: int
    gmtsck_confm_amount: int
    rm: str


@dataclass
class DirectorRemunerationAmountOutputDto:
    """
    이사·감사 전체의 보수현황(보수지급금액 - 유형별)) 조회 response dto

    param rcept_no (str): 접수번호
    param corp_cls (str): 법인구분 (Y: 유가, K: 코스닥, N: 코넥스, E: 기타)
    param corp_code (str): 고유번호
    param corp_name (str): 회사명
    param se (str): 구분
    param nmpr (int): 인원수
    param pymnt_totamt (int): 보수총액
    param psn1_avrg_pymntamt (int): 1인당 평균보수액
    param rm (str): 비고
    """

    rcept_no: str
    corp_cls: str
    corp_code: str
    corp_name: str
    se: str
    nmpr: int
    pymnt_totamt: int
    psn1_avrg_pymntamt: int
    rm: str


@dataclass
class DividendOutputDto:
    """
    배당에 관한 사항 조회 response dto

    param rcept_no (str): 접수번호
    param corp_cls (str): 법인구분 (Y: 유가, K: 코스닥, N: 코넥스, E: 기타)
    param corp_code (str): 고유번호
    param corp_name (str): 회사명
    param se (str): 구분
    param stock_knd (str): 주식 종류
    param thstrm (float): 당기
    param frmtrm (float): 전기
    param lwfr (float): 전전기
    """

    rcept_no: str
    corp_cls: str
    corp_code: str
    corp_name: str
    se: str
    stock_knd: Optional[str]
    thstrm: float
    frmtrm: float
    lwfr: float


@dataclass
class TotalStockQuantityOutputDto:
    """
    주식의 총수 현황 조회 response dto

    param rcept_no (str): 접수번호
    param corp_cls (str): 법인구분 (Y: 유가, K: 코스닥, N: 코넥스, E: 기타)
    param corp_code (str): 고유번호
    param corp_name (str): 회사명
    param se (str): 구분
    param isu_stock_totqy (int): 발행한 주식의 총수
    param now_to_isu_stock_totqy (int): 현재까지 발행한 주식의 총수
    param now_to_dcrs_stock_totqy (int): 현재까지 감소한 주식의 총수
    param redc (int): 감자
    param profit_incnr (int): 이익소각
    param rdmstk_repy (int): 상환주식의 상환
    param etc (int): 기타
    param istc_totqy (int): 발행주식의 총수
    param tesstk_co (int): 자기주식수
    param distb_stock_co (int): 유통주식수
    """

    rcept_no: str
    corp_cls: str
    corp_code: str
    corp_name: str
    se: str
    isu_stock_totqy: int
    now_to_isu_stock_totqy: int
    now_to_dcrs_stock_totqy: int
    redc: int
    profit_incnr: int
    rdmstk_repy: int
    etc: int
    istc_totqy: int
    tesstk_co: int
    distb_stock_co: int


@dataclass
class AuditOpinionInputDto:
    """
    회계감사인의 명칭 및 감사의견 조회 params dto

    param corp_code (str): 고유번호
    param bsns_year (str): 사업연도
    param reprt_code (str): 보고서 코드 (1분기보고서: 11013, 반기보고서 : 11012, 3분기보고서 : 11014, 사업보고서 : 11011)
    """

    corp_code: str
    bsns_year: str
    reprt_code: str

    def dict(self):
        return {k: str(v) for k, v in asdict(self).items()}


@dataclass
class AuditOpinionOutputDto:
    """
    회계감사인의 명칭 및 감사의견 조회 response dto

    param rcept_no (str):	접수번호
    param corp_cls (str): 법인구분 (Y: 유가, K: 코스닥, N: 코넥스, E: 기타)
    param corp_code (str): 고유번호
    param corp_name (str): 회사명
    param bsns_year (str): 사업연도
    param adtor (str): 감사인
    param adt_opinion  (Optional[str]): 감사의견
    param adt_reprt_spcmnt_matter  (str|None): 감사보고서 특기사항 (2019년 12월 8일까지 사용됨)
    param emphs_matter (Optional[str]):	강조사항 등 (2019년 12월 9일부터 추가됨)
    param core_adt_matter (Optional[str]): 핵심감사사항 (2019년 12월 9일부터 추가됨)
    """

    rcept_no: str
    corp_cls: str
    corp_code: str
    corp_name: str
    bsns_year: str
    adtor: str
    adt_opinion: Optional[str]
    adt_reprt_spcmnt_matter: Optional[str]
    emphs_matter: Optional[str]
    core_adt_matter: Optional[str]


@dataclass
class NonExecutiveDirectorOutputDto:
    """
    사외이사 및 그 변동현황 조회 response dto

    param rcept_no (str): 접수번호
    param corp_cls (str): 법인구분 (Y: 유가, K: 코스닥, N: 코넥스, E: 기타)
    param corp_code (str): 고유번호
    param corp_name (str): 회사명
    param drctr_co (int): 이사의 수
    param otcmp_drctr_co (int): 사외이사의 수
    param apnt (int): 사외이사 변동현황(선임)
    param rlsofc (int): 사외이사 변동현황(해임)
    param mdstrm_resig (int): 사외이사 변동현황(중도퇴임)
    """

    rcept_no: str
    corp_cls: str
    corp_code: str
    corp_name: str
    drctr_co: int
    otcmp_drctr_co: int
    apnt: int
    rlsofc: int
    mdstrm_resig: int


@dataclass
class AcquisitionAndDisposalOfTreasuryStocksOutputDto:
    """
    자기주식 취득 및 처분 현황 조회 response dto

    param rcept_no (str): 접수번호
    param corp_cls (str): 법인구분 (Y: 유가, K: 코스닥, N: 코넥스, E: 기타)
    param corp_code (str): 고유번호
    param corp_name (str): 회사명
    param acqs_mth1 (str): 취득방법 대분류
    param acqs_mth2 (str): 취득방법 중분류
    param acqs_mth3 (str): 취득방법 소분류
    param stock_knd (str): 주식 종류
    param bsis_qy (int): 기초 수량
    param change_qy_acqs (int): 변동 수량 취득
    param change_qy_dsps (int): 변동 수량 처분
    param change_qy_incnr (int): 변동 수량 소각
    param trmend_qy (int): 기말 수량
    param rm (str): 비고
    """

    rcept_no: str
    corp_cls: str
    corp_code: str
    corp_name: str
    acqs_mth1: str
    acqs_mth2: str
    acqs_mth3: str
    stock_knd: str
    bsis_qy: int
    change_qy_acqs: int
    change_qy_dsps: int
    change_qy_incnr: int
    trmend_qy: int
    rm: str


@dataclass
class CapitalIncreaseAndReductionOutputDto:
    """
    증자(감자) 현황 조회 response dto

    param rcept_no (str): 접수번호
    param corp_cls (str): 법인구분 (Y: 유가, K: 코스닥, N: 코넥스, E: 기타)
    param corp_code (str): 고유번호
    param corp_name (str): 회사명
    param isu_dcrs_de (str): 주식발행 감소일자
    param isu_dcrs_stle (str): 발행 감소형태
    param isu_dcrs_stock_knd (str): 발행 감소 주식 종류
    param isu_dcrs_qy (int): 발행 감소 수량
    param dcrs_mstvdv_fval_amount (int): 발행 감소 주당 액면가액
    param isu_dcrs_mstvdv_amount (int): 발행 감소 주당 가액
    """

    rcept_no: str
    corp_cls: str
    corp_code: str
    corp_name: str
    isu_dcrs_de: str
    isu_dcrs_stle: str
    isu_dcrs_stock_knd: str
    isu_dcrs_qy: int
    isu_dcrs_mstvdv_fval_amount: int
    isu_dcrs_mstvdv_amount: int


@dataclass
class LargestShareHoldersOutputDto:
    """
    최대주주 현황 조회 response dto

    param rcept_no (str): 접수번호
    param corp_cls (str): 법인구분
    param corp_code (str): 고유번호
    param corp_name (str): 법인명
    param nm (str): 성명
    param relate (str): 관계
    param stock_knd (str): 주식 종류
    param bsis_posesn_stock_co (int): 기초 소유 주식 수
    param bsis_posesn_stock_qota_rt (int): 기초 소유 주식 지분율
    param trmend_posesn_stock_co (int): 기말 소유 주식 수
    param trmend_posesn_stock_qota_rt (int): 기말 소유 주식 지분 율
    param rm (str): 비고
    """

    rcept_no: str
    corp_cls: str
    corp_code: str
    corp_name: str
    nm: str
    relate: Optional[str]
    stock_knd: str
    bsis_posesn_stock_co: int
    bsis_posesn_stock_qota_rt: float
    trmend_posesn_stock_co: int
    trmend_posesn_stock_qota_rt: float
    rm: str


@dataclass
class ChangedLargestShareHoldersOutputDto:
    """
    최대주주 변동현황 조회 response dto

    param rcept_no (str): 접수번호
    param corp_cls (str): 법인구분
    param corp_code (str): 고유번호
    param corp_name (str): 법인명
    param change_on (str): 변동
    param mxmm_shrholdr_nm (str): 최대 주주명
    param posesn_stock_co (int): 소유 주식 수
    param qota_rt (float): 지분 율
    param change_cause (str): 변동 원인
    param rm (str): 비고
    """

    rcept_no: str
    corp_cls: str
    corp_code: str
    corp_name: str
    change_on: str
    mxmm_shrholdr_nm: str
    posesn_stock_co: int
    qota_rt: float
    change_cause: str
    rm: str


@dataclass
class ExecutiveInfoOutputDto:
    """
    임원 현황 조회 response dto

    param rcept_no (str): 접수번호
    param corp_cls (str): 법인구분 (Y: 유가, K: 코스닥, N: 코넥스, E: 기타)
    param corp_code (str): 고유번호
    param corp_name (str): 법인명
    param nm (str): 성명
    param sexdstn (str): 성별
    param birth_ym (str): 출생 년월 (YYYY년 MM월)
    param ofcps (str): 직위
    param rgit_exctv_at (Optional[str]): 등기 임원 여부 (등기임원, 미등기임원 등)
    param fte_at (str): 상근 여부 (상근, 비상근 등)
    param chrg_job (str): 담당 업무
    param main_career (str): 주요 경력
    param maxmm_shrholdr_relate (Optional[str]): 최대 주주 관계
    param hffc_pd (str): 재직 기간
    param tenure_end_on (str): 임기 만료일
    """

    rcept_no: str
    corp_cls: str
    corp_code: str
    corp_name: str
    nm: str
    sexdstn: str
    birth_ym: str
    ofcps: str
    rgit_exctv_at: Optional[str]
    fte_at: str
    chrg_job: str
    main_career: str
    maxmm_shrholdr_relate: Optional[str]
    hffc_pd: str
    tenure_end_on: str


@dataclass
class EmployeeInfoOutputDto:
    """
    직원 현황 조회 response dto

    param rcept_no (str): 접수번호
    param corp_cls (str): 법인구분 (Y: 유가, K: 코스닥, N: 코넥스, E: 기타)
    param corp_code (str): 고유번호
    param corp_name (str): 법인명
    param fo_bbm (str): 사업부문
    param sexdstn (str): 성별
    param reform_bfe_emp_co_rgllbr (int): 개정 전 정규직 수
    param reform_bfe_emp_co_cnttk (int): 개정 전 계약직 수
    param reform_bfe_emp_co_etc (int): 개정 전 기타직 수
    param rgllbr_co (int): 정규직 수
    param rgllbr_abacpt_labrr_co (int): 정규직 단시간 근로자 수
    param cnttk_co (int): 계약직 수
    param cnttk_abacpt_labrr_co (int): 계약직 단시간 근로자 수
    param sm (int): 합계
    param avrg_cnwk_sdytrn (int): 평균 근속 연수
    param fyer_salary_totamt (int): 연간 급여 총액
    param jan_salary_am (int): 1월 급여액
    param rm (str): 비고
    """

    rcept_no: str
    corp_cls: str
    corp_code: str
    corp_name: str
    fo_bbm: str
    sexdstn: str
    reform_bfe_emp_co_rgllbr: int
    reform_bfe_emp_co_cnttk: int
    reform_bfe_emp_co_etc: int
    rgllbr_co: int
    rgllbr_abacpt_labrr_co: int
    cnttk_co: int
    cnttk_abacpt_labrr_co: int
    sm: int
    avrg_cnwk_sdytrn: str
    fyer_salary_totamt: int
    jan_salary_am: int
    rm: str


@dataclass
class IndividualDirectorRemunerationOutputDto:
    """
    이사·감사의 개인별 보수 현황 조회 response dto

    param rcept_no (str): 접수번호
    param corp_cls (str): 법인구분 (Y: 유가, K: 코스닥, N: 코넥스, E: 기타)
    param corp_code (str): 고유번호
    param corp_name (str): 법인명
    param nm (str): 이름
    param ofcps (str): 직위
    param mendng_totamt (int): 보수총액
    param mendng_totamt_ct_incls_mendng (int): 보수총액 중 비 포함 보수
    """

    rcept_no: str
    corp_cls: str
    corp_code: str
    corp_name: str
    nm: str
    ofcps: str
    mendng_totamt: int
    mendng_totamt_ct_incls_mendng: int


@dataclass
class TotalDirectorRemunerationOutputDto:
    """
    이사·감사의 전체의 보수 현황 조회 response dto

    param rcept_no (str): 접수번호
    param corp_cls (str): 법인구분 (Y: 유가, K: 코스닥, N: 코넥스, E: 기타)
    param corp_code (str): 고유번호
    param corp_name (str): 법인명
    param nmpr (int): 인원수
    param mendng_totamt (int): 보수총액
    param jan_avrg_mendng_am (int): 1인당 평균 보수액
    param rm (str): 비고
    """

    rcept_no: str
    corp_cls: str
    corp_code: str
    corp_name: str
    nmpr: int
    mendng_totamt: int
    jan_avrg_mendng_am: int
    rm: str


@dataclass
class IndividualRemunerationOver5OutputDto:
    """
    개인별 보수지급 금액(5억이상 상위5인) 조회 response dto

    param rcept_no (str): 접수번호
    param corp_cls (str): 법인구분 (Y: 유가, K: 코스닥, N: 코넥스, E: 기타)
    param corp_code (str): 고유번호
    param corp_name (str): 법인명
    param nm (str): 이름
    param ofcps (str): 직위
    param mendng_totamt (int): 보수총액
    param mendng_totamt_ct_incls_mendng (int): 보수총액 중 비 포함 보수
    """

    rcept_no: str
    corp_cls: str
    corp_code: str
    corp_name: str
    nm: str
    ofcps: str
    mendng_totamt: int
    mendng_totamt_ct_incls_mendng: int


@dataclass
class LargeScaleHolding:
    """Class representing large scale holding information for a corporation.

    Attributes:
        rcept_no (str): 접수번호
        rcept_dt (str): 접수일자
        corp_code (str): 고유번호
        corp_name (str): 회사명
        report_tp (str): 보고구분
        repror (str): 보고자
        stkqy (int): 보유주식등의 수
        stkqy_irds (int): 보유주식등의 증감
        stkrt (float): 보유비율
        stkrt_irds (float): 보유비율 증감
        ctr_stkqy (int): 주요체결 주식등의 수
        ctr_stkrt (float): 주요체결 보유비율
        report_resn (str): 보고사유
    """

    rcept_no: str
    rcept_dt: str
    corp_code: str
    corp_name: str
    report_tp: str
    repror: str
    stkqy: int
    stkqy_irds: int
    stkrt: float
    stkrt_irds: float
    ctr_stkqy: int
    ctr_stkrt: float
    report_resn: str


@dataclass
class ExecutivesAndMajorShareholders:
    """
    Data class representing executives and major shareholders information.

    Attributes:
        rcept_no (str): 접수번호
        rcept_dt (str): 접수일자
        corp_code (str): 고유번호
        corp_name (str): 회사명
        repror (str): 보고자
        isu_exctv_rgist_at (str): 발행 회사 관계 임원(등기여부)
        isu_exctv_ofcps (str): 발행 회사 관계 임원 직위
        isu_main_shrholdr (str): 발행회사 관계 주요 주주
        sp_stock_lmp_cnt (int): 특정 증권 등 소유 주식 수
        sp_stock_lmp_irds_cnt (int): 특정 증권 등 소유 주식 증감 수
        sp_stock_lmp_rate (float): 특정 증권 등 주식 소유 비욜
        sp_stock_lmp_irds_rate (float): 특정 증권 등 소유 증감 비율
    """

    rcept_no: str
    rcept_dt: str
    corp_code: str
    corp_name: str
    repror: str
    isu_exctv_rgist_at: str
    isu_exctv_ofcps: str
    isu_main_shrholdr: str
    sp_stock_lmp_cnt: int
    sp_stock_lmp_irds_cnt: int
    sp_stock_lmp_rate: float
    sp_stock_lmp_irds_rate: float
