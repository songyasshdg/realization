#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: R.
# email: sy.mailbox@foxmail.com

import allure
import pytest
from realization.comm.asserts.my_assert import TestAssert
from realization.comm.asserts.my_error import TestError
from realization.comm.asserts.my_jsonpath import jsonpAtLibrary
from realization.comm.asserts.my_time import TestTime
from realization.comm.base.my_base import TestPublicLibrary
from realization.test.url.url_subscribetemp import TestSubsList
from realization.tool.my_files import Testfile


@allure.epic("订阅模板参数配置")
class TestUserTemp(TestPublicLibrary, TestSubsList, TestAssert, jsonpAtLibrary, TestError, TestTime, Testfile):

    @allure.feature("订阅模板参数配置-查询")
    @allure.title('查询-用例1-正向')
    @pytest.mark.flaky(reruns=2, reruns_delay=2.5)
    def testcase_01(self):
        urls = self.base_urls + self.url_SubsList_select
        r = self.requests(method='post', url=urls, data=self.data_SubsList_select, headers=self.fromHeader())
        self.response_text_assertion_succeeded_successful(responses=r, code=200, text_ret=1, text_assertion="操作成功")
        self.json_length_xpath_assertion_structure_che(jsonPath=r)
        self.elapsed_total_response_time(__elapsed__=r)

    @allure.feature("订阅模板参数配置-增加")
    @allure.title('增加-用例1-正向')
    # @pytest.mark.flaky(reruns=2, reruns_delay=2.5)
    def testcase_02(self):
        urls = self.base_urls + self.url_SubsList_add
        r = self.requests(method='post', url=urls, data=self.data_SubsList_add, headers=self.fromHeader())
        self.elapsed_total_response_time(__elapsed__=r)
        self.asserts_fails(TrueError=r)  # 老接口  未适配swagger


if __name__ == '__main__':
    pytest.main(['-vs', 'test_subscribetemp.py'])
