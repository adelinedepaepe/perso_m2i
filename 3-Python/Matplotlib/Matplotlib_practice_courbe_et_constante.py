#Ecrire un script en utilisant matplotlib pour afficher la courbe des salaires des employés
#Lire les données salaire à partir du fichier emploees.csv
#Sotcker les sounées sour forme de liste
#Utiliser la fonction plot pour afficher la courbe des salaires
#4. Afficher une courbe pour la médiane, le min, le max et la moyenne des salaires

import matplotlib.pyplot as plt
import numpy as np

with open('C:\\Users\\Administrateur\\PycharmProjects\\Yassine\\m2i\\data\\hr\\employees.csv') as f:
    employees_salary = [
        int(line[1:-3].split(';')[7])
        for line in f if not line.startswith('\'EMPLOYEE_ID')
    ]

employees_salary_arr = np.array(employees_salary)
print(type(employees_salary_arr))
print(employees_salary_arr)

plt.plot(employees_salary_arr)
plt.axhline(y=np.median(employees_salary_arr), color='r', linestyle='-')
plt.axhline(y=np.average(employees_salary_arr), color='g', linestyle='-')
plt.axhline(y=np.min(employees_salary_arr), color='y', linestyle='-')
plt.axhline(y=np.max(employees_salary_arr), color='b', linestyle='-')
#plt.plot(np.median(employees_salary_arr))
#plt.show()
#
# fig = plt.figure()
# ax1 = fig.add_subplot(2,2,1)
# #plt.plot(np.median(employees_salary_arr))
# plt.plot(employees_salary_arr)
# ax2 = fig.add_subplot(2,2,2)
# #plt.plot(np.min(employees_salary_arr))
# plt.plot(employees_salary_arr)
# ax3 = fig.add_subplot(2,2,3)
# plt.plot(np.max(employees_salary_arr))
# ax4 = fig.add_subplot(2,2,4)
# plt.plot(np.mean(employees_salary_arr))

plt.show()