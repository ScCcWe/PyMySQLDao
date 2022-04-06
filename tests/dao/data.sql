create database python_example;

use python_example;

create table class (
   id bigint(20) unsigned primary key auto_increment,
   class_name varchar(50) not null unique,
   is_delete tinyint default 0
)engine=innodb
 auto_increment=1
 default charset=utf8;

insert into class(id, class_name) values(1, "火箭班");
insert into class(class_name) values("骏马班");
insert into class(class_name) values("明日之星");
