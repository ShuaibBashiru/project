CREATE TABLE result_tbl(
id int not null AUTO_INCREMENT,
    PRIMARY KEY(id),
    surname varchar(50) not null,
    firstname varchar(50) not null,
    othername varchar(50) not null,
    matric varchar(50) not null,
    levelName varchar(50) not null,
    semester varchar(50) not null,
    phone varchar(50) not null,
    courses text not null,
    gpa varchar(50) not null,
    cgpa varchar(50) not null,
    program_type varchar(50) not null,
    others text null,
    date_created datetime(6) not null,
    last_modified datetime(6) not null
);
CREATE TABLE file_uploaded(
id int not null AUTO_INCREMENT,
    PRIMARY KEY(id),
    filename varchar(50) not null,
    titlename varchar(50) not null,
    date_created datetime(6) not null,
    last_modified datetime(6) not null
);
