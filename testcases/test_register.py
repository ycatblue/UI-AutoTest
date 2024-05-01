# -*- coding: utf-8 -*-
import pytest


@pytest.mark.run(order=1)
class TestUser:
    def test_register(self):
        print("我现在注册。。。")
        assert 2 == 2
