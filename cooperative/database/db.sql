CREATE TABLE user_record(
id int not null AUTO_INCREMENT,
    PRIMARY KEY(id),
    surname varchar(50) not null,
    firstname varchar(50) not null,
    othername varchar(50) null DEFAULT '',
    email_one varchar(50) not null,
    email_two varchar(50) null DEFAULT '',
    phone_one varchar(50) not null,
    gender varchar(50) not null,
    age int not null,
    phone_two varchar(50) null DEFAULT '',
    countryCode varchar(50) not null,
    persional_id varchar(50) null DEFAULT '',
    account_type varchar(50) not null,
    user_role varchar(50) null DEFAULT '',
    pwd_auth_hash varchar(60) null DEFAULT '',
    pwd_auth varchar(60) not null,
    created_by int not null,
    date_created datetime(6) not null,
    last_modified datetime(6) not null
);
CREATE TABLE admin_record(
id int not null AUTO_INCREMENT,
    PRIMARY KEY(id),
    surname varchar(50) not null,
    firstname varchar(50) not null,
    othername varchar(50) null DEFAULT '',
    email_one varchar(50) not null,
    email_two varchar(50) null DEFAULT '',
    phone_one varchar(50) not null,
    phone_two varchar(50) null DEFAULT '',
    countryCode varchar(50) not null,
    persional_id varchar(50) null DEFAULT '',
    account_type varchar(50) not null,
    user_role varchar(50) null DEFAULT '',
    pwd_auth_hash varchar(60) null DEFAULT '',
    pwd_auth varchar(60) not null,
    created_by int not null,
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


INSERT INTO `admin_record` (`id`, `lastname`, `firstname`,
`othername`, `email_one`, `email_two`, `phone_one`, `phone_two`,
 `countryCode`, `persional_id`, `account_type`, `pwd_auth_hash`, `pwd_auth`,
  `date_created`, `last_modified`) VALUES
  (NULL, 'BASHIRU', 'SUAIB', 'ABIODUN', 'instructsme@gmail.com', NULL,
  '08172790181', NULL, NULL, NULL, NULL, NULL, 'Ayodele321.',
   '2021-03-26 16:13:19.000000', '2021-03-26 16:13:19.000000')



CREATE TABLE sale_prices(
id int not null AUTO_INCREMENT,
    PRIMARY KEY(id),
    category varchar(100) null,
    category_id int null,
    itemName varchar(50) not null,
    itemDescription varchar(100) null,
    range_one float not null,
    range_two float not null,
    vat float null,
    comments varchar(100) null,
    user_id int null,
    user_email varchar(60) null,
    created_by int null,
    date_created datetime(6) not null,
    last_modified datetime(6) not null
);


CREATE TABLE invoices(
id int not null AUTO_INCREMENT,
    PRIMARY KEY(id),
    service_id varchar(50) not null,
    list_id int not null,
    price float not null,
    qty int not null,
    vat float null DEFAULT 0,
    amount float not null,
    user_id int not null,
    user_email varchar(60) not null,
    created_by int not null,
    comments varchar(100) null,
    date_created datetime(6) not null,
    last_modified datetime(6) not null
);

