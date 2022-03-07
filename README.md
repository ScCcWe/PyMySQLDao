# PyMySQLPlus

不想使用繁琐的ORM框架？又想具备一定的ORM功能？来使用PyMySQLPlus吧！

PyMySQLPlus是建立在PyMySQL上的功能增强库，方便用户进行简单的进行CRUD；

你只需要简单两步，就可以获得基本的CRUD功能！无需在去使用繁琐的ORM框架！

## Requirements

[PyMySQL](https://github.com/PyMySQL/PyMySQL)

termcolor

## Install

```bash
$ pip install pymysql-dao
```

## Example

假设有下面一个`class`表

```sql
create table class (
   id bigint(20) primary key auto_increment,
   class_name varchar(50) not null unique,
   is_delete tinyint default 0,
   index idx_clsname(class_name)
)engine=innodb
 auto_increment=1
 default charset=utf8;
```

使用pymysqlplus轻松的进行CRUD

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
        super(ClassDao, self).__init__()
        self.connection = db_example_conn
        self.table_name = "class"


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
```

