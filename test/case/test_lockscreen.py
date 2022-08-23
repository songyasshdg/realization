#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: R.
# email: sy.mailbox@foxmail.com

import allure
import pytest
from realization.comm.asserts.my_assert import TestAssert
from realization.comm.asserts.my_hamcrest import TestHamcrest
from realization.comm.asserts.my_jsonpath import jsonpAtLibrary
from realization.comm.asserts.my_time import TestTime
from realization.comm.base.my_base import TestPublicLibrary
from realization.test.url.url_lockscreen import TestLockscreen
from realization.tool.my_files import Testfile


@allure.epic("新-V2锁屏配置")
class TestLockscreen(TestPublicLibrary, TestLockscreen, TestAssert, jsonpAtLibrary, TestHamcrest, TestTime, Testfile):
    @allure.feature("新-V2锁屏配置-增加")
    @allure.title('增加-用例1-正向')
    # @pytest.mark.xfail(reason='此界面的接口结合界面测试, 因为参数太多了')
    def testcase_01(self):
        urls = self.base_urls + self.url_Lockscreen_Add
        r = self.requests(method='post', url=urls, data=self.data_Lockscreen_Add, headers=self.fromHeader())
        assert False


if __name__ == '__main__':
    pytest.main(['-vs', 'test_lockscreen.py'])
