CREATE TABLE `text_summary_db`.`text_summary_tbl` (
`id` INT NOT NULL AUTO_INCREMENT ,
`username` varchar(80) NOT NULL ,
`notes` text NOT NULL ,
`notetitle` text NOT NULL ,
`summary` text NOT NULL ,
    `date_created` DATETIME(6) NOT NULL ,
`last_modified` DATETIME(6) NOT NULL ,
PRIMARY KEY (`id`)) ENGINE = InnoDB;