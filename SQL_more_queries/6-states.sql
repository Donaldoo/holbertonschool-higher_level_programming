-- creates database and tabe
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states (
	id int UNIQUE AUTO_INCREMENT NOT NULL,
	PRIMARY KEY (id),
	name VARCHAR(256)
);
