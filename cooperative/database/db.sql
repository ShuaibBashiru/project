CREATE TABLE user_record(
id int not null AUTO_INCREMENT,
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
    status_id INT NOT NULL DEFAULT 0,
    record_status INT NOT NULL DEFAULT 0,
    created_by int not null,
    modified_by int not null,
    date_created date not null,
    time_created time not null,
    date_modified date not null,
    time_modified time not null,
    PRIMARY KEY(id),
    unique(email_one, email_two, phone_one, phone_two)
);

CREATE TABLE admin_record(
id int not null AUTO_INCREMENT,
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
    status_id INT NOT NULL DEFAULT 0,
    record_status INT NOT NULL DEFAULT 0,
    created_by int not null,
    modified_by int not null,
    date_created date not null,
    time_created time not null,
    date_modified date not null,
    time_modified time not null,
    PRIMARY KEY(id),
    unique(email_one, email_two, phone_one, phone_two)
);

CREATE TABLE reset_password(
id int not null AUTO_INCREMENT,
    email_one varchar(50) not null,
    resetCode varchar(50) not null,
    expire_date datetime(6) not null,
    status_id INT NOT NULL DEFAULT 0,
    date_created date not null,
    time_created time not null,
    date_modified date not null,
    time_modified time not null,
    PRIMARY KEY(id),
    unique(resetCode)
);


CREATE TABLE user_widgets(
id int not null AUTO_INCREMENT,
    widgetName varchar(50) not null,
    widgetTitle varchar(100) null DEFAULT '',
    uniqueCode varchar(50) not null,
    status_id INT NOT NULL DEFAULT 0,
    record_status INT NOT NULL DEFAULT 0,
    created_by int not null,
    modified_by int not null,
    date_created date not null,
    time_created time not null,
    date_modified date not null,
    time_modified time not null,
    PRIMARY KEY(id),
    unique(uniqueCode)
);



CREATE TABLE site_menus(
id int not null AUTO_INCREMENT,
    menuName varchar(50) not null,
    category varchar(50) not null,
    menuTitle varchar(100) null DEFAULT '',
    menu_description text null,
    uniqueCode varchar(50) not null,
    status_id INT NOT NULL DEFAULT 0,
    record_status INT NOT NULL DEFAULT 0,
    created_by int not null,
    modified_by int not null,
    date_created date not null,
    time_created time not null,
    date_modified date not null,
    time_modified time not null,
    PRIMARY KEY(id),
    unique(menuName, uniqueCode)
);

CREATE TABLE user_menus(
id int not null AUTO_INCREMENT,
    menuName varchar(50) not null,
    category varchar(50) not null,
    menu_icon varchar(50) not null,
    menu_description text null,
    uniqueCode varchar(50) not null,
    status_id INT NOT NULL DEFAULT 0,
    record_status INT NOT NULL DEFAULT 0,
    created_by int not null,
    modified_by int not null,
    date_created date not null,
    time_created time not null,
    date_modified date not null,
    time_modified time not null,
    PRIMARY KEY(id),
    unique(menuName, uniqueCode)
);


CREATE TABLE user_priviledges(
id int not null AUTO_INCREMENT,
    menu_id INT not null,
    user_id INT not null,
    menu_description text null,
    uniqueCode varchar(50) not null,
    status_id INT NOT NULL DEFAULT 0,
    record_status INT NOT NULL DEFAULT 0,
    created_by int not null,
    modified_by int not null,
    date_created date not null,
    time_created time not null,
    date_modified date not null,
    time_modified time not null,
    PRIMARY KEY(id),
    unique(uniqueCode)
);


INSERT INTO `admin_record` (`id`, `surname`, `firstname`, `othername`, `email_one`,
`email_two`, `phone_one`, `phone_two`, `countryCode`, `persional_id`, `account_type`,
`user_role`, `pwd_auth_hash`, `pwd_auth`, `status_id`, `created_by`, `modified_by`, `date_created`,
`time_created`, `date_modified`, `time_modified`, `record_status`) VALUES (NULL, 'BASHIRU', 'SHUAIB',
'', 'INSTRUCTSME@GMAIL2.COM', '', '08172790182', '',
'+234', '', '1', '', '', 'Ayodele1', '0', '1', '1', '2021-04-15', '17:53:56', '2021-04-15', '17:53:56', 1);

ALTER TABLE `admin_record` ADD `record_status` INT NOT NULL AFTER `status_id`;
ALTER TABLE `user_record` ADD `record_status` INT NOT NULL AFTER `status_id`;
ALTER TABLE `user_widgets` ADD `record_status` INT NOT NULL AFTER `status_id`;
ALTER TABLE `site_menus` ADD `record_status` INT NOT NULL AFTER `status_id`_by`
--

INSERT INTO `user_menus` (`id`, `menuName`, `category`, `menu_icon`,
`menu_description`, `uniqueCode`, `status_id`, `record_status`, `created_by`,
`modified_by`, `date_created`, `time_created`, `date_modified`, `time_modified`)
VALUES (NULL, 'updatewidget', 'updatewidget', 'bi-bricks', 'Home', '44324215354124', '1',
'1', '1', '1', '2021-04-13', '10:56:05', '2021-04-13', '10:56:05');

INSERT INTO `user_priviledges` (`id`, `menu_id`, `user_id`,
 `menu_description`, `uniqueCode`, `status_id`,
`record_status`, `created_by`, `modified_by`, `date_created`,
  `time_created`, `date_modified`, `time_modified`)
  VALUES (NULL, '5', '1', NULL, '4432421341115', '1', '1', '1', '1', '2021-04-07',
  '11:34:10', '2021-04-07', '11:34:10');


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

