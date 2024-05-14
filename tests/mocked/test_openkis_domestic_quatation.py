import responses

from finance_clue.openkis import OpenKisClient


@responses.activate
def test_domestic_quotation_inquiry_price(
    mock_openkis_client: OpenKisClient, mock_openkis_client_url: str
):
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
            "stck_prpr": "128500",
            "prdy_vrss": "0",
            "prdy_vrss_sign": "3",
            "prdy_ctrt": "0.00",
            "acml_tr_pbmn": "344570137500",
            "acml_vol": "2669075",
            "prdy_vrss_vol_rate": "75.14",
            "stck_oprc": "128500",
            "stck_hgpr": "130000",
            "stck_lwpr": "128500",
            "stck_mxpr": "167000",
            "stck_llam": "90000",
            "stck_sdpr": "128500",
            "wghn_avrg_stck_prc": "129097.23",
            "hts_frgn_ehrt": "49.48",
            "frgn_ntby_qty": "0",
            "pgtr_ntby_qty": "287715",
            "pvt_scnd_dmrs_prc": "131833",
            "pvt_frst_dmrs_prc": "130166",
            "pvt_pont_val": "128333",
            "pvt_frst_dmsp_prc": "126666",
            "pvt_scnd_dmsp_prc": "124833",
            "dmrs_val": "129250",
            "dmsp_val": "125750",
            "cpfn": "36577",
            "rstc_wdth_prc": "38500",
            "stck_fcam": "5000",
            "stck_sspr": "97660",
            "aspr_unit": "500",
            "hts_deal_qty_unit_val": "1",
            "lstn_stcn": "728002365",
            "hts_avls": "935483",
            "per": "19.67",
            "pbr": "1.72",
            "stac_month": "12",
            "vol_tnrt": "0.37",
            "eps": "6532.00",
            "bps": "74721.00",
            "d250_hgpr": "149500",
            "d250_hgpr_date": "20210225",
            "d250_hgpr_vrss_prpr_rate": "-14.05",
            "d250_lwpr": "90500",
            "d250_lwpr_date": "20211013",
            "d250_lwpr_vrss_prpr_rate": "41.99",
            "stck_dryy_hgpr": "132500",
            "dryy_hgpr_vrss_prpr_rate": "-3.02",
            "dryy_hgpr_date": "20220103",
            "stck_dryy_lwpr": "121500",
            "dryy_lwpr_vrss_prpr_rate": "5.76",
            "dryy_lwpr_date": "20220105",
            "w52_hgpr": "149500",
            "w52_hgpr_vrss_prpr_ctrt": "-14.05",
            "w52_hgpr_date": "20210225",
            "w52_lwpr": "90500",
            "w52_lwpr_vrss_prpr_ctrt": "41.99",
            "w52_lwpr_date": "20211013",
            "whol_loan_rmnd_rate": "0.22",
            "ssts_yn": "Y",
            "stck_shrn_iscd": "000660",
            "fcam_cnnm": "5,000",
            "cpfn_cnnm": "36,576 억",
            "frgn_hldn_qty": "360220601",
            "vi_cls_code": "N",
            "ovtm_vi_cls_code": "N",
            "last_ssts_cntg_qty": "43916",
            "invt_caful_yn": "N",
            "mrkt_warn_cls_code": "00",
            "short_over_yn": "N",
            "sltr_yn": "N",
        },
        "rt_cd": "0",
        "msg_cd": "MCA00000",
        "msg1": "정상처리 되었습니다!",
    }

    responses.add(
        responses.GET,
        f"{mock_openkis_client_url}/uapi/domestic-stock/v1/quotations/inquire-price",
        json=expected,
        status=200,
    )

    resp = mock_openkis_client.get_domestic_stock_quotations_price(
        fid_cond_mrkt_div_code="J", fid_input_iscd="161390"
    )

    assert resp == expected


@responses.activate
def test_domestic_quotation_inquiry_daily_price(
    mock_openkis_client: OpenKisClient, mock_openkis_client_url: str
):
    expected = {
        "output": [
            {
                "stck_bsop_date": "20220113",
                "stck_clpr": "129500",
                "prdy_vrss": "1000",
                "prdy_vrss_sign": "2",
                "prsn_ntby_qty": "-287624",
                "frgn_ntby_qty": "797458",
                "orgn_ntby_qty": "-503653",
                "prsn_ntby_tr_pbmn": "-37176",
                "frgn_ntby_tr_pbmn": "102959",
                "orgn_ntby_tr_pbmn": "-64984",
                "prsn_shnu_vol": "467525",
                "frgn_shnu_vol": "1442791",
                "orgn_shnu_vol": "2219433",
                "prsn_shnu_tr_pbmn": "60368",
                "frgn_shnu_tr_pbmn": "186166",
                "orgn_shnu_tr_pbmn": "286505",
                "prsn_seln_vol": "755149",
                "frgn_seln_vol": "645333",
                "orgn_seln_vol": "2723086",
                "prsn_seln_tr_pbmn": "97544",
                "frgn_seln_tr_pbmn": "83207",
                "orgn_seln_tr_pbmn": "351489",
            },
            {
                "stck_bsop_date": "20220112",
                "stck_clpr": "128500",
                "prdy_vrss": "500",
                "prdy_vrss_sign": "2",
                "prsn_ntby_qty": "-74249",
                "frgn_ntby_qty": "-134600",
                "orgn_ntby_qty": "206812",
                "prsn_ntby_tr_pbmn": "-9687",
                "frgn_ntby_tr_pbmn": "-17094",
                "orgn_ntby_tr_pbmn": "26530",
                "prsn_shnu_vol": "608748",
                "frgn_shnu_vol": "721756",
                "orgn_shnu_vol": "2201966",
                "prsn_shnu_tr_pbmn": "77943",
                "frgn_shnu_tr_pbmn": "92615",
                "orgn_shnu_tr_pbmn": "281965",
                "prsn_seln_vol": "682997",
                "frgn_seln_vol": "856356",
                "orgn_seln_vol": "1995154",
                "prsn_seln_tr_pbmn": "87630",
                "frgn_seln_tr_pbmn": "109708",
                "orgn_seln_tr_pbmn": "255435",
            },
        ],
        "rt_cd": "0",
        "msg_cd": "MCA00000",
        "msg1": "정상처리 되었습니다!",
    }

    responses.add(
        responses.GET,
        f"{mock_openkis_client_url}/uapi/domestic-stock/v1/quotations/inquire-daily-price",
        json=expected,
        status=200,
    )

    resp = mock_openkis_client.get_domestic_stock_quotations_daily_price(
        fid_cond_mrkt_div_code="J",
        fid_input_iscd="161390",
        fid_period_div_code="W",
        fid_org_adj_prc="0",
    )

    assert resp == expected
