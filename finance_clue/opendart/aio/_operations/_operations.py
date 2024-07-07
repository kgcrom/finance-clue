# pylint: disable=too-many-lines,too-many-statements
# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator (autorest: 3.10.2, generator: @autorest/python@6.13.15)
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import sys
from typing import Any, AsyncIterator, Callable, Dict, Optional, Type, TypeVar, cast

from azure.core.exceptions import ClientAuthenticationError
from azure.core.exceptions import HttpResponseError
from azure.core.exceptions import ResourceExistsError
from azure.core.exceptions import ResourceNotFoundError
from azure.core.exceptions import ResourceNotModifiedError
from azure.core.exceptions import map_error
from azure.core.pipeline import PipelineResponse
from azure.core.rest import AsyncHttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator_async import distributed_trace_async

from ..._operations._operations import (
    build_gen_open_dart_get_corporate_document_request,
)
from ..._operations._operations import build_gen_open_dart_get_corporate_code_request
from ..._operations._operations import build_gen_open_dart_get_corporate_company_request
from ..._operations._operations import build_gen_open_dart_get_corporate_list_request
from .._vendor import GenOpenDartClientMixinABC

if sys.version_info >= (3, 9):
    from collections.abc import MutableMapping
else:
    from typing import (
        MutableMapping,  # type: ignore  # pylint: disable=ungrouped-imports
    )
JSON = MutableMapping[str, Any]  # pylint: disable=unsubscriptable-object
T = TypeVar("T")
ClsType = Optional[
    Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]
]


