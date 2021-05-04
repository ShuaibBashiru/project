CREATE TABLE `text_summary_db`.`text_summary_tbl` (
`id` INT NOT NULL AUTO_INCREMENT ,
`username` varchar(80) NOT NULL ,
`notes` text NOT NULL ,
`notetitle` text NOT NULL ,
`summary` text NOT NULL ,
    `date_created` DATETIME(6) NOT NULL ,
`last_modified` DATETIME(6) NOT NULL ,
PRIMARY KEY (`id`)) ENGINE = InnoDB;


CREATE TABLE `pdf_extract`.`file_uploads_tbl` (
`id` INT NOT NULL AUTO_INCREMENT ,
`user_id` varchar(80) NOT NULL ,
`file_title` text NOT NULL ,
`file_name` text NOT NULL ,
 `date_created` DATETIME(6) NOT NULL ,
`last_modified` DATETIME(6) NOT NULL ,
PRIMARY KEY (`id`)) ENGINE = InnoDB;


CREATE TABLE `pdf_extract`.`file_extracted_tbl` (
`id` INT NOT NULL AUTO_INCREMENT ,
`user_id` varchar(80) NOT NULL ,
`file_id` INT NOT NULL ,
 `date_created` DATETIME(6) NOT NULL ,
`last_modified` DATETIME(6) NOT NULL ,
PRIMARY KEY (`id`)) ENGINE = InnoDB;