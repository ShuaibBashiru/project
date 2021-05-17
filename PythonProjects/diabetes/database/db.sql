CREATE TABLE `general_db`.`diabetes_list` (
`id` INT NOT NULL AUTO_INCREMENT ,
`username` varchar(50) NOT NULL ,
`glucose` FLOAT NOT NULL ,
 `bloodPressure` FLOAT NOT NULL ,
 `skinThickness` FLOAT NOT NULL ,
  `insulin` FLOAT NOT NULL ,
  `bmi` FLOAT NOT NULL ,
   `pedigreeFunction` FLOAT NOT NULL ,
    `age` FLOAT NOT NULL ,
    `date_created` DATETIME(6) NOT NULL ,
`last_modified` DATETIME(6) NOT NULL ,
PRIMARY KEY (`id`)) ENGINE = InnoDB;