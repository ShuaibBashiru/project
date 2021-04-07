CREATE TABLE user_record(
id int not null AUTO_INCREMENT,
    PRIMARY KEY(id),
    lastname varchar(50) not null,
    firstname varchar(50) not null,
    othername varchar(50) null,
    email_one varchar(50) not null,
    email_two varchar(50) null,
    phone_one varchar(50) not null,
    phone_two varchar(50) null,
    persional_id varchar(50) null,
    account_type varchar(50) null,
    user_role varchar(50) null,
    pwd_auth_hash varchar(60) null,
    pwd_auth varchar(60) null,
    date_created datetime(6) not null,
    last_modified datetime(6) not null
);
CREATE TABLE admin_record(
id int not null AUTO_INCREMENT,
    PRIMARY KEY(id),
    lastname varchar(50) not null,
    firstname varchar(50) not null,
    othername varchar(50) null,
    email_one varchar(50) not null,
    email_two varchar(50) null,
    phone_one varchar(50) not null,
    phone_two varchar(50) null,
    persional_id varchar(50) null,
    account_type varchar(50) null,
    pwd_auth_hash varchar(60) null,
    pwd_auth varchar(60) null,
    date_created datetime(6) not null,
    last_modified datetime(6) not null
);
CREATE TABLE password_reset(
id int not null AUTO_INCREMENT,
    PRIMARY KEY(id),
    email_one varchar(50) not null,
    resetCode varchar(50) not null,
    date_created datetime(6) not null,
    last_modified datetime(6) not null
);
INSERT INTO `admin_record`
(`id`, `lastname`, `firstname`, `othername`, `email_one`, `email_two`,
 `phone_one`, `phone_two`, `persional_id`, `account_type`, `pwd_auth_hash`,
  `pwd_auth`, `pwd`, `date_created`, `last_modified`)
  VALUES (NULL, 'bashiru', 'shuaib', NULL, 'instructsme@gmail.com',
  NULL, '08172790181', NULL, NULL, NULL, NULL, NULL, NULL,
  '2021-03-09 15:14:13.000000', '2021-03-09 15:14:13.000000');