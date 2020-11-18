# Ecrire un script python afin de:
#
# * Charger les données du fichier employees.csv et les stocker dans un DataFrame
# * Afficher les employés qui ont une commission
# * Afficher le salaire  de Jennifer Whalen
# * Affiche rle nom complet des employés qui sont dans le département 50 et qui ont un salaire > 3000
# * Afficher le nom complet des managers

import pandas as pd

with open('C:\\Users\Administrateur\\PycharmProjects\\Yassine\\m2i\\data\\hr\\employees.csv') as f:

    #On crée une liste de colonnes, avec la ligne d'en-têtes et la focntion split? Elle va nous servir dans la boucle
    columns = 'EMPLOYEE_ID;FIRST_NAME;LAST_NAME;EMAIL;PHONE_NUMBER;HIRE_DATE;JOB_ID;SALARY;COMMISSION_PCT;MANAGER_ID;DEPARTMENT_ID'.split(';')
    # >>>> ['EMPLOYEE_ID', 'FIRST_NAME', 'LAST_NAME', 'EMAIL', 'PHONE_NUMBER', 'HIRE_DATE', 'JOB_ID', 'SALARY', 'COMMISSION_PCT', 'MANAGER_ID', 'DEPARTMENT_ID']

    #On crée une liste avec comme éléments, les lignes du fichier
    lines = f.readlines()

data_salaries = {j:[line[1:-3].split(';')[i] for line in lines if 'EMPLOYEE_ID' not in line] for i,j in enumerate(columns) }
    #print(data)

df = pd.DataFrame(data_salaries)
# print(df [df['COMMISSION_PCT'] != '' ])
#
# print(df[df['LAST_NAME']=='Whalen' ]['SALARY'])

# * Afficher le nom complet des employés qui sont dans le département 50 et qui ont un salaire > 3000
# print(df['SALARY'].astype(float))
emp_selected = df[(df['DEPARTMENT_ID'] =='50') & (df['SALARY'].astype(float) > 3000)]
print(emp_selected['FIRST_NAME']+' '+emp_selected['LAST_NAME'])

# * Afficher le nom complet des managers
#
# df4=df['EMPLOYEE_ID','FIRST_NAME','LAST_NAME']
# df4['EMPLOYEE_ID']=df4['EMPLOYEE_ID']+''
# df5 = df['MANAGER_ID','FIRST_NAME','LASTNAME']
# df5.columns=['EMPLOYEE_ID','FIRST_NAME','LAST_NAME']
#
# print(df4.join(df5, on='EMPLOYEE_ID'))

#Ne fonctionne pas, essayer avec des pd.series

