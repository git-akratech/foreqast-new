
drop table if exists foreqast_user;
CREATE TABLE `foreqast_user` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `user_id` VARCHAR(45) NOT NULL,
  `full_name` VARCHAR(100) NOT NULL,
  `email_id` VARCHAR(45) NOT NULL,
  `password` VARCHAR(500) NOT NULL,
  `registered_on` DATETIME NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `user_id_UNIQUE` (`user_id` ASC));

CREATE TABLE `foreqast_generation_data` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `ba_name` VARCHAR(45) NULL,
  `timestamp` DATETIME NULL,
  `freq` VARCHAR(45) NULL,
  `gen_MW` DOUBLE NULL,
  `market` VARCHAR(45) NULL,
  `fuel_name` VARCHAR(45) NULL,
  PRIMARY KEY (`id`));

CREATE TABLE `foreqast_load_data` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `ba_name` VARCHAR(45) NULL,
  `timestamp` DATETIME NULL,
  `freq` VARCHAR(45) NULL,
  `load_MW` DOUBLE NULL,
  `market` VARCHAR(45) NULL,
  PRIMARY KEY (`id`));

CREATE TABLE `foreqast_trade_data` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `ba_name` VARCHAR(45) NULL,
  `timestamp` DATETIME NULL,
  `freq` VARCHAR(45) NULL,
  `net_exp_MW` DOUBLE NULL,
  `market` VARCHAR(45) NULL,
  PRIMARY KEY (`id`));
