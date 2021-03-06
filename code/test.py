# testar arquivo XML com uso schema XSD
# depende do modulo TestValidador

import os
from TestValidador import Validador

# declaração de variaveis
xmlPath = 'D:/projetos/og1.kpmg/projetos/python-nfe/XML'
xmlFile = 'NFe35170171322150001301550000000477551772681010_procNFe.xml'
_xml = xmlPath + '/' + xmlFile

xsdPath = 'D:/projetos/og1.kpmg/projetos/python-nfe/XSD'
xsdFile = 'procNFe_v1.10.xsd'
_xsd = xsdPath + '/' + xsdFile

print('------------------------------------------------------')
print('XML path= ', xmlPath)
print('XML= ', xmlFile)
print('------------------------------------------------------')
print('XSD path= ', xmlPath)
print('XSD= ', xsdFile)

Arquivo = Validador(_xsd)


for file_name in os.listdir(xmlPath):
    print('{}: '.format(file_name), end='')

    file_path = '{}/{}'.format(xmlPath, file_name)

    if Arquivo.Check(file_path):
        print('Válido! :)')
    else:
        print('Inválido!  Erro :(')
        print