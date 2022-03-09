# PyMySQLDao

## Introduce

PyMySQLDao是建立在PyMySQL上的功能增强库，方便用户进行CRUD；

在不影响任何代码的情况下，只需要简单几行代码，便可获得表的CRUD功能！

欢迎提出修改意见！🥳🥳🥳

## Requirements

[PyMySQL](https://github.com/PyMySQL/PyMySQL)

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

假设使用此[SQL文件](https://github.com/ScCcWe/PyMySQLDao/blob/master/tests/dao/data.sql)

使用pymysqldao进行CRUD

```python
import sys
import logging

import pymysql
from pymysqldao import BaseDao, LOGGER

# 设置日志等级为DEBUG，并可以打印出来
# 只需要在顶层设置一次即可，重复设置会重复打印
# （如果不需要日志，不设置即可；默认即为不设置
LOGGER.setLevel(logging.DEBUG)
LOGGER.addHandler(logging.StreamHandler(sys.stderr))

conn = pymysql.connect(
    host='localhost',
    user='root',
    password='root',
    database='python_example',
    cursorclass=pymysql.cursors.DictCursor
)


class ClassDao(BaseDao):
    def __init__(self):
        super(ClassDao, self).__init__(conn, "class")


if __name__ == '__main__':
    dao = ClassDao()

    # select list
    dao.select_list()
    dao.select_list(limit_size=500)
    dao.execute_sql("select * from class limit 500")

    # select by field
    dao.select_by_field("火箭班", field_key="class_name")
    dao.select_by_field("骏马班", field_key="class_name", limit_size=10)
    dao.execute_sql("select * from class where class_name='骏马班' limit 10")

    # select by id
    dao.select_by_id(1)
    dao.select_by_id("1")
    dao.select_by_id(1, primary_key="id")
    dao.execute_sql("select * from class where id=1")

    # select by id_list
    dao.select_by_id_list([1, 2, 3])  # default primary_key is "id"
    dao.select_by_id_list([1, 2, 3], primary_key="id")
    dao.execute_sql("select * from class where id in (1, 2, 3)")

    # insert
    dao.insert_one({"class_name": "少年班"})

    # update
    result = dao.select_by_field("少年班", field_key="class_name")
    result[0]["class_name"] = "少年班修改"
    dao.update_by_id(result[0])

    # delete
    dao.delete_by_id(result[0]["id"])
```
