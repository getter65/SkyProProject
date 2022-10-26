SELECT *
FROM orders
ORDER BY shipped_date, required_date DESC;

SELECT AVG(shipped_date - order_date)
FROM orders
WHERE ship_country = 'USA';

SELECT SUM(unit_price * units_in_stock)
FROM products
WHERE discontinued = 0;