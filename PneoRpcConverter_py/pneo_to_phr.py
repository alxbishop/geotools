import os
from lxml import etree


REPLACEMENT_DICT = {
    "LON_DEN_COEFF_": "SAMP_DEN_COEFF_",
    "LON_NUM_COEFF_": "SAMP_NUM_COEFF_",
    "LAT_DEN_COEFF_": "LINE_DEN_COEFF_",
    "LAT_NUM_COEFF_": "LINE_NUM_COEFF_",
}

def PNEO_to_PHR(pneo_xml_path: str) -> etree._ElementTree:
    """
    Repalces all the relevant tags and generates a new file compliant to PHR.
    """
    xml_tree = etree.parse(pneo_xml_path)
    xml_tree.find(".//METADATA_FORMAT").set("profile", "PHR_SENSOR")
    xml_tree.find(".//METADATA_PROFILE").text = "PHR_SENSOR"
    xml_tree.find(
        ".//GroundtoImage_Validity_Domain"
    ).tag = "Inverse_Model_Validity_Domain"
    xml_tree.find(
        ".//ImagetoGround_Validity_Domain"
    ).tag = "Direct_Model_Validity_Domain"
    xml_tree.find(".//GroundtoImage_Values").tag = "Inverse_Model"
    xml_tree.find(".//ImagetoGround_Values").tag = "Direct_Model"
    xml_tree.find(".//ERR_BIAS_LON").tag = "ERR_BIAS_X"
    xml_tree.find(".//ERR_BIAS_LAT").tag = "ERR_BIAS_Y"
    return xml_tree


def update_tags(xml_tree: etree._ElementTree) -> etree._ElementTree:
    """
    Updates the coefficient tags.
    """
    for key, item in REPLACEMENT_DICT.items():
        i = 0
        for elem in xml_tree.find(".//Direct_Model").iter():
            if elem.tag.startswith(key):
                elem.tag = item + str(i + 1)
                i += 1
    return xml_tree


def convert(pneo_xml_path: str, out_dir: str) -> str:
    os.makedirs(out_dir, exist_ok=True)
    out_file_name = "converted_" + pneo_xml_path.split("/")[-1]
    xml_tree = PNEO_to_PHR(pneo_xml_path)
    updated_tree = update_tags(xml_tree)
    out_path = os.path.join(out_dir, out_file_name)
    updated_tree.write(
        out_path,
        encoding=xml_tree.docinfo.encoding,
        xml_declaration=True,
        standalone=True,
    )
    return out_path


if __name__ == "__main__":
    # define paths here
    pneo_xml_path = "input/RPC_PNEO4_202212181621109_PAN_SEN_PWOI_000059315_1_4_F_1.XML"
    out_dir = (
        "output/"  # directory where the resulting XML will be generated
    )

    phr_path = convert(pneo_xml_path, out_dir)
