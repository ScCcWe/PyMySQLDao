create database python_example;

use python_example;


create table student(
    id bigint(20) unsigned primary key auto_increment,
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
   id bigint(20) unsigned primary key auto_increment,
   class_name varchar(50) not null unique,
   is_delete tinyint default 0
)engine=innodb
 auto_increment=1
 default charset=utf8;

insert into class(id, class_name) values(1, "火箭班");
insert into class(class_name) values("骏马班");
insert into class(class_name) values("明日之星");

INSERT INTO student (student_name, student_age, class_id) VALUES ("张三", "12", 1);
INSERT INTO student (student_name, student_age, class_id) VALUES ("李四", "13", 1);
INSERT INTO student (student_name, student_age, class_id) VALUES ("王五", "11", 2);


create table teacher(
    teacher_id bigint(20) unsigned primary key auto_increment comment '教师表主键',
    teacher_name varchar(32) not null comment '教师姓名',
    teacher_age char(3) not null comment '教师年龄',
    last_month_average decimal(5, 2) not null comment '上个月平局分',
    joined_time datetime not null comment '入职时间',
    create_time datetime not null default current_timestamp comment '信息创建时间',
    update_time datetime not null default current_timestamp on update CURRENT_TIMESTAMP comment '信息更新时间',
    is_delete tinyint(1) default 0 comment '是否删除【1为是，0为否】'
)engine=innodb
auto_increment=1
default charset=utf8;
