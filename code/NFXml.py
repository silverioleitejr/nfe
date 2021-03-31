import xmltodict
import unittest 
from lxml import etree
import xml.etree.ElementTree as ET
import requests   

class NFXML:
  def __init__(self, local, arquivo , tipo):
    self.pasta = local
    self.nomearquivo = arquivo
    self.tiponf = tipo
    self.arquivo = local + '/' + arquivo
    
  def ImprimeNomeArquivo(self):
    print (self.arquivo)

  def AbrirArquivo(self): 
    ET.parse(self.arquivo)

pasta = 'https://raw.githubusercontent.com/silverioleitejr/python-nfe/main/XML'
arquivo = 'NFe35170171322150001301550000000477521876550573_procNFe.xml'

NF1 = NFXML(pasta, arquivo, 1)
NF1.ImprimeNomeArquivo()
NF1.AbrirArquivo()