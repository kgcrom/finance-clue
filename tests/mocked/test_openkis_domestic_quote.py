import responses

from finance_clue.openkis import OpenKisClient


@responses.activate
def test_domestic_quotation_inquiry_price(
    mock_openkis_client: OpenKisClient, mock_openkis_client_url: str
):
    """국내주식 현재가 시세 조회 mock test"""
    # TODO: expected dict should be in a separate file(fixture)
    expected = {
        "output": {
            "iscd_stat_cls_code": "55",
            "marg_rate": "20.00",
            "rprs_mrkt_kor_name": "KOSPI200",
            "bstp_kor_isnm": "전기.전자",
            "temp_stop_yn": "N",
            "oprc_rang_cont_yn": "N",
            "clpr_rang_cont_yn": "N",
            "crdt_able_yn": "Y",
            "grmn_rate_cls_code": "40",
            "elw_pblc_yn": "Y",
            "stck_prpr": "75700",
            "prdy_vrss": "-1600",
            "prdy_vrss_sign": "5",
            "prdy_ctrt": "-2.07",
            "acml_tr_pbmn": "1109351578979",
            "acml_vol": "14598755",
            "prdy_vrss_vol_rate": "68.90",
            "stck_oprc": "76100",
            "stck_hgpr": "76600",
            "stck_lwpr": "75600",
            "stck_mxpr": "100400",
            "stck_llam": "54200",
            "stck_sdpr": "77300",
            "wghn_avrg_stck_prc": "75990.12",
            "hts_frgn_ehrt": "55.34",
            "frgn_ntby_qty": "-1784782",
            "pgtr_ntby_qty": "-3070030",
            "pvt_scnd_dmrs_prc": "79166",
            "pvt_frst_dmrs_prc": "78232",
            "pvt_pont_val": "77666",
            "pvt_frst_dmsp_prc": "76732",
            "pvt_scnd_dmsp_prc": "76166",
            "dmrs_val": "77950",
            "dmsp_val": "76450",
            "cpfn": "7780",
            "rstc_wdth_prc": "23100",
            "stck_fcam": "100",
            "stck_sspr": "61840",
            "aspr_unit": "100",
            "hts_deal_qty_unit_val": "1",
            "lstn_stcn": "5969782550",
            "hts_avls": "4519125",
            "per": "35.52",
            "pbr": "1.46",
            "stac_month": "12",
            "vol_tnrt": "0.24",
            "eps": "2131.00",
            "bps": "52002.00",
            "d250_hgpr": "86000",
            "d250_hgpr_date": "20240408",
            "d250_hgpr_vrss_prpr_rate": "-11.98",
            "d250_lwpr": "65800",
            "d250_lwpr_date": "20230818",
            "d250_lwpr_vrss_prpr_rate": "15.05",
            "stck_dryy_hgpr": "86000",
            "dryy_hgpr_vrss_prpr_rate": "-11.98",
            "dryy_hgpr_date": "20240408",
            "stck_dryy_lwpr": "70700",
            "dryy_lwpr_vrss_prpr_rate": "7.07",
            "dryy_lwpr_date": "20240118",
            "w52_hgpr": "86000",
            "w52_hgpr_vrss_prpr_ctrt": "-11.98",
            "w52_hgpr_date": "20240408",
            "w52_lwpr": "65800",
            "w52_lwpr_vrss_prpr_ctrt": "15.05",
            "w52_lwpr_date": "20230818",
            "whol_loan_rmnd_rate": "0.16",
            "ssts_yn": "N",
            "stck_shrn_iscd": "005930",
            "fcam_cnnm": "100",
            "cpfn_cnnm": "7,780 억",
            "frgn_hldn_qty": "3303737099",
            "vi_cls_code": "N",
            "ovtm_vi_cls_code": "N",
            "last_ssts_cntg_qty": "40686",
            "invt_caful_yn": "N",
            "mrkt_warn_cls_code": "00",
            "short_over_yn": "N",
            "sltr_yn": "N",
        },
        "rt_cd": "0",
        "msg_cd": "MCA00000",
        "msg1": "정상처리 되었습니다.",
    }

    responses.add(
        responses.GET,
        f"{mock_openkis_client_url}/uapi/domestic-stock/v1/quotations/inquire-price",
        json=expected,
        status=200,
    )

    resp = mock_openkis_client.get_domestic_stock_price(fid_input_iscd="005930")

    assert resp == expected


