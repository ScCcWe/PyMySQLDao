import pytest

from tests import none_list, student_obj_list_id_123
from examples.studentDao import StudentDao

studentDao = StudentDao()


def test_select_by_id_list_val_value():
    """
    id_list: type: List<int> / List<str>
    """
    for none_value in none_list:
        pytest.raises(ValueError, studentDao.select_by_id_list, none_value)


def test_select_by_id_list_val_type():
    """
    id_list: type: List<int> / List<str>
    """
    pytest.raises(TypeError, studentDao.select_by_id_list, [None])

    pytest.raises(TypeError, studentDao.select_by_id_list, ["", 1, 2])

    pytest.raises(TypeError, studentDao.select_by_id_list, [1, "", 2])

    pytest.raises(TypeError, studentDao.select_by_id_list, [1, 2, ""])

    pytest.raises(TypeError, studentDao.select_by_id_list, 1)

    pytest.raises(TypeError, studentDao.select_by_id_list, (1, 2))

    pytest.raises(TypeError, studentDao.select_by_id_list, {"key1", "value1"})


def test_select_by_id_list_query():
    assert studentDao.select_by_id_list([1, 2, 3, 5]) is not None

    assert studentDao.select_by_id_list([1, 2, 3]) is not None
    assert studentDao.select_by_id_list([1, 2, 3]) == student_obj_list_id_123
