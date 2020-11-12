#Pour importer le package etree
import xml.etree.ElementTree as ET

tree= ET.parse('tuto_etree.xml')
root = tree.getroot() #root correspond à la balise 'data'

#Vérif de la valeur et du type de root, de ses tag et attrib
print(root)
print(root.tag)
print(root.attrib)
print(type(root))
print(type(root.tag))
print(type(root.attrib))

#root contient plusieurs pays, chaque pays contiennent plusieurs propriétés
#Pour parcourir les balises pays:
for country in root:
     print(country.tag, country.attrib, country.text)

#Pour parcourir toutes les propriétés de chaque pays:
for country in root:
     for children in list(country):
          print(children.tag,children.text,children.attrib) #tag=balise, text = valeur dans la balise, attrib = les attributs dans la balise

#Pour accéder à une propriété en particulier:

for rank in root.iter('rank'):
     print(rank.text)

#ou
for neighbor in root.iter('neighbor'):
     print(neighbor.attrib)


for country in root.findall('country'):
     rank = country.find('rank').text #Cette syntaxe pour la valeur d'une balise
     year = country.find ( 'year' ).text
     neighbor= country.find('neighbor').attrib #Cette syntaxe pour les attribut d'une balise de Country
     neighbor_temp = country.find('neighbor')
     neighbor_direction = neighbor_temp.get('direction') #Ces deux lignes pour accéder à un attribut en particulier d'une balise
     name = country.get('name') #Cette syntaxe pour un attruibut de la balise country
     print(name, rank, year, neighbor, neighbor_direction)



