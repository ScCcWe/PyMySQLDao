# PyMySQLDao

## Introduce

PyMySQLDao是建立在PyMySQL上的功能增强库，方便用户进行CRUD；

在不影响任何代码的情况下，只需要简单几行代码，便可获得单表的CRUD功能！

欢迎提出修改意见！🥳🥳🥳

## Requirements

[PyMySQL](https://github.com/PyMySQL/PyMySQL)

termcolor

colorama（only in windows）

## Install

```bash
(venv)$ pip install pymysql-dao
```

> 说明：如果上述的命令无法下载，请考虑使用下列命令：
>
> - pypi官方
>
>     `$ pip install pymysql-dao --index-url https://pypi.org/simple/`
>
> - 清华源
>
>     `$ pip install pymysql-dao --index-url https://pypi.tuna.tsinghua.edu.cn/simple/`

## Example

假设使用下列SQL语句：

```sql
create database python_example;

use python_example;

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
```

使用pymysqldao轻松的进行CRUD

```python
import pymysql
from pymysqldao import BaseDao

db_example_conn = pymysql.connect(
    host='localhost',
    user='root',
    password='root',
    database='python_example',
    cursorclass=pymysql.cursors.DictCursor
)


class ClassDao(BaseDao):
    def __init__(self):
        super(ClassDao, self).__init__(db_example_conn, "class")


if __name__ == '__main__':
    class_dao = ClassDao()

    # select by id
    class_dao.select_by_id(1)
    class_dao.select_by_id("1")
    class_dao.select_by_id(1, primary_key="id")

    # select by field
    class_dao.select_by_field("xxx", field_key="class_name")
    class_dao.select_by_field("xxx", field_key="class_name", limit_size=10)

    # select list
    class_dao.select_list()
    class_dao.select_list(limit_size=500)

    # select by id_list
    class_dao.select_by_id_list([1, 2, 3])  # default primary_key is "id"
    class_dao.select_by_id_list([1, 2, 3], primary_key="class_id")
    
    # insert
    obj_dict = {"class_name": "少年班"}
    class_dao.insert_one(obj_dict)
    
    # update
    new_obj_id_1 = {'id': 1, 'class_name': '火箭班修改', 'is_delete': 0}
    class_dao.update_by_id(new_obj_id_1)
    
    # delete
    class_dao.delete_by_id(1)
    class_dao.delete_by_id(1, primary_key="class_id")
```
