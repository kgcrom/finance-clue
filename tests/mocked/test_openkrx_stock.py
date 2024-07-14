import unittest

import pytest
import responses

from finance_clue.openkrx import OpenKrxClient


class OpenKrxStockTestCase(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def setup(self, mock_openkrx_client: OpenKrxClient, mock_openkrx_client_url: str):
        self.openkrx_client = mock_openkrx_client
        self.openkrx_client_url = mock_openkrx_client_url

    @responses.activate
    def test_kospi_daily_stock(self):
        expected = {
            "OutBlock_1": [
                {
                    "BAS_DD": "20200414",
                    "ISU_CD": "338100",
                    "ISU_NM": "NH프라임리츠",
                    "MKT_NM": "KOSPI",
                    "SECT_TP_NM": "-",
                    "TDD_CLSPRC": "4715",
                    "CMPPREVDD_PRC": "25",
                    "FLUC_RT": "0.53",
                    "TDD_OPNPRC": "4655",
                    "TDD_HGPRC": "4720",
                    "TDD_LWPRC": "4655",
                    "ACC_TRDVOL": "21363",
                    "ACC_TRDVAL": "100332885",
                    "MKTCAP": "87981900000",
                    "LIST_SHRS": "18660000",
                }
            ]
        }

        responses.add(
            responses.GET,
            f"{self.openkrx_client_url}/svc/apis/sto/stk_bydd_trd",
            json=expected,
            status=200,
        )

        resp = self.openkrx_client.get_kospi_stock_daily(bas_dd="20240514")

        assert resp == expected

    @responses.activate
    def test_kosdaq_daily_stock(self):
        expected = {
            "OutBlock_1": [
                {
                    "BAS_DD": "20200414",
                    "ISU_CD": "950170",
                    "ISU_NM": "JTC",
                    "MKT_NM": "KOSDAQ",
                    "SECT_TP_NM": "외국기업(소속부없음)",
                    "TDD_CLSPRC": "5100",
                    "CMPPREVDD_PRC": "125",
                    "FLUC_RT": "2.51",
                    "TDD_OPNPRC": "4940",
                    "TDD_HGPRC": "5150",
                    "TDD_LWPRC": "4940",
                    "ACC_TRDVOL": "112202",
                    "ACC_TRDVAL": "570871860",
                    "MKTCAP": "178528136700",
                    "LIST_SHRS": "35005517",
                }
            ]
        }

        responses.add(
            responses.GET,
            f"{self.openkrx_client_url}/svc/apis/sto/ksq_bydd_trd",
            json=expected,
            status=200,
        )

        resp = self.openkrx_client.get_kosdaq_stock_daily(bas_dd="20240514")

        assert resp == expected

    @responses.activate
    def test_konex_daily_stock(self):
        expected = {
            "OutBlock_1": [
                {
                    "BAS_DD": "20200414",
                    "ISU_CD": "323350",
                    "ISU_NM": "다원넥스뷰",
                    "MKT_NM": "KONEX",
                    "SECT_TP_NM": "일반기업부",
                    "TDD_CLSPRC": "23800",
                    "CMPPREVDD_PRC": "3100",
                    "FLUC_RT": "14.98",
                    "TDD_OPNPRC": "23800",
                    "TDD_HGPRC": "23800",
                    "TDD_LWPRC": "23800",
                    "ACC_TRDVOL": "1",
                    "ACC_TRDVAL": "23800",
                    "MKTCAP": "17374000000",
                    "LIST_SHRS": "730000",
                }
            ]
        }

        responses.add(
            responses.GET,
            f"{self.openkrx_client_url}/svc/apis/sto/knx_bydd_trd",
            json=expected,
            status=200,
        )

        resp = self.openkrx_client.get_konex_stock_daily(bas_dd="20240514")

        assert resp == expected

    @responses.activate
    def test_kospi_base_info(self):
        expected = {
            "OutBlock_1": [
                {
                    "ISU_CD": "KR7338100001",
                    "ISU_SRT_CD": "338100",
                    "ISU_NM": "NH프라임리츠보통주",
                    "ISU_ABBRV": "NH프라임리츠",
                    "ISU_ENG_NM": "NH Prime REIT",
                    "LIST_DD": "20191205",
                    "MKT_TP_NM": "KOSPI",
                    "SECUGRP_NM": "부동산투자회사",
                    "SECT_TP_NM": "-",
                    "KIND_STKCERT_TP_NM": "보통주",
                    "PARVAL": "500",
                    "LIST_SHRS": "18660000",
                }
            ]
        }

        responses.add(
            responses.GET,
            f"{self.openkrx_client_url}/svc/apis/sto/stk_isu_base_info",
            json=expected,
            status=200,
        )

        resp = self.openkrx_client.get_kospi_base_info(bas_dd="20240514")

        assert expected == resp

    @responses.activate
    def test_kosdaq_base_info(self):
        expected = {
            "OutBlock_1": [
                {
                    "ISU_CD": "KR8392070007",
                    "ISU_SRT_CD": "950110",
                    "ISU_NM": "SBI핀테크솔루션즈",
                    "ISU_ABBRV": "SBI핀테크솔루션즈",
                    "ISU_ENG_NM": "SBI FinTech Solutions Co., Ltd.",
                    "LIST_DD": "20121217",
                    "MKT_TP_NM": "KOSDAQ",
                    "SECUGRP_NM": "주식예탁증권",
                    "SECT_TP_NM": "외국기업(소속부없음)",
                    "KIND_STKCERT_TP_NM": "보통주",
                    "PARVAL": "무액면",
                    "LIST_SHRS": "24656540",
                }
            ]
        }

        responses.add(
            responses.GET,
            f"{self.openkrx_client_url}/svc/apis/sto/ksq_isu_base_info",
            json=expected,
            status=200,
        )

        resp = self.openkrx_client.get_kosdaq_base_info(bas_dd="20240514")

        assert expected == resp

    @responses.activate
    def test_konex_base_info(self):
        expected = {
            "OutBlock_1": [
                {
                    "ISU_CD": "KR7323350009",
                    "ISU_SRT_CD": "323350",
                    "ISU_NM": "다원넥스뷰",
                    "ISU_ABBRV": "다원넥스뷰",
                    "ISU_ENG_NM": "DAWON NEXVIEW",
                    "LIST_DD": "20190521",
                    "MKT_TP_NM": "KONEX",
                    "SECUGRP_NM": "주권",
                    "SECT_TP_NM": "일반기업부",
                    "KIND_STKCERT_TP_NM": "보통주",
                    "PARVAL": "500",
                    "LIST_SHRS": "730000",
                }
            ]
        }

        responses.add(
            responses.GET,
            f"{self.openkrx_client_url}/svc/apis/sto/knx_isu_base_info",
            json=expected,
            status=200,
        )

        resp = self.openkrx_client.get_konex_base_info(bas_dd="20240514")

        assert expected == resp
