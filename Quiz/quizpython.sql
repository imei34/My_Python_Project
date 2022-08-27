SHOW DATABASES;

CREATE DATABASE quizpy;

SHOW DATABASES;

USE quizpy;

SHOW TABLES;

CREATE TABLE user(
id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
npm VARCHAR(11) NOT NULL,
nama VARCHAR(100) NOT NULL,
jurusan VARCHAR(30) NOT NULL,
email VARCHAR(30) NOT NULL UNIQUE KEY,
password VARCHAR(20) NOT NULL,
gender ENUM('L','P') NOT NULL
)ENGINE= Innodb;

show create TABLE user;

DESC user;

INSERT INTO user(nama,email,password,gender,npm,jurusan) 
VALUES('Ucok','ucokganteng123@gmail.com','ucoktamvan','L','2115341213','Teknik Sipil'),
	  ('Otong','otongpinter@gmail.com','otongmerdeka','L','2115981543','Teknik Sipil');

SELECT * FROM user;