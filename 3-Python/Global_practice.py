# Ecrire un script afin de:
#
# Charger les données des élections USA 2020
# Créer un DF qui contient l'ensemble des tweets (des deux csv)
# Effectuer un pré-traitement du DF pour enlever les doublons
# En utilisant matplotlib ou seaborn, afficher des graphiques pour analyser le nombre de tweets, retweets,  et le nombre de likes par mois pour chaque antagoniste
# Interpréter les graphs afin de déterminer si les données twitter sont conformes avec les résultats finaux
# D'après les likes, quels sont les mots le splus importants (A partir du nombre de likes, quels mots ont été les plus utilisés)

# Hint: on peut télécharger directement de python en utilisant urllib (import urllib.request

import re
#__________________________________________________________________________________________
# Test avec une ligne puis un échantillon de lignes
ma_ligne="""2020-10-15 00:00:01,1.316529221557252e+18,"#Elecciones2020 | En #Florida: #JoeBiden dice que #DonaldTrump solo se preocupa por él mismo. El demócrata fue anfitrión de encuentros de electores en #PembrokePines y #Miramar. Clic AQUÍ ⬇️⬇️⬇️
⠀
🌐https://t.co/qhIWpIUXsT
_
#ElSolLatino #yobrilloconelsol https://t.co/6FlCBWf1Mi",0.0,0.0,TweetDeck,360666534.0,El Sol Latino News,elsollatinonews,"🌐 Noticias de interés para latinos de la costa este de #EEUU
⠀⏹️ Facebook e Instagram
⠀🏙️ Philadelphia: /elsollatinonewspaper
⠀🌅 Miami: /elsollatinonewsmiami",2011-08-23 15:33:45,1860.0,"Philadelphia, PA / Miami, FL",25.77427,-80.19366,,United States of America,North America,Florida,FL,2020-10-21 00:00:00
"""

mes_lignes=["""2020-10-15 00:00:01,1.316529221557252e+18,"#Elecciones2020 | En #Florida: #JoeBiden dice que #DonaldTrump solo se preocupa por él mismo. El demócrata fue anfitrión de encuentros de electores en #PembrokePines y #Miramar. Clic AQUÍ ⬇️⬇️⬇️
⠀
🌐https://t.co/qhIWpIUXsT
_
#ElSolLatino #yobrilloconelsol https://t.co/6FlCBWf1Mi",0.0,0.0,TweetDeck,360666534.0,El Sol Latino News,elsollatinonews,"🌐 Noticias de interés para latinos de la costa este de #EEUU
⠀⏹️ Facebook e Instagram
⠀🏙️ Philadelphia: /elsollatinonewspaper
⠀🌅 Miami: /elsollatinonewsmiami",2011-08-23 15:33:45,1860.0,"Philadelphia, PA / Miami, FL",25.77427,-80.19366,,United States of America,North America,Florida,FL,2020-10-21 00:00:00
""","""2020-10-15 00:00:01,1.3165292227484303e+18,"Usa 2020, Trump contro Facebook e Twitter: coprono Biden   #donaldtrump https://t.co/6ceURhe1VP https://t.co/94jidLjoON",26.0,9.0,Social Mediaset ,331617619.0,Tgcom24,MediasetTgcom24,Profilo ufficiale di Tgcom24: tutte le notizie sul sito https://t.co/sC5iMbymSN e sul canale 51 del digitale terrestre,2011-07-08 13:12:20,1067661.0,,,,,,,,,2020-10-21 00:00:00.373216530"""
"""2020-10-15 00:00:02,1.316529228091847e+18,"#Trump: As a student I used to hear for years, for ten years, I heard China! In 2019! And we have 1.5 and they don't know how many we have and I asked them how many do we have and they said 'sir we don't know.' But we have millions. Like 300 million.

Um. What?",2.0,1.0,Twitter Web App,8436472.0,snarke,snarke,"Will mock for food! Freelance writer, blogger, commentator. Civics nerd. She/Her",2007-08-26 05:56:11,1185.0,Portland,45.5202471,-122.6741949,Portland,United States of America,North America,Oregon,OR,2020-10-21 00:00:00.746433060""","""2020-10-15 00:00:02,1.316529227471237e+18,2 hours since last tweet from #Trump! Maybe he is VERY busy. Tremendously busy.,0.0,0.0,Trumpytweeter,8.28355589206057e+17,Trumpytweeter,trumpytweeter,"If he doesn't tweet for some time, should we be worried?",2017-02-05 21:32:17,32.0,,,,,,,,,2020-10-21 00:00:01.119649591
"""]
#
# for line in mes_lignes[:3]:
#     print(line.replace('\n',''))
#     print(line)
# ==> Ca fonctionne pour cet échantillon
#




