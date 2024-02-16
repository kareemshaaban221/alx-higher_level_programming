-- This is my comment
SELECT a.id, a.name, b.name
FROM cities AS a
JOIN states AS b ON a.state_id = b.id;
