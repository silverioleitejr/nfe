# Test para Schema XML
#
#
import  unittest
from lxml import etree
 
class TestSchemaXML(unittest.TestCase):
    def setUp(self):
        pass
   
    def test_schema_pl_006s(self):
        nfe = etree.parse("https://raw.githubusercontent.com/silverioleitejr/python-nfe/main/XML/NFe35170171322150001301550000000477521876550573_procNFe.xml")
        xmlschema_doc = etree.parse("https://raw.githubusercontent.com/silverioleitejr/python-nfe/main/XSD/leiauteNFe_v4.00.xsd/leiauteNFe_v4.00.xsd")
        xmlschema = etree.XMLSchema(xmlschema_doc)
        validado  = xmlschema.validate(nfe)
        if not validado:# se  for invalido..
            print (xmlschema.error_log)
 
 
if __name__ == '__main__':
    unittest.main()