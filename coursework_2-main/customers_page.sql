SELECT COUNT(*)
FROM customers;

SELECT DISTINCT city, country
FROM customers
ORDER BY country;

SELECT customers.company_name, last_name, first_name
FROM orders
JOIN customers ON customers.customer_id = orders.customer_id
JOIN employees ON employees.employee_id = orders.employee_id
JOIN shippers ON shippers.shipper_id = orders.ship_via
WHERE employees.city = 'London' and customers.city = 'London' and shippers.company_name = 'Speedy Express';

SELECT customers.customer_id, orders.order_id
FROM customers
LEFT JOIN orders ON orders.customer_id = customers.customer_id
WHERE orders.order_id is NULL;