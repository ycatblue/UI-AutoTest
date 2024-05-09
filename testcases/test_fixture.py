# -*- coding: utf-8 -*-
import pytest


@pytest.fixture(scope="function" )
def fixture():
    print("我是前置步骤")
    return 4


def test_fixture1(fixture):
    assert fixture == 1


def test_fixture2():
    assert 1 == 1


if __name__ == '__main__':
    pytest.main()