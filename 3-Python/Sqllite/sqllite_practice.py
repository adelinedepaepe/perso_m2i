# Ecrire un script python afin de:
#
# * Créer une base de données hr en utilisant sqlite3
# * Créer deux tables employees et departments en utilisant les colonnes spécifiées sur les deux fichiers employees.csv et departments.csv
# * Charger les données depuis les fichiers employees.csv et departments.csv
# * Créer un DataFrame pandas contenant pour chaque employé son ID, first_name, last_name, department_name en utilisant SQLAlchemy

import sqlite3

conn = sqlite3.connect('hr')
query = """
CREATE TABLE employees
(employee_id NUMBER(6,0), FIRST_NAME VARCHAR(20), LAST_NAME VARCHAR(20), EMAIL VARCHAR(20),
PHONE_NUMBER VARCHAR(20), HIRE_DATE DATE, JOB_ID VARCHAR(20), SALARY NUMBER(8,2), COMMISSION_PCT NUMBER(2,2),
MANAGER_ID NUMBER(6,0), DEPARTMENT_ID NUMBER(4,0))"""

# conn.execute(query)
# conn.commit()

with open ('C:\\Users\\Administrateur\\PycharmProjects\\Yassine\\m2i\\data\\hr\\employees.csv') as f:
    columns = 'EMPLOYEE_ID;FIRST_NAME;LAST_NAME;EMAIL;PHONE_NUMBER;HIRE_DATE;JOB_ID;SALARY;COMMISSION_PCT;MANAGER_ID;DEPARTMENT_ID'.split (
        ';' )
    lines = f.readlines ()
    data = [(line[1:-3].split ( ';' )[i] for line in lines if 'EMPLOYEE_ID' not in line) for i in
            columns]
    print (data[0])