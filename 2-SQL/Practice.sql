--Les employ�s qui ont un num�ro de t�l sous le format XXX.XXX.XXXX

select *
from employees 
where regexp_like(phone_number, '[0-9]{3}.[0-9]{3}.[0-9]{4}');

--Pour chaque employ�, Le nombre d'ann�es d'exp�rience

SELECT FIRST_NAME, LAST_NAME, HIRE_DATE, ROUND(((sysdate-hire_date)/365),0) EXPERIENCE
FROM employees;

--Les employ�s qui ont �t� recrut�s en mois de Mars

SELECT FIRST_NAME,LAST_NAME, hire_date
FROM employees
where to_char(hire_date, 'mm')='03';

--Les employ�s dont le salaire est sup�rieur au salaire moyen

SELECT FIRST_NAME, LAST_NAME, SALARY
FROM employees
WHERE SALARY > (SELECT AVG(salary)
    FROM employees);