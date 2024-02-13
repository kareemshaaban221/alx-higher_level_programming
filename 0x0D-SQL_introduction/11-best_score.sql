-- lists all records with `score >= 10` in table `second_table` of database `hbtn_0c_0`
-- results to display score and name (in this order) and orger by score (top first)
SELECT `score`, `name` FROM `second_table` WHERE `score` >= 10 ORDER BY `score` DESC;