@responses.activate
def test_domestic_quotation_inquiry_daily_price(
    mock_openkis_client: OpenKisClient, mock_openkis_client_url: str
):
    """국내주식 현재가 일자별 조회 mock test"""
    expected = {
        "output": [
            {
                "stck_cntg_hour": "155922",
                "stck_prpr": "75700",
                "prdy_vrss": "-1600",
                "prdy_vrss_sign": "5",
                "cntg_vol": "2",
                "tday_rltv": "74.95",
                "prdy_ctrt": "-2.07",
            },
            {
                "stck_cntg_hour": "155849",
                "stck_prpr": "75700",
                "prdy_vrss": "-1600",
                "prdy_vrss_sign": "5",
                "cntg_vol": "5",
                "tday_rltv": "74.95",
                "prdy_ctrt": "-2.07",
            },
            {
                "stck_cntg_hour": "155830",
                "stck_prpr": "75700",
                "prdy_vrss": "-1600",
                "prdy_vrss_sign": "5",
                "cntg_vol": "2",
                "tday_rltv": "74.95",
                "prdy_ctrt": "-2.07",
            },
            {
                "stck_cntg_hour": "155810",
                "stck_prpr": "75700",
                "prdy_vrss": "-1600",
                "prdy_vrss_sign": "5",
                "cntg_vol": "2",
                "tday_rltv": "74.95",
                "prdy_ctrt": "-2.07",
            },
            {
                "stck_cntg_hour": "155759",
                "stck_prpr": "75700",
                "prdy_vrss": "-1600",
                "prdy_vrss_sign": "5",
                "cntg_vol": "9",
                "tday_rltv": "74.95",
                "prdy_ctrt": "-2.07",
            },
            {
                "stck_cntg_hour": "155745",
                "stck_prpr": "75700",
                "prdy_vrss": "-1600",
                "prdy_vrss_sign": "5",
                "cntg_vol": "1",
                "tday_rltv": "74.95",
                "prdy_ctrt": "-2.07",
            },
            {
                "stck_cntg_hour": "155632",
                "stck_prpr": "75700",
                "prdy_vrss": "-1600",
                "prdy_vrss_sign": "5",
                "cntg_vol": "1",
                "tday_rltv": "74.95",
                "prdy_ctrt": "-2.07",
            },
            {
                "stck_cntg_hour": "155615",
                "stck_prpr": "75700",
                "prdy_vrss": "-1600",
                "prdy_vrss_sign": "5",
                "cntg_vol": "1",
                "tday_rltv": "74.95",
                "prdy_ctrt": "-2.07",
            },
            {
                "stck_cntg_hour": "155536",
                "stck_prpr": "75700",
                "prdy_vrss": "-1600",
                "prdy_vrss_sign": "5",
                "cntg_vol": "90",
                "tday_rltv": "74.95",
                "prdy_ctrt": "-2.07",
            },
            {
                "stck_cntg_hour": "155519",
                "stck_prpr": "75700",
                "prdy_vrss": "-1600",
                "prdy_vrss_sign": "5",
                "cntg_vol": "1",
                "tday_rltv": "74.95",
                "prdy_ctrt": "-2.07",
            },
            {
                "stck_cntg_hour": "155519",
                "stck_prpr": "75700",
                "prdy_vrss": "-1600",
                "prdy_vrss_sign": "5",
                "cntg_vol": "1000",
                "tday_rltv": "74.95",
                "prdy_ctrt": "-2.07",
            },
            {
                "stck_cntg_hour": "155453",
                "stck_prpr": "75700",
                "prdy_vrss": "-1600",
                "prdy_vrss_sign": "5",
                "cntg_vol": "5",
                "tday_rltv": "74.97",
                "prdy_ctrt": "-2.07",
            },
        ],
        "rt_cd": "0",
        "msg_cd": "MCA00000",
        "msg1": "정상처리 되었습니다.",
    }

    responses.add(
        responses.GET,
        f"{mock_openkis_client_url}/uapi/domestic-stock/v1/quotations/inquire-daily-price",
        json=expected,
        status=200,
    )

    resp = mock_openkis_client.get_domestic_stock_daily_price(
        fid_input_iscd="005930",
        fid_period_div_code="W",
        fid_org_adj_prc="0",
    )

    assert resp == expected


@responses.activate
def test_domestic_stock_daily_price(
    mock_openkis_client: OpenKisClient,
    mock_openkis_client_url: str,
):
    """국내주식 현재가 일자별 조회 mock test"""
    expected = {
        "output": [
            {
                "stck_bsop_date": "20240610",
                "stck_oprc": "76100",
                "stck_hgpr": "76600",
                "stck_lwpr": "75600",
                "stck_clpr": "75700",
                "acml_vol": "14598755",
                "prdy_vrss_vol_rate": "-80.32",
                "prdy_vrss": "-1600",
                "prdy_vrss_sign": "5",
                "prdy_ctrt": "-2.07",
                "hts_frgn_ehrt": "55.34",
                "frgn_ntby_qty": "-1784782",
                "flng_cls_code": "00",
                "acml_prtt_rate": "1.00",
            },
            {
                "stck_bsop_date": "20240603",
                "stck_oprc": "74400",
                "stck_hgpr": "78600",
                "stck_lwpr": "74200",
                "stck_clpr": "77300",
                "acml_vol": "74171638",
                "prdy_vrss_vol_rate": "-49.67",
                "prdy_vrss": "3800",
                "prdy_vrss_sign": "2",
                "prdy_ctrt": "5.17",
                "hts_frgn_ehrt": "55.37",
                "frgn_ntby_qty": "3732278",
                "flng_cls_code": "00",
                "acml_prtt_rate": "0.00",
            },
            {
                "stck_bsop_date": "20240527",
                "stck_oprc": "75300",
                "stck_hgpr": "78200",
                "stck_lwpr": "73500",
                "stck_clpr": "73500",
                "acml_vol": "147359198",
                "prdy_vrss_vol_rate": "48.42",
                "prdy_vrss": "-2400",
                "prdy_vrss_sign": "5",
                "prdy_ctrt": "-3.16",
                "hts_frgn_ehrt": "55.31",
                "frgn_ntby_qty": "-28820600",
                "flng_cls_code": "00",
                "acml_prtt_rate": "0.00",
            },
            {
                "stck_bsop_date": "20240520",
                "stck_oprc": "78100",
                "stck_hgpr": "79100",
                "stck_lwpr": "75700",
                "stck_clpr": "75900",
                "acml_vol": "99288237",
                "prdy_vrss_vol_rate": "47.48",
                "prdy_vrss": "-1500",
                "prdy_vrss_sign": "5",
                "prdy_ctrt": "-1.94",
                "hts_frgn_ehrt": "55.79",
                "frgn_ntby_qty": "-6259092",
                "flng_cls_code": "00",
                "acml_prtt_rate": "0.00",
            },
        ],
        "rt_cd": "0",
        "msg_cd": "MCA00000",
        "msg1": "정상처리 되었습니다.",
    }

    responses.add(
        responses.GET,
        f"{mock_openkis_client_url}/uapi/domestic-stock/v1/quotations/inquire-daily-price",
        json=expected,
        status=200,
    )

    resp = mock_openkis_client.get_domestic_stock_daily_price(
        fid_input_iscd="005930",
        fid_period_div_code="W",
        fid_org_adj_prc="0",
    )

    assert resp == expected


