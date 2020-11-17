import pandas as pd
# Concaténation de deux dataframe à partir de l'index par défaut

data1 = {'Prénom' : ['Steve','Anna','Paul', 'Tom'],
         'Age':[12,15,20,10]}

df1 = pd.DataFrame(data1)

print(df1)
print('___________________________________')
data2 = {'Ville':['Paris','Londres', 'Manchester','Casablanca']}

df2=pd.DataFrame(data2)

print(df2)

df1['Nouvelle_ville']=df2['Ville']

print(df1)
print('___________________________________')

#Concaténation de deux dataframe à partir de l'index prénom

data3= {'Prénom' : ['Steve','Anna','Paul', 'Tom'],
         'Age':[12,15,20,10]}

df3 = pd.DataFrame(data3, index=['Steve','Anna','Paul', 'Tom'])

data4= {'Ville':['Paris','Londres', 'Manchester','Casablanca']}
df4= pd.DataFrame(data4, index=['Paul', 'Tom','Steve','Anna'])

df3['Nouvelle_ville']=df4['Ville']
print (df3)
print('___________________________________')

#Et si l'on n'a pas les mêmes index:
data5= {'Prénom' : ['Steve','Anna','Paul', 'Tom'],
         'Age':[12,15,20,10]}

df5 = pd.DataFrame(data5, index=['Steve','Anna','Paul', 'Tom'])

data6= {'Ville':['Paris','Londres', 'Manchester','Casablanca']}
df6= pd.DataFrame(data6)

df5['Nouvelle_ville']=df6['Ville']
print (df5)
