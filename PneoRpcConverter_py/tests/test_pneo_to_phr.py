import xmltodict
from pathlib import Path
from pneo_to_phr import convert


def test_PNEO_to_PHR():
    sample_pneo_file_path = (
        "../input/RPC_PNEO4_202212181621109_PAN_SEN_PWOI_000059315_1_4_F_1.XML"
    )
    out_dir = "../output/test"
    phr_path = convert(sample_pneo_file_path, out_dir)
    assert Path(phr_path).is_file()
    with open(phr_path) as f:
        tree = xmltodict.parse(f.read())
        assert (
            tree["Dimap_Document"]["Metadata_Identification"]["METADATA_PROFILE"]
            == "PHR_SENSOR"
        )
        rfm_metadata = tree["Dimap_Document"]["Rational_Function_Model"]["Global_RFM"]
        assert all(key in rfm_metadata for key in ("Inverse_Model", "Direct_Model"))
        direct_model = rfm_metadata["Direct_Model"]
        assert all(
            key in direct_model
            for key in (
                "SAMP_DEN_COEFF_1",
                "SAMP_NUM_COEFF_1",
                "LINE_DEN_COEFF_1",
                "LINE_NUM_COEFF_1",
                "ERR_BIAS_X",
                "ERR_BIAS_Y",
            )
        )
