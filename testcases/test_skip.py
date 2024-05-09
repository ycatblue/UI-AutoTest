# -*- coding: utf-8 -*-
import pytest

a = 1


@pytest.mark.skip(reason="skip")
def test_skip1():
    assert 1 == 1


@pytest.mark.skipif(a >= 1, reason="判断 1 == 1")
def test_skip2():
    assert 1 == 1


def test_skip3():
    mobile = '1300000000'
    if len(mobile) != 11:
        pytest.skip("skip")
    assert len(mobile) == 11
