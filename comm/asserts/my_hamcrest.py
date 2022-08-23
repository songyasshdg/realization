#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: R.
# email: sy.mailbox@foxmail.com
from realization.log.logger.my_log import logger
from hamcrest import *


class TestHamcrest(object):
    """
    此类型断言不需要进行判断, 会根据响应的结果进行匹配, 如果匹配失败, 会自动抛异常
    """

    @classmethod
    def that_sheng_structure_assertEqual(cls, hamcrest=None):  # 文本断言 包含字符串
        """
        包含字符串,包含在内
        """
        try:
            assert_that(hamcrest.text,
                        contains_string("1") and assert_that(hamcrest.text, contains_string("生成成功")))
            logger.info("断言成功 -> 响应文本包含:[1, '生成成功']")
            assert True
        except:
            logger.error(f"hamcrest断言--此用例响应失败,请检查", exc_info=True)
            raise

    @classmethod
    def that_chao_structure_assertEqual(cls, hamcrest=None):  # 文本断言 包含字符串
        """
        包含字符串,包含在内
        """
        try:
            assert_that(hamcrest.text, contains_string("1") and assert_that(hamcrest.text, contains_string("操作成功")))
            logger.info("断言成功 -> 响应文本包含:[1, '操作成功']")
            assert True
        except:
            logger.error("hamcrest断言--此用例响应失败,请检查", exc_info=True)
            raise

    @classmethod
    def that_chao_zuo_match_se(self, hamcrest=None):
        """
        按顺序包含
        """
        assert_that(hamcrest.text, string_contains_in_order("操作成功"))

    @classmethod
    def that_sheng_cheng_match_se(cls, hamcrest=None):
        """
        按顺序包含
        """
        assert_that(hamcrest.text, string_contains_in_order("生成成功"))
        assert True

    @classmethod
    def that_sheng_cheng_match_se_s(cls, hamcrest=None):
        """
        匹配后缀
        """
        assert_that(hamcrest.text, ends_with("成功"))
        assert True

    @classmethod
    def that_sheng_cheng_match_se_se(cls, hamcrest=None):
        """
        匹配前缀
        """
        assert_that(hamcrest.text, starts_with("生成"))
        assert True
