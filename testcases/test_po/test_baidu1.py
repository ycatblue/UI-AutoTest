# -*- coding: utf-8 -*-
from asyncio import sleep

import pytest

from page.page_baidu import PageBaidu
from utils.read_yaml import read_yaml


class TestBaidu:

    @pytest.mark.parametrize("data", read_yaml()["skill"])
    def test_baidu(self, driver, data):
        page = PageBaidu(driver)
        page.search_keyword(data)
        sleep(5)
