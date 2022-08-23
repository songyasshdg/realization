#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: R.
# email: sy.mailbox@foxmail.com
from realization.log.logger.my_log import logger


class TestAssert(object):
    """
    原生判断类型断言
    """

    @classmethod
    def assert_False(cls):  # 针对导出文件流
        assert False

    @classmethod
    def assert_True(cls):  # 针对导出文件流
        assert True

    @classmethod
    def response_text_assertion_succeeded_successful(cls, responses=None, code=int, text_ret=int, text_assertion=str):
        """
        code:状态码为int类型
        文本响应:text_ret为int类型
        文本响应:text_assertion为str类型
        """
        try:
            assert responses.json()["ret"] == text_ret and responses.json()[
                "msg"] == text_assertion and responses.status_code == code
            logger.info(f"状态码:{code}, 响应ret:{text_ret}, 响应msg:{text_assertion}", stack_info=False)
            assert True
        except:
            logger.error(f"响应失败 -> 响应状态码:{responses.status_code}, 响应文本:{responses.text}", exc_info=True)
            raise

    @classmethod
    def assert_sheng_cheng_successfully_codea(cls, asserts=None):  # 先判断请求是否成功
        try:
            assert asserts.status_code == int(200) and asserts.json()["msg"] == "生成成功"
            logger.info(f"响应状态码:{asserts.status_code}, 状态描述:{asserts.json()['msg']}", stack_info=False)
            assert True
        except:
            assert asserts.status_code  # exc_info=True——出现异常时记录堆栈调用信息
            logger.error(f"接口响应失败,状态码为:{asserts.status_code}", exc_info=True)
            raise

    @classmethod
    def assert_chao_zuo_successful_code(cls, asserts=None):  # 先判断请求是否成功
        try:
            assert asserts.status_code == int(200) and asserts.json()["msg"] == "操作成功"
            logger.info(f"响应状态码:{asserts.status_code}, 状态描述:{asserts.json()['msg']}", stack_info=False)
            assert True
        except:
            assert asserts.status_code
            logger.error(f"接口响应失败,状态码为:{asserts.status_code}", exc_info=True)
            raise

    @classmethod
    def text_sheng_cheng_Assertion_tex(cls, textAssert=None):  # 请求断言成功后, 进行文本双重断言
        try:
            assert "1" and "生成成功" in textAssert.text
            assert True
        except:
            assert "1" and "生成成功" not in textAssert.text
            logger.error("文本断言失败,请检查!!!", exc_info=True)
            raise

    @classmethod
    def text_chao_zuo_Assertion_tex(cls, textAssert=None):  # 请求断言成功后, 进行文本双重断言
        try:
            assert "1" and "操作成功" in textAssert.text
            assert True
        except:
            assert "1" and "操作成功" not in textAssert.text
            logger.error("文本断言失败,请检查!!!", exc_info=True)
            raise
