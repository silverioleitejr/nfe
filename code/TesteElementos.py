# https://docs.python.org/pt-br/dev/library/xml.etree.elementtree.html

import xml.etree.ElementTree as ET

from requests.help import info

xmlPath = 'D:/projetos/og1.kpmg/projetos/python-nfe/XML'
xmlFile = 'NFe35170271322150003428550000000386591831242542_procNFe.xml'
_xml = xmlPath + '/' + xmlFile
_urlNFE ='http://www.portalfiscal.inf.br/nfe'
tree = ET.parse(_xml)
doc = tree.getroot()
print('---------------------')
print('! root =>' , doc.tag)
print('! versao =>' , doc.attrib.get('versao') )
print('---------------------')

def CriarNo( path:str) -> str:
    return '{' + _urlNFE + '}' + path


nodeinfNFE = CriarNo('NFe') + '/' + CriarNo('infNFe')
nodefind = doc.find('{http://www.portalfiscal.inf.br/nfe}NFe/'+
                    '{http://www.portalfiscal.inf.br/nfe}infNFe' )
print (nodefind.attrib.get('Id') )

nodefind = doc.find('{http://www.portalfiscal.inf.br/nfe}NFe/'+
                    '{http://www.portalfiscal.inf.br/nfe}infNFe'+
                    '{http://www.portalfiscal.inf.br/nfe}infNFe'+
                    )
print (nodefind.attrib.get('Id') )


exit(0)

for child in doc:
    print( 'tag =>' , child.tag, child.attrib)

for neighbor in root.iter('det'):
    print(neighbor.attrib)