@responses.activate
def test_domestic_stock_quote_and_expected_conclusion(
    mock_openkis_client: OpenKisClient,
    mock_openkis_client_url: str,
):
    """국내주식 현재가 호가/예상체결 조회 mock test"""
    expected = {
        "output1": {
            "aspr_acpt_hour": "160000",
            "askp1": "75800",
            "askp2": "75900",
            "askp3": "76000",
            "askp4": "76100",
            "askp5": "76200",
            "askp6": "76300",
            "askp7": "76400",
            "askp8": "76500",
            "askp9": "76600",
            "askp10": "76700",
            "bidp1": "75700",
            "bidp2": "75600",
            "bidp3": "75500",
            "bidp4": "75400",
            "bidp5": "75300",
            "bidp6": "75200",
            "bidp7": "75100",
            "bidp8": "75000",
            "bidp9": "74900",
            "bidp10": "74800",
            "askp_rsqn1": "41846",
            "askp_rsqn2": "12531",
            "askp_rsqn3": "10503",
            "askp_rsqn4": "178397",
            "askp_rsqn5": "50195",
            "askp_rsqn6": "30873",
            "askp_rsqn7": "50728",
            "askp_rsqn8": "69934",
            "askp_rsqn9": "108354",
            "askp_rsqn10": "35543",
            "bidp_rsqn1": "312258",
            "bidp_rsqn2": "347570",
            "bidp_rsqn3": "379261",
            "bidp_rsqn4": "122962",
            "bidp_rsqn5": "108556",
            "bidp_rsqn6": "73542",
            "bidp_rsqn7": "121337",
            "bidp_rsqn8": "382195",
            "bidp_rsqn9": "59117",
            "bidp_rsqn10": "60022",
            "askp_rsqn_icdc1": "0",
            "askp_rsqn_icdc2": "0",
            "askp_rsqn_icdc3": "0",
            "askp_rsqn_icdc4": "0",
            "askp_rsqn_icdc5": "0",
            "askp_rsqn_icdc6": "0",
            "askp_rsqn_icdc7": "0",
            "askp_rsqn_icdc8": "0",
            "askp_rsqn_icdc9": "0",
            "askp_rsqn_icdc10": "0",
            "bidp_rsqn_icdc1": "0",
            "bidp_rsqn_icdc2": "0",
            "bidp_rsqn_icdc3": "0",
            "bidp_rsqn_icdc4": "0",
            "bidp_rsqn_icdc5": "0",
            "bidp_rsqn_icdc6": "0",
            "bidp_rsqn_icdc7": "0",
            "bidp_rsqn_icdc8": "0",
            "bidp_rsqn_icdc9": "0",
            "bidp_rsqn_icdc10": "0",
            "total_askp_rsqn": "588904",
            "total_bidp_rsqn": "1966820",
            "total_askp_rsqn_icdc": "0",
            "total_bidp_rsqn_icdc": "0",
            "ovtm_total_askp_icdc": "0",
            "ovtm_total_bidp_icdc": "0",
            "ovtm_total_askp_rsqn": "0",
            "ovtm_total_bidp_rsqn": "27606",
            "ntby_aspr_rsqn": "1377916",
            "new_mkop_cls_code": "31",
        },
        "output2": {
            "antc_mkop_cls_code": "112",
            "stck_prpr": "75700",
            "stck_oprc": "76100",
            "stck_hgpr": "76600",
            "stck_lwpr": "75600",
            "stck_sdpr": "77300",
            "antc_cnpr": "75700",
            "antc_cntg_vrss_sign": "5",
            "antc_cntg_vrss": "-1600",
            "antc_cntg_prdy_ctrt": "-2.07",
            "antc_vol": "1000673",
            "stck_shrn_iscd": "005930",
            "vi_cls_code": "N",
        },
        "rt_cd": "0",
        "msg_cd": "MCA00000",
        "msg1": "정상처리 되었습니다.",
    }

    responses.add(
        responses.GET,
        f"{mock_openkis_client_url}/uapi/domestic-stock/v1/quotations/inquire-asking-price-exp-ccn",
        json=expected,
        status=200,
    )

    resp = mock_openkis_client.get_domestic_stock_quote_and_expected_conclusion(
        fid_input_iscd="005930"
    )

    assert resp == expected


@responses.activate
def test_domestic_stock_invest(
    mock_openkis_client: OpenKisClient, mock_openkis_client_url: str
):
    """국내주식 현재가 투자자 mock test"""
    expected = {
        "output": [
            {
                "stck_bsop_date": "20240611",
                "stck_clpr": "75700",
                "prdy_vrss": "0",
                "prdy_vrss_sign": "0",
                "prsn_ntby_qty": "",
                "frgn_ntby_qty": "",
                "orgn_ntby_qty": "",
                "prsn_ntby_tr_pbmn": "",
                "frgn_ntby_tr_pbmn": "",
                "orgn_ntby_tr_pbmn": "",
                "prsn_shnu_vol": "",
                "frgn_shnu_vol": "",
                "orgn_shnu_vol": "",
                "prsn_shnu_tr_pbmn": "",
                "frgn_shnu_tr_pbmn": "",
                "orgn_shnu_tr_pbmn": "",
                "prsn_seln_vol": "",
                "frgn_seln_vol": "",
                "orgn_seln_vol": "",
                "prsn_seln_tr_pbmn": "",
                "frgn_seln_tr_pbmn": "",
                "orgn_seln_tr_pbmn": "",
            },
            {
                "stck_bsop_date": "20240610",
                "stck_clpr": "75700",
                "prdy_vrss": "-1600",
                "prdy_vrss_sign": "5",
                "prsn_ntby_qty": "4101492",
                "frgn_ntby_qty": "-1893335",
                "orgn_ntby_qty": "-2315098",
                "prsn_ntby_tr_pbmn": "311359",
                "frgn_ntby_tr_pbmn": "-143714",
                "orgn_ntby_tr_pbmn": "-175760",
                "prsn_shnu_vol": "6871840",
                "frgn_shnu_vol": "3111002",
                "orgn_shnu_vol": "4458284",
                "prsn_shnu_tr_pbmn": "521948",
                "frgn_shnu_tr_pbmn": "236549",
                "orgn_shnu_tr_pbmn": "338887",
                "prsn_seln_vol": "2770348",
                "frgn_seln_vol": "5004337",
                "orgn_seln_vol": "6773382",
                "prsn_seln_tr_pbmn": "210588",
                "frgn_seln_tr_pbmn": "380262",
                "orgn_seln_tr_pbmn": "514646",
            },
        ],
        "rt_cd": "0",
        "msg_cd": "MCA00000",
        "msg1": "정상처리 되었습니다.",
    }

    responses.add(
        responses.GET,
        f"{mock_openkis_client_url}/uapi/domestic-stock/v1/quotations/inquire-investor",
        json=expected,
        status=200,
    )

    resp = mock_openkis_client.get_domestic_stock_investor(
        fid_input_iscd="005930",
    )

    assert resp == expected


