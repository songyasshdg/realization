#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: R.
# email: sy.mailbox@foxmail.com
import allure
import pytest
from realization.comm.asserts.my_assert import TestAssert
from realization.comm.asserts.my_error import TestError
from realization.comm.asserts.my_hamcrest import TestHamcrest
from realization.comm.asserts.my_jsonpath import jsonpAtLibrary
from realization.comm.asserts.my_time import TestTime
from realization.comm.base.my_base import TestPublicLibrary
from realization.test.url.url_retention import TestRetention
from realization.tool.my_files import Testfile


@allure.epic("应用内真实留存")
class TestRetention(TestPublicLibrary, TestRetention, TestAssert, jsonpAtLibrary, TestHamcrest, TestTime, Testfile, TestError):
    @allure.feature("应用内真实留存-查询")
    @allure.title('查询-用例1-正向')
    @pytest.mark.flaky(reruns=2, reruns_delay=2.5)
    def testcase_01(self):
        urls = self.base_urls + self.url_retention_select
        r = self.requests(method='post', url=urls, data=self.data_retention_select, headers=self.fromHeader())
        self.response_text_assertion_succeeded_successful(responses=r, code=200, text_ret=1, text_assertion="操作成功")
        self.json_length_xpath_assertion_structure_che(jsonPath=r)
        self.elapsed_total_response_time(__elapsed__=r)

    @allure.feature("应用内真实留存-导出")
    @allure.title('导出-用例1-正向')
    @pytest.mark.flaky(reruns=2, reruns_delay=2.5)
    def testcase_02(self):
        urls = self.base_urls + self.url_retention_export
        r = self.requests(method='post', url=urls, data=self.data_retention_export, headers=self.fromHeader())
        self.with_open(filename=r.content, filepath="应用内真实留存.xlsx")
        self.elapsed_total_response_time(__elapsed__=r)
        self.asserts_fails(TrueError=r)


if __name__ == '__main__':
    pytest.main(['-vs', 'test_retention.py'])
