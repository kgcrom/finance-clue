"""Disclosure Module에서 사용되는 dto(in/out) 정의한 Module"""
from dataclasses import asdict
from dataclasses import dataclass
from typing import Optional

# TODO page가 있는 api는 iterator 구현


@dataclass
class ListInputDto:
    """
    disclosure list request DTO

    param crtfc_key: API 인증키
    param corp_code: 고유번호 (8자리)
    param bgn_de: 시작일 (YYYYMMDD)
    param end_de: 종료일 (YYYYMMDD)
    param last_reprt_at: 최종보고서 검색여부 (Y or N)
    param pblntf_ty: 공시 유형 (A: 정기공시, B: 주요사항보고, C: 발행공시, D: 지분공시, E: 기타공시, F: 외부감사관련, G: 펀드공시, H: 자산유동화, I: 거래소공시, J: 공정위공시)
    param pblntf_detail_ty: 공시상세유형
    param corp_cls: 법인구분 (Y: 유가, K: 코스닥, N: 코넥스, E: 기타)
    param sort: 정렬(date: 접수일자, crp: 회사명, rpt: 보고서명 ※ 기본값 date)
    param sort_mth: 정렬방법 (asc: 오름차순, desc: 내림차순)
    param page_no: 페이지 번호 (1~n, ※ 기본값 1)
    param page_count 페이지 건수 (1~100, ※ 기본값: 10, 최대값: 100)
    """

    corp_code: Optional[str] = None
    bgn_de: Optional[str] = None
    end_de: Optional[str] = None
    last_reprt_at: Optional[str] = None
    pblntf_ty: Optional[str] = None
    pblntf_detail_ty: Optional[str] = None
    corp_cls: Optional[str] = "Y"
    sort: Optional[str] = None
    sort_mth: Optional[str] = None
    page_no: Optional[int] = 1
    page_count: Optional[int] = 10

    def dict(self):
        return {k: str(v) for k, v in asdict(self).items() if v is not None}


@dataclass
class ListOutputDto:
    """
    disclosure list response DTO

    param corp_cls:	법인구분 Y(유가), K(코스닥), N(코넥스), E(기타)
    param corp_name:	종목명(법인명)	공시대상회사의 종목명(상장사) 또는 법인명(기타법인)
    param corp_code: 고유번호(8자리)
    param stock_code: 종목코드(6자리)
    param report_nm: 보고서명 (공시구분+보고서명+기타정보)
    param rcept_no: 접수번호(14자리)
    param flr_nm: 공시 제출인명
    param rcept_dt:	공시 접수일자 (YYYYMMDD)
    param rm: 비고
    """

    corp_cls: str
    corp_name: str
    corp_code: str
    stock_code: str
    report_nm: str
    rcept_no: str
    flr_nm: str
    rcept_dt: str
    rm: str
