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

        return result

