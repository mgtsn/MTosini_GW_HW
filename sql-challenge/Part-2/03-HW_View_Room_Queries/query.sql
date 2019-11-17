CREATE VIEW title_count AS(
	select f.title, i.count AS "Number of Copies"
	from 
		(select film_id, count(*)
		 from inventory
		 group by film_id) 
		as i,
		film as f
	where f.film_id = i.film_id);
	
	
SELECT *
FROM title_count
WHERE "Number of Copies" = 7;