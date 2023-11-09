import os

from stock_clue.opendart.open_dart import OpenDart


class TestBusinessReportInfo:
    def test_get_total_director_remuneration_approval(self):
        """
        이사·감사 전체의 보수현황(주주총회 승인금액) 조회 테스트
        """
        open_dart = OpenDart(os.environ["OPENDART_API_KEY"])
        result = open_dart.business_report_info.get_director_total_remuneration_approval(
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
        open_dart = OpenDart(os.environ["OPENDART_API_KEY"])
        result = (
            open_dart.business_report_info.get_director_remuneration_amount(
                corp_code="01029394",
                bsns_year="2020",
                reprt_code="11013",
            )
        )

        assert result is not None
        assert result.status == "000"
        assert len(result.list) != 0

    def test_total_stock(self):
        """
        주식의 총수 현황 조회 테스트
        """
        open_dart = OpenDart(os.environ["OPENDART_API_KEY"])
        result = open_dart.business_report_info.total_stock_quantity(
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
        open_dart = OpenDart(os.environ["OPENDART_API_KEY"])
        result = open_dart.business_report_info.get_dividend(
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
        open_dart = OpenDart(os.environ["OPENDART_API_KEY"])

        result = open_dart.business_report_info.audit_opinion(
            corp_code="01029394",
            bsns_year="2020",
            reprt_code="11013",
        )

        assert result is not None

    def test_get_non_executive_director(self):
        """
        사외이사 및 그 변동사항 조회 테스트
        """
        open_dart = OpenDart(os.environ["OPENDART_API_KEY"])
        result = open_dart.business_report_info.get_non_executive_director(
            corp_code="01029394",
            bsns_year="2020",
            reprt_code="11013",
        )

        assert result is not None

    def test_get_acquisition_and_disposal_of_treasury_stocks(self):
        """
        자기주식의 취득 및 처분 현황 조회 테스트
        """
        open_dart = OpenDart(os.environ["OPENDART_API_KEY"])
        result = open_dart.business_report_info.get_acquisition_and_disposal_of_treasury_stocks(
            corp_code="01029394",
            bsns_year="2020",
            reprt_code="11013",
        )

        assert result is not None

    def test_get_capital_increase_and_reduction(self):
        """
        증자(감자) 현황 조회 테스트
        """
        open_dart = OpenDart(os.environ["OPENDART_API_KEY"])
        result = (
            open_dart.business_report_info.get_capital_increase_and_reduction(
                corp_code="01029394",
                bsns_year="2020",
                reprt_code="11013",
            )
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
        open_dart = OpenDart(os.environ["OPENDART_API_KEY"])
        result = open_dart.business_report_info.largest_shareholders(
            corp_code="01029394",
            bsns_year="2020",
            reprt_code="11013",
        )

        assert result is not None

    def test_changed_largest_shareholders(self):
        open_dart = OpenDart(os.environ["OPENDART_API_KEY"])
        result = open_dart.business_report_info.changed_largest_shareholders(
            corp_code="01029394",
            bsns_year="2020",
            reprt_code="11013",
        )

        assert result is not None

    def test_get_executive_info(self):
        """
        임원 현황 조회 테스트
        """
        open_dart = OpenDart(os.environ["OPENDART_API_KEY"])
        result = open_dart.business_report_info.get_executive_info(
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
        open_dart = OpenDart(os.environ["OPENDART_API_KEY"])
        result = open_dart.business_report_info.get_employee_info(
            corp_code="01029394",
            bsns_year="2020",
            reprt_code="11013",
        )

        assert result is not None

    def test_get_individual_director_remuneration(self):
        """
        이사·감사의 개인별 보수 현황 조회 테스트
        """
        open_dart = OpenDart(os.environ["OPENDART_API_KEY"])
        result = (
            open_dart.business_report_info.get_individual_director_remuneration(
                corp_code="01029394",
                bsns_year="2020",
                reprt_code="11013",
            )
        )

        assert result is not None

    def test_get_total_director_remuneration(self):
        """
        이사·감사의 전체의 보수 현황 조회 테스트
        """
        open_dart = OpenDart(os.environ["OPENDART_API_KEY"])
        result = open_dart.business_report_info.get_total_director_remuneration(
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
        open_dart = OpenDart(os.environ["OPENDART_API_KEY"])
        result = (
            open_dart.business_report_info.get_individual_remuneration_over5(
                corp_code="01029394",
                bsns_year="2020",
                reprt_code="11013",
            )
        )

        assert result is not None
        assert len(result.list) != 0
