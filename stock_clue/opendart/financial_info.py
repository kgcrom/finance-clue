"""
This module contains functions for retrieving financial information from Open DART API.
"""
from typing import Dict

from stock_clue.error import HttpError
from stock_clue.opendart.base_dto import BaseListDto
from stock_clue.opendart.base_dto import BaseParamDto
from stock_clue.opendart.financial_info_dto import (
    WholeAccountSingleCompanyOutputDto,
)
from stock_clue.opendart.financial_info_dto import MajorAccountCompanyOutputDto
from stock_clue.opendart.financial_info_dto import XbrlTaxanomyOutputDto
from stock_clue.opendart.open_dart import OpenDart
from stock_clue.opendart.utils import extract_file_name
from stock_clue.opendart.utils import str_to_int


class FinancialInfo:
    def __init__(self, open_dart: OpenDart):
        super().__init__()
        self.open_dart = open_dart

    def get_major_account_single_company(
        self, corp_code: str, bsns_year: str, reprt_code: str
    ) -> BaseListDto[MajorAccountCompanyOutputDto]:
        path = "/api/fnlttSinglAcnt.json"
        params = BaseParamDto(
            corp_code=corp_code, bsns_year=bsns_year, reprt_code=reprt_code
        )
        response = self.open_dart.get(path, params.dict())

        if response.status_code != 200:
            raise HttpError(path)

        data = response.json()

        def _mapping(x) -> MajorAccountCompanyOutputDto:
            return MajorAccountCompanyOutputDto(
                rcept_no=x["rcept_no"],
                bsns_year=x["bsns_year"],
                stock_code=x["stock_code"],
                reprt_code=x["reprt_code"],
                account_nm=x["account_nm"],
                fs_div=x["fs_div"],
                fs_nm=x["fs_nm"],
                sj_div=x["sj_div"],
                sj_nm=x["sj_nm"],
                thstrm_nm=x["thstrm_nm"],
                thstrm_dt=x["thstrm_dt"],
                thstrm_amount=str_to_int(x["thstrm_amount"]),
                thstrm_add_amount=str_to_int(x["thstrm_add_amount"])
                if "thstrm_add_amount" in x
                else None,
                frmtrm_nm=x["frmtrm_nm"],
                frmtrm_dt=x["frmtrm_dt"],
                frmtrm_amount=str_to_int(x["frmtrm_amount"]),
                frmtrm_add_amount=str_to_int(x["frmtrm_add_amount"])
                if "frmtrm_add_amount" in x
                else None,
                bfefrmtrm_nm=x["bfefrmtrm_nm"],
                bfe_frmtrm_dt=x["bfe_frmtrm_dt"]
                if "bfe_frmtrm_dt" in x
                else None,
                bfefrmtrm_amount=str_to_int(x["bfefrmtrm_amount"]),
                ord=str_to_int(x["ord"]),
                currency=x["currency"],
            )

        return BaseListDto(
            status=data["status"],
            message=data["message"],
            list=list(map(_mapping, data["list"])),
        )

    def get_major_account_multiple_company(
        self, corp_code: str, bsns_year: str, reprt_code: str
    ) -> BaseListDto[MajorAccountCompanyOutputDto]:
        path = "/api/fnlttMultiAcnt.json"
        params = BaseParamDto(
            corp_code=corp_code, bsns_year=bsns_year, reprt_code=reprt_code
        )

        response = self.open_dart.get(path, params.dict())
        if response.status_code != 200:
            raise HttpError(path)

        def _mapping(x) -> MajorAccountCompanyOutputDto:
            return MajorAccountCompanyOutputDto(
                rcept_no=x["rcept_no"],
                bsns_year=x["bsns_year"],
                stock_code=x["stock_code"],
                reprt_code=x["reprt_code"],
                account_nm=x["account_nm"],
                fs_div=x["fs_div"],
                fs_nm=x["fs_nm"],
                sj_div=x["sj_div"],
                sj_nm=x["sj_nm"],
                thstrm_nm=x["thstrm_nm"],
                thstrm_dt=x["thstrm_dt"],
                thstrm_amount=str_to_int(x["thstrm_amount"]),
                thstrm_add_amount=str_to_int(x["thstrm_add_amount"])
                if "thstrm_add_amount" in x
                else 0,
                frmtrm_nm=x["frmtrm_nm"],
                frmtrm_dt=x["frmtrm_dt"],
                frmtrm_amount=str_to_int(x["frmtrm_amount"]),
                frmtrm_add_amount=str_to_int(x["frmtrm_add_amount"])
                if "frmtrm_add_amount" in x
                else 0,
                bfefrmtrm_nm=x["bfefrmtrm_nm"],
                bfe_frmtrm_dt=x["bfe_frmtrm_dt"]
                if "bfe_frmtrm_dt" in x
                else None,
                bfefrmtrm_amount=str_to_int(x["bfefrmtrm_amount"]),
                ord=str_to_int(x["ord"]),
                currency=x["currency"],
            )

        data = response.json()

        return BaseListDto[MajorAccountCompanyOutputDto](
            status=data["status"],
            message=data["message"],
            list=list(map(_mapping, data["list"])),
        )

    def get_whole_account_single_company(
        self, corp_code: str, bsns_year: str, reprt_code: str, fs_div: str
    ) -> BaseListDto[WholeAccountSingleCompanyOutputDto]:
        path = "/api/fnlttSinglAcntAll.json"
        params = BaseParamDto(
            corp_code=corp_code,
            bsns_year=bsns_year,
            reprt_code=reprt_code,
            fs_div=fs_div,
        )

        response = self.open_dart.get(path, params.dict())
        if response.status_code != 200:
            raise HttpError(path)

        def _mapping(x: Dict[str, str]) -> WholeAccountSingleCompanyOutputDto:
            return WholeAccountSingleCompanyOutputDto(
                rcept_no=x["rcept_no"],
                reprt_code=x["reprt_code"],
                bsns_year=x["bsns_year"],
                corp_code=x["corp_code"],
                sj_div=x["sj_div"],
                sj_nm=x["sj_nm"],
                account_id=x["account_id"],
                account_nm=x["account_nm"],
                account_detail=x["account_detail"],
                thstrm_nm=x["thstrm_nm"],
                thstrm_amount=str_to_int(x["thstrm_amount"]),
                thstrm_add_amount=str_to_int(x["thstrm_add_amount"])
                if "thstrm_add_amount" in x
                else None,
                frmtrm_nm=x["frmtrm_nm"],
                frmtrm_amount=str_to_int(x["frmtrm_amount"]),
                frmtrm_q_nm=x["frmtrm_q_nm"] if "frmtrm_q_nm" in x else None,
                frmtrm_q_amount=str_to_int(x["frmtrm_q_amount"])
                if "frmtrm_q_amount" in x
                else None,
                frmtrm_add_amount=str_to_int(x["frmtrm_add_amount"])
                if "frmtrm_add_amount" in x
                else None,
                bfefrmtrm_nm=x["bfefrmtrm_nm"],
                bfefrmtrm_amount=str_to_int(x["bfefrmtrm_amount"]),
                ord=str_to_int(x["ord"]),
                currency=x["currency"],
            )

        data = response.json()
        return BaseListDto[WholeAccountSingleCompanyOutputDto](
            status=data["status"],
            message=data["message"],
            list=list(map(_mapping, data["list"])),
        )

    def download_xbrl(self, rcept_no: str, reprt_code: str, file_path: str):
        """
        Downloads the XBRL file for the given report number and report code.

        Args:
            rcept_no (str): The report number.
            reprt_code (str): The report code.

        Returns:
            None
        """
        path = "/api/fnlttXbrl.xml"

        params = BaseParamDto(rcept_no=rcept_no, reprt_code=reprt_code)
        response = self.open_dart.get(path, params.dict(), True)

        if response.status_code != 200:
            raise HttpError()

        file_name = extract_file_name(response)

        with open(f"{file_path}/{file_name}", mode="wb") as w:
            for chunk in response.iter_content(chunk_size=10 * 1024):
                w.write(chunk)

    def get_xbrl_taxanomy(
        self, sj_div: str
    ) -> BaseListDto[XbrlTaxanomyOutputDto]:
        """
        Downloads the XBRL taxonomy for the given sj_div and returns an XbrlTaxanomyOutputDto object.

        Args:
            sj_div (str): 재무제표 구분 (BS: 재무상태표, IS: 손익계산서, CIS: 포괄손익계산서, CF: 현금흐름표, SCE: 자본변동표

        Returns:
            XbrlTaxanomyOutputDto: An object containing the downloaded XBRL taxonomy.
        """
        path = "/api/xbrlTaxonomy.json"
        params = BaseParamDto(sj_div=sj_div)

        response = self.open_dart.get(path, params.dict())
        if response.status_code != 200:
            raise HttpError(path)

        def _mapping(x: Dict[str, str]) -> XbrlTaxanomyOutputDto:
            return XbrlTaxanomyOutputDto(
                sj_div=x["sj_div"],
                account_id=x["account_id"],
                account_nm=x["account_nm"],
                bsns_de=x["bsns_de"],
                label_kor=x["label_kor"],
                label_eng=x["label_eng"],
                data_tp=x["data_tp"] if "data_tp" in x else None,
                ifrs_ref=x["ifrs_ref"],
            )

        data = response.json()

        return BaseListDto[XbrlTaxanomyOutputDto](
            status=data["status"],
            message=data["message"],
            list=list(map(_mapping, data["list"])),
        )
