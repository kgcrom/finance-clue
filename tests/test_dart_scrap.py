from bs4 import BeautifulSoup
import pytest

from finance_clue.dartscrap import DartScrap
from finance_clue.dartscrap.dividend_parser import DividendParser
from finance_clue.dartscrap.dividend_parser import parse_html_table
from finance_clue.dartscrap.list_disclosure import ListDisclosure
from finance_clue.dartscrap.list_disclosure import MarketGroup
from finance_clue.dartscrap.list_disclosure import parse_daily_disclosure


@pytest.mark.skip(reason="Scrap takes a long time")
class TestDartScrap:
    def setup_class(self):
        self.dart_scrap = DartScrap(headless=True)
        self.list_disclosure = ListDisclosure(self.dart_scrap)
        self.dividend_parser = DividendParser(self.dart_scrap)

    def test_get_kospi_daily_disclosure(self):
        data = self.list_disclosure.get_daily_disclosure(
            "2023.11.14", 1, MarketGroup.KOSPI
        )

        assert data is not None
        assert data.total == 964
        assert len(data.disclosures) == 100

    def test_get_kosdaq_daily_disclosure(self):
        data = self.list_disclosure.get_daily_disclosure(
            "2023.11.14", 1, MarketGroup.KOSDAQ
        )
        assert data is not None
        assert data.total == 1424
        assert len(data.disclosures) == 100

    def test_get_all_daily_disclosure(self):
        data = self.list_disclosure.get_daily_disclosure("2023.11.14", 1)
        assert data is not None
        assert data.total > 3100
        assert len(data.disclosures) == 100

    def test_parse_daily_disclosure(self):
        html_doc = """<!--목록 -->
    <div class="tbTitle">
     	<h4>

    			유가증권시장







    		&nbsp;<span class="txtCB" id="txtCB">963</span>건




    					(2023년 11월 14일)


    	</h4>

    	<div class="sort" >








    				<a id="time" name="sort" onclick="setOrder(this);" class="downOn" href="#none" data-order="desc" title="시간 내림차순">시간</a>
    				<a id="crp" name="sort" onclick="setOrder(this);" class="upOff" href="#none" data-order="asc" title="회사명 올림차순">회사명</a>
    				<a id="rpt" name="sort"  onclick="setOrder(this);" class="upOff" href="#none" data-order="asc" title="보고서명 올림차순">보고서명</a>




    	</div>
    </div>
    <div class="tbListInner" >
    	<table class="tbList" summary="시간,공시대상회사,보고서명,제출인,접수일자,비고 순으로 되어있습니다.">
    		<caption>유가증권시장 목록</caption>
    		<colgroup>
    			<col style="width:7%">
    			<col style="width:24%">
    			<col style="width:auto">
    			<col style="width:13%">
    			<col style="width:11%">
    			<col style="width:8%">
    		</colgroup>
    		<thead>
    			<tr>
    				<th scope="row"><label for="inpSample00">시간</label></th>
    				<th scope="row"><label for="inpSample00">공시대상회사</label></th>
    				<th scope="row"><label for="inpSample00">보고서명</label></th>
    				<th scope="row"><label for="inpSample00">제출인</label></th>
    				<th scope="row"><label for="inpSample00">접수일자</label></th>
    				<th scope="row"><label for="inpSample00">비고</label></th>
    			</tr>
    		</thead>


    				<tbody>





    						<tr>
    							<td>



    								19:00
    							</td>
    							<td class="tL">
    							    <span class="innerWrap">
    							    	<span class="tagCom_kospi" title="유가증권시장" style="cursor:default">유</span>
    									<a href="javascript:openCorpInfoNew('00126089', 'winCorpInfo', '/dsae001/selectPopup.ax');" title="대유플러스 기업개황 새창" >
    										대유플러스
    									</a>
    								</span>

    							</td>
    							<td class="tL">
    								<a href="/dsaf001/main.do?rcpNo=20231114003049"  onclick="openReportViewer('20231114003049'); return false;" id="r_20231114003049"
    									title="분기보고서 공시뷰어 새창" >분기보고서
    									 (2023.09)

    								</a>
    							</td>
    							<td class="tL ellipsis" title="대유플러스">대유플러스</td>
    							<td>2023.11.14</td>
    							<td></td>
    						</tr>




    						<tr>
    							<td>



    								18:50
    							</td>
    							<td class="tL">
    							    <span class="innerWrap">
    							    	<span class="tagCom_kospi" title="유가증권시장" style="cursor:default">유</span>
    									<a href="javascript:openCorpInfoNew('01596425', 'winCorpInfo', '/dsae001/selectPopup.ax');" title="SK스퀘어 기업개황 새창" >
    										SK스퀘어
    									</a>
    								</span>

    							</td>
    							<td class="tL">
    								<a href="/dsaf001/main.do?rcpNo=20231114003047"  onclick="openReportViewer('20231114003047'); return false;" id="r_20231114003047"
    									title="분기보고서 공시뷰어 새창" >분기보고서
    									 (2023.09)

    								</a>
    							</td>
    							<td class="tL ellipsis" title="SK스퀘어">SK스퀘어</td>
    							<td>2023.11.14</td>
    							<td><span class="tagCom_jung_other" title="본 보고서 제출 후 정정신고가 있으니 관련 보고서를 참조하시기 바람" style="cursor:default">정</span></td>
    						</tr>




    						<tr>
    							<td>



    								18:39
    							</td>
    							<td class="tL">
    							    <span class="innerWrap">
    							    	<span class="tagCom_kospi" title="유가증권시장" style="cursor:default">유</span>
    									<a href="javascript:openCorpInfoNew('00137207', 'winCorpInfo', '/dsae001/selectPopup.ax');" title="유니켐 기업개황 새창" >
    										유니켐
    									</a>
    								</span>

    							</td>
    							<td class="tL">
    								<a href="/dsaf001/main.do?rcpNo=20231114003044"  onclick="openReportViewer('20231114003044'); return false;" id="r_20231114003044"
    									title="분기보고서 공시뷰어 새창" >분기보고서
    									 (2023.09)

    								</a>
    							</td>
    							<td class="tL ellipsis" title="유니켐">유니켐</td>
    							<td>2023.11.14</td>
    							<td><span class="tagCom_jung_other" title="본 보고서 제출 후 정정신고가 있으니 관련 보고서를 참조하시기 바람" style="cursor:default">정</span></td>
    						</tr>




    						<tr>
    							<td>



    								18:35
    							</td>
    							<td class="tL">
    							    <span class="innerWrap">
    							    	<span class="tagCom_kospi" title="유가증권시장" style="cursor:default">유</span>
    									<a href="javascript:openCorpInfoNew('00273615', 'winCorpInfo', '/dsae001/selectPopup.ax');" title="비케이탑스 기업개황 새창" >
    										비케이탑스
    									</a>
    								</span>

    							</td>
    							<td class="tL">
    								<a href="/dsaf001/main.do?rcpNo=20231114803354"  onclick="openReportViewer('20231114803354'); return false;" id="r_20231114803354"
    									title="기타시장안내(상장적격성 실질심사사유 추가 관련 안내) 공시뷰어 새창" >기타시장안내

    		  							(상장적격성 실질심사사유 추가 관련 안내)
    								</a>
    							</td>
    							<td class="tL ellipsis" title="유가증권시장본부">유가증권시장본부</td>
    							<td>2023.11.14</td>
    							<td><span class="tagCom_kospi_other" title="본 공시사항은 한국거래소 유가증권시장본부 소관임" style="cursor:default">유</span></td>
    						</tr>




    						<tr>
    							<td>



    								18:24
    							</td>
    							<td class="tL">
    							    <span class="innerWrap">
    							    	<span class="tagCom_kospi" title="유가증권시장" style="cursor:default">유</span>
    									<a href="javascript:openCorpInfoNew('00138279', 'winCorpInfo', '/dsae001/selectPopup.ax');" title="S-Oil 기업개황 새창" >
    										S-Oil
    									</a>
    								</span>

    							</td>
    							<td class="tL">
    								<a href="/dsaf001/main.do?rcpNo=20231114803293"  onclick="openReportViewer('20231114803293'); return false;" id="r_20231114803293"
    									title="조회공시요구(풍문또는보도)에대한답변(부인) 공시뷰어 새창" >조회공시요구(풍문또는보도)에대한답변(부인)


    								</a>
    							</td>
    							<td class="tL ellipsis" title="S-Oil">S-Oil</td>
    							<td>2023.11.14</td>
    							<td><span class="tagCom_kospi_other" title="본 공시사항은 한국거래소 유가증권시장본부 소관임" style="cursor:default">유</span></td>
    						</tr>




    						<tr>
    							<td>



    								18:21
    							</td>
    							<td class="tL">
    							    <span class="innerWrap">
    							    	<span class="tagCom_kospi" title="유가증권시장" style="cursor:default">유</span>
    									<a href="javascript:openCorpInfoNew('00131054', 'winCorpInfo', '/dsae001/selectPopup.ax');" title="유진증권 기업개황 새창" >
    										유진증권
    									</a>
    								</span>

    							</td>
    							<td class="tL">
    								<a href="/dsaf001/main.do?rcpNo=20231114002728"  onclick="openReportViewer('20231114002728'); return false;" id="r_20231114002728"
    									title="일괄신고서(기타파생결합증권) 공시뷰어 새창" ><span title="본 보고서명으로 이미 제출된 보고서의 기재내용이 변경되어 제출된 것임" class="txtCB">[기재정정]</span>일괄신고서(기타파생결합증권)


    								</a>
    							</td>
    							<td class="tL ellipsis" title="유진증권">유진증권</td>
    							<td>2023.11.14</td>
    							<td></td>
    						</tr>




    						<tr>
    							<td>



    								18:21
    							</td>
    							<td class="tL">
    							    <span class="innerWrap">
    							    	<span class="tagCom_kospi" title="유가증권시장" style="cursor:default">유</span>
    									<a href="javascript:openCorpInfoNew('00131054', 'winCorpInfo', '/dsae001/selectPopup.ax');" title="유진증권 기업개황 새창" >
    										유진증권
    									</a>
    								</span>

    							</td>
    							<td class="tL">
    								<a href="/dsaf001/main.do?rcpNo=20231114001523"  onclick="openReportViewer('20231114001523'); return false;" id="r_20231114001523"
    									title="일괄신고서(기타파생결합증권) 공시뷰어 새창" ><span title="본 보고서명으로 이미 제출된 보고서의 기재내용이 변경되어 제출된 것임" class="txtCB">[기재정정]</span>일괄신고서(기타파생결합증권)


    								</a>
    							</td>
    							<td class="tL ellipsis" title="유진증권">유진증권</td>
    							<td>2023.11.14</td>
    							<td><span class="tagCom_jung_other" title="본 보고서 제출 후 정정신고가 있으니 관련 보고서를 참조하시기 바람" style="cursor:default">정</span></td>
    						</tr>




    						<tr>
    							<td>



    								18:16
    							</td>
    							<td class="tL">
    							    <span class="innerWrap">
    							    	<span class="tagCom_kospi" title="유가증권시장" style="cursor:default">유</span>
    									<a href="javascript:openCorpInfoNew('00131054', 'winCorpInfo', '/dsae001/selectPopup.ax');" title="유진증권 기업개황 새창" >
    										유진증권
    									</a>
    								</span>

    							</td>
    							<td class="tL">
    								<a href="/dsaf001/main.do?rcpNo=20231114002682"  onclick="openReportViewer('20231114002682'); return false;" id="r_20231114002682"
    									title="일괄신고서(기타파생결합사채) 공시뷰어 새창" ><span title="본 보고서명으로 이미 제출된 보고서의 기재내용이 변경되어 제출된 것임" class="txtCB">[기재정정]</span>일괄신고서(기타파생결합사채)


    								</a>
    							</td>
    							<td class="tL ellipsis" title="유진증권">유진증권</td>
    							<td>2023.11.14</td>
    							<td></td>
    						</tr>




    						<tr>
    							<td>



    								18:16
    							</td>
    							<td class="tL">
    							    <span class="innerWrap">
    							    	<span class="tagCom_kospi" title="유가증권시장" style="cursor:default">유</span>
    									<a href="javascript:openCorpInfoNew('00131054', 'winCorpInfo', '/dsae001/selectPopup.ax');" title="유진증권 기업개황 새창" >
    										유진증권
    									</a>
    								</span>

    							</td>
    							<td class="tL">
    								<a href="/dsaf001/main.do?rcpNo=20231114001491"  onclick="openReportViewer('20231114001491'); return false;" id="r_20231114001491"
    									title="일괄신고서(기타파생결합사채) 공시뷰어 새창" ><span title="본 보고서명으로 이미 제출된 보고서의 기재내용이 변경되어 제출된 것임" class="txtCB">[기재정정]</span>일괄신고서(기타파생결합사채)


    								</a>
    							</td>
    							<td class="tL ellipsis" title="유진증권">유진증권</td>
    							<td>2023.11.14</td>
    							<td><span class="tagCom_jung_other" title="본 보고서 제출 후 정정신고가 있으니 관련 보고서를 참조하시기 바람" style="cursor:default">정</span></td>
    						</tr>




    						<tr>
    							<td>



    								18:11
    							</td>
    							<td class="tL">
    							    <span class="innerWrap">
    							    	<span class="tagCom_kospi" title="유가증권시장" style="cursor:default">유</span>
    									<a href="javascript:openCorpInfoNew('00910947', 'winCorpInfo', '/dsae001/selectPopup.ax');" title="바다로19호 기업개황 새창" >
    										바다로19호
    									</a>
    								</span>

    							</td>
    							<td class="tL">
    								<a href="/dsaf001/main.do?rcpNo=20231114003034"  onclick="openReportViewer('20231114003034'); return false;" id="r_20231114003034"
    									title="분기보고서 공시뷰어 새창" >분기보고서
    									 (2023.09)

    								</a>
    							</td>
    							<td class="tL ellipsis" title="바다로19호">바다로19호</td>
    							<td>2023.11.14</td>
    							<td></td>
    						</tr>


    						<tr>
    							<td>



    								18:11
    							</td>
    							<td class="tL">
    							    <span class="innerWrapTag">
    							    	<span class="tagCom_kospi" title="유가증권시장" style="cursor:default">유</span>
    									<a href="javascript:openCorpInfoNew('00258801', 'winCorpInfo', '/dsae001/selectPopup.ax');" title="카카오 기업개황 새창" >
    										카카오
    									</a>
    								</span>
    								<a href="https://www.kakaocorp.com/ir/main" target="new">
    										<span class="tagCom_ir" title="기업 IR페이지 연결">IR</span>
    									</a>
    							</td>
    							<td class="tL">
    								<a href="/dsaf001/main.do?rcpNo=20231114003032"  onclick="openReportViewer('20231114003032'); return false;" id="r_20231114003032"
    									title="분기보고서 공시뷰어 새창" ><span title="본 보고서명으로 이미 제출된 보고서의 기재내용이 변경되어 제출된 것임" class="txtCB">[기재정정]</span>분기보고서
    									 (2023.09)

    								</a>
    							</td>
    							<td class="tL ellipsis" title="카카오">카카오</td>
    							<td>2023.11.14</td>
    							<td></td>
    						</tr>




    						<tr>
    							<td>



    								18:08
    							</td>
    							<td class="tL">
    							    <span class="innerWrap">
    							    	<span class="tagCom_kospi" title="유가증권시장" style="cursor:default">유</span>
    									<a href="javascript:openCorpInfoNew('00131850', 'winCorpInfo', '/dsae001/selectPopup.ax');" title="SK증권 기업개황 새창" >
    										SK증권
    									</a>
    								</span>

    							</td>
    							<td class="tL">
    								<a href="/dsaf001/main.do?rcpNo=20231114002988"  onclick="openReportViewer('20231114002988'); return false;" id="r_20231114002988"
    									title="일괄신고서(기타파생결합사채) 공시뷰어 새창" ><span title="본 보고서명으로 이미 제출된 보고서의 기재내용이 변경되어 제출된 것임" class="txtCB">[기재정정]</span>일괄신고서(기타파생결합사채)


    								</a>
    							</td>
    							<td class="tL ellipsis" title="SK증권">SK증권</td>
    							<td>2023.11.14</td>
    							<td></td>
    						</tr>




    						<tr>
    							<td>



    								18:08
    							</td>
    							<td class="tL">
    							    <span class="innerWrap">
    							    	<span class="tagCom_kospi" title="유가증권시장" style="cursor:default">유</span>
    									<a href="javascript:openCorpInfoNew('00120182', 'winCorpInfo', '/dsae001/selectPopup.ax');" title="NH투자증권 기업개황 새창" >
    										NH투자증권
    									</a>
    								</span>

    							</td>
    							<td class="tL">
    								<a href="/dsaf001/main.do?rcpNo=20231114003003"  onclick="openReportViewer('20231114003003'); return false;" id="r_20231114003003"
    									title="일괄신고서(파생결합사채-주가연계파생결합사채) 공시뷰어 새창" ><span title="본 보고서명으로 이미 제출된 보고서의 기재내용이 변경되어 제출된 것임" class="txtCB">[기재정정]</span>일괄신고서(파생결합사채-주가연계파생결합사채)


    								</a>
    							</td>
    							<td class="tL ellipsis" title="NH투자증권">NH투자증권</td>
    							<td>2023.11.14</td>
    							<td></td>
    						</tr>




    						<tr>
    							<td>



    								18:08
    							</td>
    							<td class="tL">
    							    <span class="innerWrap">
    							    	<span class="tagCom_kospi" title="유가증권시장" style="cursor:default">유</span>
    									<a href="javascript:openCorpInfoNew('00120182', 'winCorpInfo', '/dsae001/selectPopup.ax');" title="NH투자증권 기업개황 새창" >
    										NH투자증권
    									</a>
    								</span>

    							</td>
    							<td class="tL">
    								<a href="/dsaf001/main.do?rcpNo=20231114002629"  onclick="openReportViewer('20231114002629'); return false;" id="r_20231114002629"
    									title="일괄신고서(파생결합사채-주가연계파생결합사채) 공시뷰어 새창" ><span title="본 보고서명으로 이미 제출된 보고서의 기재내용이 변경되어 제출된 것임" class="txtCB">[기재정정]</span>일괄신고서(파생결합사채-주가연계파생결합사채)


    								</a>
    							</td>
    							<td class="tL ellipsis" title="NH투자증권">NH투자증권</td>
    							<td>2023.11.14</td>
    							<td><span class="tagCom_jung_other" title="본 보고서 제출 후 정정신고가 있으니 관련 보고서를 참조하시기 바람" style="cursor:default">정</span></td>
    						</tr>




    						<tr>
    							<td>



    								18:07
    							</td>
    							<td class="tL">
    							    <span class="innerWrap">
    							    	<span class="tagCom_kospi" title="유가증권시장" style="cursor:default">유</span>
    									<a href="javascript:openCorpInfoNew('00120182', 'winCorpInfo', '/dsae001/selectPopup.ax');" title="NH투자증권 기업개황 새창" >
    										NH투자증권
    									</a>
    								</span>

    							</td>
    							<td class="tL">
    								<a href="/dsaf001/main.do?rcpNo=20231114003008"  onclick="openReportViewer('20231114003008'); return false;" id="r_20231114003008"
    									title="일괄신고서(기타파생결합사채) 공시뷰어 새창" ><span title="본 보고서명으로 이미 제출된 보고서의 기재내용이 변경되어 제출된 것임" class="txtCB">[기재정정]</span>일괄신고서(기타파생결합사채)


    								</a>
    							</td>
    							<td class="tL ellipsis" title="NH투자증권">NH투자증권</td>
    							<td>2023.11.14</td>
    							<td></td>
    						</tr>




    						<tr>
    							<td>



    								18:07
    							</td>
    							<td class="tL">
    							    <span class="innerWrap">
    							    	<span class="tagCom_kospi" title="유가증권시장" style="cursor:default">유</span>
    									<a href="javascript:openCorpInfoNew('00120182', 'winCorpInfo', '/dsae001/selectPopup.ax');" title="NH투자증권 기업개황 새창" >
    										NH투자증권
    									</a>
    								</span>

    							</td>
    							<td class="tL">
    								<a href="/dsaf001/main.do?rcpNo=20231114002041"  onclick="openReportViewer('20231114002041'); return false;" id="r_20231114002041"
    									title="일괄신고서(기타파생결합사채) 공시뷰어 새창" ><span title="본 보고서명으로 이미 제출된 보고서의 기재내용이 변경되어 제출된 것임" class="txtCB">[기재정정]</span>일괄신고서(기타파생결합사채)


    								</a>
    							</td>
    							<td class="tL ellipsis" title="NH투자증권">NH투자증권</td>
    							<td>2023.11.14</td>
    							<td><span class="tagCom_jung_other" title="본 보고서 제출 후 정정신고가 있으니 관련 보고서를 참조하시기 바람" style="cursor:default">정</span></td>
    						</tr>




    						<tr>
    							<td>



    								18:07
    							</td>
    							<td class="tL">
    							    <span class="innerWrap">
    							    	<span class="tagCom_kospi" title="유가증권시장" style="cursor:default">유</span>
    									<a href="javascript:openCorpInfoNew('00138224', 'winCorpInfo', '/dsae001/selectPopup.ax');" title="쌍용씨앤이 기업개황 새창" >
    										쌍용씨앤이
    									</a>
    								</span>

    							</td>
    							<td class="tL">
    								<a href="/dsaf001/main.do?rcpNo=20231114003028"  onclick="openReportViewer('20231114003028'); return false;" id="r_20231114003028"
    									title="분기보고서 공시뷰어 새창" >분기보고서
    									 (2023.09)

    								</a>
    							</td>
    							<td class="tL ellipsis" title="쌍용씨앤이">쌍용씨앤이</td>
    							<td>2023.11.14</td>
    							<td></td>
    						</tr>




    						<tr>
    							<td>



    								18:06
    							</td>
    							<td class="tL">
    							    <span class="innerWrap">
    							    	<span class="tagCom_kospi" title="유가증권시장" style="cursor:default">유</span>
    									<a href="javascript:openCorpInfoNew('00131850', 'winCorpInfo', '/dsae001/selectPopup.ax');" title="SK증권 기업개황 새창" >
    										SK증권
    									</a>
    								</span>

    							</td>
    							<td class="tL">
    								<a href="/dsaf001/main.do?rcpNo=20231114002975"  onclick="openReportViewer('20231114002975'); return false;" id="r_20231114002975"
    									title="일괄신고서(기타파생결합증권) 공시뷰어 새창" ><span title="본 보고서명으로 이미 제출된 보고서의 기재내용이 변경되어 제출된 것임" class="txtCB">[기재정정]</span>일괄신고서(기타파생결합증권)


    								</a>
    							</td>
    							<td class="tL ellipsis" title="SK증권">SK증권</td>
    							<td>2023.11.14</td>
    							<td></td>
    						</tr>




    						<tr>
    							<td>



    								18:06
    							</td>
    							<td class="tL">
    							    <span class="innerWrap">
    							    	<span class="tagCom_kospi" title="유가증권시장" style="cursor:default">유</span>
    									<a href="javascript:openCorpInfoNew('00120182', 'winCorpInfo', '/dsae001/selectPopup.ax');" title="NH투자증권 기업개황 새창" >
    										NH투자증권
    									</a>
    								</span>

    							</td>
    							<td class="tL">
    								<a href="/dsaf001/main.do?rcpNo=20231114003013"  onclick="openReportViewer('20231114003013'); return false;" id="r_20231114003013"
    									title="일괄신고서(파생결합증권-주가연계증권) 공시뷰어 새창" ><span title="본 보고서명으로 이미 제출된 보고서의 기재내용이 변경되어 제출된 것임" class="txtCB">[기재정정]</span>일괄신고서(파생결합증권-주가연계증권)


    								</a>
    							</td>
    							<td class="tL ellipsis" title="NH투자증권">NH투자증권</td>
    							<td>2023.11.14</td>
    							<td></td>
    						</tr>




    						<tr>
    							<td>



    								18:06
    							</td>
    							<td class="tL">
    							    <span class="innerWrap">
    							    	<span class="tagCom_kospi" title="유가증권시장" style="cursor:default">유</span>
    									<a href="javascript:openCorpInfoNew('00120182', 'winCorpInfo', '/dsae001/selectPopup.ax');" title="NH투자증권 기업개황 새창" >
    										NH투자증권
    									</a>
    								</span>

    							</td>
    							<td class="tL">
    								<a href="/dsaf001/main.do?rcpNo=20231114002526"  onclick="openReportViewer('20231114002526'); return false;" id="r_20231114002526"
    									title="일괄신고서(파생결합증권-주가연계증권) 공시뷰어 새창" ><span title="본 보고서명으로 이미 제출된 보고서의 기재내용이 변경되어 제출된 것임" class="txtCB">[기재정정]</span>일괄신고서(파생결합증권-주가연계증권)


    								</a>
    							</td>
    							<td class="tL ellipsis" title="NH투자증권">NH투자증권</td>
    							<td>2023.11.14</td>
    							<td><span class="tagCom_jung_other" title="본 보고서 제출 후 정정신고가 있으니 관련 보고서를 참조하시기 바람" style="cursor:default">정</span></td>
    						</tr>




    						<tr>
    							<td>



    								18:06
    							</td>
    							<td class="tL">
    							    <span class="innerWrap">
    							    	<span class="tagCom_kospi" title="유가증권시장" style="cursor:default">유</span>
    									<a href="javascript:openCorpInfoNew('00561866', 'winCorpInfo', '/dsae001/selectPopup.ax');" title="락앤락 기업개황 새창" >
    										락앤락
    									</a>
    								</span>

    							</td>
    							<td class="tL">
    								<a href="/dsaf001/main.do?rcpNo=20231114003027"  onclick="openReportViewer('20231114003027'); return false;" id="r_20231114003027"
    									title="분기보고서 공시뷰어 새창" >분기보고서
    									 (2023.09)

    								</a>
    							</td>
    							<td class="tL ellipsis" title="락앤락">락앤락</td>
    							<td>2023.11.14</td>
    							<td></td>
    						</tr>




    						<tr>
    							<td>



    								18:05
    							</td>
    							<td class="tL">
    							    <span class="innerWrap">
    							    	<span class="tagCom_kospi" title="유가증권시장" style="cursor:default">유</span>
    									<a href="javascript:openCorpInfoNew('00120182', 'winCorpInfo', '/dsae001/selectPopup.ax');" title="NH투자증권 기업개황 새창" >
    										NH투자증권
    									</a>
    								</span>

    							</td>
    							<td class="tL">
    								<a href="/dsaf001/main.do?rcpNo=20231114003016"  onclick="openReportViewer('20231114003016'); return false;" id="r_20231114003016"
    									title="일괄신고서(기타파생결합증권) 공시뷰어 새창" ><span title="본 보고서명으로 이미 제출된 보고서의 기재내용이 변경되어 제출된 것임" class="txtCB">[기재정정]</span>일괄신고서(기타파생결합증권)


    								</a>
    							</td>
    							<td class="tL ellipsis" title="NH투자증권">NH투자증권</td>
    							<td>2023.11.14</td>
    							<td></td>
    						</tr>




    						<tr>
    							<td>



    								18:05
    							</td>
    							<td class="tL">
    							    <span class="innerWrap">
    							    	<span class="tagCom_kospi" title="유가증권시장" style="cursor:default">유</span>
    									<a href="javascript:openCorpInfoNew('00120182', 'winCorpInfo', '/dsae001/selectPopup.ax');" title="NH투자증권 기업개황 새창" >
    										NH투자증권
    									</a>
    								</span>

    							</td>
    							<td class="tL">
    								<a href="/dsaf001/main.do?rcpNo=20231114002232"  onclick="openReportViewer('20231114002232'); return false;" id="r_20231114002232"
    									title="일괄신고서(기타파생결합증권) 공시뷰어 새창" ><span title="본 보고서명으로 이미 제출된 보고서의 기재내용이 변경되어 제출된 것임" class="txtCB">[기재정정]</span>일괄신고서(기타파생결합증권)


    								</a>
    							</td>
    							<td class="tL ellipsis" title="NH투자증권">NH투자증권</td>
    							<td>2023.11.14</td>
    							<td><span class="tagCom_jung_other" title="본 보고서 제출 후 정정신고가 있으니 관련 보고서를 참조하시기 바람" style="cursor:default">정</span></td>
    						</tr>




    						<tr>
    							<td>



    								18:05
    							</td>
    							<td class="tL">
    							    <span class="innerWrap">
    							    	<span class="tagCom_kospi" title="유가증권시장" style="cursor:default">유</span>
    									<a href="javascript:openCorpInfoNew('00126256', 'winCorpInfo', '/dsae001/selectPopup.ax');" title="삼성생명 기업개황 새창" >
    										삼성생명
    									</a>
    								</span>

    							</td>
    							<td class="tL">
    								<a href="/dsaf001/main.do?rcpNo=20231114003026"  onclick="openReportViewer('20231114003026'); return false;" id="r_20231114003026"
    									title="분기보고서 공시뷰어 새창" >분기보고서
    									 (2023.09)

    								</a>
    							</td>
    							<td class="tL ellipsis" title="삼성생명">삼성생명</td>
    							<td>2023.11.14</td>
    							<td></td>
    						</tr>




    						<tr>
    							<td>



    								18:04
    							</td>
    							<td class="tL">
    							    <span class="innerWrap">
    							    	<span class="tagCom_kospi" title="유가증권시장" style="cursor:default">유</span>
    									<a href="javascript:openCorpInfoNew('00131850', 'winCorpInfo', '/dsae001/selectPopup.ax');" title="SK증권 기업개황 새창" >
    										SK증권
    									</a>
    								</span>

    							</td>
    							<td class="tL">
    								<a href="/dsaf001/main.do?rcpNo=20231114002961"  onclick="openReportViewer('20231114002961'); return false;" id="r_20231114002961"
    									title="일괄신고서(파생결합사채-주가연계파생결합사채) 공시뷰어 새창" ><span title="본 보고서명으로 이미 제출된 보고서의 기재내용이 변경되어 제출된 것임" class="txtCB">[기재정정]</span>일괄신고서(파생결합사채-주가연계파생결합사채)


    								</a>
    							</td>
    							<td class="tL ellipsis" title="SK증권">SK증권</td>
    							<td>2023.11.14</td>
    							<td></td>
    						</tr>




    						<tr>
    							<td>



    								18:03
    							</td>
    							<td class="tL">
    							    <span class="innerWrap">
    							    	<span class="tagCom_kospi" title="유가증권시장" style="cursor:default">유</span>
    									<a href="javascript:openCorpInfoNew('00131850', 'winCorpInfo', '/dsae001/selectPopup.ax');" title="SK증권 기업개황 새창" >
    										SK증권
    									</a>
    								</span>

    							</td>
    							<td class="tL">
    								<a href="/dsaf001/main.do?rcpNo=20231114002938"  onclick="openReportViewer('20231114002938'); return false;" id="r_20231114002938"
    									title="일괄신고서(파생결합증권-주가연계증권) 공시뷰어 새창" ><span title="본 보고서명으로 이미 제출된 보고서의 기재내용이 변경되어 제출된 것임" class="txtCB">[기재정정]</span>일괄신고서(파생결합증권-주가연계증권)


    								</a>
    							</td>
    							<td class="tL ellipsis" title="SK증권">SK증권</td>
    							<td>2023.11.14</td>
    							<td></td>
    						</tr>




    						<tr>
    							<td>



    								18:01
    							</td>
    							<td class="tL">
    							    <span class="innerWrap">
    							    	<span class="tagCom_kospi" title="유가증권시장" style="cursor:default">유</span>
    									<a href="javascript:openCorpInfoNew('00162072', 'winCorpInfo', '/dsae001/selectPopup.ax');" title="한신기계공업 기업개황 새창" >
    										한신기계공업
    									</a>
    								</span>

    							</td>
    							<td class="tL">
    								<a href="/dsaf001/main.do?rcpNo=20231114003023"  onclick="openReportViewer('20231114003023'); return false;" id="r_20231114003023"
    									title="분기보고서 공시뷰어 새창" >분기보고서
    									 (2023.09)

    								</a>
    							</td>
    							<td class="tL ellipsis" title="한신기계공업">한신기계공업</td>
    							<td>2023.11.14</td>
    							<td></td>
    						</tr>




    						<tr>
    							<td>



    								18:00
    							</td>
    							<td class="tL">
    							    <span class="innerWrap">
    							    	<span class="tagCom_kospi" title="유가증권시장" style="cursor:default">유</span>
    									<a href="javascript:openCorpInfoNew('00138297', 'winCorpInfo', '/dsae001/selectPopup.ax');" title="STX 기업개황 새창" >
    										STX
    									</a>
    								</span>

    							</td>
    							<td class="tL">
    								<a href="/dsaf001/main.do?rcpNo=20231114003021"  onclick="openReportViewer('20231114003021'); return false;" id="r_20231114003021"
    									title="투자설명서 공시뷰어 새창" ><span title="본 보고서명으로 이미 제출된 보고서의 기재내용이 변경되어 제출된 것임" class="txtCB">[기재정정]</span>투자설명서


    								</a>
    							</td>
    							<td class="tL ellipsis" title="STX">STX</td>
    							<td>2023.11.14</td>
    							<td></td>
    						</tr>




    						<tr>
    							<td>



    								17:56
    							</td>
    							<td class="tL">
    							    <span class="innerWrap">
    							    	<span class="tagCom_kospi" title="유가증권시장" style="cursor:default">유</span>
    									<a href="javascript:openCorpInfoNew('00104856', 'winCorpInfo', '/dsae001/selectPopup.ax');" title="삼성증권 기업개황 새창" >
    										삼성증권
    									</a>
    								</span>

    							</td>
    							<td class="tL">
    								<a href="/dsaf001/main.do?rcpNo=20231114002286"  onclick="openReportViewer('20231114002286'); return false;" id="r_20231114002286"
    									title="일괄신고서(파생결합증권-상장지수증권) 공시뷰어 새창" ><span title="본 보고서명으로 이미 제출된 보고서의 기재내용이 변경되어 제출된 것임" class="txtCB">[기재정정]</span>일괄신고서(파생결합증권-상장지수증권)


    								</a>
    							</td>
    							<td class="tL ellipsis" title="삼성증권">삼성증권</td>
    							<td>2023.11.14</td>
    							<td></td>
    						</tr>




    						<tr>
    							<td>



    								17:54
    							</td>
    							<td class="tL">
    							    <span class="innerWrap">
    							    	<span class="tagCom_kospi" title="유가증권시장" style="cursor:default">유</span>
    									<a href="javascript:openCorpInfoNew('00104856', 'winCorpInfo', '/dsae001/selectPopup.ax');" title="삼성증권 기업개황 새창" >
    										삼성증권
    									</a>
    								</span>

    							</td>
    							<td class="tL">
    								<a href="/dsaf001/main.do?rcpNo=20231114002253"  onclick="openReportViewer('20231114002253'); return false;" id="r_20231114002253"
    									title="일괄신고서(기타파생결합사채) 공시뷰어 새창" ><span title="본 보고서명으로 이미 제출된 보고서의 기재내용이 변경되어 제출된 것임" class="txtCB">[기재정정]</span>일괄신고서(기타파생결합사채)


    								</a>
    							</td>
    							<td class="tL ellipsis" title="삼성증권">삼성증권</td>
    							<td>2023.11.14</td>
    							<td></td>
    						</tr>




    						<tr>
    							<td>



    								17:53
    							</td>
    							<td class="tL">
    							    <span class="innerWrap">
    							    	<span class="tagCom_kospi" title="유가증권시장" style="cursor:default">유</span>
    									<a href="javascript:openCorpInfoNew('00980122', 'winCorpInfo', '/dsae001/selectPopup.ax');" title="JB금융지주 기업개황 새창" >
    										JB금융지주
    									</a>
    								</span>

    							</td>
    							<td class="tL">
    								<a href="/dsaf001/main.do?rcpNo=20231114003006"  onclick="openReportViewer('20231114003006'); return false;" id="r_20231114003006"
    									title="일괄신고서 공시뷰어 새창" ><span title="본 보고서명으로 이미 제출된 보고서의 기재내용이 변경되어 제출된 것임" class="txtCB">[기재정정]</span>일괄신고서


    								</a>
    							</td>
    							<td class="tL ellipsis" title="JB금융지주">JB금융지주</td>
    							<td>2023.11.14</td>
    							<td></td>
    						</tr>




    						<tr>
    							<td>



    								17:53
    							</td>
    							<td class="tL">
    							    <span class="innerWrap">
    							    	<span class="tagCom_kospi" title="유가증권시장" style="cursor:default">유</span>
    									<a href="javascript:openCorpInfoNew('00104856', 'winCorpInfo', '/dsae001/selectPopup.ax');" title="삼성증권 기업개황 새창" >
    										삼성증권
    									</a>
    								</span>

    							</td>
    							<td class="tL">
    								<a href="/dsaf001/main.do?rcpNo=20231114002208"  onclick="openReportViewer('20231114002208'); return false;" id="r_20231114002208"
    									title="일괄신고서(기타파생결합증권) 공시뷰어 새창" ><span title="본 보고서명으로 이미 제출된 보고서의 기재내용이 변경되어 제출된 것임" class="txtCB">[기재정정]</span>일괄신고서(기타파생결합증권)


    								</a>
    							</td>
    							<td class="tL ellipsis" title="삼성증권">삼성증권</td>
    							<td>2023.11.14</td>
    							<td></td>
    						</tr>




    						<tr>
    							<td>



    								17:52
    							</td>
    							<td class="tL">
    							    <span class="innerWrap">
    							    	<span class="tagCom_kospi" title="유가증권시장" style="cursor:default">유</span>
    									<a href="javascript:openCorpInfoNew('00104856', 'winCorpInfo', '/dsae001/selectPopup.ax');" title="삼성증권 기업개황 새창" >
    										삼성증권
    									</a>
    								</span>

    							</td>
    							<td class="tL">
    								<a href="/dsaf001/main.do?rcpNo=20231114002162"  onclick="openReportViewer('20231114002162'); return false;" id="r_20231114002162"
    									title="일괄신고서(파생결합사채-주가연계파생결합사채) 공시뷰어 새창" ><span title="본 보고서명으로 이미 제출된 보고서의 기재내용이 변경되어 제출된 것임" class="txtCB">[기재정정]</span>일괄신고서(파생결합사채-주가연계파생결합사채)


    								</a>
    							</td>
    							<td class="tL ellipsis" title="삼성증권">삼성증권</td>
    							<td>2023.11.14</td>
    							<td></td>
    						</tr>




    						<tr>
    							<td>



    								17:52
    							</td>
    							<td class="tL">
    							    <span class="innerWrap">
    							    	<span class="tagCom_kospi" title="유가증권시장" style="cursor:default">유</span>
    									<a href="javascript:openCorpInfoNew('00113191', 'winCorpInfo', '/dsae001/selectPopup.ax');" title="코리안리 기업개황 새창" >
    										코리안리
    									</a>
    								</span>

    							</td>
    							<td class="tL">
    								<a href="/dsaf001/main.do?rcpNo=20231114003000"  onclick="openReportViewer('20231114003000'); return false;" id="r_20231114003000"
    									title="분기보고서 공시뷰어 새창" >분기보고서
    									 (2023.09)

    								</a>
    							</td>
    							<td class="tL ellipsis" title="코리안리">코리안리</td>
    							<td>2023.11.14</td>
    							<td></td>
    						</tr>




    						<tr>
    							<td>



    								17:51
    							</td>
    							<td class="tL">
    							    <span class="innerWrap">
    							    	<span class="tagCom_kospi" title="유가증권시장" style="cursor:default">유</span>
    									<a href="javascript:openCorpInfoNew('00104856', 'winCorpInfo', '/dsae001/selectPopup.ax');" title="삼성증권 기업개황 새창" >
    										삼성증권
    									</a>
    								</span>

    							</td>
    							<td class="tL">
    								<a href="/dsaf001/main.do?rcpNo=20231114002113"  onclick="openReportViewer('20231114002113'); return false;" id="r_20231114002113"
    									title="일괄신고서(파생결합증권-주가연계증권) 공시뷰어 새창" ><span title="본 보고서명으로 이미 제출된 보고서의 기재내용이 변경되어 제출된 것임" class="txtCB">[기재정정]</span>일괄신고서(파생결합증권-주가연계증권)


    								</a>
    							</td>
    							<td class="tL ellipsis" title="삼성증권">삼성증권</td>
    							<td>2023.11.14</td>
    							<td></td>
    						</tr>




    						<tr>
    							<td>



    								17:50
    							</td>
    							<td class="tL">
    							    <span class="innerWrap">
    							    	<span class="tagCom_kospi" title="유가증권시장" style="cursor:default">유</span>
    									<a href="javascript:openCorpInfoNew('00181712', 'winCorpInfo', '/dsae001/selectPopup.ax');" title="SK 기업개황 새창" >
    										SK
    									</a>
    								</span>

    							</td>
    							<td class="tL">
    								<a href="/dsaf001/main.do?rcpNo=20231114002831"  onclick="openReportViewer('20231114002831'); return false;" id="r_20231114002831"
    									title="분기보고서 공시뷰어 새창" ><span title="본 보고서명으로 이미 제출된 보고서의 첨부서류가 추가되어 제출된 것임" class="txtCB">[첨부추가]</span>분기보고서
    									 (2023.09)

    								</a>
    							</td>
    							<td class="tL ellipsis" title="SK">SK</td>
    							<td>2023.11.14</td>
    							<td></td>
    						</tr>


    						<tr>
    							<td>



    								17:49
    							</td>
    							<td class="tL">
    							    <span class="innerWrap">
    							    	<span class="tagCom_kospi" title="유가증권시장" style="cursor:default">유</span>
    									<a href="javascript:openCorpInfoNew('00152880', 'winCorpInfo', '/dsae001/selectPopup.ax');" title="코오롱글로벌 기업개황 새창" >
    										코오롱글로벌
    									</a>
    								</span>

    							</td>
    							<td class="tL">
    								<a href="/dsaf001/main.do?rcpNo=20231114002994"  onclick="openReportViewer('20231114002994'); return false;" id="r_20231114002994"
    									title="분기보고서 공시뷰어 새창" >분기보고서
    									 (2023.09)

    								</a>
    							</td>
    							<td class="tL ellipsis" title="코오롱글로벌">코오롱글로벌</td>
    							<td>2023.11.14</td>
    							<td></td>
    						</tr>



    						<tr>
    							<td>



    								17:48
    							</td>
    							<td class="tL">
    							    <span class="innerWrap">
    							    	<span class="tagCom_kospi" title="유가증권시장" style="cursor:default">유</span>
    									<a href="javascript:openCorpInfoNew('00480367', 'winCorpInfo', '/dsae001/selectPopup.ax');" title="SK오션플랜트 기업개황 새창" >
    										SK오션플랜트
    									</a>
    								</span>

    							</td>
    							<td class="tL">
    								<a href="/dsaf001/main.do?rcpNo=20231114803217"  onclick="openReportViewer('20231114803217'); return false;" id="r_20231114803217"
    									title="기업설명회(IR)개최(안내공시) 공시뷰어 새창" >기업설명회(IR)개최(안내공시)


    								</a>
    							</td>
    							<td class="tL ellipsis" title="SK오션플랜트">SK오션플랜트</td>
    							<td>2023.11.14</td>
    							<td><span class="tagCom_kospi_other" title="본 공시사항은 한국거래소 유가증권시장본부 소관임" style="cursor:default">유</span></td>
    						</tr>


    						<tr>
    							<td>



    								17:48
    							</td>
    							<td class="tL">
    							    <span class="innerWrap">
    							    	<span class="tagCom_kospi" title="유가증권시장" style="cursor:default">유</span>
    									<a href="javascript:openCorpInfoNew('00127255', 'winCorpInfo', '/dsae001/selectPopup.ax');" title="삼영 기업개황 새창" >
    										삼영
    									</a>
    								</span>

    							</td>
    							<td class="tL">
    								<a href="/dsaf001/main.do?rcpNo=20231114002993"  onclick="openReportViewer('20231114002993'); return false;" id="r_20231114002993"
    									title="의결권대리행사권유참고서류 공시뷰어 새창" >의결권대리행사권유참고서류


    								</a>
    							</td>
    							<td class="tL ellipsis" title="삼영">삼영</td>
    							<td>2023.11.14</td>
    							<td></td>
    						</tr>




    						<tr>
    							<td>



    								17:48
    							</td>
    							<td class="tL">
    							    <span class="innerWrap">
    							    	<span class="tagCom_kospi" title="유가증권시장" style="cursor:default">유</span>
    									<a href="javascript:openCorpInfoNew('00217947', 'winCorpInfo', '/dsae001/selectPopup.ax');" title="신세계건설 기업개황 새창" >
    										신세계건설
    									</a>
    								</span>

    							</td>
    							<td class="tL">
    								<a href="/dsaf001/main.do?rcpNo=20231114803261"  onclick="openReportViewer('20231114803261'); return false;" id="r_20231114803261"
    									title="현금ㆍ현물배당을위한주주명부폐쇄(기준일)결정 공시뷰어 새창" >현금ㆍ현물배당을위한주주명부폐쇄(기준일)결정


    								</a>
    							</td>
    							<td class="tL ellipsis" title="신세계건설">신세계건설</td>
    							<td>2023.11.14</td>
    							<td><span class="tagCom_kospi_other" title="본 공시사항은 한국거래소 유가증권시장본부 소관임" style="cursor:default">유</span></td>
    						</tr>



    						<tr>
    							<td>



    								17:48
    							</td>
    							<td class="tL">
    							    <span class="innerWrap">
    							    	<span class="tagCom_kospi" title="유가증권시장" style="cursor:default">유</span>
    									<a href="javascript:openCorpInfoNew('00156150', 'winCorpInfo', '/dsae001/selectPopup.ax');" title="하이트론씨스템즈 기업개황 새창" >
    										하이트론씨스템즈
    									</a>
    								</span>

    							</td>
    							<td class="tL">
    								<a href="/dsaf001/main.do?rcpNo=20231114002991"  onclick="openReportViewer('20231114002991'); return false;" id="r_20231114002991"
    									title="분기보고서 공시뷰어 새창" >분기보고서
    									 (2023.09)

    								</a>
    							</td>
    							<td class="tL ellipsis" title="하이트론씨스템즈">하이트론씨스템즈</td>
    							<td>2023.11.14</td>
    							<td></td>
    						</tr>




    						<tr>
    							<td>



    								17:48
    							</td>
    							<td class="tL">
    							    <span class="innerWrap">
    							    	<span class="tagCom_kospi" title="유가증권시장" style="cursor:default">유</span>
    									<a href="javascript:openCorpInfoNew('00109286', 'winCorpInfo', '/dsae001/selectPopup.ax');" title="대동 기업개황 새창" >
    										대동
    									</a>
    								</span>

    							</td>
    							<td class="tL">
    								<a href="/dsaf001/main.do?rcpNo=20231114002990"  onclick="openReportViewer('20231114002990'); return false;" id="r_20231114002990"
    									title="분기보고서 공시뷰어 새창" >분기보고서
    									 (2023.09)

    								</a>
    							</td>
    							<td class="tL ellipsis" title="대동">대동</td>
    							<td>2023.11.14</td>
    							<td></td>
    						</tr>




    						<tr>
    							<td>



    								17:46
    							</td>
    							<td class="tL">
    							    <span class="innerWrap">
    							    	<span class="tagCom_kospi" title="유가증권시장" style="cursor:default">유</span>
    									<a href="javascript:openCorpInfoNew('00113562', 'winCorpInfo', '/dsae001/selectPopup.ax');" title="롯데손해보험 기업개황 새창" >
    										롯데손해보험
    									</a>
    								</span>

    							</td>
    							<td class="tL">
    								<a href="/dsaf001/main.do?rcpNo=20231114002985"  onclick="openReportViewer('20231114002985'); return false;" id="r_20231114002985"
    									title="분기보고서 공시뷰어 새창" >분기보고서
    									 (2023.09)

    								</a>
    							</td>
    							<td class="tL ellipsis" title="롯데손해보험">롯데손해보험</td>
    							<td>2023.11.14</td>
    							<td></td>
    						</tr>
    				</tbody>

    		<input type="hidden" name="totalCnt" id="totalCnt" value="963">
    	</table>
    </div>

    	<div class = "psWrap">
    		<div class="pageInfo">[1/10] [총 963건]</div>

    		<div class="pageSkip">
    			<ul>
    				<li class="on"><a onClick="javascript:void(0);">1</a></li><li><a href="javascript:search(2);">2</a></li><li><a href="javascript:search(3);">3</a></li><li><a href="javascript:search(4);">4</a></li><li><a href="javascript:search(5);">5</a></li><li><a href="javascript:search(6);">6</a></li><li><a href="javascript:search(7);">7</a></li><li><a href="javascript:search(8);">8</a></li><li><a href="javascript:search(9);">9</a></li><li><a href="javascript:search(10);">10</a></li>

    			</ul>
    		</div>
    	</div>
            """

        data = parse_daily_disclosure(html_doc)
        assert data is not None
        assert data.total == 963
        assert len(data.disclosures) == 43

    def test_parse_dividend_table(self):
        html_doc = """
            <table border="1" bordercolordark="white" bordercolorlight="#666666" cellpadding="1" cellspacing="0" id="XFormD51_Form0_Table0" style="margin:0px 0px 20px 0px;width:600px;font-size:10pt;border:1px solid #7f7f7f;">
             <tbody>
              <tr>
               <td colspan="2" width="264" style="text-align: left;"> <span style="width: 264px; font-size: 10pt; display: inline;">1. 배당구분</span> </td>
               <td colspan="2" width="336" style="text-align: left;"> <span class="xforms_input" style="width: 336px; font-size: 10pt; display: inline;">중간(분기)</span> </td>
              </tr>
              <tr>
               <td rowspan="3" width="171" style="text-align: left;"> <span style="width: 171px; font-size: 10pt; display: inline;">2. 주주명부폐쇄(기준일)</span> </td>
               <td width="93" style="text-align: left;"> <span style="width: 93px; font-size: 10pt; text-align: center; display: inline;">시작일</span> </td>
               <td colspan="2" width="336" style="text-align: left;"> <span class="xforms_input" style="width: 336px; font-size: 10pt; display: inline;">2023-12-01</span> </td>
              </tr>
              <tr>
               <td width="93" style="text-align: left;"> <span style="width: 93px; font-size: 10pt; text-align: center; display: inline;">종료일</span> </td>
               <td colspan="2" width="336" style="text-align: left;"> <span class="xforms_input" style="width: 336px; font-size: 10pt; display: inline;">2023-12-05</span> </td>
              </tr>
              <tr>
               <td width="93" style="text-align: left;"> <span style="width: 93px; font-size: 10pt; text-align: center; display: inline;">기준일</span> </td>
               <td colspan="2" width="336" style="text-align: left;"> <span class="xforms_input" style="width: 336px; font-size: 10pt; display: inline;">2023-11-30</span> </td>
              </tr>
              <tr>
               <td colspan="2" width="264" style="text-align: left;"> <span style="width: 264px; font-size: 10pt; display: inline;">3. 주주명부폐쇄(기준일) 목적</span> </td>
               <td colspan="2" width="336" style="text-align: left;"> <span class="xforms_input" style="width: 336px; font-size: 10pt; display: inline;">권리주주 확정</span> </td>
              </tr>
              <tr>
               <td colspan="2" width="264" style="text-align: left;"> <span style="width: 264px; font-size: 10pt; display: inline;">4. 이사회결의일(결정일)</span> </td>
               <td colspan="2" width="336" style="text-align: left;"> <span class="xforms_input" style="width: 336px; font-size: 10pt; display: inline;">2023-11-13</span> </td>
              </tr>
              <tr>
               <td rowspan="2" width="171" style="text-align: left;"> <span style="width: 171px; font-size: 10pt; display: inline;">- 사외이사 참석여부</span> </td>
               <td width="93" style="text-align: left;"> <span style="width: 93px; font-size: 10pt; text-align: center; display: inline;">참석(명)</span> </td>
               <td colspan="2" width="336" style="text-align: left;"> <span class="xforms_input" style="width: 336px; font-size: 10pt; text-align: right; display: inline;">4</span> </td>
              </tr>
              <tr>
               <td width="93" style="text-align: left;"> <span style="width: 93px; font-size: 10pt; text-align: center; display: inline;">불참(명)</span> </td>
               <td colspan="2" width="336" style="text-align: left;"> <span class="xforms_input" style="width: 336px; font-size: 10pt; text-align: right; display: inline;">-</span> </td>
              </tr>
              <tr>
               <td colspan="2" width="264" style="text-align: left;"> <span style="width: 264px; font-size: 10pt; display: inline;">- 감사(사외이사가 아닌 감사위원) 참석여부</span> </td>
               <td colspan="2" width="336" style="text-align: left;"> <span class="xforms_input" style="width: 336px; font-size: 10pt; display: inline;">-</span> </td>
              </tr>
              <tr>
               <td colspan="2" rowspan="2" width="264" style="text-align: left;"> <span style="width: 264px; font-size: 10pt; display: inline;">5. 기타 투자판단과 관련한 중요사항</span> </td>
               <td colspan="2" width="336" style="text-align: left;"> <span class="xforms_input" style="width: 336px; font-size: 10pt; display: inline;">- 상기 사항은 2023년 중간배당 관련 내용으로 배당실시 여부 및 배당금액은 추후 개최될 이사회에서 논의하여 결정할 예정입니다. <br xmlns:java="http://xml.apache.org/xalan/java"> <br xmlns:java="http://xml.apache.org/xalan/java">- 본 공시사항은 자회사인 하이투자증권이 대주주인 DGB금융지주를 포함한 하이투자증권의 주주에 &nbsp;대해 배당하는 것과 관련된 내용입니다. <br xmlns:java="http://xml.apache.org/xalan/java"> <br xmlns:java="http://xml.apache.org/xalan/java">※ 자회사의 주요경영사항에 관한 공시 <br xmlns:java="http://xml.apache.org/xalan/java">- 자회사명 : 하이투자증권 <br xmlns:java="http://xml.apache.org/xalan/java">- 자산총액비중 : 13.14% <br xmlns:java="http://xml.apache.org/xalan/java">
                 <!--?javax.xml.transform.disable-output-escaping?-->&nbsp;
                 <!--?javax.xml.transform.enable-output-escaping?-->&nbsp;(2022.12.31 기준)</span> </td>
              </tr>
              <tr>
               <td width="112" style="text-align: left;"> <span style="width: 112px; font-size: 10pt; display: inline;">※ 관련공시</span> </td>
               <td width="224" style="text-align: left;"> <span class="xforms_input" style="width: 224px; font-size: 10pt; display: inline;">-</span> </td>
              </tr>
             </tbody>
            </table>
            """

        soup = BeautifulSoup(html_doc, "html.parser")
        table = soup.find("table")
        parsed_table = parse_html_table(table, 4)

        assert parsed_table is not None
        assert len(parsed_table) == 11
        # pprint(parsed_table)

    def test_parse_dividend_decision(self):
        html_doc = """
    	<table border="1" bordercolordark="white" bordercolorlight="#666666" cellpadding="1" cellspacing="0" id="XFormD1_Form0_Table0" style="margin:0px 0px 20px 0px;width:594px;font-size:10pt;border:1px solid #7f7f7f;">
         <tbody>
          <tr>
           <td colspan="2" width="242" style="text-align: left;"> <span style="width: 242px; font-size: 10pt; display: inline;">1. 배당구분</span> </td>
           <td colspan="2" width="352" style="text-align: left;"> <span class="xforms_input" style="width: 352px; font-size: 10pt; display: inline;">분기배당</span> </td>
          </tr>
          <tr>
           <td colspan="2" width="242" style="text-align: left;"> <span style="width: 242px; font-size: 10pt; display: inline;">2. 배당종류</span> </td>
           <td colspan="2" width="352" style="text-align: left;"> <span class="xforms_input" style="width: 352px; font-size: 10pt; display: inline;">현금배당</span> </td>
          </tr>
          <tr>
           <td colspan="2" width="242" style="text-align: left;"> <span style="width: 242px; font-size: 10pt; display: inline;">- 현물자산의 상세내역</span> </td>
           <td colspan="2" width="352" style="text-align: left;"> <span class="xforms_input" style="width: 352px; font-size: 10pt; display: inline;">-</span> </td>
          </tr>
          <tr>
           <td rowspan="2" width="165" style="text-align: left;"> <span style="width: 165px; font-size: 10pt; display: inline;">3. 1주당 배당금(원)</span> </td>
           <td width="77" style="text-align: left;"> <span style="width: 77px; font-size: 10pt; text-align: center; display: inline;">보통주식</span> </td>
           <td colspan="2" width="352" style="text-align: left;"> <span class="xforms_input" style="width: 352px; font-size: 10pt; text-align: right; display: inline;">340</span> </td>
          </tr>
          <tr>
           <td width="77" style="text-align: left;"> <span style="width: 77px; font-size: 10pt; text-align: center; display: inline;">종류주식</span> </td>
           <td colspan="2" width="352" style="text-align: left;"> <span class="xforms_input" style="width: 352px; font-size: 10pt; text-align: right; display: inline;">-</span> </td>
          </tr>
          <tr>
           <td colspan="2" width="242" style="text-align: left;"> <span style="width: 242px; font-size: 10pt; display: inline;">- 차등배당 여부</span> </td>
           <td colspan="2" width="352" style="text-align: left;"> <span class="xforms_input" style="width: 352px; font-size: 10pt; display: inline;">미해당</span> </td>
          </tr>
          <tr>
           <td rowspan="2" width="165" style="text-align: left;"> <span style="width: 165px; font-size: 10pt; display: inline;">4. 시가배당율(%)</span> </td>
           <td width="77" style="text-align: left;"> <span style="width: 77px; font-size: 10pt; text-align: center; display: inline;">보통주식</span> </td>
           <td colspan="2" width="352" style="text-align: left;"> <span class="xforms_input" style="width: 352px; font-size: 10pt; text-align: right; display: inline;">0.9</span> </td>
          </tr>
          <tr>
           <td width="77" style="text-align: left;"> <span style="width: 77px; font-size: 10pt; text-align: center; display: inline;">종류주식</span> </td>
           <td colspan="2" width="352" style="text-align: left;"> <span class="xforms_input" style="width: 352px; font-size: 10pt; text-align: right; display: inline;">-</span> </td>
          </tr>
          <tr>
           <td colspan="2" width="242" style="text-align: left;"> <span style="width: 242px; font-size: 10pt; display: inline;">5. 배당금총액(원)</span> </td>
           <td colspan="2" width="352" style="text-align: left;"> <span class="xforms_input" style="width: 352px; font-size: 10pt; text-align: right; display: inline;">20,432,585,260</span> </td>
          </tr>
          <tr>
           <td colspan="2" width="242" style="text-align: left;"> <span style="width: 242px; font-size: 10pt; display: inline;">6. 배당기준일</span> </td>
           <td colspan="2" width="352" style="text-align: left;"> <span class="xforms_input" style="width: 352px; font-size: 10pt; display: inline;">2023-09-30</span> </td>
          </tr>
          <tr>
           <td colspan="2" width="242" style="text-align: left;"> <span style="width: 242px; font-size: 10pt; display: inline;">7. 배당금지급 예정일자</span> </td>
           <td colspan="2" width="352" style="text-align: left;"> <span class="xforms_input" style="width: 352px; font-size: 10pt; display: inline;">-</span> </td>
          </tr>
          <tr>
           <td colspan="2" width="242" style="text-align: left;"> <span style="width: 242px; font-size: 10pt; display: inline;">8. 주주총회 개최여부</span> </td>
           <td colspan="2" width="352" style="text-align: left;"> <span class="xforms_input" style="width: 352px; font-size: 10pt; display: inline;">미개최</span> </td>
          </tr>
          <tr>
           <td colspan="2" width="242" style="text-align: left;"> <span style="width: 242px; font-size: 10pt; display: inline;">9. 주주총회 예정일자</span> </td>
           <td colspan="2" width="352" style="text-align: left;"> <span class="xforms_input" style="width: 352px; font-size: 10pt; display: inline;">-</span> </td>
          </tr>
          <tr>
           <td colspan="2" width="242" style="text-align: left;"> <span style="width: 242px; font-size: 10pt; display: inline;">10. 이사회결의일(결정일)</span> </td>
           <td colspan="2" width="352" style="text-align: left;"> <span class="xforms_input" style="width: 352px; font-size: 10pt; display: inline;">2023-11-14</span> </td>
          </tr>
          <tr>
           <td rowspan="2" width="165" style="text-align: left;"> <span style="width: 165px; font-size: 10pt; display: inline;">- 사외이사 참석여부</span> </td>
           <td width="77" style="text-align: left;"> <span style="width: 77px; font-size: 10pt; text-align: center; display: inline;">참석(명)</span> </td>
           <td colspan="2" width="352" style="text-align: left;"> <span class="xforms_input" style="width: 352px; font-size: 10pt; text-align: right; display: inline;">2</span> </td>
          </tr>
          <tr>
           <td width="77" style="text-align: left;"> <span style="width: 77px; font-size: 10pt; text-align: center; display: inline;">불참(명)</span> </td>
           <td colspan="2" width="352" style="text-align: left;"> <span class="xforms_input" style="width: 352px; font-size: 10pt; text-align: right; display: inline;">1</span> </td>
          </tr>
          <tr>
           <td colspan="2" width="242" style="text-align: left;"> <span style="width: 242px; font-size: 10pt; display: inline;">- 감사(사외이사가 아닌 감사위원) 참석여부</span> </td>
           <td colspan="2" width="352" style="text-align: left;"> <span class="xforms_input" style="width: 352px; font-size: 10pt; display: inline;">참석</span> </td>
          </tr>
          <tr>
           <td colspan="4" width="594" style="text-align: left;"> <span style="width: 594px; font-size: 10pt; display: inline;">11. 기타 투자판단과 관련한 중요사항</span> </td>
          </tr>
          <tr>
           <td colspan="4" width="594" style="text-align: left;"> <span class="xforms_input" style="width: 594px; font-size: 10pt; display: inline;">- 상기 '4. 시가배당율(%)' 의 기준이 되는 금액은 주주명부 폐쇄일 2매매거래일 전부터 <br xmlns:java="http://xml.apache.org/xalan/java">
             <!--?javax.xml.transform.disable-output-escaping?-->&nbsp;
             <!--?javax.xml.transform.enable-output-escaping?-->&nbsp; 과거 1주일간의 종가의 산술평균에 대한 주당배당금임. <br xmlns:java="http://xml.apache.org/xalan/java">
             <!--?javax.xml.transform.disable-output-escaping?-->&nbsp;
             <!--?javax.xml.transform.enable-output-escaping?-->&nbsp; [시가배당기준 산술평균 종가: 보통주 39,730원] <br xmlns:java="http://xml.apache.org/xalan/java"> <br xmlns:java="http://xml.apache.org/xalan/java">- 상기 '7. 배당금지급 예정일자' 는 자본시장법 제165조의12에 의거하여 <br xmlns:java="http://xml.apache.org/xalan/java">
             <!--?javax.xml.transform.disable-output-escaping?-->&nbsp;
             <!--?javax.xml.transform.enable-output-escaping?-->&nbsp; 이사회 결의일로부터 20일 이내 지급 예정임.</span> </td>
          </tr>
          <tr>
           <td width="165" style="text-align: left;"> <span style="width: 165px; font-size: 10pt; display: inline;">※ 관련공시</span> </td>
           <td colspan="3" width="429" style="text-align: left;"> <span style="width: 429px; font-size: 10pt; display: inline;"> <a href="/dsaf001/main.do?rcpNo=20231016800370" onclick="window.open('/dsaf001/main.do?rcpNo=20231016800370','r_20231016800370','width=1200,height=820,resizable=yes'); return false;">2023-10-16 현금ㆍ현물배당을 위한 주주명부폐쇄(기준일) 결정(자회사의 주요경영사항)</a> <br xmlns:java="http://xml.apache.org/xalan/java"> </span> </td>
          </tr>
         </tbody>
        </table>
    		"""

        soup = BeautifulSoup(html_doc, "html.parser")
        table = soup.find("table")
        parsed_table = parse_html_table(table, 4)

        assert parsed_table is not None
        assert len(parsed_table) == 20
        # pprint(parsed_table)

    def test_parsed_preliminary(self):
        html_doc = """
            <table border="1" bordercolordark="white" bordercolorlight="#666666" cellpadding="1" cellspacing="0" id="XFormD1_Form0_RepeatTable0" style="margin:0px 0px 20px 0px;width:602px;font-size:10pt;border:1px solid #7f7f7f;">
         <tbody>
          <tr>
           <td colspan="7" width="602" style="text-align: left;"> <span style="width: 602px; font-size: 10pt; display: inline;">※ 동 정보는 잠정치로서 향후 확정치와는 다를 수 있음.</span> </td>
          </tr>
          <tr>
           <td colspan="4" width="330" style="text-align: left;"> <span style="width: 330px; font-size: 10pt; display: inline;">1. 연결실적내용</span> </td>
           <td colspan="3" width="272" style="text-align: left;"> <span class="xforms_input" style="width: 272px; font-size: 10pt; text-align: right; display: inline;">단위 : 백만원, %</span> </td>
          </tr>
          <tr>
           <td colspan="2" rowspan="2" width="158" style="text-align: left;"> <span style="width: 158px; font-size: 10pt; text-align: center; display: inline;">구분</span> </td>
           <td width="87" style="text-align: left;"> <span style="width: 87px; font-size: 10pt; text-align: center; display: inline;">당기실적</span> </td>
           <td width="85" style="text-align: left;"> <span style="width: 85px; font-size: 10pt; text-align: center; display: inline;">전기실적</span> </td>
           <td rowspan="2" width="94" style="text-align: left;"> <span style="width: 94px; font-size: 10pt; text-align: center; display: inline;">전기대비증감율(%)</span> </td>
           <td width="92" style="text-align: left;"> <span style="width: 92px; font-size: 10pt; text-align: center; display: inline;">전년동기실적</span> </td>
           <td rowspan="2" width="86" style="text-align: left;"> <span style="width: 86px; font-size: 10pt; text-align: center; display: inline;">전년동기대비증감율(%)</span> </td>
          </tr>
          <tr>
           <td width="87" style="text-align: left;"> <span class="xforms_input" style="width: 87px; font-size: 10pt; text-align: center; display: inline;">('23.3Q)</span> </td>
           <td width="85" style="text-align: left;"> <span class="xforms_input" style="width: 85px; font-size: 10pt; text-align: center; display: inline;">('23.2Q)</span> </td>
           <td width="92" style="text-align: left;"> <span class="xforms_input" style="width: 92px; font-size: 10pt; text-align: center; display: inline;">('22.3Q)</span> </td>
          </tr>
          <tr>
           <td rowspan="2" width="86" style="text-align: left;"> <span style="width: 86px; font-size: 10pt; text-align: center; display: inline;">매출액</span> </td>
           <td width="72" style="text-align: left;"> <span style="width: 72px; font-size: 10pt; text-align: center; display: inline;">당해실적</span> </td>
           <td width="87" style="text-align: left;"> <span class="xforms_input" style="width: 87px; font-size: 10pt; text-align: right; display: inline;">12,511</span> </td>
           <td width="85" style="text-align: left;"> <span class="xforms_input" style="width: 85px; font-size: 10pt; text-align: right; display: inline;">13,095</span> </td>
           <td width="94" style="text-align: left;"> <span class="xforms_input" style="width: 94px; font-size: 10pt; text-align: right; display: inline;">-4.5</span> </td>
           <td width="92" style="text-align: left;"> <span class="xforms_input" style="width: 92px; font-size: 10pt; text-align: right; display: inline;">8,021</span> </td>
           <td width="86" style="text-align: left;"> <span class="xforms_input" style="width: 86px; font-size: 10pt; text-align: right; display: inline;">56.0</span> </td>
          </tr>
          <tr>
           <td width="72" style="text-align: left;"> <span style="width: 72px; font-size: 10pt; text-align: center; display: inline;">누계실적</span> </td>
           <td width="87" style="text-align: left;"> <span class="xforms_input" style="width: 87px; font-size: 10pt; text-align: right; display: inline;">36,162</span> </td>
           <td width="85" style="text-align: left;"> <span class="xforms_input" style="width: 85px; font-size: 10pt; text-align: right; display: inline;">23,652</span> </td>
           <td width="94" style="text-align: left;"> <span class="xforms_input" style="width: 94px; font-size: 10pt; text-align: right; display: inline;">52.9</span> </td>
           <td width="92" style="text-align: left;"> <span class="xforms_input" style="width: 92px; font-size: 10pt; text-align: right; display: inline;">30,773</span> </td>
           <td width="86" style="text-align: left;"> <span class="xforms_input" style="width: 86px; font-size: 10pt; text-align: right; display: inline;">17.5</span> </td>
          </tr>
          <tr>
           <td rowspan="2" width="86" style="text-align: left;"> <span style="width: 86px; font-size: 10pt; text-align: center; display: inline;">영업이익</span> </td>
           <td width="72" style="text-align: left;"> <span style="width: 72px; font-size: 10pt; text-align: center; display: inline;">당해실적</span> </td>
           <td width="87" style="text-align: left;"> <span class="xforms_input" style="width: 87px; font-size: 10pt; text-align: right; display: inline;">-6,137</span> </td>
           <td width="85" style="text-align: left;"> <span class="xforms_input" style="width: 85px; font-size: 10pt; text-align: right; display: inline;">-5,409</span> </td>
           <td width="94" style="text-align: left;"> <span class="xforms_input" style="width: 94px; font-size: 10pt; text-align: right; display: inline;">-13.5</span> </td>
           <td width="92" style="text-align: left;"> <span class="xforms_input" style="width: 92px; font-size: 10pt; text-align: right; display: inline;">-4,393</span> </td>
           <td width="86" style="text-align: left;"> <span class="xforms_input" style="width: 86px; font-size: 10pt; text-align: right; display: inline;">-39.7</span> </td>
          </tr>
          <tr>
           <td width="72" style="text-align: left;"> <span style="width: 72px; font-size: 10pt; text-align: center; display: inline;">누계실적</span> </td>
           <td width="87" style="text-align: left;"> <span class="xforms_input" style="width: 87px; font-size: 10pt; text-align: right; display: inline;">-16,070</span> </td>
           <td width="85" style="text-align: left;"> <span class="xforms_input" style="width: 85px; font-size: 10pt; text-align: right; display: inline;">-9,932</span> </td>
           <td width="94" style="text-align: left;"> <span class="xforms_input" style="width: 94px; font-size: 10pt; text-align: right; display: inline;">-61.8</span> </td>
           <td width="92" style="text-align: left;"> <span class="xforms_input" style="width: 92px; font-size: 10pt; text-align: right; display: inline;">-10,449</span> </td>
           <td width="86" style="text-align: left;"> <span class="xforms_input" style="width: 86px; font-size: 10pt; text-align: right; display: inline;">-53.8</span> </td>
          </tr>
          <tr>
           <td rowspan="2" width="86" style="text-align: left;"> <span style="width: 86px; font-size: 10pt; text-align: center; display: inline;">법인세비용차감전계속사업이익</span> </td>
           <td width="72" style="text-align: left;"> <span style="width: 72px; font-size: 10pt; text-align: center; display: inline;">당해실적</span> </td>
           <td width="87" style="text-align: left;"> <span class="xforms_input" style="width: 87px; font-size: 10pt; text-align: right; display: inline;">-6,456</span> </td>
           <td width="85" style="text-align: left;"> <span class="xforms_input" style="width: 85px; font-size: 10pt; text-align: right; display: inline;">-4,758</span> </td>
           <td width="94" style="text-align: left;"> <span class="xforms_input" style="width: 94px; font-size: 10pt; text-align: right; display: inline;">-35.7</span> </td>
           <td width="92" style="text-align: left;"> <span class="xforms_input" style="width: 92px; font-size: 10pt; text-align: right; display: inline;">-3,119</span> </td>
           <td width="86" style="text-align: left;"> <span class="xforms_input" style="width: 86px; font-size: 10pt; text-align: right; display: inline;">-107.0</span> </td>
          </tr>
          <tr>
           <td width="72" style="text-align: left;"> <span style="width: 72px; font-size: 10pt; text-align: center; display: inline;">누계실적</span> </td>
           <td width="87" style="text-align: left;"> <span class="xforms_input" style="width: 87px; font-size: 10pt; text-align: right; display: inline;">-15,790</span> </td>
           <td width="85" style="text-align: left;"> <span class="xforms_input" style="width: 85px; font-size: 10pt; text-align: right; display: inline;">-9,333</span> </td>
           <td width="94" style="text-align: left;"> <span class="xforms_input" style="width: 94px; font-size: 10pt; text-align: right; display: inline;">-69.2</span> </td>
           <td width="92" style="text-align: left;"> <span class="xforms_input" style="width: 92px; font-size: 10pt; text-align: right; display: inline;">-9,428</span> </td>
           <td width="86" style="text-align: left;"> <span class="xforms_input" style="width: 86px; font-size: 10pt; text-align: right; display: inline;">-67.5</span> </td>
          </tr>
          <tr>
           <td rowspan="2" width="86" style="text-align: left;"> <span style="width: 86px; font-size: 10pt; text-align: center; display: inline;">당기순이익</span> </td>
           <td width="72" style="text-align: left;"> <span style="width: 72px; font-size: 10pt; text-align: center; display: inline;">당해실적</span> </td>
           <td width="87" style="text-align: left;"> <span class="xforms_input" style="width: 87px; font-size: 10pt; text-align: right; display: inline;">-6,456</span> </td>
           <td width="85" style="text-align: left;"> <span class="xforms_input" style="width: 85px; font-size: 10pt; text-align: right; display: inline;">-4,758</span> </td>
           <td width="94" style="text-align: left;"> <span class="xforms_input" style="width: 94px; font-size: 10pt; text-align: right; display: inline;">-35.7</span> </td>
           <td width="92" style="text-align: left;"> <span class="xforms_input" style="width: 92px; font-size: 10pt; text-align: right; display: inline;">-3,119</span> </td>
           <td width="86" style="text-align: left;"> <span class="xforms_input" style="width: 86px; font-size: 10pt; text-align: right; display: inline;">-107.0</span> </td>
          </tr>
          <tr>
           <td width="72" style="text-align: left;"> <span style="width: 72px; font-size: 10pt; text-align: center; display: inline;">누계실적</span> </td>
           <td width="87" style="text-align: left;"> <span class="xforms_input" style="width: 87px; font-size: 10pt; text-align: right; display: inline;">-15,790</span> </td>
           <td width="85" style="text-align: left;"> <span class="xforms_input" style="width: 85px; font-size: 10pt; text-align: right; display: inline;">-9,333</span> </td>
           <td width="94" style="text-align: left;"> <span class="xforms_input" style="width: 94px; font-size: 10pt; text-align: right; display: inline;">-69.2</span> </td>
           <td width="92" style="text-align: left;"> <span class="xforms_input" style="width: 92px; font-size: 10pt; text-align: right; display: inline;">-9,428</span> </td>
           <td width="86" style="text-align: left;"> <span class="xforms_input" style="width: 86px; font-size: 10pt; text-align: right; display: inline;">-67.5</span> </td>
          </tr>
          <tr>
           <td rowspan="2" width="86" style="text-align: left;"> <span style="width: 86px; font-size: 10pt; text-align: center; display: inline;">지배기업 소유주지분 순이익</span> </td>
           <td width="72" style="text-align: left;"> <span style="width: 72px; font-size: 10pt; text-align: center; display: inline;">당해실적</span> </td>
           <td width="87" style="text-align: left;"> <span class="xforms_input" style="width: 87px; font-size: 10pt; text-align: right; display: inline;">-6,456</span> </td>
           <td width="85" style="text-align: left;"> <span class="xforms_input" style="width: 85px; font-size: 10pt; text-align: right; display: inline;">-4,758</span> </td>
           <td width="94" style="text-align: left;"> <span class="xforms_input" style="width: 94px; font-size: 10pt; text-align: right; display: inline;">-35.7</span> </td>
           <td width="92" style="text-align: left;"> <span class="xforms_input" style="width: 92px; font-size: 10pt; text-align: right; display: inline;">-3,119</span> </td>
           <td width="86" style="text-align: left;"> <span class="xforms_input" style="width: 86px; font-size: 10pt; text-align: right; display: inline;">-107.0</span> </td>
          </tr>
          <tr>
           <td width="72" style="text-align: left;"> <span style="width: 72px; font-size: 10pt; text-align: center; display: inline;">누계실적</span> </td>
           <td width="87" style="text-align: left;"> <span class="xforms_input" style="width: 87px; font-size: 10pt; text-align: right; display: inline;">-15,790</span> </td>
           <td width="85" style="text-align: left;"> <span class="xforms_input" style="width: 85px; font-size: 10pt; text-align: right; display: inline;">-9,333</span> </td>
           <td width="94" style="text-align: left;"> <span class="xforms_input" style="width: 94px; font-size: 10pt; text-align: right; display: inline;">-69.2</span> </td>
           <td width="92" style="text-align: left;"> <span class="xforms_input" style="width: 92px; font-size: 10pt; text-align: right; display: inline;">-9,428</span> </td>
           <td width="86" style="text-align: left;"> <span class="xforms_input" style="width: 86px; font-size: 10pt; text-align: right; display: inline;">-67.5</span> </td>
          </tr>
          <tr>
           <td colspan="2" width="158" style="text-align: left;"> <span class="xforms_input" style="width: 158px; font-size: 10pt; display: inline;">-</span> </td>
           <td width="87" style="text-align: left;"> <span class="xforms_input" style="width: 87px; font-size: 10pt; text-align: right; display: inline;">-</span> </td>
           <td width="85" style="text-align: left;"> <span class="xforms_input" style="width: 85px; font-size: 10pt; text-align: right; display: inline;">-</span> </td>
           <td width="94" style="text-align: left;"> <span class="xforms_input" style="width: 94px; font-size: 10pt; text-align: right; display: inline;">-</span> </td>
           <td width="92" style="text-align: left;"> <span class="xforms_input" style="width: 92px; font-size: 10pt; text-align: right; display: inline;">-</span> </td>
           <td width="86" style="text-align: left;"> <span class="xforms_input" style="width: 86px; font-size: 10pt; text-align: right; display: inline;">-</span> </td>
          </tr>
          <tr>
           <td colspan="2" rowspan="4" width="158" style="text-align: left;"> <span style="width: 158px; font-size: 10pt; display: inline;">2. 정보제공내역</span> </td>
           <td colspan="2" width="172" style="text-align: left;"> <span style="width: 172px; font-size: 10pt; display: inline;">정보제공자</span> </td>
           <td colspan="3" width="272" style="text-align: left;"> <span class="xforms_input" style="width: 272px; font-size: 10pt; display: inline;">두산로보틱스 IR팀</span> </td>
          </tr>
          <tr>
           <td colspan="2" width="172" style="text-align: left;"> <span style="width: 172px; font-size: 10pt; display: inline;">정보제공대상자</span> </td>
           <td colspan="3" width="272" style="text-align: left;"> <span class="xforms_input" style="width: 272px; font-size: 10pt; display: inline;">국내외 기관투자자, 애널리스트, 일반투자자 및 언론기관 등</span> </td>
          </tr>
          <tr>
           <td colspan="2" width="172" style="text-align: left;"> <span style="width: 172px; font-size: 10pt; display: inline;">정보제공(예정)일시</span> </td>
           <td colspan="3" width="272" style="text-align: left;"> <span class="xforms_input" style="width: 272px; font-size: 10pt; display: inline;">공정공시 후 수시 제공</span> </td>
          </tr>
          <tr>
           <td colspan="2" width="172" style="text-align: left;"> <span style="width: 172px; font-size: 10pt; display: inline;">행사명(장소)</span> </td>
           <td colspan="3" width="272" style="text-align: left;"> <span class="xforms_input" style="width: 272px; font-size: 10pt; display: inline;">-</span> </td>
          </tr>
          <tr>
           <td colspan="4" width="330" style="text-align: left;"> <span style="width: 330px; font-size: 10pt; display: inline;">3. 연락처(관련부서/전화번호)</span> </td>
           <td colspan="3" width="272" style="text-align: left;"> <span class="xforms_input" style="width: 272px; font-size: 10pt; display: inline;">IR팀/ 031-5179-4777</span> </td>
          </tr>
          <tr>
           <td colspan="7" width="602" style="text-align: left;"> <span style="width: 602px; font-size: 10pt; display: inline;">4. 기타 투자판단과 관련한 중요사항</span> </td>
          </tr>
          <tr>
           <td colspan="7" width="602" style="text-align: left;"> <span class="xforms_input" style="width: 602px; font-size: 10pt; display: inline;">- 상기 실적은 한국채택국제회계기준(K-IFRS)에 따라 작성된 연결재무제표 기준 잠정 영업실적입니다. <br xmlns:java="http://xml.apache.org/xalan/java"> <br xmlns:java="http://xml.apache.org/xalan/java">- 상기 실적은 외부감사인의 회계검토가 완료되지 않은 상태에서 작성된 잠정 실적으로, 향후 외부감사인의 감사결과 등에 따라 변경될 수 있습니다. <br xmlns:java="http://xml.apache.org/xalan/java"> <br xmlns:java="http://xml.apache.org/xalan/java">- 상기 자료는 요약 내용이며 상세 내용은 당사 홈페이지(www.doosanrobotics.com)의 투자정보에 게시할 예정입니다.</span> </td>
          </tr>
          <tr>
           <td colspan="2" width="158" style="text-align: left;"> <span style="width: 158px; font-size: 10pt; display: inline;">※ 관련공시</span> </td>
           <td colspan="5" width="444" style="text-align: left;"> <span style="width: 444px; font-size: 10pt; display: inline;"> <a href="/dsaf001/main.do?rcpNo=20231108800561" onclick="window.open('/dsaf001/main.do?rcpNo=20231108800561','r_20231108800561','width=1200,height=820,resizable=yes'); return false;">2023-11-08 결산실적공시 예고(안내공시)</a> <br xmlns:java="http://xml.apache.org/xalan/java"> </span> </td>
          </tr>
         </tbody>
        </table>
            """

        soup = BeautifulSoup(html_doc, "html.parser")
        table = soup.find("table")

        parsed_table = parse_html_table(table, 7)

        assert parsed_table is not None
        assert len(parsed_table) == 23
        # pprint(parsed_table)

    def test_parse_closing_shareholders(self):
        """
        주주명부 폐쇄 기준일 리포트 스크랩 & 파싱 테스트
        """
        data = self.dividend_parser.parse_closing_shareholders("20230615800239")

        assert data is not None
        assert data.start_date == "2023-07-01"
        assert data.end_date == "2023-07-10"
        assert data.base_date == "2023-06-30"

    def test_parse_decision_on_cash1(self):
        """
        현금ㆍ현물배당결정 스크랩 & 파싱 테스트
        """

        # 기재정정 공시
        data = self.dividend_parser.parse_decision_on_cash("20230802800569")

        assert data is not None
        assert data.dividend_classification == "분기배당"
        assert data.dividend_kind == "현금배당"
        assert data.dividend_amount == 415
        assert data.dividend_rate == 0.2
        assert data.dividend_date == "2023-06-30"
        assert data.total_dividend_amount == 62397685220

    def test_parse_decision_on_cash2(self):
        """
        현금ㆍ현물배당결정 스크랩 & 파싱 테스트
        """

        # 기재정정 공시
        data = self.dividend_parser.parse_decision_on_cash("20240119800544")

        assert data is not None
        assert data.dividend_classification == "결산배당"
        assert data.dividend_kind == "현금배당"
        assert data.dividend_amount == 500
        assert data.dividend_rate == 0.3
        assert data.dividend_date == "2023-12-31"
        assert data.total_dividend_amount == 103603075500

    def test_parse_decision_on_cash3(self):
        """
        현금ㆍ현물배당결정 스크랩 & 파싱 테스트
        """

        # 우선주 표시되는 공시
        data = self.dividend_parser.parse_decision_on_cash("20231219800337")

        assert data is not None
        assert data.dividend_classification == "결산배당"
        assert data.dividend_kind == "현금배당"
        assert data.dividend_amount == 200
        assert data.dividend_rate == 0.0
        assert data.dividend_date == "2023-12-31"
        assert data.total_dividend_amount == 20013639150

    def test_parse_preliminary_estimate(self):
        """
        영업(잠정)실적(공정공시) 페이지 파싱 테스트
        """

        preliminary_parser = self.dart_scrap.preliminary_parser
        data = preliminary_parser.parse_preliminary_estimate("20240119900515")

        assert data is not None

        assert data.revenue_current_quarter == 44046
        assert data.op_qoq == "+9,249(+240.92)"
        assert data.net_income_yoy == "흑자전환"

    def test_parse_preliminary_estimate1(self):
        """
        영업(잠정)실적(공정공시), 매출액은 없고 수주 정보만 있는 페이지 파싱 테스트
        """
        preliminary_parser = self.dart_scrap.preliminary_parser
        data = preliminary_parser.parse_preliminary_estimate("20240118800214")

        assert data is not None
        assert len(data.etc_info) == 4
        assert data.etc_info[1][0] == "조선"
        assert data.etc_info[2][0] == "해양·플랜트"
        assert data.etc_info[2][2] == "1,285"
        assert data.etc_info[3][0] == "엔진기계"

    def test_parse_preliminary_estimate2(self):
        """
        영업(잠정)실적(공정공시), 매출액과 총 매출이 있는 페이지 파싱 테스트
        """
        preliminary_parser = self.dart_scrap.preliminary_parser
        data = preliminary_parser.parse_preliminary_estimate("20240110800127")

        assert data is not None
        assert len(data.etc_info) == 5
        assert data.etc_info[0][0] == "총매출액"
        assert data.etc_info[1][0] == "(할 \xa0인 \xa0점)"
        assert data.etc_info[2][0] == "(트레이더스)"
        assert data.etc_info[2][2] == "3,010"
        assert data.etc_info[2][3] == "2,514"
        assert data.etc_info[3][0] == "(전 \xa0문 \xa0점)"
        assert data.etc_info[4][0] == "(기 \xa0 \xa0 \xa0타)"

    def test_parse_revenue_volatility(self):
        """
        매출액 또는 손익30%(대규모법인은15%)이상 변경 공시 페이지 파싱 테스트
        """
        revenue_volatility = self.dart_scrap.revenue_volatility_parser
        data = revenue_volatility.parse_revenue_volatility("20240126900525")

        assert data is not None
        assert data.fs_kind == "개별"
        assert data.current_revenue == 8789087326
        assert data.previous_revenue == 7644000304
        assert data.diff_revenue_amount == 1145087022
        assert data.diff_revenue_ratio == "15.0"

    def test_parse_revenue_volatility1(self):
        """
        매출액 또는 손익30%(대규모법인은15%)이상 변경 첫줄에 주석이 있는 공시 페이지 파싱 테스트
        """
        revenue_volatility = self.dart_scrap.revenue_volatility_parser
        data = revenue_volatility.parse_revenue_volatility("20240126800566")

        assert data is not None
        assert data.fs_kind == "연결"
        assert data.current_net_income == 85978496
        assert data.previous_net_income == -50164252
        assert data.diff_net_income_amount == 136142748
        assert data.diff_net_income_ratio == "흑자전환"

    def test_parse_facility_invest_parser(self):
        """
        신규시설투자 공시 페이지 파싱 테스트
        """
        facility_parser = self.dart_scrap.facility_invest_parser
        data = facility_parser.parse_facility_invest("20240112900165")

        assert data is not None
        assert data.invest_amount == 180000000000
        assert data.equity_amount == 111462878646
        assert data.equity_ratio == 161.5
        assert data.is_large_scale_corporation
        assert data.investment_purpose == "전구체 생산 Capacity 증설"
        assert data.investment_start_date == "2024-01-12"
        assert data.investment_end_date == "2025-03-31"
        assert data.investment_decision_date == "2024-01-12"
        assert data.investment_note is not None

    def test_parse_facility_invest_parser1(self):
        """
        [기재정정] 신규시설투자 공시 페이지 파싱 테스트
        """
        facility_parser = self.dart_scrap.facility_invest_parser
        data = facility_parser.parse_facility_invest("20240119900138")

        assert data is not None
        assert data.correction_publish_date == "2024-01-19"
        assert data.correction_submit_date == "2023-12-27"
        assert data.correction_cause == "투자금액 증액"
        assert (
            data.correction_cause_detail == "▶투자금액 증액사유 - 설계변경에 따른 증액"
        )
        assert data.correction_note1[1] == "8,358,000,000"
        assert data.correction_note2[1] == "19.48"

        assert data.invest_amount == 8908000000
        assert data.equity_amount == 42901898234
        assert data.equity_ratio == 20.76
        assert not data.is_large_scale_corporation
        assert data.investment_purpose == "고객수요 증대 대응 위한 생산능력 확충"
        assert data.investment_start_date == "2022-09-07"
        assert data.investment_end_date == "2024-02-29"
        assert data.investment_decision_date == "2022-09-06"
        assert data.investment_note is not None

    def test_parse_facility_invest_parser2(self):
        """
        자회사 신규시설투자 공시 페이지 파싱 테스트
        """
        facility_parser = self.dart_scrap.facility_invest_parser
        data = facility_parser.parse_facility_invest("20231220800236")

        assert data is not None
        assert data.correction_publish_date is None
        assert data.correction_submit_date is None
        assert data.correction_cause is None
        assert data.correction_cause_detail is None

        assert data.invest_amount == 1753400000000
        assert data.equity_amount == 5936038726293
        assert data.equity_ratio == 29.54
        assert data.is_large_scale_corporation == True
        assert data.investment_purpose == "신규 수주 대응을 위한 시설 투자"
        assert data.investment_start_date == "2023-12-19"
        assert data.investment_end_date == "2025-12-31"
        assert data.investment_decision_date == "2023-12-19"

        assert data.investment_note is not None

    def test_parse_supply_agreement(self):
        """
        단일판매 공급계약 체결 공시 페이지 파싱 테스트
        """
        supply_agreement_parser = self.dart_scrap.supply_agreement_parser
        data = supply_agreement_parser.parse_supply_agreement("20240202800122")

        assert data is not None
        assert data.contract_amount == 86042000000
        assert data.revenue_ratio == 26.26
        assert data.contractual_partner == "SK하이닉스(SK Hynix Inc.)"
        assert data.contract_start_date == "2024-02-01"

    def test_parse_supply_agreement1(self):
        """
        [기재정정]단일판매 공급계약 체결 공시 페이지 파싱 테스트
        """
        supply_agreement_parser = self.dart_scrap.supply_agreement_parser
        data = supply_agreement_parser.parse_supply_agreement("20240202800919")

        assert data is not None
        assert data.correction_publish_date == "2024-02-02"
        assert (
            data.correction_cause
            == "주요 계약조건에 따른 2년차 연간 유지보수료 계약체결"
        )
        assert data.contract_name_detail == "차세대 전산 시스템 유지보수 계약"
        assert data.contract_amount == 23623887320
        assert data.revenue_ratio == 2.41
        assert data.contract_start_date == "2023-01-01"
        assert data.contract_end_date == "2025-12-31"

    def test_parse_supply_agreement2(self):
        """
        [기재정정]단일판매 공급계약 체결 공시 페이지 파싱 테스트
        """
        supply_agreement_parser = self.dart_scrap.supply_agreement_parser
        data = supply_agreement_parser.parse_supply_agreement("20240202800919")

        assert data is not None
        assert data.correction_publish_date == "2024-02-02"
        assert (
            data.correction_cause
            == "주요 계약조건에 따른 2년차 연간 유지보수료 계약체결"
        )
        assert data.contract_name_detail == "차세대 전산 시스템 유지보수 계약"
        assert data.contract_amount == 23623887320
        assert data.revenue_ratio == 2.41
        assert data.contract_start_date == "2023-01-01"
        assert data.contract_end_date == "2025-12-31"

    def test_parse_supply_agreement3(self):
        """
        [기재정정]단일판매 공급계약 체결 공시2 페이지 파싱 테스트
        """
        supply_agreement_parser = self.dart_scrap.supply_agreement_parser
        data = supply_agreement_parser.parse_supply_agreement("20240202900843")

        assert data is not None
        assert data.correction_publish_date == "2024-02-02"
        assert data.correction_cause == "계약기간 변경"
        assert data.contract_name == "부광초교 서측 주택재개발정비사업 건축설계 용역"
        assert data.contract_name_detail is None
        assert data.contract_amount == 3431890000
        assert data.recent_revenue == 155837235737
        assert data.revenue_ratio == 2.20
        assert data.contract_start_date == "2010-02-03"
        assert data.contract_end_date == "2026-02-02"
        assert data.contract_date == "2010-02-03"

    def test_parse_supply_agreement4(self):
        """
        [기재정정]단일판매 공급계약 체결 코넥스는 계약내역이 3개 파싱 테스트
        """
        supply_agreement_parser = self.dart_scrap.supply_agreement_parser
        data = supply_agreement_parser.parse_supply_agreement("20231220600643")

        assert data is not None
        assert data.correction_publish_date == "2023-12-20"
        assert data.correction_cause == "계약 금액 변경"
        assert data.contract_name == "2차전지 활성화장비 공급계약"
        assert data.contract_amount == 6520121361
        assert data.revenue_ratio == 210.76
        assert data.contract_start_date == "2022-08-09"
        assert data.contract_end_date == "2023-12-20"

    def test_parse_retirement1(self):
        """
        주식소각 결정 파싱 테스트
        """
        retirement_parser = self.dart_scrap.retirement_treasury_stock_parser
        data = retirement_parser.parse_retirement_treasury_stock("20230920800221")

        assert data is not None
        assert data.common_share_count == 1576903
        assert data.issued_common_share_count == 503859595
        assert data.retirement_amount == 8206157417
        assert data.acquisition_method == "기취득 자기주식"

    def test_parse_retirement2(self):
        """
        [기재정정]주식소각 결정 파싱 테스트
        """
        retirement_parser = self.dart_scrap.retirement_treasury_stock_parser
        data = retirement_parser.parse_retirement_treasury_stock("20230831800042")

        assert data is not None
        assert data.common_share_count == 2842929
        assert data.issued_common_share_count == 518347118
        assert data.retirement_amount == 100000051050
        assert data.acquisition_start_date_for_retirement == "2023-07-28"
        assert data.acquisition_end_date_for_retirement == "2023-08-31"
        assert data.acquisition_method == "장내매수"
        assert data.acquisition_broker == "신한투자증권"
