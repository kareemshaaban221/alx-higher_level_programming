-- creates table `second_table` in database `hbtn_0c_0` and adds multiple rows
-- table description: `id` INT, `name` VARCHAR(256), `score` INT
-- add records (1, "John", 10), (2, "Alex", 3), (3, "Bob", 14), and (4, "George", 8)
CREATE TABLE IF NOT EXISTS `second_table` (
	`id` INT,
	`name` VARCHAR(256),
	`score` INT
);
INSERT INTO `second_table` VALUES(1, "John", 10);
INSERT INTO `second_table` VALUES(2, "Alex", 3);
INSERT INTO `second_table` VALUES(3, "Bob", 14);
INSERT INTO `second_table` VALUES(4, "George", 8);
