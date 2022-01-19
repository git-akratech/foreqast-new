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
