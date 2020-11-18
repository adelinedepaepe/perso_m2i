# Ecrire un script python afin de:
# * Créer une base de données hr en utilisant sqlite3
# * Créer deux tables employees et departments en utilisant les colonnes spécifiées sur les deux fichiers employees.csv et departments.csv
# * Charger les données depuis les fichiers employees.csv et departments.csv
# * Afficher pour chaque employé son ID, first_name, last_name, department_name en utilisant SQLAlchemy

import sqlite3
name = 'hr'
con = sqlite3.connect('hr')
query = 'drop table employees'
con.execute(query)

query = """
  CREATE TABLE employees
  (a INTEGER, b VARCHAR(20), c VARCHAR(20), d VARCHAR(20), e VARCHAR(20), f DATE, g VARCHAR(20), h NUMBER(20), 
  i REAL, j INTEGER, k NUMBER(20)
  );"""

con.execute(query)
con.commit()
with open('../../data/hr/employees.csv') as f:
    lines = f.readlines()


data = [(int(line[1:-3].split(';')[0]),
        line[1:-3].split(';')[1],
         line[1:-3].split(';')[2],
         line[1:-3].split(';')[3],
         line[1:-3].split(';')[4],
         line[1:-3].split(';')[5],
         line[1:-3].split(';')[6],
         line[1:-3].split(';')[7],
         float(line[1:-3].split(';')[8].replace(',', '.') if line[1:-3].split(';')[8] != '' else 0),
         int(line[1:-3].split(';')[9] if line[1:-3].split(';')[9] != '' else 0),
         int(line[1:-3].split(';')[10] if line[1:-3].split(';')[10] != '' else 0))
        for line in lines if 'EMPLOYEE_ID' not in line]

print(data)


stmt = "INSERT INTO employees VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
con.executemany(stmt, data)
con.commit()
cursor = con.execute('SELECT * FROM employees')
rows = cursor.fetchall()
x = cursor.description

import pandas as pd
df = pd.DataFrame(rows, columns=[x[0] for x in cursor.description])
print(df)