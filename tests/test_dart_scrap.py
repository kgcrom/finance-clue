from stock_clue.dart_scrap import DartScrap
from stock_clue.dart_scrap import parse_daily_disclosure


class TestDartScrap:
    def setup_class(self):
        self.dart_scrap = DartScrap()

    def test_get_kospi_daily_disclosure(self):
        data = self.dart_scrap.get_kospi_daily_disclosure("2023.11.14", 1)

        assert data is not None
        assert data.total == 963
        assert len(data.disclosures) == 100

    def test_get_kosdaq_daily_disclosure(self):
        data = self.dart_scrap.get_kosdaq_daily_disclosure("2023.11.14", 1)
        assert data is not None
        assert data.total == 1429
        assert len(data.disclosures) == 100

    def test_get_all_daily_disclosure(self):
        data = self.dart_scrap.get_all_daily_disclosure("2023.11.14", 1)
        assert data is not None
        assert data.total == 3109
        assert len(data.disclosures) == 100

    def test_parse_daily_disclosure(self):
        html_doc = """

<!--목록 -->
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
					
					
					
					
					
					
					
					
				
					
						
						
						
						
						
						
					
					
						
						
						
						
						
						
					
					
					
					
					
						<tr>
							<td>
								
								
								
								17:44
							</td>
							<td class="tL">
							    <span class="innerWrapTag">
							    	<span class="tagCom_kospi" title="유가증권시장" style="cursor:default">유</span>
									<a href="javascript:openCorpInfoNew('00111722', 'winCorpInfo', '/dsae001/selectPopup.ax');" title="미래에셋증권 기업개황 새창" >
										미래에셋증권
									</a>
								</span>
								<a href="http://ci.securities.miraeasset.com" target="new">
										<span class="tagCom_ir" title="기업 IR페이지 연결">IR</span>
									</a>
							</td>
							<td class="tL">
								<a href="/dsaf001/main.do?rcpNo=20231114002892"  onclick="openReportViewer('20231114002892'); return false;" id="r_20231114002892"
									title="일괄신고서(파생결합사채-주가연계파생결합사채) 공시뷰어 새창" ><span title="본 보고서명으로 이미 제출된 보고서의 기재내용이 변경되어 제출된 것임" class="txtCB">[기재정정]</span>일괄신고서(파생결합사채-주가연계파생결합사채)
									
		  					
								</a>
							</td>
							<td class="tL ellipsis" title="미래에셋증권">미래에셋증권</td>
							<td>2023.11.14</td>
							<td></td>
						</tr>
					
					
					
					
					
					
					
					
				
					
						
						
						
						
						
						
					
					
						
						
						
						
						
						
					
					
					
					
					
						<tr>
							<td>
								
								
								
								17:44
							</td>
							<td class="tL">
							    <span class="innerWrapTag">
							    	<span class="tagCom_kospi" title="유가증권시장" style="cursor:default">유</span>
									<a href="javascript:openCorpInfoNew('00111722', 'winCorpInfo', '/dsae001/selectPopup.ax');" title="미래에셋증권 기업개황 새창" >
										미래에셋증권
									</a>
								</span>
								<a href="http://ci.securities.miraeasset.com" target="new">
										<span class="tagCom_ir" title="기업 IR페이지 연결">IR</span>
									</a>
							</td>
							<td class="tL">
								<a href="/dsaf001/main.do?rcpNo=20231114002854"  onclick="openReportViewer('20231114002854'); return false;" id="r_20231114002854"
									title="일괄신고서(기타파생결합사채) 공시뷰어 새창" ><span title="본 보고서명으로 이미 제출된 보고서의 기재내용이 변경되어 제출된 것임" class="txtCB">[기재정정]</span>일괄신고서(기타파생결합사채)
									
		  					
								</a>
							</td>
							<td class="tL ellipsis" title="미래에셋증권">미래에셋증권</td>
							<td>2023.11.14</td>
							<td></td>
						</tr>
					
					
					
					
					
					
					
					
				
					
						
						
						
						
						
						
					
					
						
						
						
						
						
						
					
					
					
					
					
						<tr>
							<td>
								
								
								
								17:44
							</td>
							<td class="tL">
							    <span class="innerWrapTag">
							    	<span class="tagCom_kospi" title="유가증권시장" style="cursor:default">유</span>
									<a href="javascript:openCorpInfoNew('00111722', 'winCorpInfo', '/dsae001/selectPopup.ax');" title="미래에셋증권 기업개황 새창" >
										미래에셋증권
									</a>
								</span>
								<a href="http://ci.securities.miraeasset.com" target="new">
										<span class="tagCom_ir" title="기업 IR페이지 연결">IR</span>
									</a>
							</td>
							<td class="tL">
								<a href="/dsaf001/main.do?rcpNo=20231114002816"  onclick="openReportViewer('20231114002816'); return false;" id="r_20231114002816"
									title="일괄신고서(기타파생결합증권) 공시뷰어 새창" ><span title="본 보고서명으로 이미 제출된 보고서의 기재내용이 변경되어 제출된 것임" class="txtCB">[기재정정]</span>일괄신고서(기타파생결합증권)
									
		  					
								</a>
							</td>
							<td class="tL ellipsis" title="미래에셋증권">미래에셋증권</td>
							<td>2023.11.14</td>
							<td></td>
						</tr>
					
					
					
					
					
					
					
					
				
					
						
						
						
						
						
						
					
					
						
						
						
						
						
						
					
					
					
					
					
						<tr>
							<td>
								
								
								
								17:44
							</td>
							<td class="tL">
							    <span class="innerWrapTag">
							    	<span class="tagCom_kospi" title="유가증권시장" style="cursor:default">유</span>
									<a href="javascript:openCorpInfoNew('00111722', 'winCorpInfo', '/dsae001/selectPopup.ax');" title="미래에셋증권 기업개황 새창" >
										미래에셋증권
									</a>
								</span>
								<a href="http://ci.securities.miraeasset.com" target="new">
										<span class="tagCom_ir" title="기업 IR페이지 연결">IR</span>
									</a>
							</td>
							<td class="tL">
								<a href="/dsaf001/main.do?rcpNo=20231114002780"  onclick="openReportViewer('20231114002780'); return false;" id="r_20231114002780"
									title="일괄신고서(파생결합증권-주식워런트증권) 공시뷰어 새창" ><span title="본 보고서명으로 이미 제출된 보고서의 기재내용이 변경되어 제출된 것임" class="txtCB">[기재정정]</span>일괄신고서(파생결합증권-주식워런트증권)
									
		  					
								</a>
							</td>
							<td class="tL ellipsis" title="미래에셋증권">미래에셋증권</td>
							<td>2023.11.14</td>
							<td></td>
						</tr>
					
					
					
					
					
					
					
					
				
					
						
						
						
						
						
						
					
					
						
						
						
						
						
						
					
					
					
					
					
						<tr>
							<td>
								
								
								
								17:44
							</td>
							<td class="tL">
							    <span class="innerWrapTag">
							    	<span class="tagCom_kospi" title="유가증권시장" style="cursor:default">유</span>
									<a href="javascript:openCorpInfoNew('00111722', 'winCorpInfo', '/dsae001/selectPopup.ax');" title="미래에셋증권 기업개황 새창" >
										미래에셋증권
									</a>
								</span>
								<a href="http://ci.securities.miraeasset.com" target="new">
										<span class="tagCom_ir" title="기업 IR페이지 연결">IR</span>
									</a>
							</td>
							<td class="tL">
								<a href="/dsaf001/main.do?rcpNo=20231114002748"  onclick="openReportViewer('20231114002748'); return false;" id="r_20231114002748"
									title="일괄신고서(파생결합증권-상장지수증권) 공시뷰어 새창" ><span title="본 보고서명으로 이미 제출된 보고서의 기재내용이 변경되어 제출된 것임" class="txtCB">[기재정정]</span>일괄신고서(파생결합증권-상장지수증권)
									
		  					
								</a>
							</td>
							<td class="tL ellipsis" title="미래에셋증권">미래에셋증권</td>
							<td>2023.11.14</td>
							<td></td>
						</tr>
					
					
					
					
					
					
					
					
				
					
						
						
						
						
						
						
					
					
						
						
						
						
						
						
					
					
					
					
					
						<tr>
							<td>
								
								
								
								17:44
							</td>
							<td class="tL">
							    <span class="innerWrapTag">
							    	<span class="tagCom_kospi" title="유가증권시장" style="cursor:default">유</span>
									<a href="javascript:openCorpInfoNew('00111722', 'winCorpInfo', '/dsae001/selectPopup.ax');" title="미래에셋증권 기업개황 새창" >
										미래에셋증권
									</a>
								</span>
								<a href="http://ci.securities.miraeasset.com" target="new">
										<span class="tagCom_ir" title="기업 IR페이지 연결">IR</span>
									</a>
							</td>
							<td class="tL">
								<a href="/dsaf001/main.do?rcpNo=20231114002673"  onclick="openReportViewer('20231114002673'); return false;" id="r_20231114002673"
									title="일괄신고서(파생결합증권-주가연계증권) 공시뷰어 새창" ><span title="본 보고서명으로 이미 제출된 보고서의 기재내용이 변경되어 제출된 것임" class="txtCB">[기재정정]</span>일괄신고서(파생결합증권-주가연계증권)
									
		  					
								</a>
							</td>
							<td class="tL ellipsis" title="미래에셋증권">미래에셋증권</td>
							<td>2023.11.14</td>
							<td></td>
						</tr>
					
					
					
					
					
					
					
					
				
					
						
						
						
						
						
						
					
					
					
					
					
					
						<tr>
							<td>
								
								
								
								17:43
							</td>
							<td class="tL">
							    <span class="innerWrap">
							    	<span class="tagCom_kospi" title="유가증권시장" style="cursor:default">유</span>
									<a href="javascript:openCorpInfoNew('00101220', 'winCorpInfo', '/dsae001/selectPopup.ax');" title="KG케미칼 기업개황 새창" >
										KG케미칼
									</a>
								</span>
								
							</td>
							<td class="tL">
								<a href="/dsaf001/main.do?rcpNo=20231114002976"  onclick="openReportViewer('20231114002976'); return false;" id="r_20231114002976"
									title="분기보고서 공시뷰어 새창" >분기보고서
									 (2023.09)
		  						
								</a>
							</td>
							<td class="tL ellipsis" title="KG케미칼">KG케미칼</td>
							<td>2023.11.14</td>
							<td></td>
						</tr>
					
					
					
					
					
					
					
					
				
					
						
						
						
						
						
						
					
					
					
					
					
					
						<tr>
							<td>
								
								
								
								17:43
							</td>
							<td class="tL">
							    <span class="innerWrap">
							    	<span class="tagCom_kospi" title="유가증권시장" style="cursor:default">유</span>
									<a href="javascript:openCorpInfoNew('00113544', 'winCorpInfo', '/dsae001/selectPopup.ax');" title="대한화섬 기업개황 새창" >
										대한화섬
									</a>
								</span>
								
							</td>
							<td class="tL">
								<a href="/dsaf001/main.do?rcpNo=20231114002974"  onclick="openReportViewer('20231114002974'); return false;" id="r_20231114002974"
									title="분기보고서 공시뷰어 새창" >분기보고서
									 (2023.09)
		  						
								</a>
							</td>
							<td class="tL ellipsis" title="대한화섬">대한화섬</td>
							<td>2023.11.14</td>
							<td></td>
						</tr>
					
					
					
					
					
					
					
					
				
					
						
						
						
						
						
						
					
					
					
					
					
					
						<tr>
							<td>
								
								
								
								17:43
							</td>
							<td class="tL">
							    <span class="innerWrap">
							    	<span class="tagCom_kospi" title="유가증권시장" style="cursor:default">유</span>
									<a href="javascript:openCorpInfoNew('00148984', 'winCorpInfo', '/dsae001/selectPopup.ax');" title="시알홀딩스 기업개황 새창" >
										시알홀딩스
									</a>
								</span>
								
							</td>
							<td class="tL">
								<a href="/dsaf001/main.do?rcpNo=20231114002970"  onclick="openReportViewer('20231114002970'); return false;" id="r_20231114002970"
									title="분기보고서 공시뷰어 새창" >분기보고서
									 (2023.09)
		  						
								</a>
							</td>
							<td class="tL ellipsis" title="시알홀딩스">시알홀딩스</td>
							<td>2023.11.14</td>
							<td></td>
						</tr>
					
					
					
					
					
					
					
					
				
					
						
						
						
						
						
						
					
					
					
					
					
					
						<tr>
							<td>
								
								
								
								17:42
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
								<a href="/dsaf001/main.do?rcpNo=20231114803237"  onclick="openReportViewer('20231114803237'); return false;" id="r_20231114803237"
									title="파생상품거래손실발생 공시뷰어 새창" >파생상품거래손실발생
									
		  					
								</a>
							</td>
							<td class="tL ellipsis" title="롯데손해보험">롯데손해보험</td>
							<td>2023.11.14</td>
							<td><span class="tagCom_kospi_other" title="본 공시사항은 한국거래소 유가증권시장본부 소관임" style="cursor:default">유</span></td>
						</tr>
					
					
					
					
					
					
					
					
				
					
						
						
						
						
						
						
					
					
					
					
					
					
						<tr>
							<td>
								
								
								
								17:42
							</td>
							<td class="tL">
							    <span class="innerWrap">
							    	<span class="tagCom_kospi" title="유가증권시장" style="cursor:default">유</span>
									<a href="javascript:openCorpInfoNew('00164812', 'winCorpInfo', '/dsae001/selectPopup.ax');" title="현대코퍼레이션 기업개황 새창" >
										현대코퍼레이션
									</a>
								</span>
								
							</td>
							<td class="tL">
								<a href="/dsaf001/main.do?rcpNo=20231114002967"  onclick="openReportViewer('20231114002967'); return false;" id="r_20231114002967"
									title="분기보고서 공시뷰어 새창" >분기보고서
									 (2023.09)
		  						
								</a>
							</td>
							<td class="tL ellipsis" title="현대코퍼레이션">현대코퍼레이션</td>
							<td>2023.11.14</td>
							<td></td>
						</tr>
					
					
					
					
					
					
					
					
				
					
						
						
						
						
						
						
					
					
					
					
					
					
						<tr>
							<td>
								
								
								
								17:41
							</td>
							<td class="tL">
							    <span class="innerWrap">
							    	<span class="tagCom_kospi" title="유가증권시장" style="cursor:default">유</span>
									<a href="javascript:openCorpInfoNew('01762569', 'winCorpInfo', '/dsae001/selectPopup.ax');" title="이수스페셜티케미컬 기업개황 새창" >
										이수스페셜티케미컬
									</a>
								</span>
								
							</td>
							<td class="tL">
								<a href="/dsaf001/main.do?rcpNo=20231114002962"  onclick="openReportViewer('20231114002962'); return false;" id="r_20231114002962"
									title="분기보고서 공시뷰어 새창" >분기보고서
									 (2023.09)
		  						
								</a>
							</td>
							<td class="tL ellipsis" title="이수스페셜티케미컬">이수스페셜티케미컬</td>
							<td>2023.11.14</td>
							<td></td>
						</tr>
					
					
					
					
					
					
					
					
				
					
						
						
						
						
						
						
					
					
					
					
					
					
						<tr>
							<td>
								
								
								
								17:40
							</td>
							<td class="tL">
							    <span class="innerWrap">
							    	<span class="tagCom_kospi" title="유가증권시장" style="cursor:default">유</span>
									<a href="javascript:openCorpInfoNew('00160302', 'winCorpInfo', '/dsae001/selectPopup.ax');" title="코스모화학 기업개황 새창" >
										코스모화학
									</a>
								</span>
								
							</td>
							<td class="tL">
								<a href="/dsaf001/main.do?rcpNo=20231114002958"  onclick="openReportViewer('20231114002958'); return false;" id="r_20231114002958"
									title="분기보고서 공시뷰어 새창" >분기보고서
									 (2023.09)
		  						
								</a>
							</td>
							<td class="tL ellipsis" title="코스모화학">코스모화학</td>
							<td>2023.11.14</td>
							<td></td>
						</tr>
					
					
					
					
					
					
					
					
				
					
						
						
						
						
						
						
					
					
					
					
					
					
						<tr>
							<td>
								
								
								
								17:40
							</td>
							<td class="tL">
							    <span class="innerWrap">
							    	<span class="tagCom_kospi" title="유가증권시장" style="cursor:default">유</span>
									<a href="javascript:openCorpInfoNew('00136721', 'winCorpInfo', '/dsae001/selectPopup.ax');" title="신영증권 기업개황 새창" >
										신영증권
									</a>
								</span>
								
							</td>
							<td class="tL">
								<a href="/dsaf001/main.do?rcpNo=20231114002957"  onclick="openReportViewer('20231114002957'); return false;" id="r_20231114002957"
									title="투자설명서(일괄신고) 공시뷰어 새창" >투자설명서(일괄신고)
									
		  					
								</a>
							</td>
							<td class="tL ellipsis" title="신영증권">신영증권</td>
							<td>2023.11.14</td>
							<td></td>
						</tr>
					
					
					
					
					
					
					
					
				
					
						
						
						
						
						
						
					
					
					
					
					
					
						<tr>
							<td>
								
								
								
								17:39
							</td>
							<td class="tL">
							    <span class="innerWrap">
							    	<span class="tagCom_kospi" title="유가증권시장" style="cursor:default">유</span>
									<a href="javascript:openCorpInfoNew('00136721', 'winCorpInfo', '/dsae001/selectPopup.ax');" title="신영증권 기업개황 새창" >
										신영증권
									</a>
								</span>
								
							</td>
							<td class="tL">
								<a href="/dsaf001/main.do?rcpNo=20231114002955"  onclick="openReportViewer('20231114002955'); return false;" id="r_20231114002955"
									title="일괄신고추가서류(파생결합증권-주가연계증권) 공시뷰어 새창" >일괄신고추가서류(파생결합증권-주가연계증권)
									
		  					
								</a>
							</td>
							<td class="tL ellipsis" title="신영증권">신영증권</td>
							<td>2023.11.14</td>
							<td></td>
						</tr>
					
					
					
					
					
					
					
					
				
					
						
						
						
						
						
						
					
					
					
					
					
					
						<tr>
							<td>
								
								
								
								17:39
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
								<a href="/dsaf001/main.do?rcpNo=20231114002954"  onclick="openReportViewer('20231114002954'); return false;" id="r_20231114002954"
									title="반기보고서 공시뷰어 새창" ><span title="본 보고서명으로 이미 제출된 보고서의 기재내용이 변경되어 제출된 것임" class="txtCB">[기재정정]</span>반기보고서
									 (2023.06)
		  						
								</a>
							</td>
							<td class="tL ellipsis" title="롯데손해보험">롯데손해보험</td>
							<td>2023.11.14</td>
							<td></td>
						</tr>
					
					
					
					
					
					
					
					
				
					
						
						
						
						
						
						
					
					
					
					
					
					
						<tr>
							<td>
								
								
								
								17:39
							</td>
							<td class="tL">
							    <span class="innerWrap">
							    	<span class="tagCom_kospi" title="유가증권시장" style="cursor:default">유</span>
									<a href="javascript:openCorpInfoNew('00159616', 'winCorpInfo', '/dsae001/selectPopup.ax');" title="두산에너빌리티 기업개황 새창" >
										두산에너빌리티
									</a>
								</span>
								
							</td>
							<td class="tL">
								<a href="/dsaf001/main.do?rcpNo=20231114002953"  onclick="openReportViewer('20231114002953'); return false;" id="r_20231114002953"
									title="분기보고서 공시뷰어 새창" >분기보고서
									 (2023.09)
		  						
								</a>
							</td>
							<td class="tL ellipsis" title="두산에너빌리티">두산에너빌리티</td>
							<td>2023.11.14</td>
							<td></td>
						</tr>
					
					
					
					
					
					
					
					
				
					
						
						
						
						
						
						
					
					
					
					
					
					
						<tr>
							<td>
								
								
								
								17:38
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
								<a href="/dsaf001/main.do?rcpNo=20231114002949"  onclick="openReportViewer('20231114002949'); return false;" id="r_20231114002949"
									title="증권신고서(지분증권) 공시뷰어 새창" ><span title="본 보고서명으로 이미 제출된 보고서의 기재내용이 변경되어 제출된 것임" class="txtCB">[기재정정]</span>증권신고서(지분증권)
									 (2023.12)
		  						
								</a>
							</td>
							<td class="tL ellipsis" title="STX">STX</td>
							<td>2023.11.14</td>
							<td></td>
						</tr>
					
					
					
					
					
					
					
					
				
					
						
						
						
						
						
						
					
					
					
					
					
					
						<tr>
							<td>
								
								
								
								17:38
							</td>
							<td class="tL">
							    <span class="innerWrap">
							    	<span class="tagCom_kospi" title="유가증권시장" style="cursor:default">유</span>
									<a href="javascript:openCorpInfoNew('00160843', 'winCorpInfo', '/dsae001/selectPopup.ax');" title="DB하이텍 기업개황 새창" >
										DB하이텍
									</a>
								</span>
								
							</td>
							<td class="tL">
								<a href="/dsaf001/main.do?rcpNo=20231114002947"  onclick="openReportViewer('20231114002947'); return false;" id="r_20231114002947"
									title="분기보고서 공시뷰어 새창" >분기보고서
									 (2023.09)
		  						
								</a>
							</td>
							<td class="tL ellipsis" title="DB하이텍">DB하이텍</td>
							<td>2023.11.14</td>
							<td></td>
						</tr>
					
					
					
					
					
					
					
					
				
					
						
						
						
						
						
						
					
					
					
					
					
					
						<tr>
							<td>
								
								
								
								17:36
							</td>
							<td class="tL">
							    <span class="innerWrap">
							    	<span class="tagCom_kospi" title="유가증권시장" style="cursor:default">유</span>
									<a href="javascript:openCorpInfoNew('00486705', 'winCorpInfo', '/dsae001/selectPopup.ax');" title="아주스틸 기업개황 새창" >
										아주스틸
									</a>
								</span>
								
							</td>
							<td class="tL">
								<a href="/dsaf001/main.do?rcpNo=20231114002933"  onclick="openReportViewer('20231114002933'); return false;" id="r_20231114002933"
									title="분기보고서 공시뷰어 새창" >분기보고서
									 (2023.09)
		  						
								</a>
							</td>
							<td class="tL ellipsis" title="아주스틸">아주스틸</td>
							<td>2023.11.14</td>
							<td></td>
						</tr>
					
					
					
					
					
					
					
					
				
					
						
						
						
						
						
						
					
					
					
					
					
					
						<tr>
							<td>
								
								
								
								17:35
							</td>
							<td class="tL">
							    <span class="innerWrap">
							    	<span class="tagCom_kospi" title="유가증권시장" style="cursor:default">유</span>
									<a href="javascript:openCorpInfoNew('00469799', 'winCorpInfo', '/dsae001/selectPopup.ax');" title="이엔플러스 기업개황 새창" >
										이엔플러스
									</a>
								</span>
								
							</td>
							<td class="tL">
								<a href="/dsaf001/main.do?rcpNo=20231114002930"  onclick="openReportViewer('20231114002930'); return false;" id="r_20231114002930"
									title="반기보고서 공시뷰어 새창" ><span title="본 보고서명으로 이미 제출된 보고서의 기재내용이 변경되어 제출된 것임" class="txtCB">[기재정정]</span>반기보고서
									 (2023.06)
		  						
								</a>
							</td>
							<td class="tL ellipsis" title="이엔플러스">이엔플러스</td>
							<td>2023.11.14</td>
							<td></td>
						</tr>
					
					
					
					
					
					
					
					
				
					
						
						
						
						
						
						
					
					
						
						
						
						
						
						
					
					
					
					
					
						<tr>
							<td>
								
								
								
								17:35
							</td>
							<td class="tL">
							    <span class="innerWrapTag">
							    	<span class="tagCom_kospi" title="유가증권시장" style="cursor:default">유</span>
									<a href="javascript:openCorpInfoNew('00160588', 'winCorpInfo', '/dsae001/selectPopup.ax');" title="한화 기업개황 새창" >
										한화
									</a>
								</span>
								<a href="http://www.hanwhacorp.co.kr" target="new">
										<span class="tagCom_ir" title="기업 IR페이지 연결">IR</span>
									</a>
							</td>
							<td class="tL">
								<a href="/dsaf001/main.do?rcpNo=20231114002929"  onclick="openReportViewer('20231114002929'); return false;" id="r_20231114002929"
									title="분기보고서 공시뷰어 새창" >분기보고서
									 (2023.09)
		  						
								</a>
							</td>
							<td class="tL ellipsis" title="한화">한화</td>
							<td>2023.11.14</td>
							<td></td>
						</tr>
					
					
					
					
					
					
					
					
				
					
						
						
						
						
						
						
					
					
					
					
					
					
						<tr>
							<td>
								
								
								
								17:35
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
								<a href="/dsaf001/main.do?rcpNo=20231114002928"  onclick="openReportViewer('20231114002928'); return false;" id="r_20231114002928"
									title="분기보고서 공시뷰어 새창" ><span title="본 보고서명으로 이미 제출된 보고서의 기재내용이 변경되어 제출된 것임" class="txtCB">[기재정정]</span>분기보고서
									 (2023.03)
		  						
								</a>
							</td>
							<td class="tL ellipsis" title="롯데손해보험">롯데손해보험</td>
							<td>2023.11.14</td>
							<td></td>
						</tr>
					
					
					
					
					
					
					
					
				
					
						
						
						
						
						
						
					
					
					
					
					
					
						<tr>
							<td>
								
								
								
								17:35
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
								<a href="/dsaf001/main.do?rcpNo=20231114002924"  onclick="openReportViewer('20231114002924'); return false;" id="r_20231114002924"
									title="주주총회소집공고 공시뷰어 새창" >주주총회소집공고
									
		  					
								</a>
							</td>
							<td class="tL ellipsis" title="삼영">삼영</td>
							<td>2023.11.14</td>
							<td></td>
						</tr>
					
					
					
					
					
					
					
					
				
					
						
						
						
						
						
						
					
					
						
						
						
						
						
						
					
					
					
					
					
						<tr>
							<td>
								
								
								
								17:34
							</td>
							<td class="tL">
							    <span class="innerWrapTag">
							    	<span class="tagCom_kospi" title="유가증권시장" style="cursor:default">유</span>
									<a href="javascript:openCorpInfoNew('00102618', 'winCorpInfo', '/dsae001/selectPopup.ax');" title="계양전기 기업개황 새창" >
										계양전기
									</a>
								</span>
								<a href="http://www.keyang.co.kr" target="new">
										<span class="tagCom_ir" title="기업 IR페이지 연결">IR</span>
									</a>
							</td>
							<td class="tL">
								<a href="/dsaf001/main.do?rcpNo=20231114002921"  onclick="openReportViewer('20231114002921'); return false;" id="r_20231114002921"
									title="분기보고서 공시뷰어 새창" >분기보고서
									 (2023.09)
		  						
								</a>
							</td>
							<td class="tL ellipsis" title="계양전기">계양전기</td>
							<td>2023.11.14</td>
							<td></td>
						</tr>
					
					
					
					
					
					
					
					
				
					
						
						
						
						
						
						
					
					
					
					
					
					
						<tr>
							<td>
								
								
								
								17:34
							</td>
							<td class="tL">
							    <span class="innerWrap">
							    	<span class="tagCom_kospi" title="유가증권시장" style="cursor:default">유</span>
									<a href="javascript:openCorpInfoNew('00203290', 'winCorpInfo', '/dsae001/selectPopup.ax');" title="한국콜마홀딩스 기업개황 새창" >
										한국콜마홀딩스
									</a>
								</span>
								
							</td>
							<td class="tL">
								<a href="/dsaf001/main.do?rcpNo=20231114002919"  onclick="openReportViewer('20231114002919'); return false;" id="r_20231114002919"
									title="분기보고서 공시뷰어 새창" >분기보고서
									 (2023.09)
		  						
								</a>
							</td>
							<td class="tL ellipsis" title="한국콜마홀딩스">한국콜마홀딩스</td>
							<td>2023.11.14</td>
							<td></td>
						</tr>
					
					
					
					
					
					
					
					
				
					
						
						
						
						
						
						
					
					
						
						
						
						
						
						
					
					
					
					
					
						<tr>
							<td>
								
								
								
								17:34
							</td>
							<td class="tL">
							    <span class="innerWrapTag">
							    	<span class="tagCom_kospi" title="유가증권시장" style="cursor:default">유</span>
									<a href="javascript:openCorpInfoNew('00123143', 'winCorpInfo', '/dsae001/selectPopup.ax');" title="보령 기업개황 새창" >
										보령
									</a>
								</span>
								<a href="https://pharm.boryung.co.kr/ir/resource.do" target="new">
										<span class="tagCom_ir" title="기업 IR페이지 연결">IR</span>
									</a>
							</td>
							<td class="tL">
								<a href="/dsaf001/main.do?rcpNo=20231114002918"  onclick="openReportViewer('20231114002918'); return false;" id="r_20231114002918"
									title="분기보고서 공시뷰어 새창" >분기보고서
									 (2023.09)
		  						
								</a>
							</td>
							<td class="tL ellipsis" title="보령">보령</td>
							<td>2023.11.14</td>
							<td></td>
						</tr>
					
					
					
					
					
					
					
					
				
					
						
						
						
						
						
						
					
					
					
					
					
					
						<tr>
							<td>
								
								
								
								17:33
							</td>
							<td class="tL">
							    <span class="innerWrap">
							    	<span class="tagCom_kospi" title="유가증권시장" style="cursor:default">유</span>
									<a href="javascript:openCorpInfoNew('01316227', 'winCorpInfo', '/dsae001/selectPopup.ax');" title="효성티앤씨 기업개황 새창" >
										효성티앤씨
									</a>
								</span>
								
							</td>
							<td class="tL">
								<a href="/dsaf001/main.do?rcpNo=20231114002916"  onclick="openReportViewer('20231114002916'); return false;" id="r_20231114002916"
									title="분기보고서 공시뷰어 새창" ><span title="본 보고서명으로 이미 제출된 보고서의 기재내용이 변경되어 제출된 것임" class="txtCB">[기재정정]</span>분기보고서
									 (2023.09)
		  						
								</a>
							</td>
							<td class="tL ellipsis" title="효성티앤씨">효성티앤씨</td>
							<td>2023.11.14</td>
							<td></td>
						</tr>
					
					
					
					
					
					
					
					
				
					
						
						
						
						
						
						
					
					
					
					
					
					
						<tr>
							<td>
								
								
								
								17:33
							</td>
							<td class="tL">
							    <span class="innerWrap">
							    	<span class="tagCom_kospi" title="유가증권시장" style="cursor:default">유</span>
									<a href="javascript:openCorpInfoNew('00261443', 'winCorpInfo', '/dsae001/selectPopup.ax');" title="엔씨소프트 기업개황 새창" >
										엔씨소프트
									</a>
								</span>
								
							</td>
							<td class="tL">
								<a href="/dsaf001/main.do?rcpNo=20231114002915"  onclick="openReportViewer('20231114002915'); return false;" id="r_20231114002915"
									title="분기보고서 공시뷰어 새창" >분기보고서
									 (2023.09)
		  						
								</a>
							</td>
							<td class="tL ellipsis" title="엔씨소프트">엔씨소프트</td>
							<td>2023.11.14</td>
							<td></td>
						</tr>
					
					
					
					
					
					
					
					
				
					
						
						
						
						
						
						
					
					
					
					
					
					
						<tr>
							<td>
								
								
								
								17:32
							</td>
							<td class="tL">
							    <span class="innerWrap">
							    	<span class="tagCom_kospi" title="유가증권시장" style="cursor:default">유</span>
									<a href="javascript:openCorpInfoNew('01311408', 'winCorpInfo', '/dsae001/selectPopup.ax');" title="에코프로머티 기업개황 새창" >
										에코프로머티
									</a>
								</span>
								
							</td>
							<td class="tL">
								<a href="/dsaf001/main.do?rcpNo=20231114002907"  onclick="openReportViewer('20231114002907'); return false;" id="r_20231114002907"
									title="증권발행실적보고서 공시뷰어 새창" >증권발행실적보고서
									
		  					
								</a>
							</td>
							<td class="tL ellipsis" title="에코프로머티">에코프로머티</td>
							<td>2023.11.14</td>
							<td></td>
						</tr>
					
					
					
					
					
					
					
					
				
					
						
						
						
						
						
						
					
					
					
					
					
					
						<tr>
							<td>
								
								
								
								17:32
							</td>
							<td class="tL">
							    <span class="innerWrap">
							    	<span class="tagCom_kospi" title="유가증권시장" style="cursor:default">유</span>
									<a href="javascript:openCorpInfoNew('00244455', 'winCorpInfo', '/dsae001/selectPopup.ax');" title="케이티앤지 기업개황 새창" >
										케이티앤지
									</a>
								</span>
								
							</td>
							<td class="tL">
								<a href="/dsaf001/main.do?rcpNo=20231114002901"  onclick="openReportViewer('20231114002901'); return false;" id="r_20231114002901"
									title="분기보고서 공시뷰어 새창" >분기보고서
									 (2023.09)
		  						
								</a>
							</td>
							<td class="tL ellipsis" title="케이티앤지">케이티앤지</td>
							<td>2023.11.14</td>
							<td></td>
						</tr>
					
					
					
					
					
					
					
					
				
					
						
						
						
						
						
						
					
					
						
						
						
						
						
						
					
					
					
					
					
						<tr>
							<td>
								
								
								
								17:31
							</td>
							<td class="tL">
							    <span class="innerWrapTag">
							    	<span class="tagCom_kospi" title="유가증권시장" style="cursor:default">유</span>
									<a href="javascript:openCorpInfoNew('00120562', 'winCorpInfo', '/dsae001/selectPopup.ax');" title="롯데지주 기업개황 새창" >
										롯데지주
									</a>
								</span>
								<a href="http://www.lotte.co.kr" target="new">
										<span class="tagCom_ir" title="기업 IR페이지 연결">IR</span>
									</a>
							</td>
							<td class="tL">
								<a href="/dsaf001/main.do?rcpNo=20231114002899"  onclick="openReportViewer('20231114002899'); return false;" id="r_20231114002899"
									title="분기보고서 공시뷰어 새창" >분기보고서
									 (2023.09)
		  						
								</a>
							</td>
							<td class="tL ellipsis" title="롯데지주">롯데지주</td>
							<td>2023.11.14</td>
							<td></td>
						</tr>
					
					
					
					
					
					
					
					
				
					
						
						
						
						
						
						
					
					
					
					
					
					
						<tr>
							<td>
								
								
								
								17:31
							</td>
							<td class="tL">
							    <span class="innerWrap">
							    	<span class="tagCom_kospi" title="유가증권시장" style="cursor:default">유</span>
									<a href="javascript:openCorpInfoNew('00147860', 'winCorpInfo', '/dsae001/selectPopup.ax');" title="에스엠벡셀 기업개황 새창" >
										에스엠벡셀
									</a>
								</span>
								
							</td>
							<td class="tL">
								<a href="/dsaf001/main.do?rcpNo=20231114002897"  onclick="openReportViewer('20231114002897'); return false;" id="r_20231114002897"
									title="분기보고서 공시뷰어 새창" >분기보고서
									 (2023.09)
		  						
								</a>
							</td>
							<td class="tL ellipsis" title="에스엠벡셀">에스엠벡셀</td>
							<td>2023.11.14</td>
							<td></td>
						</tr>
					
					
					
					
					
					
					
					
				
					
						
						
						
						
						
						
					
					
					
					
					
					
						<tr>
							<td>
								
								
								
								17:31
							</td>
							<td class="tL">
							    <span class="innerWrap">
							    	<span class="tagCom_kospi" title="유가증권시장" style="cursor:default">유</span>
									<a href="javascript:openCorpInfoNew('00152862', 'winCorpInfo', '/dsae001/selectPopup.ax');" title="코오롱 기업개황 새창" >
										코오롱
									</a>
								</span>
								
							</td>
							<td class="tL">
								<a href="/dsaf001/main.do?rcpNo=20231114002895"  onclick="openReportViewer('20231114002895'); return false;" id="r_20231114002895"
									title="분기보고서 공시뷰어 새창" >분기보고서
									 (2023.09)
		  						
								</a>
							</td>
							<td class="tL ellipsis" title="코오롱">코오롱</td>
							<td>2023.11.14</td>
							<td></td>
						</tr>
					
					
					
					
					
					
					
					
				
					
						
						
						
						
						
						
					
					
						
						
						
						
						
						
					
					
					
					
					
						<tr>
							<td>
								
								
								
								17:30
							</td>
							<td class="tL">
							    <span class="innerWrapTag">
							    	<span class="tagCom_kospi" title="유가증권시장" style="cursor:default">유</span>
									<a href="javascript:openCorpInfoNew('00108913', 'winCorpInfo', '/dsae001/selectPopup.ax');" title="대교 기업개황 새창" >
										대교
									</a>
								</span>
								<a href="http://company.daekyo.com" target="new">
										<span class="tagCom_ir" title="기업 IR페이지 연결">IR</span>
									</a>
							</td>
							<td class="tL">
								<a href="/dsaf001/main.do?rcpNo=20231114002890"  onclick="openReportViewer('20231114002890'); return false;" id="r_20231114002890"
									title="분기보고서 공시뷰어 새창" >분기보고서
									 (2023.09)
		  						
								</a>
							</td>
							<td class="tL ellipsis" title="대교">대교</td>
							<td>2023.11.14</td>
							<td></td>
						</tr>
					
					
					
					
					
					
					
					
				
					
						
						
						
						
						
						
					
					
					
					
					
					
						<tr>
							<td>
								
								
								
								17:30
							</td>
							<td class="tL">
							    <span class="innerWrap">
							    	<span class="tagCom_kospi" title="유가증권시장" style="cursor:default">유</span>
									<a href="javascript:openCorpInfoNew('00128032', 'winCorpInfo', '/dsae001/selectPopup.ax');" title="삼일제약 기업개황 새창" >
										삼일제약
									</a>
								</span>
								
							</td>
							<td class="tL">
								<a href="/dsaf001/main.do?rcpNo=20231114002888"  onclick="openReportViewer('20231114002888'); return false;" id="r_20231114002888"
									title="분기보고서 공시뷰어 새창" >분기보고서
									 (2023.09)
		  						
								</a>
							</td>
							<td class="tL ellipsis" title="삼일제약">삼일제약</td>
							<td>2023.11.14</td>
							<td></td>
						</tr>
					
					
					
					
					
					
					
					
				
					
						
						
						
						
						
						
					
					
					
					
					
					
						<tr>
							<td>
								
								
								
								17:30
							</td>
							<td class="tL">
							    <span class="innerWrap">
							    	<span class="tagCom_kospi" title="유가증권시장" style="cursor:default">유</span>
									<a href="javascript:openCorpInfoNew('00469799', 'winCorpInfo', '/dsae001/selectPopup.ax');" title="이엔플러스 기업개황 새창" >
										이엔플러스
									</a>
								</span>
								
							</td>
							<td class="tL">
								<a href="/dsaf001/main.do?rcpNo=20231114002824"  onclick="openReportViewer('20231114002824'); return false;" id="r_20231114002824"
									title="주요사항보고서(유상증자결정) 공시뷰어 새창" ><span title="본 보고서명으로 이미 제출된 보고서의 기재내용이 변경되어 제출된 것임" class="txtCB">[기재정정]</span>주요사항보고서(유상증자결정)
									
		  					
								</a>
							</td>
							<td class="tL ellipsis" title="이엔플러스">이엔플러스</td>
							<td>2023.11.14</td>
							<td></td>
						</tr>
					
					
					
					
					
					
					
					
				
					
						
						
						
						
						
						
					
					
					
					
					
					
						<tr>
							<td>
								
								
								
								17:30
							</td>
							<td class="tL">
							    <span class="innerWrap">
							    	<span class="tagCom_kospi" title="유가증권시장" style="cursor:default">유</span>
									<a href="javascript:openCorpInfoNew('00469799', 'winCorpInfo', '/dsae001/selectPopup.ax');" title="이엔플러스 기업개황 새창" >
										이엔플러스
									</a>
								</span>
								
							</td>
							<td class="tL">
								<a href="/dsaf001/main.do?rcpNo=20231114002808"  onclick="openReportViewer('20231114002808'); return false;" id="r_20231114002808"
									title="주요사항보고서(유상증자결정) 공시뷰어 새창" ><span title="본 보고서명으로 이미 제출된 보고서의 기재내용이 변경되어 제출된 것임" class="txtCB">[기재정정]</span>주요사항보고서(유상증자결정)
									
		  					
								</a>
							</td>
							<td class="tL ellipsis" title="이엔플러스">이엔플러스</td>
							<td>2023.11.14</td>
							<td></td>
						</tr>
					
					
					
					
					
					
					
					
				
					
						
						
						
						
						
						
					
					
					
					
					
					
						<tr>
							<td>
								
								
								
								17:29
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
								<a href="/dsaf001/main.do?rcpNo=20231114002880"  onclick="openReportViewer('20231114002880'); return false;" id="r_20231114002880"
									title="분기보고서 공시뷰어 새창" >분기보고서
									 (2023.09)
		  						
								</a>
							</td>
							<td class="tL ellipsis" title="SK증권">SK증권</td>
							<td>2023.11.14</td>
							<td></td>
						</tr>
					
					
					
					
					
					
					
					
				
					
						
						
						
						
						
						
					
					
						
						
						
						
						
						
					
					
					
					
					
						<tr>
							<td>
								
								
								
								17:28
							</td>
							<td class="tL">
							    <span class="innerWrapTag">
							    	<span class="tagCom_kospi" title="유가증권시장" style="cursor:default">유</span>
									<a href="javascript:openCorpInfoNew('01394377', 'winCorpInfo', '/dsae001/selectPopup.ax');" title="이지스밸류플러스리츠 기업개황 새창" >
										이지스밸류플러스리츠
									</a>
								</span>
								<a href="http://www.igisvaluereit.com" target="new">
										<span class="tagCom_ir" title="기업 IR페이지 연결">IR</span>
									</a>
							</td>
							<td class="tL">
								<a href="/dsaf001/main.do?rcpNo=20231114002876"  onclick="openReportViewer('20231114002876'); return false;" id="r_20231114002876"
									title="의결권대리행사권유참고서류 공시뷰어 새창" >의결권대리행사권유참고서류
									
		  					
								</a>
							</td>
							<td class="tL ellipsis" title="이지스밸류플러스리츠">이지스밸류플러스리츠</td>
							<td>2023.11.14</td>
							<td><span class="tagCom_jung_other" title="본 보고서 제출 후 정정신고가 있으니 관련 보고서를 참조하시기 바람" style="cursor:default">정</span></td>
						</tr>
					
					
					
					
					
					
					
					
				
					
						
						
						
						
						
						
					
					
					
					
					
					
						<tr>
							<td>
								
								
								
								17:28
							</td>
							<td class="tL">
							    <span class="innerWrap">
							    	<span class="tagCom_kospi" title="유가증권시장" style="cursor:default">유</span>
									<a href="javascript:openCorpInfoNew('00102858', 'winCorpInfo', '/dsae001/selectPopup.ax');" title="고려아연 기업개황 새창" >
										고려아연
									</a>
								</span>
								
							</td>
							<td class="tL">
								<a href="/dsaf001/main.do?rcpNo=20231114002871"  onclick="openReportViewer('20231114002871'); return false;" id="r_20231114002871"
									title="분기보고서 공시뷰어 새창" >분기보고서
									 (2023.09)
		  						
								</a>
							</td>
							<td class="tL ellipsis" title="고려아연">고려아연</td>
							<td>2023.11.14</td>
							<td></td>
						</tr>
					
					
					
					
					
					
					
					
				
					
						
						
						
						
						
						
					
					
					
					
					
					
						<tr>
							<td>
								
								
								
								17:27
							</td>
							<td class="tL">
							    <span class="innerWrap">
							    	<span class="tagCom_kospi" title="유가증권시장" style="cursor:default">유</span>
									<a href="javascript:openCorpInfoNew('00113243', 'winCorpInfo', '/dsae001/selectPopup.ax');" title="대한제분 기업개황 새창" >
										대한제분
									</a>
								</span>
								
							</td>
							<td class="tL">
								<a href="/dsaf001/main.do?rcpNo=20231114002866"  onclick="openReportViewer('20231114002866'); return false;" id="r_20231114002866"
									title="분기보고서 공시뷰어 새창" >분기보고서
									 (2023.09)
		  						
								</a>
							</td>
							<td class="tL ellipsis" title="대한제분">대한제분</td>
							<td>2023.11.14</td>
							<td></td>
						</tr>
					
					
					
					
					
					
					
					
				
					
						
						
						
						
						
						
					
					
					
					
					
					
						<tr>
							<td>
								
								
								
								17:27
							</td>
							<td class="tL">
							    <span class="innerWrap">
							    	<span class="tagCom_kospi" title="유가증권시장" style="cursor:default">유</span>
									<a href="javascript:openCorpInfoNew('00112332', 'winCorpInfo', '/dsae001/selectPopup.ax');" title="미래에셋생명 기업개황 새창" >
										미래에셋생명
									</a>
								</span>
								
							</td>
							<td class="tL">
								<a href="/dsaf001/main.do?rcpNo=20231114002863"  onclick="openReportViewer('20231114002863'); return false;" id="r_20231114002863"
									title="분기보고서 공시뷰어 새창" >분기보고서
									 (2023.09)
		  						
								</a>
							</td>
							<td class="tL ellipsis" title="미래에셋생명">미래에셋생명</td>
							<td>2023.11.14</td>
							<td></td>
						</tr>
					
					
					
					
					
					
					
					
				
					
						
						
						
						
						
						
					
					
					
					
					
					
						<tr>
							<td>
								
								
								
								17:27
							</td>
							<td class="tL">
							    <span class="innerWrap">
							    	<span class="tagCom_kospi" title="유가증권시장" style="cursor:default">유</span>
									<a href="javascript:openCorpInfoNew('00159102', 'winCorpInfo', '/dsae001/selectPopup.ax');" title="DB손해보험 기업개황 새창" >
										DB손해보험
									</a>
								</span>
								
							</td>
							<td class="tL">
								<a href="/dsaf001/main.do?rcpNo=20231114002857"  onclick="openReportViewer('20231114002857'); return false;" id="r_20231114002857"
									title="분기보고서 공시뷰어 새창" >분기보고서
									 (2023.09)
		  						
								</a>
							</td>
							<td class="tL ellipsis" title="DB손해보험">DB손해보험</td>
							<td>2023.11.14</td>
							<td></td>
						</tr>
					
					
					
					
					
					
					
					
				
					
						
						
						
						
						
						
					
					
					
					
					
					
						<tr>
							<td>
								
								
								
								17:27
							</td>
							<td class="tL">
							    <span class="innerWrap">
							    	<span class="tagCom_kospi" title="유가증권시장" style="cursor:default">유</span>
									<a href="javascript:openCorpInfoNew('00106119', 'winCorpInfo', '/dsae001/selectPopup.ax');" title="금양 기업개황 새창" >
										금양
									</a>
								</span>
								
							</td>
							<td class="tL">
								<a href="/dsaf001/main.do?rcpNo=20231114002855"  onclick="openReportViewer('20231114002855'); return false;" id="r_20231114002855"
									title="분기보고서 공시뷰어 새창" >분기보고서
									 (2023.09)
		  						
								</a>
							</td>
							<td class="tL ellipsis" title="금양">금양</td>
							<td>2023.11.14</td>
							<td></td>
						</tr>
					
					
					
					
					
					
					
					
				
					
						
						
						
						
						
						
					
					
					
					
					
					
						<tr>
							<td>
								
								
								
								17:26
							</td>
							<td class="tL">
							    <span class="innerWrap">
							    	<span class="tagCom_kospi" title="유가증권시장" style="cursor:default">유</span>
									<a href="javascript:openCorpInfoNew('00163716', 'winCorpInfo', '/dsae001/selectPopup.ax');" title="한창 기업개황 새창" >
										한창
									</a>
								</span>
								
							</td>
							<td class="tL">
								<a href="/dsaf001/main.do?rcpNo=20231114803027"  onclick="openReportViewer('20231114803027'); return false;" id="r_20231114803027"
									title="소송등의판결ㆍ결정 공시뷰어 새창" >소송등의판결ㆍ결정
									
		  					
								</a>
							</td>
							<td class="tL ellipsis" title="한창">한창</td>
							<td>2023.11.14</td>
							<td><span class="tagCom_kospi_other" title="본 공시사항은 한국거래소 유가증권시장본부 소관임" style="cursor:default">유</span></td>
						</tr>
					
					
					
					
					
					
					
					
				
					
						
						
						
						
						
						
					
					
						
						
						
						
						
						
					
					
					
					
					
						<tr>
							<td>
								
								
								
								17:26
							</td>
							<td class="tL">
							    <span class="innerWrapTag">
							    	<span class="tagCom_kospi" title="유가증권시장" style="cursor:default">유</span>
									<a href="javascript:openCorpInfoNew('01394377', 'winCorpInfo', '/dsae001/selectPopup.ax');" title="이지스밸류플러스리츠 기업개황 새창" >
										이지스밸류플러스리츠
									</a>
								</span>
								<a href="http://www.igisvaluereit.com" target="new">
										<span class="tagCom_ir" title="기업 IR페이지 연결">IR</span>
									</a>
							</td>
							<td class="tL">
								<a href="/dsaf001/main.do?rcpNo=20231114002851"  onclick="openReportViewer('20231114002851'); return false;" id="r_20231114002851"
									title="주주총회소집공고 공시뷰어 새창" >주주총회소집공고
									
		  					
								</a>
							</td>
							<td class="tL ellipsis" title="이지스밸류플러스리츠">이지스밸류플러스리츠</td>
							<td>2023.11.14</td>
							<td><span class="tagCom_jung_other" title="본 보고서 제출 후 정정신고가 있으니 관련 보고서를 참조하시기 바람" style="cursor:default">정</span></td>
						</tr>
					
					
					
					
					
					
					
					
				
					
						
						
						
						
						
						
					
					
					
					
					
					
						<tr>
							<td>
								
								
								
								17:26
							</td>
							<td class="tL">
							    <span class="innerWrap">
							    	<span class="tagCom_kospi" title="유가증권시장" style="cursor:default">유</span>
									<a href="javascript:openCorpInfoNew('00136721', 'winCorpInfo', '/dsae001/selectPopup.ax');" title="신영증권 기업개황 새창" >
										신영증권
									</a>
								</span>
								
							</td>
							<td class="tL">
								<a href="/dsaf001/main.do?rcpNo=20231114002848"  onclick="openReportViewer('20231114002848'); return false;" id="r_20231114002848"
									title="투자설명서(일괄신고) 공시뷰어 새창" >투자설명서(일괄신고)
									
		  					
								</a>
							</td>
							<td class="tL ellipsis" title="신영증권">신영증권</td>
							<td>2023.11.14</td>
							<td></td>
						</tr>
					
					
					
					
					
					
					
					
				
					
						
						
						
						
						
						
					
					
					
					
					
					
						<tr>
							<td>
								
								
								
								17:26
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
								<a href="/dsaf001/main.do?rcpNo=20231114002494"  onclick="openReportViewer('20231114002494'); return false;" id="r_20231114002494"
									title="일괄신고서(파생결합증권-상장지수증권) 공시뷰어 새창" ><span title="본 보고서명으로 이미 제출된 보고서의 기재내용이 변경되어 제출된 것임" class="txtCB">[기재정정]</span>일괄신고서(파생결합증권-상장지수증권)
									
		  					
								</a>
							</td>
							<td class="tL ellipsis" title="NH투자증권">NH투자증권</td>
							<td>2023.11.14</td>
							<td></td>
						</tr>
					
					
					
					
					
					
					
					
				
					
						
						
						
						
						
						
					
					
					
					
					
					
						<tr>
							<td>
								
								
								
								17:26
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
								<a href="/dsaf001/main.do?rcpNo=20231114002014"  onclick="openReportViewer('20231114002014'); return false;" id="r_20231114002014"
									title="일괄신고서(파생결합증권-상장지수증권) 공시뷰어 새창" ><span title="본 보고서명으로 이미 제출된 보고서의 기재내용이 변경되어 제출된 것임" class="txtCB">[기재정정]</span>일괄신고서(파생결합증권-상장지수증권)
									
		  					
								</a>
							</td>
							<td class="tL ellipsis" title="NH투자증권">NH투자증권</td>
							<td>2023.11.14</td>
							<td><span class="tagCom_jung_other" title="본 보고서 제출 후 정정신고가 있으니 관련 보고서를 참조하시기 바람" style="cursor:default">정</span></td>
						</tr>
					
					
					
					
					
					
					
					
				
					
						
						
						
						
						
						
					
					
					
					
					
					
						<tr>
							<td>
								
								
								
								17:25
							</td>
							<td class="tL">
							    <span class="innerWrap">
							    	<span class="tagCom_kospi" title="유가증권시장" style="cursor:default">유</span>
									<a href="javascript:openCorpInfoNew('01562589', 'winCorpInfo', '/dsae001/selectPopup.ax');" title="LX홀딩스 기업개황 새창" >
										LX홀딩스
									</a>
								</span>
								
							</td>
							<td class="tL">
								<a href="/dsaf001/main.do?rcpNo=20231114002842"  onclick="openReportViewer('20231114002842'); return false;" id="r_20231114002842"
									title="분기보고서 공시뷰어 새창" >분기보고서
									 (2023.09)
		  						
								</a>
							</td>
							<td class="tL ellipsis" title="LX홀딩스">LX홀딩스</td>
							<td>2023.11.14</td>
							<td></td>
						</tr>
					
					
					
					
					
					
					
					
				
					
						
						
						
						
						
						
					
					
					
					
					
					
						<tr>
							<td>
								
								
								
								17:25
							</td>
							<td class="tL">
							    <span class="innerWrap">
							    	<span class="tagCom_kospi" title="유가증권시장" style="cursor:default">유</span>
									<a href="javascript:openCorpInfoNew('00261285', 'winCorpInfo', '/dsae001/selectPopup.ax');" title="한국가스공사 기업개황 새창" >
										한국가스공사
									</a>
								</span>
								
							</td>
							<td class="tL">
								<a href="/dsaf001/main.do?rcpNo=20231114002837"  onclick="openReportViewer('20231114002837'); return false;" id="r_20231114002837"
									title="분기보고서 공시뷰어 새창" >분기보고서
									 (2023.09)
		  						
								</a>
							</td>
							<td class="tL ellipsis" title="한국가스공사">한국가스공사</td>
							<td>2023.11.14</td>
							<td></td>
						</tr>
					
					
					
					
					
					
					
					
				
					
						
						
						
						
						
						
					
					
					
					
					
					
						<tr>
							<td>
								
								
								
								17:24
							</td>
							<td class="tL">
							    <span class="innerWrap">
							    	<span class="tagCom_kospi" title="유가증권시장" style="cursor:default">유</span>
									<a href="javascript:openCorpInfoNew('00112059', 'winCorpInfo', '/dsae001/selectPopup.ax');" title="상상인증권 기업개황 새창" >
										상상인증권
									</a>
								</span>
								
							</td>
							<td class="tL">
								<a href="/dsaf001/main.do?rcpNo=20231114002833"  onclick="openReportViewer('20231114002833'); return false;" id="r_20231114002833"
									title="분기보고서 공시뷰어 새창" >분기보고서
									 (2023.09)
		  						
								</a>
							</td>
							<td class="tL ellipsis" title="상상인증권">상상인증권</td>
							<td>2023.11.14</td>
							<td><span class="tagCom_jung_other" title="본 보고서 제출 후 정정신고가 있으니 관련 보고서를 참조하시기 바람" style="cursor:default">정</span></td>
						</tr>
					
					
					
					
					
					
					
					
				
					
						
						
						
						
						
						
					
					
					
					
					
					
						<tr>
							<td>
								
								
								
								17:24
							</td>
							<td class="tL">
							    <span class="innerWrap">
							    	<span class="tagCom_kospi" title="유가증권시장" style="cursor:default">유</span>
									<a href="javascript:openCorpInfoNew('00103042', 'winCorpInfo', '/dsae001/selectPopup.ax');" title="케이씨티시 기업개황 새창" >
										케이씨티시
									</a>
								</span>
								
							</td>
							<td class="tL">
								<a href="/dsaf001/main.do?rcpNo=20231114002832"  onclick="openReportViewer('20231114002832'); return false;" id="r_20231114002832"
									title="분기보고서 공시뷰어 새창" >분기보고서
									 (2023.09)
		  						
								</a>
							</td>
							<td class="tL ellipsis" title="케이씨티시">케이씨티시</td>
							<td>2023.11.14</td>
							<td></td>
						</tr>
					
					
					
					
					
					
					
					
				
					
						
						
						
						
						
						
					
					
					
					
					
					
						<tr>
							<td>
								
								
								
								17:24
							</td>
							<td class="tL">
							    <span class="innerWrap">
							    	<span class="tagCom_kospi" title="유가증권시장" style="cursor:default">유</span>
									<a href="javascript:openCorpInfoNew('00828789', 'winCorpInfo', '/dsae001/selectPopup.ax');" title="대성산업 기업개황 새창" >
										대성산업
									</a>
								</span>
								
							</td>
							<td class="tL">
								<a href="/dsaf001/main.do?rcpNo=20231114002827"  onclick="openReportViewer('20231114002827'); return false;" id="r_20231114002827"
									title="분기보고서 공시뷰어 새창" >분기보고서
									 (2023.09)
		  						
								</a>
							</td>
							<td class="tL ellipsis" title="대성산업">대성산업</td>
							<td>2023.11.14</td>
							<td></td>
						</tr>
					
					
					
					
					
					
					
					
				
					
						
						
						
						
						
						
					
					
					
					
					
					
						<tr>
							<td>
								
								
								
								17:22
							</td>
							<td class="tL">
							    <span class="innerWrap">
							    	<span class="tagCom_kospi" title="유가증권시장" style="cursor:default">유</span>
									<a href="javascript:openCorpInfoNew('01412822', 'winCorpInfo', '/dsae001/selectPopup.ax');" title="솔루스첨단소재 기업개황 새창" >
										솔루스첨단소재
									</a>
								</span>
								
							</td>
							<td class="tL">
								<a href="/dsaf001/main.do?rcpNo=20231114002810"  onclick="openReportViewer('20231114002810'); return false;" id="r_20231114002810"
									title="분기보고서 공시뷰어 새창" >분기보고서
									 (2023.09)
		  						
								</a>
							</td>
							<td class="tL ellipsis" title="솔루스첨단소재">솔루스첨단소재</td>
							<td>2023.11.14</td>
							<td></td>
						</tr>
					
					
					
					
					
					
					
					
				
					
						
						
						
						
						
						
					
					
					
					
					
					
						<tr>
							<td>
								
								
								
								17:20
							</td>
							<td class="tL">
							    <span class="innerWrap">
							    	<span class="tagCom_kospi" title="유가증권시장" style="cursor:default">유</span>
									<a href="javascript:openCorpInfoNew('00142661', 'winCorpInfo', '/dsae001/selectPopup.ax');" title="우성 기업개황 새창" >
										우성
									</a>
								</span>
								
							</td>
							<td class="tL">
								<a href="/dsaf001/main.do?rcpNo=20231114002796"  onclick="openReportViewer('20231114002796'); return false;" id="r_20231114002796"
									title="분기보고서 공시뷰어 새창" >분기보고서
									 (2023.09)
		  						
								</a>
							</td>
							<td class="tL ellipsis" title="우성">우성</td>
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
        assert len(data.disclosures) == 100
