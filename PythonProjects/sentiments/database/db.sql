CREATE TABLE `general_db`.`crop_list` (
`id` INT NOT NULL AUTO_INCREMENT ,
`username` varchar(50) NOT NULL ,
`areaCode` FLOAT NOT NULL ,
 `element` VARCHAR(50) NOT NULL ,
 `itemCode` VARCHAR(50) NOT NULL ,
 `item` VARCHAR(50) NOT NULL ,
 `itemYear` VARCHAR(50) NOT NULL ,
 `unit` VARCHAR(50) NOT NULL ,
 `itemValue` VARCHAR(50) NOT NULL ,
    `date_created` DATETIME(6) NOT NULL ,
`last_modified` DATETIME(6) NOT NULL ,
PRIMARY KEY (`id`)) ENGINE = InnoDB;