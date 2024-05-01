# -*- coding: utf-8 -*-
import pytest


class TestUser:
    @pytest.mark.run(order=3)
    def test_logout(self):
        print("我现在退出登录。。。")
        assert 1 == 1

    @pytest.mark.run(order=2)
    def test_login(self):
        print("我现在登录。。。")
        assert 1 == 1

