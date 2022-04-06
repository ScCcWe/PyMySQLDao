import pytest

from tests.curd import base
from tests import none_list, student_list_123


class TestSelectByIdList(base.PyMySQLDaoTestCase):
    def setUp(self) -> None:
        super(TestSelectByIdList, self).setUp()

    def test_param_validation(self):
        for none_value in none_list:
            pytest.raises(ValueError, self.studentDao.select_by_id_list, none_value)

    def test_query(self):
        assert self.studentDao.select_by_id_list([1, 2, 3]) is not None
        assert self.studentDao.select_by_id_list([1, 2, 3]) == student_list_123

        assert self.studentDao.select_by_id_list([1, "2", 3]) is not None
        assert self.studentDao.select_by_id_list([1, "2", 3]) == student_list_123

    def tearDown(self) -> None:
        self.studentDao.execute_sql("use test1")
        self.studentDao.execute_sql("drop table student")