@responses.activate
def test_domestic_stock_period_price(
    mock_openkis_client: OpenKisClient, mock_openkis_client_url: str
):
    """"""
    expected = {
        "output1": {
            "prdy_vrss": "0",
            "prdy_vrss_sign": "3",
            "prdy_ctrt": "0.00",
            "stck_prdy_clpr": "75700",
            "acml_vol": "0",
            "acml_tr_pbmn": "0",
            "hts_kor_isnm": "삼성전자",
            "stck_prpr": "75700",
            "stck_shrn_iscd": "005930",
            "prdy_vol": "14598755",
            "stck_mxpr": "98400",
            "stck_llam": "53000",
            "stck_oprc": "0",
            "stck_hgpr": "0",
            "stck_lwpr": "0",
            "stck_prdy_oprc": "76100",
            "stck_prdy_hgpr": "76600",
            "stck_prdy_lwpr": "75600",
            "askp": "0",
            "bidp": "0",
            "prdy_vrss_vol": "-14598755",
            "vol_tnrt": "0.00",
            "stck_fcam": "100",
            "lstn_stcn": "5969782550",
            "cpfn": "7780",
            "hts_avls": "4519125",
            "per": "35.52",
            "eps": "2131.00",
            "pbr": "1.46",
            "itewhol_loan_rmnd_ratem name": "0.16",
        },
        "output2": [
            {
                "stck_bsop_date": "20240510",
                "stck_clpr": "79200",
                "stck_oprc": "80400",
                "stck_hgpr": "81100",
                "stck_lwpr": "78900",
                "acml_vol": "16976124",
                "acml_tr_pbmn": "1351235284800",
                "flng_cls_code": "00",
                "prtt_rate": "0.00",
                "mod_yn": "N",
                "prdy_vrss_sign": "5",
                "prdy_vrss": "-500",
                "revl_issu_reas": "",
            }
        ],
        "rt_cd": "0",
        "msg_cd": "MCA00000",
        "msg1": "정상처리 되었습니다.",
    }

    responses.add(
        responses.GET,
        f"{mock_openkis_client_url}/uapi/domestic-stock/v1/quotations/inquire-daily-itemchartprice",
        json=expected,
        status=200,
    )

    resp = mock_openkis_client.get_domestic_stock_period_price(
        fid_input_iscd="005930",
        fid_input_date1="20240410",
        fid_input_date2="20240510",
        fid_period_div_code="D",
        fid_org_adj_prc="0",
    )

    assert resp == expected


@responses.activate
def test_domestic_stock_time_conclusion(
    mock_openkis_client: OpenKisClient, mock_openkis_client_url: str
):
    """국내주식 현재가 당일시간대별체결 조회 mock test"""
    expected = {
        "output1": {
            "stck_prpr": "75200",
            "prdy_vrss": "-500",
            "prdy_vrss_sign": "5",
            "prdy_ctrt": "-0.66",
            "acml_vol": "16971175",
            "prdy_vol": "14598755",
            "rprs_mrkt_kor_name": "KOSPI200",
        },
        "output2": [
            {
                "stck_cntg_hour": "154957",
                "stck_prpr": "75200",
                "prdy_vrss": "-500",
                "prdy_vrss_sign": "5",
                "prdy_ctrt": "-0.66",
                "askp": "75300",
                "bidp": "75200",
                "tday_rltv": "75.94",
                "acml_vol": "16649559",
                "cnqn": "4",
            }
        ],
        "rt_cd": "0",
        "msg_cd": "MCA00000",
        "msg1": "정상처리 되었습니다.",
    }

    responses.add(
        responses.GET,
        f"{mock_openkis_client_url}/uapi/domestic-stock/v1/quotations/inquire-time-itemconclusion",
        json=expected,
        status=200,
    )

    resp = mock_openkis_client.get_domestic_stock_time_conclusion(
        fid_input_iscd="005930",
        fid_input_hour1="155000",
    )

    assert resp == expected


@responses.activate
def test_domestic_stock_over_time_conclusion(
    mock_openkis_client: OpenKisClient, mock_openkis_client_url: str
):
    """국내주식 현재가 시간외시간별체결 조회 mock test"""
    expected = {
        "output1": {
            "ovtm_untp_prpr": "75300",
            "ovtm_untp_prdy_vrss": "100",
            "ovtm_untp_prdy_vrss_sign": "2",
            "ovtm_untp_prdy_ctrt": "0.13",
            "ovtm_untp_vol": "57438",
            "ovtm_untp_tr_pbmn": "4327338700",
            "ovtm_untp_mxpr": "82700",
            "ovtm_untp_llam": "67700",
            "ovtm_untp_oprc": "75300",
            "ovtm_untp_hgpr": "75400",
            "ovtm_untp_lwpr": "75300",
            "ovtm_untp_antc_cnpr": "0",
            "ovtm_untp_antc_cntg_vrss": "0",
            "ovtm_untp_antc_cntg_vrss_sign": "3",
            "ovtm_untp_antc_cntg_ctrt": "0.00",
            "ovtm_untp_antc_vol": "0",
            "uplm_sign": "1",
            "lslm_sign": "4",
        },
        "output2": [
            {
                "stck_cntg_hour": "180016",
                "stck_prpr": "75300",
                "prdy_vrss": "100",
                "prdy_vrss_sign": "2",
                "prdy_ctrt": "0.13",
                "askp": "75400",
                "bidp": "75300",
                "acml_vol": "57438",
                "cntg_vol": "8887",
            }
        ],
        "rt_cd": "0",
        "msg_cd": "MCA00000",
        "msg1": "정상처리 되었습니다.",
    }

    responses.add(
        responses.GET,
        f"{mock_openkis_client_url}/uapi/domestic-stock/v1/quotations/inquire-time-overtimeconclusion",
        json=expected,
        status=200,
    )

    resp = mock_openkis_client.get_domestic_stock_over_time_conclusion(
        fid_input_iscd="005930",
    )

    assert resp == expected


