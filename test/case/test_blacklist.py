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
from realization.test.url.url_blacklist import TestLackList
from realization.tool.my_files import Testfile


@allure.epic("黑名单管理")
class TestBlackLisTt(TestPublicLibrary, TestLackList, TestAssert, jsonpAtLibrary, TestHamcrest, TestTime, Testfile):
    @allure.feature("黑名单管理-查询是否被封禁")
    @allure.title('查询是否被封禁-用例1-正向')
    @pytest.mark.flaky(reruns=2, reruns_delay=2.5)
    def testcase_01(self):
        urls = self.base_urls + self.url_blacklist
        r = self.requests(method='post', url=urls, data=self.data_blacklist, headers=self.fromHeader())
        self.response_text_assertion_succeeded_successful(responses=r, code=200, text_ret=1, text_assertion="操作成功")
        self.json_length_xpath_assertion_structure_che(jsonPath=r)
        self.elapsed_total_response_time(__elapsed__=r)


if __name__ == '__main__':
    pytest.main(['-vs', 'test_blacklist.py'])
