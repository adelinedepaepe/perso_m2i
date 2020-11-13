#Comparer les salaires des départmeents shipping et sales (50 et 20)
#Lire les données de salaires du fichier employees
#Lire les données de departments.csv
#Créer deux listes pour stocker les salaires pour les deux départments
#Créer deux tracés  pour chaque département
#Créer un troisème tracé  pour comparer les salaires des deux départements

import matplotlib.pyplot as plt
import numpy as np

with open('C:\\Users\\Administrateur\\PycharmProjects\\Yassine\\m2i\\data\\hr\\employees.csv') as f:
    salary = [
        {line[1:-3].split(';')[10]:int(line[1:-3].split(';')[7])} for line in f if not line.startswith ( '\'EMPLOYEE_ID' )
    ]

with open('C:\\Users\\Administrateur\\PycharmProjects\\Yassine\\m2i\\data\\hr\\departments.csv') as f:
    departments=[
        line[1:].split(';')[0]
        for line in f if not 'DEPARTMENT_ID' in line
    ]


print(salary)
shipping_salary=[]
sales_salary=[]
for s in salary:
    if int(s.get('50',0))>0:
        shipping_salary.append(s.get('50'))
    if int ( s.get ( '80', 0 ) ) > 0:
        sales_salary.append(s.get('80'))

print(shipping_salary)
print(sales_salary)

fig = plt.figure()
ax1 = fig.add_subplot(2,2,1)
plt.hist(shipping_salary, bins=5)
ax2 = fig.add_subplot(2,2,2)
plt.hist(sales_salary, bins=5)
ax3 = fig.add_subplot(2,2,3)
plt.hist([shipping_salary,sales_salary], bins=5)

#Voir dans notebook, l'autre syntaxe qui permet de mettre les memes axes pour les différnets tracés

plt.show()