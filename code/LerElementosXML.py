import xmltodict
import xml.etree.ElementTree as ET

xmlPath = 'D:/projetos/og1.kpmg/projetos/python-nfe/XML'
xmlFile = 'NFe35170171322150001301550000000477551772681010_procNFe.xml'
_xml = xmlPath + '/' + xmlFile


tree = ET.parse(_xml)
doc = tree.getroot()
nodefind = doc.find('{http://www.portalfiscal.inf.br/nfe}NFe/{http://www.portalfiscal.inf.br/nfe}infNFe/{http://www.portalfiscal.inf.br/nfe}ide/{http://www.portalfiscal.inf.br/nfe}cUF')
print (nodefind.attrib)
print (nodefind.text)




