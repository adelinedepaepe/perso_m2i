# Ecrire un script Python afin de:
#
# * Lire les données des employés en utilisant la lecture des fichiers (sans utiliser read_csv de pandas)
# * Créer une Series pour chaque colonne du fichier
# * Créer un DataFrame df1 à partir des Series
# * Créer un DataFrame df2 en utilisant un dictionnaire de listes
# * Créer un DataFrame df3 en utilisant un dictionnaire de dictionnaire
# * Eliminer les employés qui n'appartiennet à aucun département


import pandas as pd

with open('C:\\Users\Administrateur\\PycharmProjects\\Yassine\\m2i\\data\\hr\\employees.csv') as f:
        id = pd.Series([line[1:].split ( ';' )[0] for line in f if not 'EMPLOYEE_ID' in line])
with open ( 'C:\\Users\Administrateur\\PycharmProjects\\Yassine\\m2i\\data\\hr\\employees.csv' ) as f:
        firstName = pd.Series([line.split ( ';' )[1] for line in f if not 'FIRST_NAME' in line])
with open ( 'C:\\Users\Administrateur\\PycharmProjects\\Yassine\\m2i\\data\\hr\\employees.csv' ) as f:
        lastName = pd.Series([line.split ( ';' )[2] for line in f if not 'LAST_NAME' in line])
with open ( 'C:\\Users\Administrateur\\PycharmProjects\\Yassine\\m2i\\data\\hr\\employees.csv' ) as f:
        email =pd.Series([line.split ( ';' )[3] for line in f if not 'EMPLOYEE_ID' in line])
with open ( 'C:\\Users\Administrateur\\PycharmProjects\\Yassine\\m2i\\data\\hr\\employees.csv' ) as f:
        phone = pd.Series([line.split ( ';' )[4] for line in f if not 'EMPLOYEE_ID' in line])
with open ( 'C:\\Users\Administrateur\\PycharmProjects\\Yassine\\m2i\\data\\hr\\employees.csv' ) as f:
        department_id = pd.Series ( [line[:-3].split ( ';' )[10] for line in f if not 'EMPLOYEE_ID' in line] )

# with open ( 'C:\\Users\Administrateur\\PycharmProjects\\Yassine\\m2i\\data\\hr\\employees.csv' ) as f:
#     for line in f:
#         if not 'EMPLOYEE_ID' in line:
#             id = pd.Series ( [line[1:].split ( ';' )[0]] )
#             firstName = pd.Series ( [line.split ( ';' )[1]])
#             lastName = pd.Series ( [line.split ( ';' )[2]])
#             email = pd.Series ( [line.split ( ';' )[3]])
#             phone = pd.Series ( [line.split ( ';' )[4]])
#             department_id = pd.Series ( [line[:-3].split ( ';' )[10]])
# ==> Pour que cela fonctionne, il ne faut pas créer des listes les unes en dessous des autres, mais un dictionnaire de listes, ou bien une liste de listes

#==> à noter également, ci-dessous, on réalise une action répétitive, il faut améliorer ça en faisant une boucle. La fonction enumerate peut être utile.

# essai dans le fichier pandas_pratice_tempo

df1 = pd.DataFrame({'id': id,
        'firstName': firstName,
        'lastName': lastName,
        'department_id':department_id})

print(df1)

print(('_________________________________'))

print(df1[department_id==''])

print(('_________________________________'))

no_department_index = df1[department_id==''].index

df1.drop(no_department_index,inplace=True)

print (df1)