columns = ['created_at', 'tweet_id', 'tweet', 'likes', 'retweet_count', 'source', 'user_id', 'user_name',
           'user_screen_name', 'user_description', 'user_join_date', 'user_followers_count', 'user_location', 'lat',
           'long', 'city', 'country', 'continent', 'state', 'state_code', 'collected_at']

with open ('C:\\Users\\Administrateur\\PycharmProjects\\Data\\hashtag_donaldtrump.csv', encoding='UTF-8') as f1:
    lines =f1.readlines()
    # data = {j: [line.replace('\n','').split ( ',' )[i] for line in lines if 'created_at' not in line] for i, j in
    #             enumerate ( columns )}
    # ==> Ne fonctionne pas
    # J'essaye avec un échantillon:' \
    #  '    for line in lines[0:10]:
    #     print(line.replace('\n',''))'
    # ==> Ne fonctionne pas non plus
    # print(data)
    #
    #Pour avancer, je vais sauter les exceptions
    # try:
    #     data = {j:[line.split(',')[i] for line in lines if 'created_at' not in line] for i, j in enumerate ( columns )}
    # except:
    #     #test
    #     continue

    # for line in lines:
    #     try:
    #         line.replace ( '\n', '' )
    #         print ( line )
    #     except:
    #         continue
    # lines = myf1.readlines()
    # print(lines[2])

     #
     # lines = f.readlines()
     # for line in lines:
     #     line.replace('\n','hehe')
     #     print(line)
     # print (lines[2])
#     # print(lines[1])
#     # print(type(lines[0])) #Chaque ligne est une liste de caractère ==> Il faut la transformer en liste avec des splits(',')
#     # Il fait créer un dictionnaire data sous la forme {Entête1:[valeur1,valeur2],entete2:[valeur1,valeur2,...
#     #Il faut vérifier que les entêtes sont les mêmes:
#     # created_at,tweet_id,tweet,likes,retweet_count,source,user_id,user_name,user_screen_name,user_description,user_join_date,user_followers_count,user_location,lat,long,city,country,continent,state,state_code,collected_at
#     # created_at,tweet_id,tweet,likes,retweet_count,source,user_id,user_name,user_screen_name,user_description,user_join_date,user_followers_count,user_location,lat,long,city,country,continent,state,state_code,collected_at
#     # ==> Ok, en-têtes identiques
#     data = {j: [line.split ( ',' )[i] for line in lines if 'created_at' not in line] for i, j in
#             enumerate ( columns )}
#     ==> Ne fonctionne pas tel quel car il y a des \n qui font que chaque item est sur plusieurs lignes et python lit ligne par ligne
#      Il faut supprimer le \n
     #data = {j: [lines[1].split ( ',' )[i]] for i, j in enumerate ( columns )}
     #print(data)
     # print({j:[lines[2].split( ',' )[0]] for i,j in enumerate(columns)})

#             enumerate ( columns )}
    #Pour mettre les deux fichiers dans le même df: on essaye de faire un append?
import pandas as pd

f1 = pd.read_csv ( 'C:\\Users\\Administrateur\\PycharmProjects\\Data\\hashtag_donaldtrump.csv', encoding='UTF-8' )

df1 = pd.DataFrame ( f1 )
df1 = df1[pd.notnull ( df1['collected_at'] )]

f2 = pd.read_csv ( 'C:\\Users\\Administrateur\\PycharmProjects\\Data\\hashtag_joebiden.csv', encoding='UTF-8' )

df2 = pd.DataFrame ( f2 )
df2 = df2[pd.notnull ( df2['collected_at'] )]

frames = [df1, df2]

df = pd.concat(frames)

df= df.drop_duplicates()
print(df1['created_at'].count())
print(df2['created_at'].count())
print(df['created_at'].count())