class GenOpenDartClientOperationsMixin(GenOpenDartClientMixinABC):

    @distributed_trace_async
    async def get_corporate_list(
        self,
        *,
        bgn_de: Optional[str] = None,
        end_de: Optional[str] = None,
        corp_code: Optional[str] = None,
        last_reprt_at: str = "N",
        pblntf_ty: Optional[str] = None,
        pblntf_detail_ty: Optional[str] = None,
        corp_cls: Optional[str] = None,
        sort: str = "date",
        sort_mth: str = "desc",
        page_no: int = 1,
        page_count: int = 10,
        **kwargs: Any,
    ) -> JSON:
        # pylint: disable=line-too-long
        """공시검색.

        공시 유형별, 회사별, 날짜별 등 여러가지 조건으로 공시보고서 검색기능을 제공합니다.

        :keyword bgn_de: 시작일

         검색시작 접수일자(YYYYMMDD):code:`<br/>`
         1) 기본값 : 종료일(end_de):code:`<br/>`
         2) 고유번호(corp_code)가 없는 경우 검색기간은 3개월로 제한. Default value is None.
        :paramtype bgn_de: str
        :keyword end_de: 종료일

         검색종료 접수일자(YYYYMMDD)
         1) 기본값 : 당일. Default value is None.
        :paramtype end_de: str
        :keyword corp_code: 고유번호

         공시대상회사의 고유번호(8자리). Default value is None.
        :paramtype corp_code: str
        :keyword last_reprt_at: 최종보고서 검색여부

         최종보고서만 검색여부(Y or N)
         1) 기본값 : N(정정이 있는 경우 최종정정만 검색). Known values are: "Y" and "N". Default value is "N".
        :paramtype last_reprt_at: str
        :keyword pblntf_ty: 공시유형

         A : 정기공시:code:`<br/>`
         B : 주요사항보고:code:`<br/>`
         C : 발행공시:code:`<br/>`
         D : 지분공시:code:`<br/>`
         E : 기타공시:code:`<br/>`
         F : 외부감사관련:code:`<br/>`
         G : 펀드공시:code:`<br/>`
         H : 자산유동화:code:`<br/>`
         I : 거래소공시:code:`<br/>`
         J : 공정위공시. Known values are: "A", "B", "C", "D", "E", "F", "G", "H", "I", and "J". Default
         value is None.
        :paramtype pblntf_ty: str
        :keyword pblntf_detail_ty: 공시상세유형


         * A001 : 사업보고서:code:`<br/>`
         * A002 : 반기보고서:code:`<br/>`
         * A003 : 분기보고서:code:`<br/>`
         * A004 : 등록법인결산서류(자본시장법이전):code:`<br/>`
         * A005 : 소액공모법인결산서류:code:`<br/>`
         * B001 : 주요사항보고서:code:`<br/>`
         * B002 : 주요경영사항신고(자본시장법 이전):code:`<br/>`
         * B003 : 최대주주등과의거래신고(자본시장법 이전):code:`<br/>`
         * C001 : 증권신고(지분증권):code:`<br/>`
         * C002 : 증권신고(채무증권):code:`<br/>`
         * C003 : 증권신고(파생결합증권):code:`<br/>`
         * C004 : 증권신고(합병등):code:`<br/>`
         * C005 : 증권신고(기타):code:`<br/>`
         * C006 : 소액공모(지분증권):code:`<br/>`
         * C007 : 소액공모(채무증권):code:`<br/>`
         * C008 : 소액공모(파생결합증권):code:`<br/>`
         * C009 : 소액공모(합병등):code:`<br/>`
         * C010 : 소액공모(기타):code:`<br/>`
         * C011 : 호가중개시스템을통한소액매출:code:`<br/>`
         * D001 : 주식등의대량보유상황보고서:code:`<br/>`
         * D002 : 임원ㆍ주요주주특정증권등소유상황보고서:code:`<br/>`
         * D003 : 의결권대리행사권유:code:`<br/>`
         * D004 : 공개매수:code:`<br/>`
         * E001 : 자기주식취득/처분:code:`<br/>`
         * E002 : 신탁계약체결/해지:code:`<br/>`
         * E003 : 합병등종료보고서:code:`<br/>`
         * E004 : 주식매수선택권부여에관한신고:code:`<br/>`
         * E005 : 사외이사에관한신고:code:`<br/>`
         * E006 : 주주총회소집보고서:code:`<br/>`
         * E007 : 시장조성/안정조작:code:`<br/>`
         * E008 : 합병등신고서(자본시장법 이전):code:`<br/>`
         * E009 : 금융위등록/취소(자본시장법 이전):code:`<br/>`
         * F001 : 감사보고서:code:`<br/>`
         * F002 : 연결감사보고서:code:`<br/>`
         * F003 : 결합감사보고서:code:`<br/>`
         * F004 : 회계법인사업보고서:code:`<br/>`
         * F005 : 감사전재무제표미제출신고서:code:`<br/>`
         * G001 : 증권신고(집합투자증권-신탁형):code:`<br/>`
         * G002 : 증권신고(집합투자증권-회사형):code:`<br/>`
         * G003 : 증권신고(집합투자증권-합병):code:`<br/>`
         * H001 : 자산유동화계획/양도등록:code:`<br/>`
         * H002 : 사업/반기/분기보고서:code:`<br/>`
         * H003 : 증권신고(유동화증권등):code:`<br/>`
         * H004 : 채권유동화계획/양도등록:code:`<br/>`
         * H005 : 자산유동화관련중요사항발생등보고:code:`<br/>`
         * H006 : 주요사항보고서:code:`<br/>`
         * I001 : 수시공시:code:`<br/>`
         * I002 : 공정공시:code:`<br/>`
         * I003 : 시장조치/안내:code:`<br/>`
         * I004 : 지분공시:code:`<br/>`
         * I005 : 증권투자회사:code:`<br/>`
         * I006 : 채권공시:code:`<br/>`
         * J001 : 대규모내부거래관련:code:`<br/>`
         * J002 : 대규모내부거래관련(구):code:`<br/>`
         * J004 : 기업집단현황공시:code:`<br/>`
         * J005 : 비상장회사중요사항공시:code:`<br/>`
         * J006 : 기타공정위공시:code:`<br/>`
         * J008 : 대규모내부거래관련(공익법인용):code:`<br/>`
         * J009 : 하도급대금결제조건공시. Known values are: "A001", "A002", "A003", "A004", "A005", "B001",
         "B002", "B003", "C001", "C002", "C003", "C004", "C005", "C006", "C007", "C008", "C009", "C010",
         "C011", "D001", "D002", "D003", "D004", "E001", "E002", "E003", "E004", "E005", "E006", "E007",
         "E008", "E009", "F001", "F002", "F003", "F004", "F005", "G001", "G002", "G003", "H001", "H002",
         "H003", "H004", "H005", "H006", "I001", "I002", "I003", "I004", "I005", "I006", "J001", "J002",
         "J004", "J005", "J006", "J008", and "J009". Default value is None.
        :paramtype pblntf_detail_ty: str
        :keyword corp_cls: 법인구분


         * Y : 유가증권시장:code:`<br/>`
         * K : 코스닥:code:`<br/>`
         * N : 코넥스:code:`<br/>`
         * E : 기타:code:`<br/>`
           ※ 없으면 전체조회, 복수조건 불가. Known values are: "Y", "K", "N", and "E". Default value is None.
        :paramtype corp_cls: str
        :keyword sort: 정렬


         * date : 접수일자:code:`<br/>`
         * crp : 회사명:code:`<br/>`
         * rpt : 보고서명:code:`<br/>`
           ※ 기본값 : date. Known values are: "date", "crp", and "rpt". Default value is "date".
        :paramtype sort: str
        :keyword sort_mth: 정렬방법


         * asc : 오름차순:code:`<br/>`
         * desc : 내림차순:code:`<br/>`
           ※ 기본값 : desc. Known values are: "asc" and "desc". Default value is "desc".
        :paramtype sort_mth: str
        :keyword page_no: 페이지 번호(1~n):code:`<br/>`
         ※ 기본값 : 1. Default value is 1.
        :paramtype page_no: int
        :keyword page_count: 페이지 별 건수(1~100):code:`<br/>`
         ※ 기본값 : 10:code:`<br/>`
         ※ 최대값 : 100. Default value is 10.
        :paramtype page_count: int
        :return: JSON object
        :rtype: JSON
        :raises ~azure.core.exceptions.HttpResponseError:

        Example:
            .. code-block:: python

                # response body for status code(s): 200
                response == {
                    "result": {
                        "list": [
                            {
                                "corp_cls": "str",  # Optional.
                                  "ubc95"uc778"uad6c"ubd84   * Y :
                                  "uc720"uac00"uc99d"uad8c"uc2dc"uc7a5:code:`<br/>` * K :
                                  "ucf54"uc2a4"ub2e5:code:`<br/>` * N : "ucf54"ub125"uc2a4:code:`<br/>`
                                  * E : "uae30"ud0c0:code:`<br/>`.
                                "corp_code": "str",  # Optional.
                                  "uacf5"uc2dc"ub300"uc0c1"ud68c"uc0ac"uc758
                                  "uace0"uc720"ubc88"ud638(8"uc790"ub9ac).
                                "corp_name": "str",  # Optional.
                                  "uc885"ubaa9"uba85("ubc95"uc778"uba85):code:`<br/>`
                                  "uacf5"uc2dc"ub300"uc0c1"ud68c"uc0ac"uc758
                                  "uc885"ubaa9"uba85("uc0c1"uc7a5"uc0ac) "ub610"ub294
                                  "ubc95"uc778"uba85("uae30"ud0c0"ubc95"uc778).
                                "flr_nm": "str",  # Optional. "uacf5"uc2dc
                                  "uc81c"ucd9c"uc778"uba85.
                                "rcept_dt": "str",  # Optional. "uacf5"uc2dc
                                  "uc811"uc218"uc77c"uc790(YYYYMMDD).
                                "rcept_no": "str",  # Optional.
                                  "uc811"uc218"ubc88"ud638(14"uc790"ub9ac)  "u203b
                                  "uacf5"uc2dc"ubdf0"uc5b4 "uc5f0"uacb0"uc5d0
                                  "uc774"uc6a9"uc608"uc2dc:code:`<br/>`   * PC"uc6a9 :
                                  https://dart.fss.or.kr/dsaf001/main.do?rcpNo="uc811"uc218"ubc88"ud638.
                                "report_nm": "str",  # Optional.
                                  "ubcf4"uace0"uc11c"uba85
                                  "uacf5"uc2dc"uad6c"ubd84+"ubcf4"uace0"uc11c"uba85+"uae30"ud0c0"uc815"ubcf4:code:`<br/>`
                                  ["uae30"uc7ac"uc815"uc815] : "ubcf8
                                  "ubcf4"uace0"uc11c"uba85"uc73c"ub85c "uc774"ubbf8 "uc81c"ucd9c"ub41c
                                  "ubcf4"uace0"uc11c"uc758 "uae30"uc7ac"ub0b4"uc6a9"uc774
                                  "ubcc0"uacbd"ub418"uc5b4 "uc81c"ucd9c"ub41c "uac83"uc784:code:`<br/>`
                                  ["ucca8"ubd80"uc815"uc815] : "ubcf8
                                  "ubcf4"uace0"uc11c"uba85"uc73c"ub85c "uc774"ubbf8 "uc81c"ucd9c"ub41c
                                  "ubcf4"uace0"uc11c"uc758 "ucca8"ubd80"ub0b4"uc6a9"uc774
                                  "ubcc0"uacbd"ub418"uc5b4 "uc81c"ucd9c"ub41c "uac83"uc784:code:`<br/>`
                                  ["ucca8"ubd80"ucd94"uac00] : "ubcf8
                                  "ubcf4"uace0"uc11c"uba85"uc73c"ub85c "uc774"ubbf8 "uc81c"ucd9c"ub41c
                                  "ubcf4"uace0"uc11c"uc758 "ucca8"ubd80"uc11c"ub958"uac00
                                  "ucd94"uac00"ub418"uc5b4 "uc81c"ucd9c"ub41c "uac83"uc784:code:`<br/>`
                                  ["ubcc0"uacbd"ub4f1"ub85d] : "ubcf8
                                  "ubcf4"uace0"uc11c"uba85"uc73c"ub85c "uc774"ubbf8 "uc81c"ucd9c"ub41c
                                  "ubcf4"uace0"uc11c"uc758 "uc720"ub3d9"ud654"uacc4"ud68d"uc774
                                  "ubcc0"uacbd"ub418"uc5b4 "uc81c"ucd9c"ub41c "uac83"uc784:code:`<br/>`
                                  ["uc5f0"uc7a5"uacb0"uc815] : "ubcf8
                                  "ubcf4"uace0"uc11c"uba85"uc73c"ub85c "uc774"ubbf8 "uc81c"ucd9c"ub41c
                                  "ubcf4"uace0"uc11c"uc758 "uc2e0"ud0c1"uacc4"uc57d"uc774
                                  "uc5f0"uc7a5"ub418"uc5b4 "uc81c"ucd9c"ub41c "uac83"uc784:code:`<br/>`
                                  ["ubc1c"ud589"uc870"uac74"ud655"uc815] : "ubcf8
                                  "ubcf4"uace0"uc11c"uba85"uc73c"ub85c "uc774"ubbf8 "uc81c"ucd9c"ub41c
                                  "ubcf4"uace0"uc11c"uc758 "uc720"uac00"uc99d"uad8c
                                  "ubc1c"ud589"uc870"uac74"uc774 "ud655"uc815"ub418"uc5b4
                                  "uc81c"ucd9c"ub41c "uac83"uc784:code:`<br/>`
                                  ["uc815"uc815"uba85"ub839"ubd80"uacfc] : "ubcf8
                                  "ubcf4"uace0"uc11c"uc5d0 "ub300"ud558"uc5ec
                                  "uae08"uc735"uac10"ub3c5"uc6d0"uc774 "uc815"uc815"uba85"ub839"uc744
                                  "ubd80"uacfc"ud55c "uac83"uc784:code:`<br/>`
                                  ["uc815"uc815"uc81c"ucd9c"uc694"uad6c] : "ubcf8
                                  "ubcf4"uace0"uc11c"uc5d0 "ub300"ud558"uc5ec
                                  "uae08"uc735"uac10"ub3c5"uc6d0"uc774
                                  "uc815"uc815"uc81c"ucd9c"uc694"uad6c"uc744 "ubd80"uacfc"ud55c
                                  "uac83"uc784.
                                "rm": "str",  # Optional. "ube44"uace0
                                  "uc870"ud569"ub41c "ubb38"uc790"ub85c "uac01"uac01"uc740
                                  "uc544"ub798"uc640 "uac19"uc740 "uc758"ubbf8"uac00
                                  "uc788"uc74c:code:`<br/>`   * "uc720 : "ubcf8
                                  "uacf5"uc2dc"uc0ac"ud56d"uc740 "ud55c"uad6d"uac70"ub798"uc18c
                                  "uc720"uac00"uc99d"uad8c"uc2dc"uc7a5"ubcf8"ubd80
                                  "uc18c"uad00"uc784:code:`<br/>` * "ucf54 : "ubcf8
                                  "uacf5"uc2dc"uc0ac"ud56d"uc740 "ud55c"uad6d"uac70"ub798"uc18c
                                  "ucf54"uc2a4"ub2e5"uc2dc"uc7a5"ubcf8"ubd80
                                  "uc18c"uad00"uc784:code:`<br/>` * "ucc44 : "ubcf8 "ubb38"uc11c"ub294
                                  "ud55c"uad6d"uac70"ub798"uc18c "ucc44"uad8c"uc0c1"uc7a5"ubc95"uc778
                                  "uacf5"uc2dc"uc0ac"ud56d"uc784:code:`<br/>` * "ub125 : "ubcf8
                                  "ubb38"uc11c"ub294 "ud55c"uad6d"uac70"ub798"uc18c
                                  "ucf54"ub125"uc2a4"uc2dc"uc7a5 "uc18c"uad00"uc784:code:`<br/>` *
                                  "uacf5 : "ubcf8 "uacf5"uc2dc"uc0ac"ud56d"uc740
                                  "uacf5"uc815"uac70"ub798"uc704"uc6d0"ud68c
                                  "uc18c"uad00"uc784:code:`<br/>` * "uc5f0 : "ubcf8
                                  "ubcf4"uace0"uc11c"ub294 "uc5f0"uacb0"ubd80"ubd84"uc744
                                  "ud3ec"ud568"ud55c "uac83"uc784:code:`<br/>` * "uc815 : "ubcf8
                                  "ubcf4"uace0"uc11c "uc81c"ucd9c "ud6c4 "uc815"uc815"uc2e0"uace0"uac00
                                  "uc788"uc73c"ub2c8 "uad00"ub828 "ubcf4"uace0"uc11c"ub97c
                                  "ucc38"uc870"ud558"uc2dc"uae30 "ubc14"ub78c:code:`<br/>` * "ucca0 :
                                  "ubcf8 "ubcf4"uace0"uc11c"ub294
                                  "ucca0"ud68c("uac04"uc8fc)"ub418"uc5c8"uc73c"ub2c8 "uad00"ub828
                                  "ucca0"ud68c"uc2e0"uace0"uc11c("ucca0"ud68c"uac04"uc8fc"uc548"ub0b4)"ub97c
                                  "ucc38"uace0"ud558"uc2dc"uae30 "ubc14"ub78c.
                                "stock_code": "str"  # Optional.
                                  "uc0c1"uc7a5"ud68c"uc0ac"uc758
                                  "uc885"ubaa9"ucf54"ub4dc(6"uc790"ub9ac).
                            }
                        ],
                        "message": "str",  # Optional. "uc5d0"ub7ec "ubc0f "uc815"ubcf4
                          "uba54"uc2dc"uc9c0.
                        "page_count": 0,  # Optional. "ud398"uc774"uc9c0 "ubcc4 "uac74"uc218.
                        "page_no": 0,  # Optional. "ud398"uc774"uc9c0 "ubc88"ud638.
                        "status": "str",  # Optional. "uc5d0"ub7ec "ubc0f
                          "uc815"ubcf4"ucf54"ub4dc  000 :"uc815"uc0c1 010 :"ub4f1"ub85d"ub418"uc9c0
                          "uc54a"uc740 "ud0a4"uc785"ub2c8"ub2e4. 011 :"uc0ac"uc6a9"ud560 "uc218
                          "uc5c6"ub294 "ud0a4"uc785"ub2c8"ub2e4. "uc624"ud508API"uc5d0
                          "ub4f1"ub85d"ub418"uc5c8"uc73c"ub098, "uc77c"uc2dc"uc801"uc73c"ub85c
                          "uc0ac"uc6a9 "uc911"uc9c0"ub41c "ud0a4"ub97c "ud1b5"ud558"uc5ec
                          "uac80"uc0c9"ud558"ub294 "uacbd"uc6b0 "ubc1c"uc0dd"ud569"ub2c8"ub2e4. 012
                          :"uc811"uadfc"ud560 "uc218 "uc5c6"ub294 IP"uc785"ub2c8"ub2e4. 013
                          :"uc870"ud68c"ub41c "ub370"uc774"ud0c0"uac00 "uc5c6"uc2b5"ub2c8"ub2e4. 014
                          :"ud30c"uc77c"uc774 "uc874"uc7ac"ud558"uc9c0 "uc54a"uc2b5"ub2c8"ub2e4. 020
                          :"uc694"uccad "uc81c"ud55c"uc744 "ucd08"uacfc"ud558"uc600"uc2b5"ub2c8"ub2e4.
                          "uc801"uc73c"ub85c"ub294 20,000"uac74 "uc774"uc0c1"uc758 "uc694"uccad"uc5d0
                          "ub300"ud558"uc5ec "uc774 "uc5d0"ub7ec "uba54"uc2dc"uc9c0"uac00
                          "ubc1c"uc0dd"ub418"ub098, "uc694"uccad "uc81c"ud55c"uc774 "ub2e4"ub974"uac8c
                          "uc124"uc815"ub41c "uacbd"uc6b0"uc5d0"ub294 "uc774"uc5d0 "uc900"ud558"uc5ec
                          "ubc1c"uc0dd"ub429"ub2c8"ub2e4. 021 :"uc870"ud68c "uac00"ub2a5"ud55c
                          "ud68c"uc0ac "uac1c"uc218"uac00
                          "ucd08"uacfc"ud558"uc600"uc2b5"ub2c8"ub2e4.("ucd5c"ub300 100"uac74) 100
                          :"ud544"ub4dc"uc758 "ubd80"uc801"uc808"ud55c "uac12"uc785"ub2c8"ub2e4.
                          "ud544"ub4dc "uc124"uba85"uc5d0 "uc5c6"ub294 "uac12"uc744 "uc0ac"uc6a9"ud55c
                          "uacbd"uc6b0"uc5d0 "ubc1c"uc0dd"ud558"ub294
                          "uba54"uc2dc"uc9c0"uc785"ub2c8"ub2e4. 101 :"ubd80"uc801"uc808"ud55c
                          "uc811"uadfc"uc785"ub2c8"ub2e4. 800 :"uc2dc"uc2a4"ud15c
                          "uc810"uac80"uc73c"ub85c "uc778"ud55c "uc11c"ube44"uc2a4"uac00 "uc911"uc9c0
                          "uc911"uc785"ub2c8"ub2e4. 900 :"uc815"uc758"ub418"uc9c0 "uc54a"uc740
                          "uc624"ub958"uac00 "ubc1c"uc0dd"ud558"uc600"uc2b5"ub2c8"ub2e4. 901
                          :"uc0ac"uc6a9"uc790 "uacc4"uc815"uc758 "uac1c"uc778"uc815"ubcf4
                          "ubcf4"uc720"uae30"uac04"uc774 "ub9cc"ub8cc"ub418"uc5b4 "uc0ac"uc6a9"ud560
                          "uc218 "uc5c6"ub294 "ud0a4"uc785"ub2c8"ub2e4. "uad00"ub9ac"uc790
                          "uc774"uba54"uc77c(opendart@fss.or.kr)"ub85c "ubb38"uc758"ud558"uc2dc"uae30
                          "ubc14"ub78d"ub2c8"ub2e4. Known values are: "000", "010", "011", "012",
                          "013", "014", "020", "021", "100", "101", "800", "900", and "901".
                        "total_count": 0,  # Optional. "ucd1d "uac74"uc218.
                        "total_page": 0  # Optional. "ucd1d "ud398"uc774"uc9c0 "uc218.
                    }
                }
        """
        error_map: MutableMapping[int, Type[HttpResponseError]] = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls: ClsType[JSON] = kwargs.pop("cls", None)

        _request = build_gen_open_dart_get_corporate_list_request(
            bgn_de=bgn_de,
            end_de=end_de,
            corp_code=corp_code,
            last_reprt_at=last_reprt_at,
            pblntf_ty=pblntf_ty,
            pblntf_detail_ty=pblntf_detail_ty,
            corp_cls=corp_cls,
            sort=sort,
            sort_mth=sort_mth,
            page_no=page_no,
            page_count=page_count,
            headers=_headers,
            params=_params,
        )
        _request.url = self._client.format_url(_request.url)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            if _stream:
                await response.read()  # Load the body in memory and close the socket
            map_error(
                status_code=response.status_code, response=response, error_map=error_map
            )
            raise HttpResponseError(response=response)

        if response.content:
            deserialized = response.json()
        else:
            deserialized = None

        if cls:
            return cls(pipeline_response, cast(JSON, deserialized), {})  # type: ignore

        return cast(JSON, deserialized)  # type: ignore

    @distributed_trace_async
    async def get_corporate_company(self, *, corp_code: str, **kwargs: Any) -> JSON:
        # pylint: disable=line-too-long
        """기업개황.

        DART에 등록되어있는 기업의 개황정보를 제공합니다.

        :keyword corp_code: 고유번호

         공시대상회사의 고유번호(8자리). Required.
        :paramtype corp_code: str
        :return: JSON object
        :rtype: JSON
        :raises ~azure.core.exceptions.HttpResponseError:

        Example:
            .. code-block:: python

                # response body for status code(s): 200
                response == {
                    "acc_mt": "str",  # Optional. "uacb0"uc0b0"uc6d4(MM).
                    "adres": "str",  # Optional. "uc8fc"uc18c.
                    "bizr_no": "str",  # Optional. "uc0ac"uc5c5"uc790"ub4f1"ub85d"ubc88"ud638.
                    "ceo_nm": "str",  # Optional. "ub300"ud45c"uc790"uba85.
                    "corp_cls": "str",  # Optional. "ubc95"uc778"uad6c"ubd84. Known values are:
                      "Y" and "N".
                    "corp_name": "str",  # Optional. "uc815"uc2dd"uba85"uce6d.
                    "corp_name_eng": "str",  # Optional. "uc601"ubb38"uba85"uce6d.
                    "est_dt": "str",  # Optional. "uc124"ub9bd"uc77c(YYYYMMDD).
                    "fax_no": "str",  # Optional. "ud329"uc2a4"ubc88"ud638.
                    "hm_url": "str",  # Optional. "ud648"ud398"uc774"uc9c0.
                    "induty_code": "str",  # Optional. "uc5c5"uc885"ucf54"ub4dc.
                    "ir_url": "str",  # Optional. IR"ud648"ud398"uc774"uc9c0.
                    "jurir_no": "str",  # Optional. "ubc95"uc778"ub4f1"ub85d"ubc88"ud638.
                    "message": "str",  # Optional. "uc5d0"ub7ec "ubc0f "uc815"ubcf4
                      "uba54"uc2dc"uc9c0.
                    "phn_no": "str",  # Optional. "uc804"ud654"ubc88"ud638.
                    "status": "str",  # Optional. "uc5d0"ub7ec "ubc0f "uc815"ubcf4"ucf54"ub4dc
                      000 :"uc815"uc0c1 010 :"ub4f1"ub85d"ub418"uc9c0 "uc54a"uc740
                      "ud0a4"uc785"ub2c8"ub2e4. 011 :"uc0ac"uc6a9"ud560 "uc218 "uc5c6"ub294
                      "ud0a4"uc785"ub2c8"ub2e4. "uc624"ud508API"uc5d0
                      "ub4f1"ub85d"ub418"uc5c8"uc73c"ub098, "uc77c"uc2dc"uc801"uc73c"ub85c "uc0ac"uc6a9
                      "uc911"uc9c0"ub41c "ud0a4"ub97c "ud1b5"ud558"uc5ec "uac80"uc0c9"ud558"ub294
                      "uacbd"uc6b0 "ubc1c"uc0dd"ud569"ub2c8"ub2e4. 012 :"uc811"uadfc"ud560 "uc218
                      "uc5c6"ub294 IP"uc785"ub2c8"ub2e4. 013 :"uc870"ud68c"ub41c
                      "ub370"uc774"ud0c0"uac00 "uc5c6"uc2b5"ub2c8"ub2e4. 014 :"ud30c"uc77c"uc774
                      "uc874"uc7ac"ud558"uc9c0 "uc54a"uc2b5"ub2c8"ub2e4. 020 :"uc694"uccad
                      "uc81c"ud55c"uc744 "ucd08"uacfc"ud558"uc600"uc2b5"ub2c8"ub2e4.
                      "uc801"uc73c"ub85c"ub294 20,000"uac74 "uc774"uc0c1"uc758 "uc694"uccad"uc5d0
                      "ub300"ud558"uc5ec "uc774 "uc5d0"ub7ec "uba54"uc2dc"uc9c0"uac00
                      "ubc1c"uc0dd"ub418"ub098, "uc694"uccad "uc81c"ud55c"uc774 "ub2e4"ub974"uac8c
                      "uc124"uc815"ub41c "uacbd"uc6b0"uc5d0"ub294 "uc774"uc5d0 "uc900"ud558"uc5ec
                      "ubc1c"uc0dd"ub429"ub2c8"ub2e4. 021 :"uc870"ud68c "uac00"ub2a5"ud55c "ud68c"uc0ac
                      "uac1c"uc218"uac00 "ucd08"uacfc"ud558"uc600"uc2b5"ub2c8"ub2e4.("ucd5c"ub300
                      100"uac74) 100 :"ud544"ub4dc"uc758 "ubd80"uc801"uc808"ud55c
                      "uac12"uc785"ub2c8"ub2e4. "ud544"ub4dc "uc124"uba85"uc5d0 "uc5c6"ub294
                      "uac12"uc744 "uc0ac"uc6a9"ud55c "uacbd"uc6b0"uc5d0 "ubc1c"uc0dd"ud558"ub294
                      "uba54"uc2dc"uc9c0"uc785"ub2c8"ub2e4. 101 :"ubd80"uc801"uc808"ud55c
                      "uc811"uadfc"uc785"ub2c8"ub2e4. 800 :"uc2dc"uc2a4"ud15c "uc810"uac80"uc73c"ub85c
                      "uc778"ud55c "uc11c"ube44"uc2a4"uac00 "uc911"uc9c0 "uc911"uc785"ub2c8"ub2e4. 900
                      :"uc815"uc758"ub418"uc9c0 "uc54a"uc740 "uc624"ub958"uac00
                      "ubc1c"uc0dd"ud558"uc600"uc2b5"ub2c8"ub2e4. 901 :"uc0ac"uc6a9"uc790
                      "uacc4"uc815"uc758 "uac1c"uc778"uc815"ubcf4 "ubcf4"uc720"uae30"uac04"uc774
                      "ub9cc"ub8cc"ub418"uc5b4 "uc0ac"uc6a9"ud560 "uc218 "uc5c6"ub294
                      "ud0a4"uc785"ub2c8"ub2e4. "uad00"ub9ac"uc790
                      "uc774"uba54"uc77c(opendart@fss.or.kr)"ub85c "ubb38"uc758"ud558"uc2dc"uae30
                      "ubc14"ub78d"ub2c8"ub2e4. Known values are: "000", "010", "011", "012", "013",
                      "014", "020", "021", "100", "101", "800", "900", and "901".
                    "stock_code": "str",  # Optional. "uc0c1"uc7a5"ud68c"uc0ac"uc778 "uacbd"uc6b0
                      "uc8fc"uc2dd"uc758 "uc885"ubaa9"ucf54"ub4dc.
                    "stock_name": "str"  # Optional. "uc885"ubaa9"uba85("uc0c1"uc7a5"uc0ac)
                      "ub610"ub294 "uc57d"uc2dd"uba85"uce6d("uae30"ud0c0"ubc95"uc778).
                }
        """
        error_map: MutableMapping[int, Type[HttpResponseError]] = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls: ClsType[JSON] = kwargs.pop("cls", None)

        _request = build_gen_open_dart_get_corporate_company_request(
            corp_code=corp_code,
            headers=_headers,
            params=_params,
        )
        _request.url = self._client.format_url(_request.url)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            if _stream:
                await response.read()  # Load the body in memory and close the socket
            map_error(
                status_code=response.status_code, response=response, error_map=error_map
            )
            raise HttpResponseError(response=response)

        if response.content:
            deserialized = response.json()
        else:
            deserialized = None

        if cls:
            return cls(pipeline_response, cast(JSON, deserialized), {})  # type: ignore

        return cast(JSON, deserialized)  # type: ignore

    @distributed_trace_async
    async def get_corporate_document(
        self, *, rcept_no: str, **kwargs: Any
    ) -> AsyncIterator[bytes]:
        """공시서류원본파일.

        공시보고서 원본파일을 제공합니다.

        :keyword rcept_no: 접수번호. Required.
        :paramtype rcept_no: str
        :return: AsyncIterator[bytes]
        :rtype: AsyncIterator[bytes]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map: MutableMapping[int, Type[HttpResponseError]] = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls: ClsType[AsyncIterator[bytes]] = kwargs.pop("cls", None)

        _request = build_gen_open_dart_get_corporate_document_request(
            rcept_no=rcept_no,
            headers=_headers,
            params=_params,
        )
        _request.url = self._client.format_url(_request.url)

        _stream = True
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            if _stream:
                await response.read()  # Load the body in memory and close the socket
            map_error(
                status_code=response.status_code, response=response, error_map=error_map
            )
            raise HttpResponseError(response=response)

        deserialized = response.iter_bytes()

        if cls:
            return cls(pipeline_response, cast(AsyncIterator[bytes], deserialized), {})  # type: ignore

        return cast(AsyncIterator[bytes], deserialized)  # type: ignore

    @distributed_trace_async
    async def get_corporate_code(self, **kwargs: Any) -> AsyncIterator[bytes]:
        """고유번호.

        DART에 등록되어있는 공시대상회사의 고유번호,회사명,종목코드, 최근변경일자를 파일로 제공합니다.

        :return: AsyncIterator[bytes]
        :rtype: AsyncIterator[bytes]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map: MutableMapping[int, Type[HttpResponseError]] = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls: ClsType[AsyncIterator[bytes]] = kwargs.pop("cls", None)

        _request = build_gen_open_dart_get_corporate_code_request(
            headers=_headers,
            params=_params,
        )
        _request.url = self._client.format_url(_request.url)

        _stream = True
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            if _stream:
                await response.read()  # Load the body in memory and close the socket
            map_error(
                status_code=response.status_code, response=response, error_map=error_map
            )
            raise HttpResponseError(response=response)

        deserialized = response.iter_bytes()

        if cls:
            return cls(pipeline_response, cast(AsyncIterator[bytes], deserialized), {})  # type: ignore

        return cast(AsyncIterator[bytes], deserialized)  # type: ignore
