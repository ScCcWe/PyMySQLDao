create database python_example;

use python_example;


create table student(
    id bigint(20) primary key auto_increment,
    student_name varchar(10) not null,
    student_age varchar (5) not null,
    class_id bigint(20) not null ,
    is_delete tinyint default 0,
    index idx_clsid (class_id),
    index idx_name (student_name),
    index idx_age (student_age)
)engine=innodb
 auto_increment=1
 default charset=utf8;


create table class (
   id bigint(20) primary key auto_increment,
   class_name varchar(50) not null unique,
   is_delete tinyint default 0,
   index idx_clsname(class_name)
)engine=innodb
 auto_increment=1
 default charset=utf8;

insert into class(id, class_name) values(1, "火箭班");
insert into class(class_name) values("骏马班");

INSERT INTO student (student_name, student_age, class_id) VALUES ("张三", "12", 1);
INSERT INTO student (student_name, student_age, class_id) VALUES ("李四", "13", 1);
INSERT INTO student (student_name, student_age, class_id) VALUES ("王五", "11", 2);


create table teacher(
    teacher_id bigint(20) primary key auto_increment,
    teacher_name varchar(255) not null,
    join_time DATE,
    create_time Date,
    update_time Date,
)engine=innodb
auto_increment=1
default charset=utf8;
