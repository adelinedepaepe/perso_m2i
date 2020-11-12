##Les boucles
# afficher le nombre d'employés pour chaque entreprises du cdictionnaire en utilisant, for, comprehension list puis while.

employees = {'Société Générale': 30, 'Engie':20, 'La Poste':10, 'Bouygues Telecom':100}

#Solution for
for (k,v) in employees.items():
  print(f"Le nombre d'employés de la société {k} est de {v}")

#Solution comprehesion list
print("\n".join([f"Le nombre d'employés de la société {k} est de {v}" for (k,v) in employees.items()]))

#Solution while

long = len(employees)-1
counter =0
company = list(employees.keys())

while counter <= long:
    print(long)
    print(counter)
    print(f"Le nombre de'employés de la société: {company[counter]} est de {employees[company[counter]]}")
    counter =counter+1

# Solution while pop
long = len(employees)
#print(employees.pop)

# while long >=0:
#     print(long)
#     for k in employees:
#         print(employees.pop(k))
#         long = len(employees)

# avec next

employees_iter = iter(employees)
item = next(employees_iter)

while item: #Ici on sous entend 'while item not null'
    print(f"Le nombre d'employés de la société {item} est de: {employees[item]}")
    try:
        item=next(employees_iter)
    except StopIteration:
        break

#Imprimer les chiffres impairs
l = list(range(10))

for i in range(len(l)):
    if i % 2 == 0:
        continue
    print(l[i])

#ou
odds = [i for i in range(10) if i%2 != 0]
print(odds)