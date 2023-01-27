import xml.etree.ElementTree as ET

tree = ET.parse('uniq.xml')

root = tree.getroot()

dicionario = dict()


for child in root:
    dicionario[child.tag] = child.text
    
for k, v in dicionario.items():
    print(k, v)

