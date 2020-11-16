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

  def resign(_self):
    print(f"L'employé {_self.lastName} {_self.firstName} portant l'id: {_self.id} a démissioné")

  def fire(_self):
      print(f"{_self.firstName} {_self.lastName} est licencié")
      del _self.firstName
      del _self.lastName
      del _self.hireDate
      del _self.id
      print ( f"{_self.firstName} {_self.firstName} est licencié" )

  def hire(_self, hireDate):
      _self.hireDate =hireDate
      print(f"La nouvelle date d'embauche de {_self.firstName} {_self.lastName} est le {_self.hireDate}")



#On lit le fichier enployees, et pour chaque ligne, on crée un oblet de la classe employee
employees_list=[]
with open ( 'C:\\Users\\Administrateur\\PycharmProjects\\Yassine\\m2i\\data\\hr\\employees.csv' ) as f:
     for line in f:
         if not line.startswith ( '\'EMPLOYEE_ID' ):
            employees_list.append(
                Employee(
                    line[1:-3].split ( ';' )[0],
                    line[1:-3].split ( ';' )[1],
                    line[1:-3].split ( ';' )[2],
                    line[1:-3].split ( ';' )[5]
                )
            )

#Comment interroger cette liste?
# Pour avoir l'id du premier: print(employees_list[0].id)
#Pour chercher l'employé avec l'id 120
# for e in employees_list:
#     if e.id == '120':
#         print(f"L'employé avec l'id 120 s'appelle {e.firstName} {e.lastName}")
#Pour chercher employé avec un id dynamique:
# id='120'
# for e in employees_list:
#      if e.id == id:
#          print(f"L'employé avec l'id {id} s'appelle {e.firstName} {e.lastName}")

#A l'extérieur de la classe, on peut définir une fonction puis l'appeler. Cette onction a pour but d'identifier l'employé rechercher.
#Elle peu ensuite faire appel à une fonction de la classe. (voir plus bas)
# def affiche(id):
#   """affiche id, nom, prénom lorsqu'on renseigne l'id"""
#   for e in employees_list:
#       if e.id == id:
#           print ( f"L'employé avec l'id {id} s'appelle {e.firstName} {e.lastName}" )
#
# affiche('134')

def read_employees(id):
    """Lit la liste des employés"""
    for e in employees_list:
        if e.id == id:
            #print ( e )
            #print ( e.lastName)
            print(f"Une action va être effectuée sur l'employé {e.firstName} {e.lastName} portant l'id: {e.id} et ayant été embauché le {e.hireDate}")
            return e



# def fire_employee(id):
#     """Identifie le salarié désigné par l'id, puis applique la méthode resign à cet employé"""
#     for e in employees_list:
#         if e.id == id:
#             e.fire()


def fire_employee2(id):
    read_employees(id).fire()

def resign_employee(id):
    """Affiche les informations de l'employé nom de l'employé qui a demissionné"""
    read_employees ( id ).resign()

def hire_employee(id, hireDate):
    """Change la hireDate"""
    read_employees(id).hire(hireDate)



fire_employee2('120')
resign_employee('134')
hire_employee('110','02/02/2020')


# fire_employee2('120')


# for e in employees_list:
#    print ( e.id )
