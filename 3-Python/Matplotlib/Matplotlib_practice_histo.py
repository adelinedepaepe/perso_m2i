#Afficher un tracé pour chaque salaire le nb d'employés qui le perçoivent
#LIre les données de salaire depuis le fichier employés
#Stocker les valeurs dans une liste
#Créer un dictionnaire sous forme {1200:3, ...} pour stocker pour chaque salaire le nombre d'employés qui le perçoivent
#En utilisant la fonction plot, afficher le diagrame où x est le salaire et y est le nombre d'employés qui perçoivent ce salaire

import matplotlib.pyplot as plt
import numpy as np

with open('C:\\Users\\Administrateur\\PycharmProjects\\Yassine\\m2i\\data\\hr\\employees.csv') as f:
    employees_salary = [
        int(line[1:-3].split(';')[7])
        for line in f if not line.startswith('\'EMPLOYEE_ID')
    ]

salary_dict={}
for e in employees_salary:
    salary_dict[e] = employees_salary.count(e)

print(salary_dict)
print(salary_dict.values())

fig = plt.figure()
ax1 = fig.add_subplot(2,2,1)
plt.plot(salary_dict.keys(), salary_dict.values())
ax2 = fig.add_subplot(2,2,2)
plt.hist(employees_salary, bins = 5, color = 'yellow', edgecolor = 'red')
#ou plt.hist(employees_salary, bins = [0,5000,10000, 15000, 20000, 25000], color = 'yellow', edgecolor = 'red')
ax3 = fig.add_subplot(2,2,3)
plt.scatter(salary_dict.keys(), salary_dict.values())


plt.show()



# plt.hist(employees_salary, range = (0, 25000), bins = 10, color = 'yellow',
#             edgecolor = 'red')
# plt.xlabel('valeurs')
# plt.ylabel('nombres')
# plt.title('Exemple d\' histogramme simple')
#
# plt.show()