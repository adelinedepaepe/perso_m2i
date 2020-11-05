--Les employés qui ont un numéro de tél sous le format XXX.XXX.XXXX

select *
from employees 
where regexp_like(phone_number, '[0-9]{3}.[0-9]{3}.[0-9]{4}');

--Pour chaque employé, Le nombre d'années d'expérience

SELECT FIRST_NAME, LAST_NAME, HIRE_DATE, ROUND(((sysdate-hire_date)/365),0) EXPERIENCE
FROM employees;

--Les employés qui ont été recrutés en mois de Mars

SELECT FIRST_NAME,LAST_NAME, hire_date
FROM employees
where to_char(hire_date, 'mm')='03';

--Les employés dont le salaire est supérieur au salaire moyen

SELECT FIRST_NAME, LAST_NAME, SALARY
FROM employees
WHERE SALARY > (SELECT AVG(salary)
    FROM employees);