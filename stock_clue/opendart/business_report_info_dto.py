"""사업보고서 주요정보 OpenDart 연동 dto Module"""
from dataclasses import asdict
from dataclasses import dataclass
from typing import Optional


@dataclass
class DirectorTotalRemunerationApprovalOutputDto:
    """
    이사·감사 전체의 보수현황(주주총회 승인금액) 조회 response dto

    param rcept_no: 접수번호
    param corp_cls: 법인구분 (Y: 유가, K: 코스닥, N: 코넥스, E: 기타)
    param corp_code: 고유번호
    param corp_name: 회사명
    param se: 구분
    param nmpr: 인원수
    param gmtsck_confm_amount: 주주총회 승인금액
    param rm: 비고
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

    param rcept_no: 접수번호
    param corp_cls: 법인구분 (Y: 유가, K: 코스닥, N: 코넥스, E: 기타)
    param corp_code: 고유번호
    param corp_name: 회사명
    param se: 구분
    param nmpr: 인원수
    param pymnt_totamt: 보수총액
    param psn1_avrg_pymntamt: 1인당 평균보수액
    param rm: 비고
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

    param rcept_no: 접수번호
    param corp_cls: 법인구분 (Y: 유가, K: 코스닥, N: 코넥스, E: 기타)
    param corp_code: 고유번호
    param corp_name: 회사명
    param se: 구분
    param stock_knd: 주식 종류
    param thstrm: 당기
    param frmtrm: 전기
    param lwfr: 전전기
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

    param rcept_no: 접수번호
    param corp_cls: 법인구분 (Y: 유가, K: 코스닥, N: 코넥스, E: 기타)
    param corp_code: 고유번호
    param corp_name: 회사명
    param se: 구분
    param isu_stock_totqy: 발행한 주식의 총수
    param now_to_isu_stock_totqy: 현재까지 발행한 주식의 총수
    param now_to_dcrs_stock_totqy: 현재까지 감소한 주식의 총수
    param redc: 감자
    param profit_incnr: 이익소각
    param rdmstk_repy: 상환주식의 상환
    param etc: 기타
    param istc_totqy: 발행주식의 총수
    param tesstk_co: 자기주식수
    param distb_stock_co: 유통주식수
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

    param corp_code: 고유번호
    param bsns_year: 사업연도
    param reprt_code: 보고서 코드 (1분기보고서: 11013, 반기보고서 : 11012, 3분기보고서 : 11014, 사업보고서 : 11011)
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

    param rcept_no:	접수번호
    param corp_cls: 법인구분 (Y: 유가, K: 코스닥, N: 코넥스, E: 기타)
    param corp_code: 고유번호
    param corp_name: 회사명
    param bsns_year: 사업연도
    param adtor: 감사인
    param adt_opinion: 감사의견
    param adt_reprt_spcmnt_matter: 감사보고서 특기사항 (2019년 12월 8일까지 사용됨)
    param emphs_matter:	강조사항 등 (2019년 12월 9일부터 추가됨)
    param core_adt_matter: 핵심감사사항 (2019년 12월 9일부터 추가됨)
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

    param rcept_no: 접수번호
    param corp_cls: 법인구분 (Y: 유가, K: 코스닥, N: 코넥스, E: 기타)
    param corp_code: 고유번호
    param corp_name: 회사명
    param drctr_co: 이사의 수
    param otcmp_drctr_co: 사외이사의 수
    param apnt: 사외이사 변동현황(선임)
    param rlsofc: 사외이사 변동현황(해임)
    param mdstrm_resig: 사외이사 변동현황(중도퇴임)
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

    param rcept_no: 접수번호
    param corp_cls: 법인구분 (Y: 유가, K: 코스닥, N: 코넥스, E: 기타)
    param corp_code: 고유번호
    param corp_name: 회사명
    param acqs_mth1: 취득방법 대분류
    param acqs_mth2: 취득방법 중분류
    param acqs_mth3: 취득방법 소분류
    param stock_knd: 주식 종류
    param bsis_qy: 기초 수량
    param change_qy_acqs: 변동 수량 취득
    param change_qy_dsps: 변동 수량 처분
    param change_qy_incnr: 변동 수량 소각
    param trmend_qy: 기말 수량
    param rm: 비고
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

    param rcept_no: 접수번호
    param corp_cls: 법인구분 (Y: 유가, K: 코스닥, N: 코넥스, E: 기타)
    param corp_code: 고유번호
    param corp_name: 회사명
    param isu_dcrs_de: 주식발행 감소일자
    param isu_dcrs_stle: 발행 감소형태
    param isu_dcrs_stock_knd: 발행 감소 주식 종류
    param isu_dcrs_qy: 발행 감소 수량
    param dcrs_mstvdv_fval_amount: 발행 감소 주당 액면가액
    param isu_dcrs_mstvdv_amount: 발행 감소 주당 가액
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

    param rcept_no: 접수번호
    param corp_cls: 법인구분
    param corp_code: 고유번호
    param corp_name: 법인명
    param nm: 성명
    param relate: 관계
    param stock_knd: 주식 종류
    param bsis_posesn_stock_co: 기초 소유 주식 수
    param bsis_posesn_stock_qota_rt: 기초 소유 주식 지분율
    param trmend_posesn_stock_co: 기말 소유 주식 수
    param trmend_posesn_stock_qota_rt: 기말 소유 주식 지분 율
    param rm: 비고
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

    param rcept_no: 접수번호
    param corp_cls: 법인구분
    param corp_code: 고유번호
    param corp_name: 법인명
    param change_on: 변동
    param mxmm_shrholdr_nm: 최대 주주명
    param posesn_stock_co: 소유 주식 수
    param qota_rt: 지분 율
    param change_cause: 변동 원인
    param rm: 비고
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

    param rcept_no: 접수번호
    param corp_cls: 법인구분 (Y: 유가, K: 코스닥, N: 코넥스, E: 기타)
    param corp_code: 고유번호
    param corp_name: 법인명
    param nm: 성명
    param sexdstn: 성별
    param birth_ym: 출생 년월 (YYYY년 MM월)
    param ofcps: 직위
    param rgit_exctv_at: 등기 임원 여부 (등기임원, 미등기임원 등)
    param fte_at: 상근 여부 (상근, 비상근 등)
    param chrg_job: 담당 업무
    param main_career: 주요 경력
    param maxmm_shrholdr_relate: 최대 주주 관계
    param hffc_pd: 재직 기간
    param tenure_end_on: 임기 만료일
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

    param rcept_no: 접수번호
    param corp_cls: 법인구분 (Y: 유가, K: 코스닥, N: 코넥스, E: 기타)
    param corp_code: 고유번호
    param corp_name: 법인명
    param fo_bbm: 사업부문
    param sexdstn: 성별
    param reform_bfe_emp_co_rgllbr: 개정 전 정규직 수
    param reform_bfe_emp_co_cnttk: 개정 전 계약직 수
    param reform_bfe_emp_co_etc: 개정 전 기타직 수
    param rgllbr_co: 정규직 수
    param rgllbr_abacpt_labrr_co: 정규직 단시간 근로자 수
    param cnttk_co: 계약직 수
    param cnttk_abacpt_labrr_co: 계약직 단시간 근로자 수
    param sm: 합계
    param avrg_cnwk_sdytrn: 평균 근속 연수
    param fyer_salary_totamt: 연간 급여 총액
    param jan_salary_am: 1월 급여액
    param rm: 비고
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

    param rcept_no: 접수번호
    param corp_cls: 법인구분 (Y: 유가, K: 코스닥, N: 코넥스, E: 기타)
    param corp_code: 고유번호
    param corp_name: 법인명
    param nm: 이름
    param ofcps: 직위
    param mendng_totamt: 보수총액
    param mendng_totamt_ct_incls_mendng: 보수총액 중 비 포함 보수
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

    param rcept_no: 접수번호
    param corp_cls: 법인구분 (Y: 유가, K: 코스닥, N: 코넥스, E: 기타)
    param corp_code: 고유번호
    param corp_name: 법인명
    param nmpr: 인원수
    param mendng_totamt: 보수총액
    param jan_avrg_mendng_am: 1인당 평균 보수액
    param rm: 비고
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

    param rcept_no: 접수번호
    param corp_cls: 법인구분 (Y: 유가, K: 코스닥, N: 코넥스, E: 기타)
    param corp_code: 고유번호
    param corp_name: 법인명
    param nm: 이름
    param ofcps: 직위
    param mendng_totamt: 보수총액
    param mendng_totamt_ct_incls_mendng: 보수총액 중 비 포함 보수
    """

    rcept_no: str
    corp_cls: str
    corp_code: str
    corp_name: str
    nm: str
    ofcps: str
    mendng_totamt: int
    mendng_totamt_ct_incls_mendng: int
