CREATE USER UNIVERSITY IDENTIFIED BY university_mdp;

GRANT CREATE SESSION TO UNIVERSITY;

GRANT CREATE TABLE TO UNIVERSITY;

GRANT UNLIMITED TABLESPACE TO UNIVERSITY;

CREATE ROLE administration;
CREATE ROLE teachers;
CREATE ROLE student;

GRANT SELECT, UPDATE, DELETE ON university.students to administration;
GRANT SELECT, UPDATE, DELETE ON university.modules to administration;
GRANT SELECT, UPDATE, DELETE ON university.marks to administration;
GRANT SELECT, UPDATE, DELETE ON university.modules to teachers;
GRANT SELECT, UPDATE, DELETE ON university.marks to teachers;
GRANT INSERT ON university.students to administration;
GRANT INSERT ON university.modules to administration;
GRANT INSERT ON university.marks to administration;
GRANT INSERT ON university.modules to teachers;
GRANT INSERT ON university.marks to teachers;


CREATE USER SONIA IDENTIFIED BY sonia_mdp;
GRANT CREATE SESSION TO SONIA;
GRANT administration TO SONIA;

CREATE USER YASMINE IDENTIFIED BY yasmine_mdp;
GRANT CREATE SESSION TO YASMINE;
GRANT teachers TO YASMINE;

CREATE USER MARLOW IDENTIFIED BY marlow_mdp;
GRANT CREATE SESSION TO MARLOW;
GRANT teachers TO MARLOW;