@responses.activate
def test_domestic_stock_over_time_daily_price(
    mock_openkis_client: OpenKisClient, mock_openkis_client_url: str
):
    """국내주식 시간외일자별 주가 조회 integrated test"""
    expected = {
        "output1": {
            "ovtm_untp_prpr": "75300",
            "ovtm_untp_prdy_vrss": "100",
            "ovtm_untp_prdy_vrss_sign": "2",
            "ovtm_untp_prdy_ctrt": "0.13",
            "ovtm_untp_vol": "57438",
            "ovtm_untp_tr_pbmn": "4327338700",
            "ovtm_untp_mxpr": "82700",
            "ovtm_untp_llam": "67700",
            "ovtm_untp_oprc": "75300",
            "ovtm_untp_hgpr": "75400",
            "ovtm_untp_lwpr": "75300",
            "ovtm_untp_antc_cnpr": "0",
            "ovtm_untp_antc_cntg_vrss": "0",
            "ovtm_untp_antc_cntg_vrss_sign": "3",
            "ovtm_untp_antc_cntg_ctrt": "0.00",
            "ovtm_untp_antc_vol": "0",
        },
        "output2": [
            {
                "stck_bsop_date": "20240611",
                "ovtm_untp_prpr": "75300",
                "ovtm_untp_prdy_vrss": "100",
                "ovtm_untp_prdy_vrss_sign": "2",
                "ovtm_untp_prdy_ctrt": "0.13",
                "ovtm_untp_vol": "57438",
                "stck_clpr": "75200",
                "prdy_vrss": "-500",
                "prdy_vrss_sign": "5",
                "prdy_ctrt": "-0.66",
                "acml_vol": "16971176",
                "ovtm_untp_tr_pbmn": "4327338700",
            }
        ],
        "rt_cd": "0",
        "msg_cd": "MCA00000",
        "msg1": "정상처리 되었습니다.",
    }

    responses.add(
        responses.GET,
        f"{mock_openkis_client_url}/uapi/domestic-stock/v1/quotations/inquire-daily-overtimeprice",
        json=expected,
        status=200,
    )

    resp = mock_openkis_client.get_domestic_stock_over_time_daily_price(
        fid_input_iscd="005930",
    )
    assert resp == expected


@responses.activate
def test_domestic_stock_time_minute_price(
    mock_openkis_client: OpenKisClient, mock_openkis_client_url: str
):
    """국내주식 당일분봉 조회 mock test"""
    expected = {
        "output1": {
            "prdy_vrss": "-500",
            "prdy_vrss_sign": "5",
            "prdy_ctrt": "-0.66",
            "stck_prdy_clpr": "75700",
            "acml_vol": "16971175",
            "acml_tr_pbmn": "1280831574634",
            "hts_kor_isnm": "삼성전자",
            "stck_prpr": "75200",
        },
        "output2": [
            {
                "stck_bsop_date": "20240611",
                "stck_cntg_hour": "125000",
                "stck_prpr": "75300",
                "stck_oprc": "75300",
                "stck_hgpr": "75400",
                "stck_lwpr": "75300",
                "cntg_vol": "69449",
                "acml_tr_pbmn": "677732980500",
            },
            {
                "stck_bsop_date": "20240611",
                "stck_cntg_hour": "124900",
                "stck_prpr": "75300",
                "stck_oprc": "75300",
                "stck_hgpr": "75400",
                "stck_lwpr": "75300",
                "cntg_vol": "19914",
                "acml_tr_pbmn": "672499305400",
            },
        ],
        "rt_cd": "0",
        "msg_cd": "MCA00000",
        "msg1": "정상처리 되었습니다.",
    }
    responses.add(
        responses.GET,
        f"{mock_openkis_client_url}/uapi/domestic-stock/v1/quotations/inquire-time-itemchartprice",
        json=expected,
        status=200,
    )
    resp = mock_openkis_client.get_domestic_stock_time_minute_price(
        fid_input_iscd="005930",
        fid_input_hour1="125000",
    )

    assert resp == expected


@responses.activate
def test_domestic_stock_price2(
    mock_openkis_client: OpenKisClient, mock_openkis_client_url: str
):
    """국내주식 현재가 시세2 조회 mock test"""

    expected = {
        "output": {
            "rprs_mrkt_kor_name": "KOSPI200",
            "insn_pbnt_yn": "N",
            "stck_prpr": "75200",
            "prdy_vrss": "-500",
            "prdy_vrss_sign": "5",
            "prdy_ctrt": "-0.66",
            "acml_tr_pbmn": "1280831574634",
            "acml_vol": "16971175",
            "prdy_vol": "14598755",
            "prdy_vrss_vol_rate": "116.25",
            "bstp_kor_isnm": "전기.전자",
            "sltr_yn": "N",
            "mang_issu_yn": "N",
            "trht_yn": "N",
            "oprc_rang_cont_yn": "N",
            "vlnt_fin_cls_code": "N",
            "stck_prdy_clpr": "75700",
            "stck_oprc": "75900",
            "prdy_clpr_vrss_oprc_rate": "0.26",
            "oprc_vrss_prpr_sign": "5",
            "oprc_vrss_prpr": "-700",
            "stck_hgpr": "76000",
            "prdy_clpr_vrss_hgpr_rate": "0.40",
            "hgpr_vrss_prpr_sign": "5",
            "hgpr_vrss_prpr": "-800",
            "stck_lwpr": "75100",
            "prdy_clpr_vrss_lwpr_rate": "-0.79",
            "lwpr_vrss_prpr_sign": "2",
            "lwpr_vrss_prpr": "100",
            "marg_rate": "20.00",
            "crdt_rate": "20.00",
            "crdt_able_yn": "Y",
            "elw_pblc_yn": "Y",
            "stck_mxpr": "98400",
            "stck_llam": "53000",
            "bstp_cls_code": "005930",
            "stck_sdpr": "75700",
            "vlnt_deal_cls_name": " ",
            "new_lstn_cls_name": "        ",
            "divi_app_cls_code": "  ",
            "short_over_cls_code": "          ",
            "vi_cls_code": "N",
            "low_current_yn": "N",
            "ssts_hot_yn": " ",
            "stange_runup_yn": "N",
            "invt_caful_yn": "N",
            "mrkt_warn_cls_code": "00",
            "short_over_yn": "N",
        },
        "rt_cd": "0",
        "msg_cd": "MCA00000",
        "msg1": "정상처리 되었습니다.",
    }

    responses.add(
        responses.GET,
        f"{mock_openkis_client_url}/uapi/domestic-stock/v1/quotations/inquire-price-2",
        json=expected,
        status=200,
    )

    resp = mock_openkis_client.get_domestic_stock_price2(fid_input_iscd="005930")
    assert resp == expected


