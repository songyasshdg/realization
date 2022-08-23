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
from realization.test.url.url_revision import TestRevision
from realization.tool.my_files import Testfile
from realization.log.logger.my_log import logger


@allure.epic("修图分类管理 -> Api已关联")
class TestRevision(TestPublicLibrary, TestRevision, TestAssert, jsonpAtLibrary, TestHamcrest, TestTime, Testfile):
    @classmethod
    def GepDependent_function(cls, rely_on=None):
        ids = str(rely_on.json()['data'][0]['id'])  # 项目响应结果为json,提取id出来关联下一个接口
        cls.Dependent_function['ids'] = ids
        logger.info(f"提取返回的ID,进行下一个Api的关联:{ids}")

    @allure.feature("修图分类管理-增加")
    @allure.title('增加-用例1-正向')
    @pytest.mark.run(order=1)
    def testcase_01(self):
        urls = self.base_urls + self.urls_add_Revision
        r = self.requests(method='post', url=urls, data=self.data_add_Revision, headers=self.fromHeader())
        self.response_text_assertion_succeeded_successful(responses=r, code=200, text_ret=1, text_assertion="操作成功")
        self.json_length_xpath_assertion_structure_che(jsonPath=r)
        self.elapsed_total_response_time(__elapsed__=r)

    @allure.feature("修图分类管理-查询")
    @allure.title('查询状态打开的数据-用例1-正向')
    @pytest.mark.run(order=2)
    def testcase_02(self):
        urls = self.base_urls + self.url_revision_select
        r = self.requests(method='post', url=urls, data=self.data_revision_select, headers=self.fromHeader())
        self.GepDependent_function(rely_on=r)
        self.response_text_assertion_succeeded_successful(responses=r, code=200, text_ret=1, text_assertion="操作成功")
        self.json_length_xpath_assertion_structure_che(jsonPath=r)
        self.elapsed_total_response_time(__elapsed__=r)

    @allure.feature("修图分类管理-修改")
    @allure.title('修改-用例1-正向')
    @pytest.mark.run(order=3)
    def testcase_03(self):
        urls = self.base_urls + self.urls_Revision_update
        r = self.requests(method='post', url=urls, data=self.data_Revision_update, headers=self.fromHeader())
        self.response_text_assertion_succeeded_successful(responses=r, code=200, text_ret=1, text_assertion="操作成功")
        self.json_length_xpath_assertion_structure_che(jsonPath=r)
        self.elapsed_total_response_time(__elapsed__=r)

    @allure.feature("修图分类管理-删除")
    @allure.title('删除-用例1-正向')
    @pytest.mark.run(order=4)
    def testcase_04(self):
        urls = self.base_urls + self.url_revision_delete
        r = self.requests(method='post', url=urls, data=self.data_revision_delete, headers=self.fromHeader())
        self.response_text_assertion_succeeded_successful(responses=r, code=200, text_ret=1, text_assertion="操作成功")
        self.json_length_xpath_assertion_structure_che(jsonPath=r)
        self.elapsed_total_response_time(__elapsed__=r)


if __name__ == '__main__':
    pytest.main(['-vs', 'test_revision.py'])
