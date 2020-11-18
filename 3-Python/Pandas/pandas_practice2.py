# Ecrire un script afin de:
# * CHarger les employés depuis le fichier employees dan sle dataframe df
# * Remplacer les deux colonnes first_name et last_name avec une colonne name qui contient la concaténation des deux colonnes

import pandas as pd

with open ( 'C:\\Users\Administrateur\\PycharmProjects\\Yassine\\m2i\\data\\hr\\employees.csv' ) as f:
    id = pd.Series ( [line[1:].split ( ';' )[0] for line in f if not 'EMPLOYEE_ID' in line] )
with open ( 'C:\\Users\Administrateur\\PycharmProjects\\Yassine\\m2i\\data\\hr\\employees.csv' ) as f:
    firstName = pd.Series ( [line.split ( ';' )[1] for line in f if not 'FIRST_NAME' in line] )
with open ( 'C:\\Users\Administrateur\\PycharmProjects\\Yassine\\m2i\\data\\hr\\employees.csv' ) as f:
    lastName = pd.Series ( [line.split ( ';' )[2] for line in f if not 'LAST_NAME' in line] )

df = pd.DataFrame({'id': id,
        'firstName': firstName,
        'lastName': lastName,
         'name': firstName +' '+ lastName})

print(df)