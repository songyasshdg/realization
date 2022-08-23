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
from realization.test.url.url_mailsending import TestMailsend
from realization.tool.my_files import Testfile


@allure.epic("礼包补发")
class TestMaisEnDing(TestPublicLibrary, TestMailsend, TestAssert, jsonpAtLibrary, TestHamcrest, TestTime, Testfile):
    @allure.feature("礼包补发-获取邮件接口")
    @allure.title('获取邮件接口-用例1-正向')
    @pytest.mark.flaky(reruns=2, reruns_delay=2.5)
    def testcase_01(self):
        urls = self.base_urls + self.url_MaiLsEnDing
        r = self.requests(method='post', url=urls, data=self.data_POST_Mail, headers=self.fromHeader())
        self.response_text_assertion_succeeded_successful(responses=r, code=200, text_ret=1, text_assertion="操作成功")
        self.json_length_xpath_assertion_structure_che(jsonPath=r)
        self.elapsed_total_response_time(__elapsed__=r)


if __name__ == '__main__':
    pytest.main(['-vs', 'test_mailsending.py'])
