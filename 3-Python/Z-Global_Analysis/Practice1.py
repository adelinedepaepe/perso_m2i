#Prendre toutes les variables sauf longitude et latitue
#Créer un graph divisé en plusieurs graphe

import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv ('C:\\Users\\Administrateur\\PycharmProjects\\Yassine\\m2i\\matplotlib\\labs\\lab4\\california_housing_train.csv')
# print(data)
households = data['households']
population = data ['population']
median_income = data ['median_income']
total_bedrooms=data['total_bedrooms']
total_rooms=data['total_rooms']
housing_median_age = data['housing_median_age']
#
fig = plt.figure(figsize=(20,20))
#
# ax1 = fig.add_subplot(6,6,1)
# plt.scatter(households,households)
# ax2 = fig.add_subplot(6,6,2)
# plt.scatter(households,population)
# ax3 = fig.add_subplot(6,6,3)
# plt.scatter(households,median_income)
# ax4 = fig.add_subplot(6,6,4)
# plt.scatter(households,total_bedrooms)
# ax5 = fig.add_subplot(6,6,5)
# plt.scatter(households,total_rooms)
# ax6 = fig.add_subplot(6,6,6)
# plt.scatter(households,housing_median_age)
# ax7 = fig.add_subplot(6,6,7)
# plt.scatter(population,households)

print(housing_median_age)

series= ['households','population','median_income','total_bedrooms','total_rooms','housing_median_age']

i=1
x=0

while x<6:
    y=0
    while y<6:
        variable='ax'+str(i)
        variable=fig.add_subplot(6,6,i)
        plt.scatter(data[series[x]],data[series[y]])
        variable.set_xlabel ( str(series[x]) )
        variable.set_ylabel ( str(series[y]) )
        i = i+1
        y = y+1
    x = x+1

plt.show()

# print(i)
# print(series[x])
# print(series[y])
#print(variable)