# Test para Schema XML
#
#
import  unittest
from lxml import etree
 
class TestSchemaXML(unittest.TestCase):
    def setUp(self):
        pass
 
    def test_schema_pl_006s(self):
        nfe = etree.parse("/home/lukaswilkeer/web2py/applications/spotnfe/uploads/nfe.xml")
        xmlschema_doc = etree.parse("/home/lukaswilkeer/web2py/applications/spotnfe/modules/schemas/PL_006s/leiauteNFe_v2.00.xsd")
        xmlschema = etree.XMLSchema(xmlschema_doc)
        validado  = xmlschema.validate(nfe)
        if not validado:# se  for invalido..
            print xmlschema.error_log
 
 
if __name__ == '__main__':
    unittest.main()