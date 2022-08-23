#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: R.
# email: sy.mailbox@foxmail.com
import pytest

from realization.log.logger.my_log import logger


class TestError(object):
    """
    异常断言类
    """

    @classmethod  # 针对导出异常断言
    def asserts_fails(cls, TrueError):
        if "token is error!" in TrueError.text:
            logger.error(f"导出数据失败,请检查!!:{TrueError.text}", exc_info=True)
            assert False
        elif "操作失败" in TrueError.text:
            logger.error(f"导出数据失败,请检查!!:{TrueError.text}", exc_info=True)
            assert False
        elif TrueError.text is None:
            logger.error(f"导出结果为空,请检查!!:{TrueError.text}", exc_info=True)
            assert False
        else:
            assert True