@responses.activate
def test_domestic_stock_over_time_price(
    mock_openkis_client: OpenKisClient, mock_openkis_client_url: str
):
    """국내주식 시간외현재가 조회 mock test"""
    expected = {
        "output": {
            "bstp_kor_isnm": "전기.전자",
            "ovtm_untp_prpr": "76300",
            "ovtm_untp_prdy_vrss": "-200",
            "ovtm_untp_prdy_vrss_sign": "5",
            "ovtm_untp_prdy_ctrt": "-0.26",
            "ovtm_untp_vol": "114141",
            "ovtm_untp_tr_pbmn": "8715131400",
            "ovtm_untp_mxpr": "84100",
            "ovtm_untp_llam": "68900",
            "ovtm_untp_oprc": "76400",
            "ovtm_untp_hgpr": "76400",
            "ovtm_untp_lwpr": "76300",
            "marg_rate": "20.00",
            "ovtm_untp_antc_cnpr": "0",
            "ovtm_untp_antc_cntg_vrss": "0",
            "ovtm_untp_antc_cntg_vrss_sign": "3",
            "ovtm_untp_antc_cntg_ctrt": "0.00",
            "ovtm_untp_antc_cnqn": "0",
            "crdt_able_yn": "Y",
            "new_lstn_cls_name": "        ",
            "sltr_yn": "N",
            "mang_issu_yn": "N",
            "mrkt_warn_cls_code": "00",
            "trht_yn": "N",
            "vlnt_deal_cls_name": " ",
            "ovtm_untp_sdpr": "76500",
            "insn_pbnt_yn": "N",
            "rprs_mrkt_kor_name": "KOSPI200",
            "ovtm_vi_cls_code": "N",
            "bidp": "76400",
            "askp": "76500",
        },
        "rt_cd": "0",
        "msg_cd": "MCA00000",
        "msg1": "정상처리 되었습니다.",
    }

    responses.add(
        responses.GET,
        f"{mock_openkis_client_url}/uapi/domestic-stock/v1/quotations/inquire-overtime-price",
        json=expected,
        status=200,
    )
    resp = mock_openkis_client.get_domestic_stock_over_time_price(
        fid_input_iscd="005930",
    )

    assert resp == expected


@responses.activate
def test_domestic_stock_over_time_quote(
    mock_openkis_client: OpenKisClient, mock_openkis_client_url: str
):
    """국내주식 시간외호가 조회 mock test"""
    expected = {
        "ovtm_untp_last_hour": "180014",
        "ovtm_untp_askp1": "76400",
        "ovtm_untp_askp2": "76500",
        "ovtm_untp_askp3": "76600",
        "ovtm_untp_askp4": "76700",
        "ovtm_untp_askp5": "76800",
        "ovtm_untp_askp6": "76900",
        "ovtm_untp_askp7": "77000",
        "ovtm_untp_askp8": "77100",
        "ovtm_untp_askp9": "77200",
        "ovtm_untp_askp10": "77300",
        "ovtm_untp_bidp1": "76300",
        "ovtm_untp_bidp2": "76200",
        "ovtm_untp_bidp3": "76100",
        "ovtm_untp_bidp4": "76000",
        "ovtm_untp_bidp5": "75900",
        "ovtm_untp_bidp6": "75800",
        "ovtm_untp_bidp7": "75700",
        "ovtm_untp_bidp8": "75600",
        "ovtm_untp_bidp9": "75500",
        "ovtm_untp_bidp10": "75400",
        "ovtm_untp_askp_icdc1": "0",
        "ovtm_untp_askp_icdc2": "0",
        "ovtm_untp_askp_icdc3": "0",
        "ovtm_untp_bidp_icdc1": "0",
        "ovtm_untp_bidp_icdc2": "0",
        "ovtm_untp_bidp_icdc3": "0",
        "ovtm_untp_askp_rsqn1": "12408",
        "ovtm_untp_askp_rsqn2": "19023",
        "ovtm_untp_askp_rsqn3": "10262",
        "ovtm_untp_askp_rsqn4": "9273",
        "ovtm_untp_askp_rsqn5": "5104",
        "ovtm_untp_askp_rsqn6": "3911",
        "ovtm_untp_askp_rsqn7": "7323",
        "ovtm_untp_askp_rsqn8": "2862",
        "ovtm_untp_askp_rsqn9": "699",
        "ovtm_untp_askp_rsqn10": "1039",
        "ovtm_untp_bidp_rsqn1": "6325",
        "ovtm_untp_bidp_rsqn2": "9159",
        "ovtm_untp_bidp_rsqn3": "9338",
        "ovtm_untp_bidp_rsqn4": "5478",
        "ovtm_untp_bidp_rsqn5": "1114",
        "ovtm_untp_bidp_rsqn6": "447",
        "ovtm_untp_bidp_rsqn7": "133",
        "ovtm_untp_bidp_rsqn8": "161",
        "ovtm_untp_bidp_rsqn9": "964",
        "ovtm_untp_bidp_rsqn10": "1166",
        "ovtm_untp_total_askp_rsqn": "71904",
        "ovtm_untp_total_bidp_rsqn": "34285",
        "ovtm_untp_total_askp_rsqn_icdc": "30211",
        "ovtm_untp_total_bidp_rsqn_icdc": "9463",
        "ovtm_untp_ntby_bidp_rsqn": "-37619",
        "total_askp_rsqn": "842462",
        "total_bidp_rsqn": "637237",
        "total_askp_rsqn_icdc": "0",
        "total_bidp_rsqn_icdc": "0",
        "ovtm_total_askp_rsqn": "41880",
        "ovtm_total_bidp_rsqn": "0",
        "ovtm_total_askp_icdc": "0",
        "ovtm_total_bidp_icdc": "0",
    }

    responses.add(
        responses.GET,
        f"{mock_openkis_client_url}/uapi/domestic-stock/v1/quotations/inquire-overtime-asking-price",
        json=expected,
        status=200,
    )
    resp = mock_openkis_client.get_domestic_stock_over_time_quote(
        fid_input_iscd="005930",
    )

    assert resp == expected


@responses.activate
def test_domestic_stock_closing_expected_conclusion(
    mock_openkis_client: OpenKisClient, mock_openkis_client_url: str
):
    """국내주식 장마감 예상체결가 조회 mock test"""

    expected = {
        "output": [
            {
                "stck_shrn_iscd": "000020",
                "hts_kor_isnm": "동화약품",
                "stck_prpr": "8140",
                "prdy_vrss": "60",
                "prdy_vrss_sign": "2",
                "prdy_ctrt": "0.74",
                "sdpr_vrss_prpr": "0",
                "sdpr_vrss_prpr_rate": "0.00",
                "cntg_vol": "326",
            },
            {
                "stck_shrn_iscd": "000040",
                "hts_kor_isnm": "KR모터스",
                "stck_prpr": "643",
                "prdy_vrss": "-13",
                "prdy_vrss_sign": "5",
                "prdy_ctrt": "-1.98",
                "sdpr_vrss_prpr": "0",
                "sdpr_vrss_prpr_rate": "0.00",
                "cntg_vol": "12051",
            },
        ],
        "rt_cd": "0",
        "msg_cd": "MCA00000",
        "msg1": "정상처리 되었습니다.",
    }

    responses.add(
        responses.GET,
        f"{mock_openkis_client_url}/uapi/domestic-stock/v1/quotations/exp-closing-price",
        json=expected,
        status=200,
    )

    resp = mock_openkis_client.get_domestic_stock_closing_expected_conclusion(
        fid_input_iscd="0000"
    )
    assert resp == expected


