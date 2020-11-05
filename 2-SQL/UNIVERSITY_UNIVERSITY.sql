
CREATE TABLE students
(
    id NUMBER(6) CONSTRAINT stu_id_pk PRIMARY KEY,
    first_name VARCHAR2 (30) ,
    last_name VARCHAR2 (30),
    birth_date DATE,
    address VARCHAR2 (255),
    ville VARCHAR2 (30),
    pays VARCHAR2 (30)
);

CREATE TABLE modules
(
    id NUMBER(6) CONSTRAINT mod_id_pk PRIMARY KEY,
    label VARCHAR2 (30) ,
    start_date DATE,
    end_date DATE -- Question, est-ce qu'on peut dire > à start date, erreur on ne peut faire reference à une autre colonne
);

CREATE TABLE marks
(
    id NUMBER(6) ,
    mark NUMBER(6) ,
    student_id NUMBER(6),
    module_id NUMBER(6),
    CONSTRAINT mar_id_pk PRIMARY KEY (id),
    CONSTRAINT mar_mar_min CHECK (mark>0),
    CONSTRAINT mar_student_fk FOREIGN KEY (student_id) REFERENCES students(id),
    CONSTRAINT mar_module_fk FOREIGN KEY (module_id) REFERENCES modules(id)
);

ALTER TABLE marks
MODIFY mark NUMBER(4,2);
