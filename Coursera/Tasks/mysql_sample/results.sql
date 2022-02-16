use test
set names utf8;

-- 1. Выбрать все товары (все поля)
SELECT * FROM product

-- 2. Выбрать названия всех автоматизированных складов
SELECT name FROM store WHERE is_automated = 1

-- 3. Посчитать общую сумму в деньгах всех продаж
SELECT SUM(total) FROM sale

-- 4. Получить уникальные store_id всех складов, с которых была хоть одна продажа
SELECT DISTINCT store_id FROM sale

-- 5. Получить уникальные store_id всех складов, с которых не было ни одной продажи
SELECT store_id FROM store WHERE store_id NOT IN (SELECT DISTINCT store_id FROM sale)

-- 6. Получить для каждого товара название и среднюю стоимость единицы товара avg(total/quantity), если товар не продавался, он не попадает в отчет.
SELECT product.name, AVG(total/quantity) FROM sale JOIN product ON product.product_id = sale.product_id GROUP BY product.name

-- 7. Получить названия всех продуктов, которые продавались только с единственного склада
SELECT product.name FROM sale JOIN product ON product.product_id = sale.product_id GROUP BY product.name HAVING COUNT(DISTINCT store_id) = 1

-- 8. Получить названия всех складов, с которых продавался только один продукт
SELECT store.name FROM sale JOIN store ON sale.store_id = store.store_id GROUP BY store.name HAVING COUNT(DISTINCT product_id) = 1

-- 9. Выберите все ряды (все поля) из продаж, в которых сумма продажи (total) максимальна (равна максимальной из всех встречающихся)
SELECT * FROM sale WHERE total = (SELECT MAX(total) FROM sale)

-- 10. Выведите дату самых максимальных продаж, если таких дат несколько, то самую раннюю из них
SELECT date FROM sale GROUP BY date ORDER BY SUM(total) DESC limit 1

-- #####################################################################################################################
-- Решение задания по MySQL
-- #####################################################################################################################
use test
set names uft8;

-- 1. Выбрать все товары (все поля)
select * from product

-- 2. Выбрать названия всех автоматизированных складов
select name from store where is_automated = 1

-- 3. Посчитать общую сумму в деньгах всех продаж
select sum(total) from sale

-- 4. Получить уникальные store_id всех складов, с которых была хоть одна продажа
select distinct(store_id) from sale

-- 5. Получить уникальные store_id всех складов, с которых не было ни одной продажи
select store_id from store natural left join sale where sale.store_id is null

-- 6. Получить для каждого товара название и среднюю стоимость единицы товара avg(total/quantity), если товар не продавался, он не попадает в отчет.
select name, avg(total/quantity) from product natural join sale group by product_id


-- 7. Получить названия всех продуктов, которые продавались только с единственного склада
select name from product natural join sale group by product_id having count(distinct store_id) = 1

-- 8. Получить названия всех складов, с которых продавался только один продукт
select name from store natural join sale group by store_id having count(distinct product_id) = 1

-- 9. Выберите все ряды (все поля) из продаж, в которых сумма продажи (total) максимальна (равна максимальной из всех встречающихся)
select * from sale where total = (select max(total) from sale);

-- 10. Выведите дату самых максимальных продаж, если таких дат несколько, то самую раннюю из них
select date from sale group by date order by sum(total) DESC, date ASC LIMIT 1

-- ###################################################################################################################

-- Создать базу данных "test": https://dev.mysql.com/doc/refman/5.7/en/create-database.html
CREATE DATABASE test CHARACTER SET utf8 COLLATE utf8_general_ci;


-- Создать пользователя dbuser с паролем dbpass и дать ему права на test: https://dev.mysql.com/doc/refman/5.7/en/adding-users.html
CREATE USER 'dbuser'@'%' IDENTIFIED BY 'dbpass';
GRANT ALL PRIVILEGES ON test.* TO 'dbuser'@'%' WITH GRANT OPTION;


-- Использовать базу "test" для всех последующих запросов, в которых явно не указана база: https://dev.mysql.com/doc/refman/5.7/en/database-use.html
USE test;


