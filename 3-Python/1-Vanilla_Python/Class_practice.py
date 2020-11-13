# Ecrire un script Python pour :
#
# Créer une classe Employee avec les attributs et les méthodes suivantes:
#
# * id
# * firstName
# * lastName
# * hireDate
#
# Créer Les méthodes suivantes pour la classe Employee:
#
# * hire: elle permet de changer la valeur de la date d'embauche à l'argument passé
# * fire: elle permet de supprimer l'employé de la liste
# * resign: elle permet d'afficher le message "Employé démissionné"
#
# En utilisant une boucle ou une comprehension list, créer des objets contenant les différents employés contenus
# dans le fichier employees.csv
#
# Exécuter la méthode fire pour remercier l'employé dont l'id est 120



class Employee():
  # Les attributs de chaque employé
  id = ''
  firstName = ''
  lastName = ''
  hireDate = ''

  def __init__(_self, id, firstName, lastName, hireDate): # L'initialisation de l'objet
    """
      Méthode permettant d'initialiser un objet de type Employee
    """
    _self.id = id
    _self.firstName = firstName
    _self.lastName = lastName
    _self.hireDate = hireDate



#Tempo2: On créé une méthode qui affiche id, nom, prénom lorsqu'on renseigne l'id
  def affiche(_self):
      """affiche id, nom, prénom lorsqu'on renseigne l'id"""
      #for e in list:
      #    if e.id==_self:
      #        print(e.id +' '+ e.firstName +' '+ e.lastName)
      print(_self.id)

  def hire(_self, hireDate='01/01/2020'):
     _self.hireDate =hireDate
#
# def fire(_self, id):
#   pass
#
# def resign(_self):
#   pass
employees_list=[]
with open ( 'C:\\Users\\Administrateur\\PycharmProjects\\Yassine\\m2i\\data\\hr\\employees.csv' ) as f:
     for line in f:
         if not line.startswith ( '\'EMPLOYEE_ID' ):
            employees_list.append(
                Employee(
                    line[1:-3].split ( ';' )[0],
                    line[1:-3].split ( ';' )[1],
                    line[1:-3].split ( ';' )[2],
                    line[1:-3].split ( ';' )[7]
                )
            )

i=0
id='120'
for emp in employees_list:
    print(emp.id)
    if int(emp.id) == int(id):
        index= employees_list
        print(f"nous avons trouvé l'employé {id} et son nom est {employees_list[int(id)].firstName}")


# print(employees_list)
# print(employees_list[0].id)

#Je cherche à concaténer un nom de variable et un choffre pour faire une varible qui s'incrémente
# variable_list = 'employee'+ str(2*2)
# print(variable_list)
emp_test=Employee('999','Adeline','DIDIER','01/01/2020')
variable=Employee('998','Adeline','DIDIER','01/01/2020')

#Employee.affiche(120)


    #emp_test.affiche(120)

    # #tempo1: on crée une boucle pour parcourir tous les salariés, et afficher id, prénom et nom si id = 120
    #
    # for e in employees_list:
    #     if e.id=='120':
    #         print(e.id +' '+ e.firstName +' '+ e.lastName)