@responses.activate
def test_domestic_stock_vi_status(
    mock_openkis_client: OpenKisClient, mock_openkis_client_url: str
):
    expected = {
        "output": [
            {
                "hts_kor_isnm": "유아이디",
                "mksc_shrn_iscd": "069330",
                "vi_cls_code": "N",
                "bsop_date": "20240126",
                "cntg_vi_hour": "180030",
                "vi_cncl_hour": "180242",
                "vi_kind_code": "2",
                "vi_prc": "1523",
                "vi_stnd_prc": "0",
                "vi_dprt": "0.00",
                "vi_dmc_stnd_prc": "1640",
                "vi_dmc_dprt": "-7.13",
                "vi_count": "2",
            },
            {
                "hts_kor_isnm": "성창기업지주",
                "mksc_shrn_iscd": "000180",
                "vi_cls_code": "N",
                "bsop_date": "20240126",
                "cntg_vi_hour": "175030",
                "vi_cncl_hour": "175252",
                "vi_kind_code": "2",
                "vi_prc": "1857",
                "vi_stnd_prc": "0",
                "vi_dprt": "0.00",
                "vi_dmc_stnd_prc": "1992",
                "vi_dmc_dprt": "-6.78",
                "vi_count": "3",
            },
        ],
        "rt_cd": "0",
        "msg_cd": "MCA00000",
        "msg1": "정상처리 되었습니다.",
    }

    responses.add(
        responses.GET,
        f"{mock_openkis_client_url}/uapi/domestic-stock/v1/quotations/inquire-vi-status",
        json=expected,
        status=200,
    )
    resp = mock_openkis_client.get_vi_status(
        fid_input_iscd="",
        fid_input_date1="20240126",
        fid_rank_sort_cls_code="1",
        fid_trgt_cls_code="",
        fid_trgt_exls_cls_code="",
    )

    assert resp == expected


@responses.activate
def test_domestic_stock_credit_by_company(
    mock_openkis_client: OpenKisClient, mock_openkis_client_url: str
):
    expected = {
        "output": [
            {
                "stck_shrn_iscd": "000020",
                "hts_kor_isnm": "동화약품",
                "crdt_rate": "60.00",
            },
            {
                "stck_shrn_iscd": "000070",
                "hts_kor_isnm": "삼양홀딩스",
                "crdt_rate": "40.00",
            },
            {
                "stck_shrn_iscd": "000080",
                "hts_kor_isnm": "하이트진로",
                "crdt_rate": "40.00",
            },
        ],
        "rt_cd": "0",
        "msg_cd": "MCA00000",
        "msg1": "정상처리 되었습니다.",
    }
    responses.add(
        responses.GET,
        f"{mock_openkis_client_url}/uapi/domestic-stock/v1/quotations/credit-by-company",
        json=expected,
        status=200,
    )
    resp = mock_openkis_client.get_financial_credit_by_company(fid_input_iscd="0000")

    assert resp == expected


@responses.activate
def test_domestic_stock_invest_opinion(
    mock_openkis_client: OpenKisClient, mock_openkis_client_url: str
):
    expected = {
        "output": [
            {
                "stck_bsop_date": "20240226",
                "invt_opnn": "BUY",
                "invt_opnn_cls_code": "2",
                "rgbf_invt_opnn": "BUY",
                "rgbf_invt_opnn_cls_code": "3",
                "mbcr_name": "하이투자",
                "hts_goal_prc": "84000",
                "stck_prdy_clpr": "72900",
                "stck_nday_esdg": "-11100",
                "nday_dprt": "-13.21",
                "stft_esdg": "-4000",
                "dprt": "-4.76",
            }
        ],
        "rt_cd": "0",
        "msg_cd": "MCA00000",
        "msg1": "정상처리 되었습니다.",
    }

    responses.add(
        responses.GET,
        f"{mock_openkis_client_url}/uapi/domestic-stock/v1/quotations/invest-opinion",
        json=expected,
        status=200,
    )

    resp = mock_openkis_client.get_domestic_stock_invest_opinion(
        fid_input_iscd="005930",
        fid_input_date1="20240126",
        fid_input_date2="20240226",
    )

    assert resp == expected


@responses.activate
def test_domestic_stock_check_holiday(
    mock_openkis_client: OpenKisClient, mock_openkis_client_url: str
):
    expected = {
        "ctx_area_nk": "20240704            ",
        "ctx_area_fk": "20240611            ",
        "output": [
            {
                "bass_dt": "20240611",
                "wday_dvsn_cd": "03",
                "bzdy_yn": "Y",
                "tr_day_yn": "Y",
                "opnd_yn": "Y",
                "sttl_day_yn": "Y",
            },
            {
                "bass_dt": "20240612",
                "wday_dvsn_cd": "04",
                "bzdy_yn": "Y",
                "tr_day_yn": "Y",
                "opnd_yn": "Y",
                "sttl_day_yn": "Y",
            },
            {
                "bass_dt": "20240613",
                "wday_dvsn_cd": "05",
                "bzdy_yn": "Y",
                "tr_day_yn": "Y",
                "opnd_yn": "Y",
                "sttl_day_yn": "Y",
            },
        ],
        "rt_cd": "0",
        "msg_cd": "KIOK0500",
        "msg1": "조회가 계속됩니다..다음버튼을 Click 하십시오.",
    }
    responses.add(
        responses.GET,
        f"{mock_openkis_client_url}/uapi/domestic-stock/v1/quotations/chk-holiday",
        json=expected,
        status=200,
    )
    resp = mock_openkis_client.check_domestic_holiday(bass_dt="20240611")
    assert resp == expected


