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
from realization.test.url.url_wechatsharing import TestWecTshRing
from realization.tool.my_files import Testfile


@allure.epic("微信分享内容配置 -> Api已关联")
class TestWecTest(TestPublicLibrary, TestWecTshRing, TestAssert, jsonpAtLibrary, TestHamcrest, TestTime, Testfile,
                  TestError):
    @classmethod
    def GepDependent_function(cls, rely_on=None):
        st_ids = str(rely_on.json()['data']['list'][0]['id'])  # 项目响应结果为json,提取id出来关联下一个接口
        cls.Dependent_function['ids'] = st_ids

    @allure.feature("微信分享内容配置-增加")
    @allure.title('增加-用例1-正向')
    @pytest.mark.run(order=1)  # 执行顺序控制
    def testcase_01(self):
        urls = self.base_urls + self.url_wecTshRing_add
        r = self.requests(method='post', url=urls, data=self.data_wecTshRing_add, headers=self.fromHeader())
        self.response_text_assertion_succeeded_successful(responses=r, code=200, text_ret=1, text_assertion="操作成功")
        self.json_length_xpath_assertion_structure_che(jsonPath=r)
        self.elapsed_total_response_time(__elapsed__=r)

    @allure.feature("微信分享内容配置-查询")
    @allure.title('查询-用例1-正向')
    @pytest.mark.run(order=2)
    def testcase_02(self):
        urls = self.base_urls + self.url_wecTshRing_select
        r = self.requests(method='post', url=urls, data=self.data_wecTshRing_select, headers=self.fromHeader())
        self.GepDependent_function(rely_on=r)  # 由于关联接口返回的id没有在data里面返回, 所以使用先查询提取出来,然后再关联
        self.response_text_assertion_succeeded_successful(responses=r, code=200, text_ret=1, text_assertion="操作成功")
        self.json_length_xpath_assertion_structure_che(jsonPath=r)
        self.elapsed_total_response_time(__elapsed__=r)

    @allure.feature("微信分享内容配置-修改")
    @allure.title('修改-用例1-正向')
    @pytest.mark.run(order=3)
    def testcase_03(self):
        urls = self.base_urls + self.url_wecTshRing_update
        r = self.requests(method='post', url=urls, data=self.data_wecTshRing_update, headers=self.fromHeader())
        self.response_text_assertion_succeeded_successful(responses=r, code=200, text_ret=1, text_assertion="操作成功")
        self.json_length_xpath_assertion_structure_che(jsonPath=r)
        self.elapsed_total_response_time(__elapsed__=r)

    @allure.feature("微信分享内容配置-删除")
    @allure.title('删除-用例1-正向')
    @pytest.mark.run(order=4)
    def testcase_04(self):
        urls = self.base_urls + self.url_wecTshRing_delete
        r = self.requests(method='post', url=urls, data=self.data_wecTshRing_delete, headers=self.fromHeader())
        self.response_text_assertion_succeeded_successful(responses=r, code=200, text_ret=1, text_assertion="操作成功")
        self.json_length_xpath_assertion_structure_che(jsonPath=r)
        self.elapsed_total_response_time(__elapsed__=r)

    @allure.feature("微信分享内容配置-导出")
    @allure.title('导出-用例1-正向')
    @pytest.mark.flaky(reruns=2, reruns_delay=5)
    def testcase_05(self):
        urls = self.base_urls + self.url_wecTshRing_export
        r = self.requests(method='post', url=urls, data=self.data_wecTshRing_export, headers=self.fromHeader())
        self.with_open(filename=r.content, filepath="微信分享内容配置.xlsx")
        self.elapsed_total_response_time(__elapsed__=r)
        self.asserts_fails(TrueError=r)


if __name__ == '__main__':
    pytest.main(['-vs', 'test_wechatsharing.py'])
