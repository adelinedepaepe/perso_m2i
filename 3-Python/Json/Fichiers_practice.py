import pandas as pd
import json

with open('../../../Yassine/m2i/data/hr/employees.csv') as f:
  employees = [ ##Ici on crée une liste de dictionnaires avec le '[]'
      {
        'FIRST_NAME':line.split(';')[1],
        'LAST_NAME':line.split(';')[2],
        'DEPARTMENT_ID':line[:-3].split(';')[10],
      }
        for line in f if 'EMPLOYEE_ID' not in line ]


with open('../../../Yassine/m2i/data/hr/departments.csv') as f:
   departments ={ ##En ne mettant pas les crochets, on créé un dictionnaore simple, et non une liste de dictionnaires
            line[1:].split(';')[0]:line.split ( ';' )[1] #On ne s'intéresse qu'aux valeurs
       for line in f if 'DEPARTMENT_ID' not in line} #Le if permet de supprimer la ligne des en-tetes
#
print(departments)
#
#
# Je veux stocker first_name, last_name et department_name
my_employees=[{'FIRST_NAME':e['FIRST_NAME'], 'LAST_NAME': e['LAST_NAME'], 'DEPARTMENT_NAME':departments.get(e['DEPARTMENT_ID'],0)} for e in employees]

#J'écris mon résultat dans un fichier json. Il faut en amont importer json en haut du fichier 'import json'
with open('my_employees.jsonl', 'w') as f:
  json.dump(my_employees, f)


