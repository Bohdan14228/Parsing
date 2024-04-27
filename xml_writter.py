import xlsxwriter
import json
import xml.etree.ElementTree as ET


def create_xml(json_file="F:\\project PyCharm\\Jooble_test\\data.json",
               xml_file="F:\\project PyCharm\\Jooble_test\\data.xml"):
    with open(json_file, 'r') as f:
        data = json.load(f)

    root = ET.Element("products")

    for item in data:
        product = ET.SubElement(root, "product")

        columns = [
            "id", "item_group_id", "mpn", "title", "description", "image_link",
            "additional_image_link", "link", "gender", "age_group", "brand",
            "color", "size", "availability", "price", "condition",
            "product_type", "google_product_category"
        ]

        for i, column in enumerate(columns):
            if item[i] != "None":
                ET.SubElement(product, column).text = str(item[i])  # Convert int to str if necessary

    tree = ET.ElementTree(root)
    with open(xml_file, 'wb') as xf:
        tree.write(xf, xml_declaration=True, encoding='utf-8', method="xml")


create_xml()



