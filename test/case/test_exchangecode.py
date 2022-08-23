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
from realization.test.url.url_exchangecode import TestExchange
from realization.tool.my_files import Testfile
from realization.comm.asserts.my_error import TestError


@allure.epic("单机兑换码V1")
class TestExcHnGecode(TestPublicLibrary, TestExchange, TestAssert, jsonpAtLibrary, TestHamcrest, TestTime, Testfile,
                      TestError):
    @allure.feature("单机兑换码V1-生成单个")
    @allure.title('生成单个-用例1-正向')
    @pytest.mark.flaky(reruns=2, reruns_delay=2.5)
    def testcase_01(self):
        urls = self.base_urls + self.url_exchange_code_add
        r = self.requests(method='post', url=urls, data=self.data_exchange_code_add, headers=self.fromHeader())
        self.response_text_assertion_succeeded_successful(responses=r, code=200, text_ret=1, text_assertion="生成成功")
        self.json_length_xpath_assertion_structure_ches(jsonPath=r)
        self.elapsed_total_response_time(__elapsed__=r)

    @allure.feature("单机兑换码V1-批量生成")
    @allure.title('批量生成-用例1-正向')
    @pytest.mark.flaky(reruns=2, reruns_delay=2.5)
    def testcase_02(self):
        urls = self.base_urls + self.url_code_adds
        r = self.requests(method='post', url=urls, data=self.data_exchange_code_adds, headers=self.headers())
        self.with_open(filename=r.content, filepath="单机兑换码V1.xlsx")
        self.elapsed_total_response_time(__elapsed__=r)
        self.asserts_fails(TrueError=r)

    @allure.feature("单机兑换码V1-查询")
    @allure.title('查询-用例1-正向')
    @pytest.mark.flaky(reruns=2, reruns_delay=2.5)
    def testcase_03(self):
        urls = self.base_urls + self.url_exchange_code_select
        r = self.requests(method='post', url=urls, data=self.data_exchange_code_select, headers=self.fromHeader())
        self.response_text_assertion_succeeded_successful(responses=r, code=200, text_ret=1, text_assertion="操作成功")
        self.json_length_xpath_assertion_structure_che(jsonPath=r)
        self.elapsed_total_response_time(__elapsed__=r)

    @allure.feature("单机兑换码V1-使用测试")
    @allure.title('使用测试-用例1-正向')
    # @pytest.mark.flaky(reruns=2, reruns_delay=2.5)
    # @pytest.mark.xfail(reason='此接口需要刷新缓存功能才能结合测,未配置断言')
    def testcase_04(self):
        urls = self.base_urls + self.url_code_debuGapi
        r = self.requests(method='post', url=urls, data=self.data_code_debuGapi, headers=self.jsonHeaders())
        assert False


if __name__ == '__main__':
    pytest.main(['-vs', 'test_exchangecode.py'])
