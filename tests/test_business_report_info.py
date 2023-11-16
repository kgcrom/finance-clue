import os

from stock_clue.opendart.business_report_info import BusinessReportInfo
from stock_clue.opendart.open_dart import OpenDart


class TestBusinessReportInfo:
    def test_get_total_director_remuneration_approval(self):
        """
        이사·감사 전체의 보수현황(주주총회 승인금액) 조회 테스트
        """
        result = BusinessReportInfo(
            OpenDart(os.environ["OPENDART_API_KEY"])
        ).get_director_total_remuneration_approval(
            corp_code="01029394", bsns_year="2020", reprt_code="11013"
        )

        assert result is not None
        assert result.status == "000"
        assert len(list(filter(lambda x: x.corp_cls == "K", result.list))) == 2
        assert (
            len(
                list(
                    filter(
                        lambda x: x.gmtsck_confm_amount >= 100000000,
                        result.list,
                    )
                )
            )
            == 2
        )

    def test_get_director_remuneration_amount(self):
        result = BusinessReportInfo(
            OpenDart(os.environ["OPENDART_API_KEY"])
        ).get_director_remuneration_amount(
            corp_code="01029394",
            bsns_year="2020",
            reprt_code="11013",
        )

        assert result is not None
        assert result.status == "000"
        assert len(result.list) != 0

    def test_total_stock(self):
        """
        주식의 총수 현황 조회 테스트
        """
        result = BusinessReportInfo(
            OpenDart(os.environ["OPENDART_API_KEY"])
        ).total_stock_quantity(
            corp_code="01029394",
            bsns_year="2020",
            reprt_code="11013",
        )

        assert result is not None
        assert len(result.list) == 4

    def test_get_dividend(self):
        """
        배당에 관한 사항 조회 테스트
        """
        result = BusinessReportInfo(
            OpenDart(os.environ["OPENDART_API_KEY"])
        ).get_dividend(
            corp_code="01029394",
            bsns_year="2020",
            reprt_code="11013",
        )

        assert result is not None
        assert len(result.list) != 0

    def test_audit_opinion(self):
        """
        회계감사인의 명칭 및 감사의견 조회 테스트
        """
        result = BusinessReportInfo(
            OpenDart(os.environ["OPENDART_API_KEY"])
        ).audit_opinion(
            corp_code="01029394",
            bsns_year="2020",
            reprt_code="11013",
        )

        assert result is not None

    def test_get_non_executive_director(self):
        """
        사외이사 및 그 변동사항 조회 테스트
        """
        result = BusinessReportInfo(
            OpenDart(os.environ["OPENDART_API_KEY"])
        ).get_non_executive_director(
            corp_code="01029394",
            bsns_year="2020",
            reprt_code="11013",
        )

        assert result is not None

    def test_get_acquisition_and_disposal_of_treasury_stocks(self):
        """
        자기주식의 취득 및 처분 현황 조회 테스트
        """
        result = BusinessReportInfo(
            OpenDart(os.environ["OPENDART_API_KEY"])
        ).get_acquisition_and_disposal_of_treasury_stocks(
            corp_code="01029394",
            bsns_year="2020",
            reprt_code="11013",
        )

        assert result is not None

    def test_get_capital_increase_and_reduction(self):
        """
        증자(감자) 현황 조회 테스트
        """
        result = BusinessReportInfo(
            OpenDart(os.environ["OPENDART_API_KEY"])
        ).get_capital_increase_and_reduction(
            corp_code="01029394",
            bsns_year="2020",
            reprt_code="11013",
        )

        assert result is not None
        assert (
            filter(lambda x: x.isu_dcrs_stock_knd == "유상증자(일반공모)", result.list)
            is not None
        )

    def test_largest_shareholders(self):
        """
        최대주주 현황 조회 테스트
        """
        result = BusinessReportInfo(
            OpenDart(os.environ["OPENDART_API_KEY"])
        ).largest_shareholders(
            corp_code="01029394",
            bsns_year="2020",
            reprt_code="11013",
        )

        assert result is not None

    def test_changed_largest_shareholders(self):
        result = BusinessReportInfo(
            OpenDart(os.environ["OPENDART_API_KEY"])
        ).changed_largest_shareholders(
            corp_code="01029394",
            bsns_year="2020",
            reprt_code="11013",
        )

        assert result is not None

    def test_get_executive_info(self):
        """
        임원 현황 조회 테스트
        """
        result = BusinessReportInfo(
            OpenDart(os.environ["OPENDART_API_KEY"])
        ).get_executive_info(
            corp_code="01029394",
            bsns_year="2020",
            reprt_code="11013",
        )

        assert result is not None
        assert len(result.list) != 0

    def test_get_employee_info(self):
        """
        직원 현황 조회 테스트
        """
        result = BusinessReportInfo(
            OpenDart(os.environ["OPENDART_API_KEY"])
        ).get_employee_info(
            corp_code="01029394",
            bsns_year="2020",
            reprt_code="11013",
        )

        assert result is not None

    def test_get_individual_director_remuneration(self):
        """
        이사·감사의 개인별 보수 현황 조회 테스트
        """
        result = BusinessReportInfo(
            OpenDart(os.environ["OPENDART_API_KEY"])
        ).get_individual_director_remuneration(
            corp_code="01029394",
            bsns_year="2020",
            reprt_code="11013",
        )

        assert result is not None

    def test_get_total_director_remuneration(self):
        """
        이사·감사의 전체의 보수 현황 조회 테스트
        """
        result = BusinessReportInfo(
            OpenDart(os.environ["OPENDART_API_KEY"])
        ).get_total_director_remuneration(
            corp_code="01029394",
            bsns_year="2020",
            reprt_code="11013",
        )

        assert result is not None
        assert len(result.list) != 0

    def test_get_individual_remuneration_over5(self):
        """
        개인별 보수지급 금액(5억이상 상위5인) 조회 테스트
        """
        result = BusinessReportInfo(
            OpenDart(os.environ["OPENDART_API_KEY"])
        ).get_individual_remuneration_over5(
            corp_code="01029394",
            bsns_year="2020",
            reprt_code="11013",
        )

        assert result is not None
        assert len(result.list) != 0

    def test_get_large_scale_holding(self):
        """
        대량보유 상황보고서 내역 조회 테스트
        """
        result = BusinessReportInfo(
            OpenDart(os.environ["OPENDART_API_KEY"])
        ).get_large_scale_holding(corp_code="01029394")

        assert result is not None
        assert result.status == "000"
        assert len(result.list) != 0

    def test_get_executives_and_major_shareholders(self):
        """
        임원 및 주요주주 현황 조회 테스트
        """
        result = BusinessReportInfo(
            OpenDart(os.environ["OPENDART_API_KEY"])
        ).get_executives_and_major_shareholders(corp_code="01029394")

        assert result is not None
        assert result.status == "000"
        assert len(result.list) != 0
