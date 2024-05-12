import responses

from stock_clue.opendart import OpenDartClient


@responses.activate
def test_list_disclosure(
    mock_opendart_client: OpenDartClient, mock_opendart_client_url: str
):
    expected = {
        "status": "000",
        "message": "정상",
        "page_no": 1,
        "page_count": 10,
        "total_count": 217,
        "total_page": 22,
        "list": [
            {
                "corp_code": "00120182",
                "corp_name": "NH투자증권",
                "stock_code": "005940",
                "corp_cls": "Y",
                "report_nm": "[첨부추가]일괄신고추가서류(파생결합증권-주가연계증권)",
                "rcept_no": "20200117000559",
                "flr_nm": "NH투자증권",
                "rcept_dt": "20200117",
                "rm": "",
            }
        ],
    }
    responses.add(
        responses.GET,
        f"{mock_opendart_client_url}/list.json",
        json=expected,
        status=200,
    )

    resp = mock_opendart_client.list_disclosure_info(
        bgn_de="20210101",
        end_de="20210131",
        page_no="1",
        page_count="10",
    )

    assert resp == expected
