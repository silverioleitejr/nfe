from lxml import etree

def validate(xml_path: str, xsd_path: str) -> bool:

    xmlschema_doc = etree.parse(xsd_path)
    xmlschema = etree.XMLSchema(xmlschema_doc)

    xml_doc = etree.parse(xml_path)
    result = xmlschema.validate(xml_doc)

    return result

path = 'D:\projetos\og1.kpmg\projetos\python-nfe\XML'
xmlFile = 'NFe35170171322150001301550000000477551772681010_procNFe.xml'
xsdFile = 'NFe35170171322150001301550000000477551772681010_procNFe.xsd'