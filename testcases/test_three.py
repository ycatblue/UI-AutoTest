# -*- coding: utf-8 -*-
import pytest
from pytest_assume.plugin import assume


@pytest.mark.p1
def test_three():
    assert 1 == 1
    assert 1 != 2
    assert 3 > 1
    assert 1 < 3
    assert 3 >= 3
    assert 'a' in 'abc'
    assert 'r' not in 'abc'  # 使用assume, 断言失败也会继续往下判断
    assert True is True
    assert False is not True


@pytest.mark.test
def test_assume():
    with assume:
        assert 1 == 1
        assert 1 != 2
        assert 3 > 1
        assert 1 < 3
        assert 3 >= 3
        assert 'a' in 'abc'
        # assert 'a' not in 'abc'  # 使用assume, 断言失败也会继续往下判断
        assert True is True
        assert False is not True