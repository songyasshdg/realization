#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: R.
# email: sy.mailbox@foxmail.com
from realization.log.logger.my_log import logger
import pytest_check as check


class TestCheck(object):
    @classmethod
    def check_sheng_cheng_inspection(cls, pyst_check_=None):  # 文本断言
        try:
            check.is_in("1" and "生成成功", pyst_check_.text)
            assert True
        except:
            check.is_not_in("1" and "生成成功", pyst_check_.text)
            logger.error(f"chk方式断言失败,请检查!:{pyst_check_.text}", exc_info=True)
            raise

    @classmethod
    def check_chao_zuo_inspection_ass(cls, pyst_check_=None):  # 文本断言
        try:
            check.is_in("1" and "操作成功", pyst_check_.text[0][1])
            assert True
        except:
            check.is_not_in("1" and "操作成功", pyst_check_.text)
            logger.error(f"chk方式断言失败,请检查!:{pyst_check_.text}", exc_info=True)
            raise