-- Создать таблицу пользователей с разными типами полей, настройки индексов в полях: https://dev.mysql.com/doc/refman/5.7/en/create-table.html
CREATE TABLE user (
	`user_id`  INTEGER UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY COMMENT 'id',
	`login` VARCHAR(32) NOT NULL UNIQUE COMMENT 'логин (уникален и до 32 символов)',
	`password_hash` BINARY(32) NOT NULL COMMENT 'хеш пароля, всегда ровно 32 байта',
	`created_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT 'дата создания',
	`updated_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT 'дата обновления',
	`gender` ENUM('male', 'female', 'other') NOT NULL DEFAULT 'male' COMMENT 'пол',
	`flags` SET('disabled', 'moderator', 'verified') NOT NULL COMMENT 'разные флаги',
	`about` TEXT NULL COMMENT 'текст о себе (до 65535 символов)'
)
ENGINE = INNODB
COMMENT = 'Талица пользователей';


-- Создать таблицу сообщений, настройки индексов и ограничений отдельно от полей
CREATE TABLE message (
  message_id INT UNSIGNED NOT NULL AUTO_INCREMENT COMMENT 'id',
  user_id INT UNSIGNED NOT NULL COMMENT 'пользователь',
  message TEXT NOT NULL COMMENT 'текст сообщения',
  PRIMARY KEY (message_id),
  CONSTRAINT FK_message_user_user_id FOREIGN KEY (user_id) REFERENCES user(user_id) ON DELETE RESTRICT ON UPDATE RESTRICT
)
ENGINE = INNODB
COMMENT = 'Сообщения пользователей';


-- Добавить пользователей, два вида синтаксиса INSERT: https://dev.mysql.com/doc/refman/5.7/en/insert.html
INSERT INTO `user` ( `login`, `password_hash`, `gender`, `flags`, `about`) VALUES ('admin', UNHEX('5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8'), 'male', 'moderator,verified', 'I\'m a superuser');
INSERT INTO `user` SET `login`='user', `password_hash`=UNHEX('113459eb7bb31bddee85ade5230d6ad5d8b2fb52879e00a84ff6ae1067a210d3'), `gender`='female', `flags`='disabled,verified', `about`='hello!';


-- Выбрать логины всех пользователей: https://dev.mysql.com/doc/refman/5.7/en/select.html
SELECT login FROM user;


-- Добавить три сообщения пользователя admin (user_id=1) одним INSERT
INSERT INTO message(user_id, message) VALUES (1, 'one'), (1, 'two'), (1, 'three');


-- Скопировать и модифицировать сообщения admin'а в сообщения user (user_id=2): https://dev.mysql.com/doc/refman/5.7/en/insert-select.html
INSERT INTO message(user_id, message) SELECT 2, CONCAT('user: ', message) FROM message;


-- Выбрать все сообщения всех пользователей женского пола https://dev.mysql.com/doc/refman/5.7/en/join.html:
SELECT m.message FROM message m JOIN user u ON(m.user_id = u.user_id) WHERE u.gender = 'female';


-- Посчитать для каждого пользователя, сколько он оставил сообщений, содержащих букву "e": https://dev.mysql.com/doc/refman/5.7/en/string-comparison-functions.html#operator_like
SELECT u.*, COUNT(m.message_id) msg_cnt FROM user u NATURAL JOIN message m WHERE m.message LIKE '%e%' GROUP BY u.user_id;


-- Выбрать пользователя (одного), у которого больше всех сообщений, содержащих букву "е": https://dev.mysql.com/doc/refman/5.7/en/group-by-functions-and-modifiers.html
SELECT u.* FROM user u NATURAL JOIN message m WHERE m.message LIKE '%e%' GROUP BY u.user_id ORDER BY COUNT(m.message_id) DESC LIMIT 1;


-- Изменить сообщения пользователей, добавив в текст логин отправителя и id сообщения. MySQL Workbench ругается, если update без where, поэтому надо изменить его настройки, как написано в абзаце перед примерами: https://dev.mysql.com/doc/refman/5.7/en/update.html
UPDATE message m NATURAL JOIN user u SET m.message=CONCAT('user "', u.login, '", message #', m.message_id, ': ', REPLACE(m.message, 'user: ', ''));


-- Удалить все сообщения с четными id: https://dev.mysql.com/doc/refman/5.7/en/delete.html
DELETE FROM message WHERE NOT message_id % 2;