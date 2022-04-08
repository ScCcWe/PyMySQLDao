# PyMySQLDao

## Introduce

PyMySQLDao是建立在PyMySQL上的功能增强库，方便用户进行CRUD；

在不影响任何代码的情况下，只需要简单几行代码，便可获得表的CRUD功能！

欢迎提出修改意见！🥳🥳🥳

## Requirements

[PyMySQL](https://github.com/PyMySQL/PyMySQL)

[pydantic](https://github.com/samuelcolvin/pydantic/)

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

## Examples

### 1)使用pymysqldao进行CRUD

假设使用此[SQL文件](https://github.com/ScCcWe/PyMySQLDao/blob/master/tests/dao/data.sql)

```python
# !/usr/bin/env python 
# -*- coding: utf-8 -*-
import pymysql
from pymysqldao import CRUDHelper

conn = pymysql.connect(
    host='localhost',
    user='root',
    password='',
    database='python_example',
    cursorclass=pymysql.cursors.DictCursor
)


class ClassDao(CRUDHelper):
    def __init__(self):
        super().__init__(connection=conn, table_name="class", size=500)


if __name__ == '__main__':
    # print(ClassDao.__mro__)
    dao = ClassDao()

    # select * from class limit 20
    dao.select_list()

    # select * from class limit 2
    dao.select_list(2)

    # select * from class where class_name='火箭班' limit 20
    dao.select_by_field("class_name", "火箭班")

    # select * from class where class_name='骏马班' limit 10
    dao.select_by_field("class_name", "骏马班", size=10)

    # select * from class where id=1
    dao.select_by_id(1)

    # select * from class where id in (1, 2, 3)
    dao.select_by_id_list([1, 2, 3])

    # insert into class("class_name") values("少年班")
    dao.insert_one({"class_name": "少年班"})

    # update by id
    result = dao.select_by_field("class_name", "少年班")
    result[0]["class_name"] = "少年班修改"
    dao.update_by_id(result[0])

    # delete by id
    dao.delete_by_id(result[0]["id"])
```

### 2)使用自己定义的log格式

```python
import sys
import logging

import pymysql
from pymysqldao import CRUDHelper, LOGGER

LOGGER.setLevel(logging.DEBUG)
LOGGER.addHandler(logging.StreamHandler(sys.stderr))

conn = pymysql.connect(
    host='localhost',
    user='root',
    password='',
    database='python_example',
    cursorclass=pymysql.cursors.DictCursor
)


class ClassDao(CRUDHelper):
    def __init__(self):
        super().__init__(connection=conn, table_name="class", size=500, use_own_log_config=True)


if __name__ == '__main__':
    # print(ClassDao.__mro__)
    dao = ClassDao()

    # select * from class limit 20
    dao.select_list()

    # select * from class limit 2
    dao.select_list(2)
```

