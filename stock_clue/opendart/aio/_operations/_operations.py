# pylint: disable=too-many-lines,too-many-statements
# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator (autorest: 3.10.2, generator: @autorest/python@6.13.15)
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import sys
from typing import Any, Callable, Dict, Optional, Type, TypeVar, cast

from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    ResourceNotModifiedError,
    map_error,
)
from azure.core.pipeline import PipelineResponse
from azure.core.rest import AsyncHttpResponse, HttpRequest
from azure.core.tracing.decorator_async import distributed_trace_async

from ..._operations._operations import build_gen_open_dart_list_disclosure_info_request
from .._vendor import GenOpenDartClientMixinABC

if sys.version_info >= (3, 9):
    from collections.abc import MutableMapping
else:
    from typing import MutableMapping  # type: ignore  # pylint: disable=ungrouped-imports
JSON = MutableMapping[str, Any]  # pylint: disable=unsubscriptable-object
T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class GenOpenDartClientOperationsMixin(GenOpenDartClientMixinABC):

    @distributed_trace_async
    async def list_disclosure_info(
        self,
        *,
        corp_code: Optional[str] = None,
        bgn_de: Optional[str] = None,
        end_de: Optional[str] = None,
        last_reprt_at: Optional[str] = None,
        pblntf_ty: Optional[str] = None,
        pblntf_detail_ty: Optional[str] = None,
        corp_cls: Optional[str] = None,
        sort: Optional[str] = None,
        sort_mth: Optional[str] = None,
        page_no: Optional[str] = None,
        page_count: Optional[str] = None,
        **kwargs: Any
    ) -> JSON:
        # pylint: disable=line-too-long
        """List of Disclosure Information.

        공시검색
        ========

        공시 유형별, 회사별, 날짜별 등 여러가지 조건으로 공시보고서 검색기능을 제공합니다.

        :keyword corp_code: 공시대상회사의 고유번호(8자리). Default value is None.
        :paramtype corp_code: str
        :keyword bgn_de: 시작일
         검색시작 접수일자(YYYYMMDD)
         1) 기본값 : 종료일(end_de)
         2) 고유번호(corp_code)가 없는 경우 검색기간은 3개월로 제한. Default value is None.
        :paramtype bgn_de: str
        :keyword end_de: 검색종료 접수일자(YYYYMMDD)
         1) 기본값 : 당일. Default value is None.
        :paramtype end_de: str
        :keyword last_reprt_at: 최종보고서 검색여부
         최종보고서만 검색여부(Y or N)
         1) 기본값 : N(정정이 있는 경우 최종정정만 검색). Known values are: "Y" and "N". Default value is None.
        :paramtype last_reprt_at: str
        :keyword pblntf_ty: 공시유형
         A : 정기공시
         B: 주요사항보고
         C: 발행공시
         D: 지분공시
         E: 기타공시
         F: 외부감사관련
         G: 펀드공시
         H: 자산유동화
         I: 거래소공시
         J: 공정위공시. Known values are: "A", "B", "C", "D", "E", "F", "G", "H", "I", and "J". Default
         value is None.
        :paramtype pblntf_ty: str
        :keyword pblntf_detail_ty: 공시상세유형. Default value is None.
        :paramtype pblntf_detail_ty: str
        :keyword corp_cls: 법인구분
         Y : 유가증권시장
         K: 코스닥
         N: 코넥스
         E: 기타. Known values are: "Y", "K", "N", and "E". Default value is None.
        :paramtype corp_cls: str
        :keyword sort: 정렬
         접수일자: date
         회사명 : crp
         보고서명 : rpt
         ※ 기본값 : date. Known values are: "date", "crp", and "rpt". Default value is None.
        :paramtype sort: str
        :keyword sort_mth: 정렬방식
         오름차순(asc), 내림차순(desc)
         ※ 기본값 : desc. Known values are: "asc" and "desc". Default value is None.
        :paramtype sort_mth: str
        :keyword page_no: 페이지 번호
         페이지 번호(1~n) 기본값 : 1. Default value is None.
        :paramtype page_no: str
        :keyword page_count: 페이지 별 건수
         페이지당 건수(1~100) 기본값 : 10, 최대값 : 100. Default value is None.
        :paramtype page_count: str
        :return: JSON object
        :rtype: JSON
        :raises ~azure.core.exceptions.HttpResponseError:

        Example:
            .. code-block:: python

                # response body for status code(s): 200
                response == {
                    "list": {
                        "corp_cls": "str",  # Optional. "ubc95"uc778"uad6c"ubd84.
                          Y("uc720"uac00), K("ucf54"uc2a4"ub2e5), N("ucf54"ub125"uc2a4),
                          E("uae30"ud0c0).
                        "corp_code": "str",  # Optional.
                          "uacf5"uc2dc"ub300"uc0c1"ud68c"uc0ac"uc758
                          "uace0"uc720"ubc88"ud638(8"uc790"ub9ac).
                        "corp_name": "str",  # Optional.
                          "uacf5"uc2dc"ub300"uc0c1"ud68c"uc0ac"uc758
                          "uc885"ubaa9"uba85("uc0c1"uc7a5"uc0ac) "ub610"ub294
                          "ubc95"uc778"uba85("uae30"ud0c0"ubc95"uc778).
                        "flr_nm": "str",  # Optional. "uacf5"uc2dc "uc81c"ucd9c"uc778"uba85.
                        "rcept_dt": "str",  # Optional. "uc811"uc218"uc77c"uc790(YYYYMMDD).
                        "rcept_no": "str",  # Optional.
                          "uc811"uc218"ubc88"ud638(14"uc790"ub9ac).
                        "report_nm": "str",  # Optional. "ubcf4"uace0"uc11c"uba85
                          "uacf5"uc2dc"uad6c"ubd84+"ubcf4"uace0"uc11c"uba85+"uae30"ud0c0"uc815"ubcf4
                          ["uae30"uc7ac"uc815"uc815] : "ubcf8 "ubcf4"uace0"uc11c"uba85"uc73c"ub85c
                          "uc774"ubbf8 "uc81c"ucd9c"ub41c "ubcf4"uace0"uc11c"uc758
                          "uae30"uc7ac"ub0b4"uc6a9"uc774 "ubcc0"uacbd"ub418"uc5b4 "uc81c"ucd9c"ub41c
                          "uac83"uc784 ["ucca8"ubd80"uc815"uc815] : "ubcf8
                          "ubcf4"uace0"uc11c"uba85"uc73c"ub85c "uc774"ubbf8 "uc81c"ucd9c"ub41c
                          "ubcf4"uace0"uc11c"uc758 "ucca8"ubd80"ub0b4"uc6a9"uc774
                          "ubcc0"uacbd"ub418"uc5b4 "uc81c"ucd9c"ub41c "uac83"uc784
                          ["ucca8"ubd80"ucd94"uac00] : "ubcf8 "ubcf4"uace0"uc11c"uba85"uc73c"ub85c
                          "uc774"ubbf8 "uc81c"ucd9c"ub41c "ubcf4"uace0"uc11c"uc758
                          "ucca8"ubd80"uc11c"ub958"uac00 "ucd94"uac00"ub418"uc5b4 "uc81c"ucd9c"ub41c
                          "uac83"uc784 ["ubcc0"uacbd"ub4f1"ub85d] : "ubcf8
                          "ubcf4"uace0"uc11c"uba85"uc73c"ub85c "uc774"ubbf8 "uc81c"ucd9c"ub41c
                          "ubcf4"uace0"uc11c"uc758 "uc720"ub3d9"ud654"uacc4"ud68d"uc774
                          "ubcc0"uacbd"ub418"uc5b4 "uc81c"ucd9c"ub41c "uac83"uc784
                          ["uc5f0"uc7a5"uacb0"uc815] : "ubcf8 "ubcf4"uace0"uc11c"uba85"uc73c"ub85c
                          "uc774"ubbf8 "uc81c"ucd9c"ub41c "ubcf4"uace0"uc11c"uc758
                          "uc2e0"ud0c1"uacc4"uc57d"uc774 "uc5f0"uc7a5"ub418"uc5b4 "uc81c"ucd9c"ub41c
                          "uac83"uc784 ["ubc1c"ud589"uc870"uac74"ud655"uc815] : "ubcf8
                          "ubcf4"uace0"uc11c"uba85"uc73c"ub85c "uc774"ubbf8 "uc81c"ucd9c"ub41c
                          "ubcf4"uace0"uc11c"uc758 "uc720"uac00"uc99d"uad8c
                          "ubc1c"ud589"uc870"uac74"uc774 "ud655"uc815"ub418"uc5b4 "uc81c"ucd9c"ub41c
                          "uac83"uc784 ["uc815"uc815"uba85"ub839"ubd80"uacfc] : "ubcf8
                          "ubcf4"uace0"uc11c"uc5d0 "ub300"ud558"uc5ec
                          "uae08"uc735"uac10"ub3c5"uc6d0"uc774 "uc815"uc815"uba85"ub839"uc744
                          "ubd80"uacfc"ud55c "uac83"uc784 ["uc815"uc815"uc81c"ucd9c"uc694"uad6c] :
                          "ubcf8 "ubcf4"uace0"uc11c"uc5d0 "ub300"ud558"uc5ec
                          "uae08"uc735"uac10"ub3c5"uc6d0"uc774
                          "uc815"uc815"uc81c"ucd9c"uc694"uad6c"uc744 "ubd80"uacfc"ud55c "uac83"uc784.
                        "rm": "str",  # Optional. "ube44"uace0  "uc870"ud569"ub41c
                          "ubb38"uc790"ub85c "uac01"uac01"uc740 "uc544"ub798"uc640 "uac19"uc740
                          "uc758"ubbf8"uac00 "uc788"uc74c "uc720 : "ubcf8
                          "uacf5"uc2dc"uc0ac"ud56d"uc740 "ud55c"uad6d"uac70"ub798"uc18c
                          "uc720"uac00"uc99d"uad8c"uc2dc"uc7a5"ubcf8"ubd80 "uc18c"uad00"uc784 "ucf54 :
                          "ubcf8 "uacf5"uc2dc"uc0ac"ud56d"uc740 "ud55c"uad6d"uac70"ub798"uc18c
                          "ucf54"uc2a4"ub2e5"uc2dc"uc7a5"ubcf8"ubd80 "uc18c"uad00"uc784 "ucc44 : "ubcf8
                          "ubb38"uc11c"ub294 "ud55c"uad6d"uac70"ub798"uc18c
                          "ucc44"uad8c"uc0c1"uc7a5"ubc95"uc778 "uacf5"uc2dc"uc0ac"ud56d"uc784 "ub125 :
                          "ubcf8 "ubb38"uc11c"ub294 "ud55c"uad6d"uac70"ub798"uc18c
                          "ucf54"ub125"uc2a4"uc2dc"uc7a5 "uc18c"uad00"uc784 "uacf5 : "ubcf8
                          "uacf5"uc2dc"uc0ac"ud56d"uc740 "uacf5"uc815"uac70"ub798"uc704"uc6d0"ud68c
                          "uc18c"uad00"uc784 "uc5f0 : "ubcf8 "ubcf4"uace0"uc11c"ub294
                          "uc5f0"uacb0"ubd80"ubd84"uc744 "ud3ec"ud568"ud55c "uac83"uc784 "uc815 :
                          "ubcf8 "ubcf4"uace0"uc11c "uc81c"ucd9c "ud6c4 "uc815"uc815"uc2e0"uace0"uac00
                          "uc788"uc73c"ub2c8 "uad00"ub828 "ubcf4"uace0"uc11c"ub97c
                          "ucc38"uc870"ud558"uc2dc"uae30 "ubc14"ub78c "ucca0 : "ubcf8
                          "ubcf4"uace0"uc11c"ub294 "ucca0"ud68c("uac04"uc8fc)"ub418"uc5c8"uc73c"ub2c8
                          "uad00"ub828
                          "ucca0"ud68c"uc2e0"uace0"uc11c("ucca0"ud68c"uac04"uc8fc"uc548"ub0b4)"ub97c
                          "ucc38"uace0"ud558"uc2dc"uae30 "ubc14"ub78c.
                        "stock_code": "str"  # Optional.
                          "uacf5"uc2dc"ub300"uc0c1"ud68c"uc0ac"uc758
                          "uc885"ubaa9"ucf54"ub4dc(6"uc790"ub9ac).
                    },
                    "message": "str",  # Optional. "uc5d0"ub7ec "uc815"ubcf4 "uba54"uc2dc"uc9c0.
                    "page_count": 0,  # Optional. "ud398"uc774"uc9c0 "ubcc4 "uac74"uc218.
                    "page_no": 0,  # Optional. "ud398"uc774"uc9c0 "ubc88"ud638.
                    "status": "str",  # Optional. "uc5d0"ub7ec "uc815"ubcf4 "ucf54"ub4dc   * 000
                      :"uc815"uc0c1 * 010 :"ub4f1"ub85d"ub418"uc9c0 "uc54a"uc740
                      "ud0a4"uc785"ub2c8"ub2e4. * 011 :"uc0ac"uc6a9"ud560 "uc218 "uc5c6"ub294
                      "ud0a4"uc785"ub2c8"ub2e4. "uc624"ud508API"uc5d0
                      "ub4f1"ub85d"ub418"uc5c8"uc73c"ub098, "uc77c"uc2dc"uc801"uc73c"ub85c "uc0ac"uc6a9
                      "uc911"uc9c0"ub41c "ud0a4"ub97c "ud1b5"ud558"uc5ec "uac80"uc0c9"ud558"ub294
                      "uacbd"uc6b0 "ubc1c"uc0dd"ud569"ub2c8"ub2e4. * 012 :"uc811"uadfc"ud560 "uc218
                      "uc5c6"ub294 IP"uc785"ub2c8"ub2e4. * 013 :"uc870"ud68c"ub41c
                      "ub370"uc774"ud0c0"uac00 "uc5c6"uc2b5"ub2c8"ub2e4. * 014 :"ud30c"uc77c"uc774
                      "uc874"uc7ac"ud558"uc9c0 "uc54a"uc2b5"ub2c8"ub2e4. * 020 :"uc694"uccad
                      "uc81c"ud55c"uc744 "ucd08"uacfc"ud558"uc600"uc2b5"ub2c8"ub2e4.   .. code-block::
                      "uc77c"ubc18"uc801"uc73c"ub85c"ub294 20,000"uac74 "uc774"uc0c1"uc758
                      "uc694"uccad"uc5d0 "ub300"ud558"uc5ec "uc774 "uc5d0"ub7ec
                      "uba54"uc2dc"uc9c0"uac00 "ubc1c"uc0dd"ub418"ub098, "uc694"uccad
                      "uc81c"ud55c"uc774 "ub2e4"ub974"uac8c "uc124"uc815"ub41c "uacbd"uc6b0"uc5d0"ub294
                      "uc774"uc5d0 "uc900"ud558"uc5ec "ubc1c"uc0dd"ub429"ub2c8"ub2e4.  * 021
                      :"uc870"ud68c "uac00"ub2a5"ud55c "ud68c"uc0ac "uac1c"uc218"uac00
                      "ucd08"uacfc"ud558"uc600"uc2b5"ub2c8"ub2e4.("ucd5c"ub300 100"uac74) * 100
                      :"ud544"ub4dc"uc758 "ubd80"uc801"uc808"ud55c "uac12"uc785"ub2c8"ub2e4.
                      "ud544"ub4dc "uc124"uba85"uc5d0 "uc5c6"ub294 "uac12"uc744 "uc0ac"uc6a9"ud55c
                      "uacbd"uc6b0"uc5d0 "ubc1c"uc0dd"ud558"ub294 "uba54"uc2dc"uc9c0"uc785"ub2c8"ub2e4.
                      * 101 :"ubd80"uc801"uc808"ud55c "uc811"uadfc"uc785"ub2c8"ub2e4. * 800
                      :"uc2dc"uc2a4"ud15c "uc810"uac80"uc73c"ub85c "uc778"ud55c
                      "uc11c"ube44"uc2a4"uac00 "uc911"uc9c0 "uc911"uc785"ub2c8"ub2e4. * 900
                      :"uc815"uc758"ub418"uc9c0 "uc54a"uc740 "uc624"ub958"uac00
                      "ubc1c"uc0dd"ud558"uc600"uc2b5"ub2c8"ub2e4. * 901 :"uc0ac"uc6a9"uc790
                      "uacc4"uc815"uc758 "uac1c"uc778"uc815"ubcf4 "ubcf4"uc720"uae30"uac04"uc774
                      "ub9cc"ub8cc"ub418"uc5b4 "uc0ac"uc6a9"ud560 "uc218 "uc5c6"ub294
                      "ud0a4"uc785"ub2c8"ub2e4. "uad00"ub9ac"uc790
                      "uc774"uba54"uc77c(opendart@fss.or.kr)"ub85c "ubb38"uc758"ud558"uc2dc"uae30
                      "ubc14"ub78d"ub2c8"ub2e4.
                    "total_count": 0,  # Optional. "ucd1d "uac74"uc218.
                    "total_page": 0  # Optional. "ucd1d "ud398"uc774"uc9c0 "uc218.
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

        _request = build_gen_open_dart_list_disclosure_info_request(
            corp_code=corp_code,
            bgn_de=bgn_de,
            end_de=end_de,
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
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if response.content:
            deserialized = response.json()
        else:
            deserialized = None

        if cls:
            return cls(pipeline_response, cast(JSON, deserialized), {})  # type: ignore

        return cast(JSON, deserialized)  # type: ignore
