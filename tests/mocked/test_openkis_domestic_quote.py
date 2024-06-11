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
    """국내주식 현재가 시간외시간별체결 integrated test"""
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
    """국내주식 현재가 시세2 조회 integrated test"""

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
