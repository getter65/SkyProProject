SELECT last_name, first_name, home_phone, region
FROM employees
WHERE region is NULL;

SELECT DISTINCT customers.country
FROM customers
INTERSECT
SELECT suppliers.country
FROM suppliers
EXCEPT 
SELECT employees.country
FROM employees;