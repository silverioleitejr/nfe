from lxml import etree
from lxml.etree import xmlfile


class Validador:

    def __init__(self, xsd_path: str):
        xmlschema_doc = etree.parse(xsd_path)
        self.xmlschema = etree.XMLSchema(xmlschema_doc)
        self.error = ''

    def Check(self, xml_path: str) -> bool:
        xml_doc = etree.parse(xml_path)
        result = self.xmlschema.validate(xml_doc)
        self.error = self.xmlschema.error_log

    def ListElement(self, xml_path: str):
        root_node = etree.parse(xml_path).getroot()
        print(root_node)
        for tag in root_node.find_all(level):
            value = tag.get(attribute)
            if value is not None: print(value)
        return result

