import time
import unittest

import pytest

from finance_clue.opendart import OpenDartClient


@pytest.mark.usefixtures("integration_opendart_client")
class RegularDisclosureKeyCase(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def setup(self, integration_opendart_client: OpenDartClient):
        self.opendart_client = integration_opendart_client
        time.sleep(1)

    def test_conditional_capital_not_reimbursed_balance(self):
        resp = self.opendart_client.get_conditional_capital_not_reimbursed_balance(
            bsns_year=2023,
            corp_code="00126380",
            reprt_code="11011",
        )
        example = {
            "status": "000",
            "message": "정상",
            "list": [
                {
                    "rcept_no": "20240312000736",
                    "corp_cls": "Y",
                    "corp_code": "00126380",
                    "corp_name": "삼성전자",
                    "sm": "-",
                    "remndr_exprtn1": "미상환잔액",
                    "remndr_exprtn2": "공모",
                    "yy1_excess_yy2_below": "-",
                    "yy2_excess_yy3_below": "-",
                    "yy1_below": "-",
                    "yy3_excess_yy4_below": "-",
                    "yy4_excess_yy5_below": "-",
                    "yy5_excess_yy10_below": "-",
                    "yy20_excess_yy30_below": "-",
                    "yy30_excess": "-",
                    "yy10_excess_yy20_below": "-",
                }
            ],
        }
        assert resp is not None

    def test_corporate_bond_not_reimbursed_balance(self):
        resp = self.opendart_client.get_corporate_bond_not_reimbursed_balance(
            bsns_year=2023,
            corp_code="00126380",
            reprt_code="11011",
        )

        example = {
            "status": "000",
            "message": "정상",
            "list": [
                {
                    "rcept_no": "20240312000736",
                    "corp_cls": "Y",
                    "corp_code": "00126380",
                    "corp_name": "삼성전자",
                    "sm": "541,548,000,000",
                    "remndr_exprtn1": "미상환잔액",
                    "remndr_exprtn2": "공모",
                    "yy1_excess_yy2_below": "522,207,000,000",
                    "yy2_excess_yy3_below": "6,447,000,000",
                    "yy1_below": "6,447,000,000",
                    "yy3_excess_yy4_below": "6,447,000,000",
                    "yy4_excess_yy5_below": "-",
                    "yy5_excess_yy10_below": "-",
                    "yy10_excess": "-",
                }
            ],
        }
        assert resp is not None

    def test_short_term_bond_not_reimbursed_balance(self):
        resp = self.opendart_client.get_short_term_bond_not_reimbursed_balance(
            bsns_year=2023,
            corp_code="00126380",
            reprt_code="11011",
        )

        example = {
            "status": "000",
            "message": "정상",
            "list": [
                {
                    "rcept_no": "20240312000736",
                    "corp_cls": "Y",
                    "corp_code": "00126380",
                    "corp_name": "삼성전자",
                    "sm": "-",
                    "remndr_exprtn1": "미상환잔액",
                    "remndr_exprtn2": "공모",
                    "de10_below": "-",
                    "de10_excess_de30_below": "-",
                    "de30_excess_de90_below": "-",
                    "de90_excess_de180_below": "-",
                    "de180_excess_yy1_below": "-",
                    "isu_lmt": "-",
                    "remndr_lmt": "-",
                }
            ],
        }
        assert resp is not None

    def test_enterprises_bill_not_reimbursed_balance(self):
        resp = self.opendart_client.get_enterprises_bill_not_reimbursed_balance(
            bsns_year=2023,
            corp_code="00126380",
            reprt_code="11011",
        )

        example = {
            "status": "000",
            "message": "정상",
            "list": [
                {
                    "rcept_no": "20240312000736",
                    "corp_cls": "Y",
                    "corp_code": "00126380",
                    "corp_name": "삼성전자",
                    "sm": "-",
                    "remndr_exprtn1": "미상환잔액",
                    "remndr_exprtn2": "공모",
                    "de10_below": "-",
                    "de10_excess_de30_below": "-",
                    "de30_excess_de90_below": "-",
                    "de90_excess_de180_below": "-",
                    "de180_excess_yy1_below": "-",
                    "yy1_excess_yy2_below": "-",
                    "yy2_excess_yy3_below": "-",
                    "yy3_excess": "-",
                }
            ],
        }
        assert resp is not None

    def test_debt_securities_issue_accomplishment(self):
        resp = self.opendart_client.get_debt_securities_issue_accomplishment(
            bsns_year=2023,
            corp_code="00126380",
            reprt_code="11011",
        )
        example = {
            "status": "000",
            "message": "정상",
            "list": [
                {
                    "rcept_no": "20240312000736",
                    "corp_cls": "Y",
                    "corp_code": "00126380",
                    "corp_name": "삼성전자",
                    "isu_cmpny": "삼성전자㈜",
                    "scrits_knd_nm": "회사채",
                    "isu_mth_nm": "공모",
                    "isu_de": "1997.10.02",
                    "facvalu_totamt": "128,940,000,000",
                    "intrt": "7.7%",
                    "evl_grad_instt": "Aa2 (Moody's),\n AA- (S&P)",
                    "mtd": "2027.10.01",
                    "repy_at": "일부상환",
                    "mngt_cmpny": "Goldman Sachs 등",
                }
            ],
        }
        assert resp is not None

    def test_private_equity_capital_use_details(self):
        resp = self.opendart_client.get_private_equity_capital_use_details(
            bsns_year=2023,
            corp_code="00126380",
            reprt_code="11011",
        )

        example = {
            "status": "000",
            "message": "정상",
            "list": [
                {
                    "rcept_no": "20240312000736",
                    "corp_cls": "Y",
                    "corp_code": "00126380",
                    "corp_name": "삼성전자",
                    "se_nm": "-",
                    "tm": "-",
                    "pay_de": "-",
                    "pay_amount": "-",
                    "real_cptal_use_sttus": "-",
                    "real_cptal_use_dtls_cn": "-",
                    "real_cptal_use_dtls_amount": "-",
                    "dffrnc_occrrnc_resn": "-",
                    "cptal_use_plan": "-",
                    "mtrpt_cptal_use_plan_useprps": "-",
                    "mtrpt_cptal_use_plan_prcure_amount": "-",
                }
            ],
        }
        assert resp is not None

    def test_public_equity_capital_use_details(self):
        resp = self.opendart_client.get_public_equity_capital_use_details(
            bsns_year=2023,
            corp_code="00126380",
            reprt_code="11011",
        )

        example = {
            "status": "000",
            "message": "정상",
            "list": [
                {
                    "rcept_no": "20240312000736",
                    "corp_cls": "Y",
                    "corp_code": "00126380",
                    "corp_name": "삼성전자",
                    "se_nm": "-",
                    "tm": "-",
                    "pay_de": "-",
                    "pay_amount": "-",
                    "on_dclrt_cptal_use_plan": "-",
                    "real_cptal_use_sttus": "-",
                    "rs_cptal_use_plan_useprps": "-",
                    "rs_cptal_use_plan_prcure_amount": "-",
                    "real_cptal_use_dtls_cn": "-",
                    "real_cptal_use_dtls_amount": "-",
                    "dffrnc_occrrnc_resn": "-",
                }
            ],
        }
        assert resp is not None

    def test_director_audit_all_mending_status_shareholders_general_meeting_confirm_amount(
        self,
    ):
        resp = self.opendart_client.get_director_audit_all_mending_status_shareholders_general_meeting_confirm_amount(
            bsns_year=2023,
            corp_code="00126380",
            reprt_code="11011",
        )

        example = {
            "status": "000",
            "message": "정상",
            "list": [
                {
                    "rcept_no": "20240312000736",
                    "corp_cls": "Y",
                    "corp_code": "00126380",
                    "corp_name": "삼성전자",
                    "se": "등기이사",
                    "nmpr": "5",
                    "gmtsck_confm_amount": "-",
                    "rm": "-",
                }
            ],
        }
        assert resp is not None

    def test_director_audit_all_mending_status_mending_payment_amount_type_classification(
        self,
    ):
        resp = self.opendart_client.get_director_audit_all_mending_status_mending_payment_amount_type_classification(
            bsns_year=2023,
            corp_code="00126380",
            reprt_code="11011",
        )

        example = {
            "status": "000",
            "message": "정상",
            "list": [
                {
                    "rcept_no": "20240312000736",
                    "corp_cls": "Y",
                    "corp_code": "00126380",
                    "corp_name": "삼성전자",
                    "se": "등기이사(사외이사, 감사위원회 위원 제외)",
                    "nmpr": "5",
                    "pymnt_totamt": "22,009,000,000",
                    "psn1_avrg_pymntamt": "4,402,000,000",
                    "rm": "-",
                }
            ],
        }
        assert resp is not None

    def test_stock_total_quantity_status(self):
        resp = self.opendart_client.get_stock_total_quantity_status(
            bsns_year=2023,
            corp_code="00126380",
            reprt_code="11011",
        )

        example = {
            "status": "000",
            "message": "정상",
            "list": [
                {
                    "rcept_no": "20240312000736",
                    "corp_cls": "Y",
                    "corp_code": "00126380",
                    "corp_name": "삼성전자",
                    "se": "보통주",
                    "isu_stock_totqy": "20,000,000,000",
                    "now_to_isu_stock_totqy": "7,780,466,850",
                    "now_to_dcrs_stock_totqy": "1,810,684,300",
                    "redc": "-",
                    "profit_incnr": "1,810,684,300",
                    "rdmstk_repy": "-",
                    "etc": "-",
                    "istc_totqy": "5,969,782,550",
                    "tesstk_co": "-",
                    "distb_stock_co": "5,969,782,550",
                }
            ],
        }
        assert resp is not None

    def test_account_auditor_name_and_opinion(self):
        resp = self.opendart_client.get_account_auditor_name_and_opinion(
            bsns_year=2023,
            corp_code="00126380",
            reprt_code="11011",
        )

        example = {
            "status": "000",
            "message": "정상",
            "list": [
                {
                    "rcept_no": "20240312000736",
                    "corp_cls": "Y",
                    "corp_code": "00126380",
                    "corp_name": "삼성전자",
                    "bsns_year": "제55기\n(당기)",
                    "adtor": "삼정회계법인",
                    "adt_opinion": "적정",
                    "adt_reprt_spcmnt_matter": "-",
                    "emphs_matter": "해당사항 없음",
                    "core_adt_matter": "(연결재무제표)\n 1. 메모리 반도체 재고자산 순실현가치 평가\n 2. 재화의 판매장려활동에 대한 매출차감의 정확성과 완전성\n(별도재무제표)\n 1. 메모리 반도체 재고자산 순실현가치 평가\n 2. 재화의 판매장려활동에 대한 매출차감의 정확성과 완전성",
                }
            ],
        }
        assert resp is not None

    def test_audit_service_conclusion_status(self):
        resp = self.opendart_client.get_audit_service_conclusion_status(
            bsns_year=2023,
            corp_code="00126380",
            reprt_code="11011",
        )

        example = {
            "status": "000",
            "message": "정상",
            "list": [
                {
                    "rcept_no": "20240312000736",
                    "corp_cls": "Y",
                    "corp_code": "00126380",
                    "corp_name": "삼성전자",
                    "bsns_year": "제55기\n(당기)",
                    "adtor": "삼정회계법인",
                    "cn": "분ㆍ반기 재무제표 검토\n별도 및 연결 재무제표에 대한 감사\n별도 및 연결 내부회계관리제도 감사",
                    "mendng": "-",
                    "tot_reqre_time": "-",
                    "adt_cntrct_dtls_mendng": "7,800",
                    "adt_cntrct_dtls_time": "85,700",
                    "real_exc_dtls_mendng": "7,800",
                    "real_exc_dtls_time": "85,036",
                }
            ],
        }
        assert resp is not None

    def test_account_auditor_non_audit_service_conclusion_status(self):
        resp = self.opendart_client.get_account_auditor_non_audit_service_conclusion_status(
            bsns_year=2023,
            corp_code="00126380",
            reprt_code="11011",
        )

        example = {
            "status": "000",
            "message": "정상",
            "list": [
                {
                    "rcept_no": "20240312000736",
                    "corp_cls": "Y",
                    "corp_code": "00126380",
                    "corp_name": "삼성전자",
                    "bsns_year": "제55기\n(당기)",
                    "cntrct_cncls_de": "2017.02\n2018.09\n2019.05\n2023.05",
                    "servc_cn": "세무자문업무(해외종속기업)\n세무자문업무(해외종속기업)\n세무자문업무(해외종속기업)\nESG인증업무(국내종속기업)",
                    "servc_exc_pd": "2023.01~2023.12\n2023.01~2023.12\n2023.01~2023.12\n2023.05~2023.07",
                    "servc_mendng": "202\n27\n79\n25",
                    "rm": "삼정회계법인",
                }
            ],
        }
        assert resp is not None

    def test_outside_director_change_status(self):
        resp = self.opendart_client.get_outside_director_change_status(
            bsns_year=2023,
            corp_code="00126380",
            reprt_code="11011",
        )

        example = {
            "list": [
                {
                    "apnt": "-",
                    "corp_cls": "Y",
                    "corp_code": "00126380",
                    "corp_name": "삼성전자",
                    "drctr_co": "11",
                    "mdstrm_resig": "-",
                    "otcmp_drctr_co": "6",
                    "rcept_no": "20240312000736",
                    "rlsofc": "-",
                }
            ],
            "message": "정상",
            "status": "000",
        }
        assert resp is not None

    def test_new_capital_securities_not_reimbursed_balance(self):
        resp = self.opendart_client.get_new_capital_securities_not_reimbursed_balance(
            bsns_year=2023,
            corp_code="00126380",
            reprt_code="11011",
        )

        example = {
            "status": "000",
            "message": "정상",
            "list": [
                {
                    "rcept_no": "20240312000736",
                    "corp_cls": "Y",
                    "corp_code": "00126380",
                    "corp_name": "삼성전자",
                    "sm": "-",
                    "remndr_exprtn1": "미상환잔액",
                    "remndr_exprtn2": "공모",
                    "yy1_below": "-",
                    "yy5_excess_yy10_below": "-",
                    "yy1_excess_yy5_below": "-",
                    "yy10_excess_yy15_below": "-",
                    "yy15_excess_yy20_below": "-",
                    "yy20_excess_yy30_below": "-",
                    "yy30_excess": "-",
                }
            ],
        }
        assert resp is not None

    def test_increase_decrease_status(self):
        resp = self.opendart_client.get_increase_decrease_status(
            bsns_year=2023,
            corp_code="00126380",
            reprt_code="11011",
        )

        example = {
            "status": "000",
            "message": "정상",
            "list": [
                {
                    "rcept_no": "20240312000736",
                    "corp_cls": "Y",
                    "corp_code": "00126380",
                    "corp_name": "삼성전자",
                    "isu_dcrs_de": "-",
                    "isu_dcrs_stle": "-",
                    "isu_dcrs_stock_knd": "-",
                    "isu_dcrs_qy": "-",
                    "isu_dcrs_mstvdv_fval_amount": "-",
                    "isu_dcrs_mstvdv_amount": "-",
                }
            ],
        }
        assert resp is not None

    def test_allocation_matter(self):
        resp = self.opendart_client.get_allocation_matter(
            bsns_year=2023,
            corp_code="00126380",
            reprt_code="11011",
        )

        example = {
            "status": "000",
            "message": "정상",
            "list": [
                {
                    "rcept_no": "20240312000736",
                    "corp_cls": "Y",
                    "corp_code": "00126380",
                    "corp_name": "삼성전자",
                    "se": "주당액면가액(원)",
                    "thstrm": "100",
                    "frmtrm": "100",
                    "lwfr": "100",
                }
            ],
        }
        assert resp is not None

    def test_treasury_shares_acquisition_disposal_status(self):
        resp = self.opendart_client.get_treasury_shares_acquisition_disposal_status(
            bsns_year=2023,
            corp_code="00126380",
            reprt_code="11011",
        )

        example = {
            "status": "000",
            "message": "정상",
            "list": [
                {
                    "rcept_no": "20240312000736",
                    "corp_cls": "Y",
                    "corp_code": "00126380",
                    "corp_name": "삼성전자",
                    "stock_knd": "-",
                    "acqs_mth1": "-",
                    "acqs_mth2": "-",
                    "acqs_mth3": "-",
                    "bsis_qy": "-",
                    "change_qy_acqs": "-",
                    "change_qy_dsps": "-",
                    "change_qy_incnr": "-",
                    "trmend_qy": "-",
                    "rm": "-",
                }
            ],
        }
        assert resp is not None

    def test_largest_shareholder_status(self):
        resp = self.opendart_client.get_largest_shareholder_status(
            bsns_year=2023,
            corp_code="00126380",
            reprt_code="11011",
        )

        example = {
            "status": "000",
            "message": "정상",
            "list": [
                {
                    "rcept_no": "20240312000736",
                    "corp_cls": "Y",
                    "corp_code": "00126380",
                    "corp_name": "삼성전자",
                    "stock_knd": "보통주",
                    "nm": "삼성생명보험㈜",
                    "relate": "최대주주 본인",
                    "bsis_posesn_stock_co": "508,157,148",
                    "bsis_posesn_stock_qota_rt": "8.51",
                    "trmend_posesn_stock_co": "508,157,148",
                    "trmend_posesn_stock_qota_rt": "8.51",
                    "rm": "-",
                }
            ],
        }
        assert resp is not None

    def test_largest_shareholder_change_status(self):
        resp = self.opendart_client.get_largest_shareholder_change_status(
            bsns_year=2023,
            corp_code="00126380",
            reprt_code="11011",
        )

        example = {
            "status": "000",
            "message": "정상",
            "list": [
                {
                    "rcept_no": "20240312000736",
                    "corp_cls": "Y",
                    "corp_code": "00126380",
                    "corp_name": "삼성전자",
                    "change_on": "2021년 04월 29일",
                    "mxmm_shrholdr_nm": "삼성생명보험㈜",
                    "posesn_stock_co": "1,263,050,053",
                    "qota_rt": "21.16%",
                    "change_cause": "변동전 최대주주의 피상속",
                    "rm": "-",
                }
            ],
        }
        assert resp is not None

    def test_minority_shareholders_status(self):
        resp = self.opendart_client.get_minority_shareholders_status(
            bsns_year=2023,
            corp_code="00126380",
            reprt_code="11011",
        )

        example = {
            "status": "000",
            "message": "정상",
            "list": [
                {
                    "rcept_no": "20240312000736",
                    "corp_cls": "Y",
                    "corp_code": "00126380",
                    "corp_name": "삼성전자",
                    "se": "소액주주",
                    "shrholdr_co": "4,672,039",
                    "shrholdr_tot_co": "4,672,130",
                    "shrholdr_rate": "99.99%",
                    "hold_stock_co": "4,017,892,514",
                    "stock_tot_co": "5,969,782,550",
                    "hold_stock_rate": "67.30%",
                }
            ],
        }
        assert resp is not None

    def test_executive_status(self):
        resp = self.opendart_client.get_executive_status(
            bsns_year=2023,
            corp_code="00126380",
            reprt_code="11011",
        )

        example = {
            "status": "000",
            "message": "정상",
            "list": [
                {
                    "rcept_no": "20240312000736",
                    "corp_cls": "Y",
                    "corp_code": "00126380",
                    "corp_name": "삼성전자",
                    "nm": "한종희",
                    "sexdstn": "남",
                    "birth_ym": "1962년 03월",
                    "ofcps": "부회장",
                    "rgist_exctv_at": "사내이사",
                    "fte_at": "상근",
                    "chrg_job": "ㆍ대표이사   (DX 부문 경영전반 총괄)",
                    "main_career": "ㆍ인하대 전자공학 학사ㆍ삼성전자 DX부문장",
                    "mxmm_shrholdr_relate": "계열회사\n임원",
                    "hffc_pd": "46개월",
                    "tenure_end_on": "2026년 03월 17일",
                }
            ],
        }
        assert resp is not None

    def test_employee_status(self):
        resp = self.opendart_client.get_employee_status(
            bsns_year=2023,
            corp_code="00126380",
            reprt_code="11011",
        )

        example = {
            "status": "000",
            "message": "정상",
            "list": [
                {
                    "rcept_no": "20240312000736",
                    "corp_cls": "Y",
                    "corp_code": "00126380",
                    "corp_name": "삼성전자",
                    "sexdstn": "남",
                    "fo_bbm": "DX",
                    "reform_bfe_emp_co_rgllbr": "-",
                    "reform_bfe_emp_co_cnttk": "-",
                    "reform_bfe_emp_co_etc": "-",
                    "rgllbr_co": "37,962",
                    "rgllbr_abacpt_labrr_co": "-",
                    "cnttk_co": "324",
                    "cnttk_abacpt_labrr_co": "-",
                    "sm": "38,286",
                    "avrg_cnwk_sdytrn": "16.5",
                    "fyer_salary_totamt": "-",
                    "jan_salary_am": "-",
                    "rm": "-",
                }
            ],
        }
        assert resp is not None

    def test_director_auditor_individual_mending(self):
        resp = self.opendart_client.get_director_auditor_individual_mending(
            bsns_year=2023,
            corp_code="00126380",
            reprt_code="11011",
        )

        example = {
            "status": "000",
            "message": "정상",
            "list": [
                {
                    "rcept_no": "20240312000736",
                    "corp_cls": "Y",
                    "corp_code": "00126380",
                    "corp_name": "삼성전자",
                    "nm": "경계현",
                    "ofcps": "대표이사",
                    "mendng_totamt": "2,403,000,000",
                    "mendng_totamt_ct_incls_mendng": "-",
                }
            ],
        }
        assert resp is not None

    def test_director_audit_all_mending(self):
        resp = self.opendart_client.get_director_audit_all_mending(
            bsns_year=2023,
            corp_code="00126380",
            reprt_code="11011",
        )

        example = {
            "list": [
                {
                    "corp_cls": "Y",
                    "corp_code": "00126380",
                    "corp_name": "삼성전자",
                    "jan_avrg_mendng_am": "2,112,000,000",
                    "mendng_totamt": "23,227,000,000",
                    "nmpr": "11",
                    "rcept_no": "20240312000736",
                    "rm": "-",
                }
            ],
            "message": "정상",
            "status": "000",
        }
        assert resp is not None

    def test_individual_by_pay(self):
        resp = self.opendart_client.get_individual_by_pay(
            bsns_year=2023,
            corp_code="00126380",
            reprt_code="11011",
        )

        example = {
            "status": "000",
            "message": "정상",
            "list": [
                {
                    "rcept_no": "20240312000736",
                    "corp_cls": "Y",
                    "corp_code": "00126380",
                    "corp_name": "삼성전자",
                    "nm": "김기남",
                    "ofcps": "고문",
                    "mendng_totamt": "17,265,000,000",
                    "mendng_totamt_ct_incls_mendng": "-",
                }
            ],
        }
        assert resp is not None

    def test_outer_corporate_investment_status(self):
        resp = self.opendart_client.get_outer_corporate_investment_status(
            bsns_year=2023,
            corp_code="00126380",
            reprt_code="11011",
        )

        example = {
            "status": "000",
            "message": "정상",
            "list": [
                {
                    "rcept_no": "20240312000736",
                    "corp_cls": "Y",
                    "corp_code": "00126380",
                    "corp_name": "삼성전자",
                    "inv_prm": "삼성전기㈜",
                    "frst_acqs_de": "1977.01.01",
                    "invstmnt_purps": "경영참여",
                    "frst_acqs_amount": "250,000,000",
                    "bsis_blce_qy": "17,693,000",
                    "bsis_blce_qota_rt": "23.7",
                    "bsis_blce_acntbk_amount": "445,244,000,000",
                    "incrs_dcrs_acqs_dsps_qy": "-",
                    "incrs_dcrs_acqs_dsps_amount": "-",
                    "incrs_dcrs_evl_lstmn": "-",
                    "trmend_blce_qy": "17,693,000",
                    "trmend_blce_qota_rt": "23.7",
                    "trmend_blce_acntbk_amount": "445,244,000,000",
                    "recent_bsns_year_fnnr_sttus_tot_assets": "11,657,872,000,000",
                    "recent_bsns_year_fnnr_sttus_thstrm_ntpf": "450,482,000,000",
                }
            ],
        }
        assert resp is not None


if __name__ == "__main__":
    unittest.main()
