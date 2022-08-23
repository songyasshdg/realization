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
from realization.log.logger.my_log import logger
from realization.test.url.url_businessmodel import TestBusiness
from realization.tool.my_files import Testfile
from realization.comm.asserts.my_regular import TestResult


@allure.epic("业务模式配置 -> Api已关联")
class TestBusInes(TestPublicLibrary, TestBusiness, TestAssert, jsonpAtLibrary, TestError, TestTime, Testfile,
                  TestResult):
    @classmethod
    def GepDependent_function(cls, rely_on=None):
        str_id = str(rely_on.json()['data'])  # 项目响应结果为json,提取id出来关联下一个接口
        cls.Dependent_function['ids'] = str_id
        logger.info(f"提取返回的ID,进行下一个Api的关联:{str_id}")

    @allure.feature("业务模式配置-增加")
    @allure.title('增加-用例1-正向')
    @pytest.mark.run(order=1)
    def testcase_01(self):
        urls = self.base_urls + self.url_Business_model_add
        r = self.requests(method='post', url=urls, data=self.function_data_add, headers=self.fromHeader())
        self.GepDependent_function(rely_on=r)
        self.response_text_assertion_succeeded_successful(responses=r, code=200, text_ret=1, text_assertion="操作成功")
        self.json_length_xpath_assertion_structure_che(jsonPath=r)
        self.regular_expression_Assert(regular_group=r)
        self.elapsed_total_response_time(__elapsed__=r)

    @allure.feature("业务模式配置-修改")
    @allure.title('修改-用例1-正向')
    @pytest.mark.run(order=2)
    def testcase_02(self):
        urls = self.base_urls + self.url_Business_model_update
        r = self.requests(method='post', url=urls, data=self.function_data_update, headers=self.fromHeader())
        self.response_text_assertion_succeeded_successful(responses=r, code=200, text_ret=1, text_assertion="操作成功")
        self.json_length_xpath_assertion_structure_che(jsonPath=r)
        self.elapsed_total_response_time(__elapsed__=r)

    @allure.feature("业务模式配置-删除")
    @allure.title('删除-用例1-正向')
    @pytest.mark.run(order=3)
    def testcase_03(self):
        urls = self.base_urls + self.urls_Business_model_delete
        r = self.requests(method='post', url=urls, data=self.function_data_delete, headers=self.fromHeader())
        self.response_text_assertion_succeeded_successful(responses=r, code=200, text_ret=1, text_assertion="操作成功")
        self.json_length_xpath_assertion_structure_che(jsonPath=r)
        self.elapsed_total_response_time(__elapsed__=r)

    @allure.feature("业务模式配置-查询")
    @allure.title('查询-用例1-正向')
    @pytest.mark.run(order=4)
    def testcase_04(self):
        urls = self.base_urls + self.urls_Business_model_select
        r = self.requests(method='post', url=urls, data=self.function_data_select, headers=self.fromHeader())
        self.response_text_assertion_succeeded_successful(responses=r, code=200, text_ret=1, text_assertion="操作成功")
        self.json_length_xpath_assertion_structure_che(jsonPath=r)
        self.regular_expression_Assert(regular_group=r)
        self.elapsed_total_response_time(__elapsed__=r)

    @allure.feature("业务模式配置-获取业务配置列表-此接口只要状态为打开的数据")
    @allure.title('获取业务配置列表-状态为"打开"的数据-用例1-正向')
    @pytest.mark.flaky(reruns=2, reruns_delay=2.5)
    def testcase_05(self):
        urls = self.base_urls + self.urls_Business_model_selects
        r = self.requests(method='post', url=urls, headers=self.fromHeader())
        self.response_text_assertion_succeeded_successful(responses=r, code=200, text_ret=1, text_assertion="操作成功")
        self.json_length_xpath_assertion_structure_che(jsonPath=r)
        self.elapsed_total_response_time(__elapsed__=r)

    @allure.feature("业务模式配置-导出文件数据")
    @allure.title('导出文件数据-用例1-正向')
    # @pytest.mark.flaky(reruns=2, reruns_delay=2.5)
    def testcase_06(self):
        urls = self.base_urls + self.urls_Business_model_exit
        r = self.requests(method='post', url=urls, data=self.function_data_exit, headers=self.fromHeader())
        self.with_open(filename=r.content, filepath="业务模式配置.xlsx")
        self.elapsed_total_response_time(__elapsed__=r)
        self.asserts_fails(TrueError=r)


if __name__ == '__main__':
    pytest.main(['-vs', 'test_businessmen.py'])
