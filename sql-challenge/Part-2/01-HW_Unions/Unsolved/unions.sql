CREATE VIEW all_parties AS
SELECT first_name, last_name, 'actor' AS Source
FROM actor
UNION
SELECT first_name, last_name, 'staff' AS Source
FROM staff
UNION
SELECT first_name, last_name, 'customer' AS Source
FROM customer;

select * from all_parties



SELECT id
FROM customer_list
WHERE city = 'London'
UNION ALL
SELECT
	c.customer_id
FROM customer c
INNER JOIN address a
ON a.address_id = c.address_id
INNER JOIN city y
ON y.city_id = a.city_id
WHERE y.city = 'London'