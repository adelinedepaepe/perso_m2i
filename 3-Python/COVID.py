import re
import requests
import pandas as pd

#Je n'arrive plus à lire à partir du fichier html (même problème qu'avait Yersin au début, du coup j'ai trouvé ça sur internet qui m'a dépanné, mais n'en tenez pas compte
html_source = requests.get("https://www.worldometers.info/coronavirus/").text
html_source = re.sub(r'<.*?>', lambda g: g.group(0).upper(), html_source)

#Sur ces trois lignes, je lis les 3 tableau et leur affecte des noms
corona_today=pd.read_html(html_source)[0]
corona_yesterday=pd.read_html(html_source)[1]
corona_twoDago=pd.read_html(html_source)[2]

#Pour chaque dataframe j'ajoute une colonne qui contiendra le nom du fichier
corona_today['File_name']='1.Today'
corona_yesterday['File_name']='2. Yesterday'
corona_twoDago['File_name']='3. Two days ago'



#Je merge le dataframe corona_today et corona_yesterday
corona_merged_tempo = pd.merge(corona_today,corona_yesterday, how = 'outer')

#Je merge le résultat ci-dessus avec corona_twoDago
corona_merged= pd.merge(corona_merged_tempo,corona_twoDago, how = 'outer')

#Je pivote (selon l'exemple p.12 de ce pdf: http://eric.univ-lyon2.fr/~ricco/tanagra/fichiers/fr_Tanagra_Data_Manipulation_Pandas.pdf)
résultat=corona_merged.pivot_table(index=['Country,Other'],columns=['File_name'],values=['TotalCases'])
print(résultat)