@responses.activate
def test_domestic_stock_search_product_info(
    mock_openkis_client: OpenKisClient, mock_openkis_client_url: str
):
    expected = {
        "output": {
            "pdno": "AAPL",
            "prdt_type_cd": "512",
            "prdt_name": "애플",
            "prdt_name120": "애플",
            "prdt_abrv_name": "애플",
            "prdt_eng_name": "APPLE INC",
            "prdt_eng_name120": "APPLE INC",
            "prdt_eng_abrv_name": "APPLE INC",
            "std_pdno": "US0378331005",
            "shtn_pdno": "AAPL",
            "prdt_sale_stat_cd": "",
            "prdt_risk_grad_cd": "",
            "prdt_clsf_cd": "101210",
            "prdt_clsf_name": "해외주식",
            "sale_strt_dt": "",
            "sale_end_dt": "",
            "wrap_asst_type_cd": "06",
            "ivst_prdt_type_cd": "1012",
            "ivst_prdt_type_cd_name": "해외주식",
            "frst_erlm_dt": "",
        },
        "rt_cd": "0",
        "msg_cd": "KIOK0530",
        "msg1": "조회되었습니다                                                                  ",
    }

    responses.add(
        responses.GET,
        f"{mock_openkis_client_url}/uapi/domestic-stock/v1/quotations/search-info",
        json=expected,
        status=200,
    )

    resp = mock_openkis_client.search_product_info(pdno="AAPL", prdt_type_cd="512")

    assert resp == expected


@responses.activate
def test_domestic_stock_search_stock_info(
    mock_openkis_client: OpenKisClient, mock_openkis_client_url: str
):
    expected = {
        "output": {
            "pdno": "00000A000660",
            "prdt_type_cd": "300",
            "mket_id_cd": "STK",
            "scty_grp_id_cd": "ST",
            "excg_dvsn_cd": "02",
            "setl_mmdd": "12",
            "lstg_stqt": "728002365",
            "lstg_cptl_amt": "0",
            "cpta": "3657652050000",
            "papr": "5000",
            "issu_pric": "5000",
            "kospi200_item_yn": "Y",
            "scts_mket_lstg_dt": "19961226",
            "scts_mket_lstg_abol_dt": "",
            "kosdaq_mket_lstg_dt": "",
            "kosdaq_mket_lstg_abol_dt": "",
            "frbd_mket_lstg_dt": "19961226",
            "frbd_mket_lstg_abol_dt": "",
            "reits_kind_cd": "",
            "etf_dvsn_cd": "0",
            "oilf_fund_yn": "N",
            "idx_bztp_lcls_cd": "002",
            "idx_bztp_mcls_cd": "013",
            "idx_bztp_scls_cd": "013",
            "stck_kind_cd": "101",
            "mfnd_opng_dt": "",
            "mfnd_end_dt": "",
            "dpsi_erlm_cncl_dt": "",
            "etf_cu_qty": "0",
            "prdt_name": "에스케이하이닉스보통주",
            "prdt_name120": "에스케이하이닉스보통주",
            "prdt_abrv_name": "SK하이닉스",
            "std_pdno": "KR7000660001",
            "prdt_eng_name": "SK hynix",
            "prdt_eng_name120": "SK hynix",
            "prdt_eng_abrv_name": "SK hynix",
            "dpsi_aptm_erlm_yn": "Y",
            "etf_txtn_type_cd": "00",
            "etf_type_cd": "",
            "lstg_abol_dt": "",
            "nwst_odst_dvsn_cd": "1",
            "sbst_pric": "172380",
            "thco_sbst_pric": "172380",
            "thco_sbst_pric_chng_dt": "20240614",
            "tr_stop_yn": "N",
            "admn_item_yn": "N",
            "thdt_clpr": "221000",
            "bfdy_clpr": "221000",
            "clpr_chng_dt": "20240614",
            "std_idst_clsf_cd": "032601",
            "std_idst_clsf_cd_name": "반도체 제조업",
            "idx_bztp_lcls_cd_name": "시가총액규모대",
            "idx_bztp_mcls_cd_name": "전기,전자",
            "idx_bztp_scls_cd_name": "전기,전자",
            "ocr_no": "1147",
            "crfd_item_yn": "N",
            "elec_scty_yn": "Y",
            "issu_istt_cd": "00066",
            "etf_chas_erng_rt_dbnb": "0",
            "etf_etn_ivst_heed_item_yn": "N",
            "stln_int_rt_dvsn_cd": "01",
            "frnr_psnl_lmt_rt": "0.00000000",
            "lstg_rqsr_issu_istt_cd": "",
            "lstg_rqsr_item_cd": "",
            "trst_istt_issu_istt_cd": "",
        },
        "rt_cd": "0",
        "msg_cd": "KIOK0530",
        "msg1": "조회되었습니다                                                                  ",
    }

    responses.add(
        responses.GET,
        f"{mock_openkis_client_url}/uapi/domestic-stock/v1/quotations/search-stock-info",
        json=expected,
        status=200,
    )

    resp = mock_openkis_client.search_stock_info(pdno="000660", prdt_type_cd="300")

    assert resp == expected


@responses.activate
def test_domestic_stock_securities_opinion(
    mock_openkis_client: OpenKisClient, mock_openkis_client_url: str
):
    expected = {
        "output": [
            {
                "stck_bsop_date": "20240613",
                "stck_shrn_iscd": "286940",
                "hts_kor_isnm": "롯데이노베이트",
                "invt_opnn": "BUY",
                "invt_opnn_cls_code": "2",
                "rgbf_invt_opnn": "BUY",
                "rgbf_invt_opnn_cls_code": "3",
                "mbcr_name": "상상인",
                "stck_prpr": "28150",
                "prdy_vrss": "-450",
                "prdy_vrss_sign": "5",
                "prdy_ctrt": "-1.57",
                "hts_goal_prc": "38000",
                "stck_prdy_clpr": "27900",
                "stft_esdg": "-9850",
                "dprt": "-25.92",
            }
        ],
        "rt_cd": "0",
        "msg_cd": "MCA00000",
        "msg1": "정상처리 되었습니다.",
    }

    responses.add(
        responses.GET,
        f"{mock_openkis_client_url}/uapi/domestic-stock/v1/quotations/invest-opbysec",
        json=expected,
        status=200,
    )
    resp = mock_openkis_client.get_domestic_stock_securities_opinion(
        fid_input_iscd="999",
        fid_input_date1="20240601",
        fid_input_date2="20240613",
    )

    assert resp == expected
