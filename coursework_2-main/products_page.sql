SELECT product_name, units_in_stock, contact_person, phone
FROM products
JOIN suppliers ON suppliers.id_supplier = products.fk_id_suppliers
JOIN categories ON categories.category_id = products.category_id
WHERE categories.category_name in ('Beverages', 'Seafood') and products.discontinued <> 1 and products.units_in_stock < 20;