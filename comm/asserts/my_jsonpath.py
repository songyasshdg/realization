#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: R.
# email: sy.mailbox@foxmail.com
import json
import jsonpath
from realization.log.logger.my_log import logger


class jsonpAtLibrary(object):
    """
    匹配类型断言
    """

    @classmethod
    def json_xpath_chao_structure_as_s(cls, jsonPath=None):
        try:
            response = json.loads(jsonPath.text)  # 把返回的字符串转换为json字典
            su_list = jsonpath.jsonpath(response, '$.*')  # 获取data的所有内容
            assert su_list == [1, '操作成功']  # 判断返回的数据是否一致
            logger.info(f"断言成功 -> 响应结果包含:{su_list}", stack_info=False)
        except:
            logger.error("---断言失败 -> 请求检查!!", exc_info=True)  # 当exc_info为true时, 会将异常信息日志打印到日志中,反之false则不会打印
            raise

    @classmethod
    def json_xpath_sheng_structure_as(cls, jsonPath=None):
        try:
            response = json.loads(jsonPath.text)
            su_list = jsonpath.jsonpath(response, '$.*')
            assert su_list == [1, '生成成功']
            logger.info(f"断言成功 -> 响应结果包含:{su_list}", stack_info=False)
        except:
            logger.error("---断言失败 -> 请求检查!!", exc_info=True)
            raise

    @classmethod
    def json_length_xpath_assertion_structure_che(cls, jsonPath=None):
        try:
            response = json.loads(jsonPath.text)
            su_list = jsonpath.jsonpath(response, '$.[ret,msg]')
            assert su_list == [1, '操作成功']
            assert True
            logger.info(f"响应结果包含:{su_list}", stack_info=False)
        except:
            logger.error("---断言失败 -> 请求检查!!", exc_info=True)
            raise

    @classmethod
    def json_length_xpath_assertion_structure_ches(cls, jsonPath=None):
        try:
            response = json.loads(jsonPath.text)
            su_list = jsonpath.jsonpath(response, '$.[ret,msg]')
            assert su_list == [1, '生成成功']
            assert True
            logger.info(f"断言成功 -> 响应结果包含:{su_list}", stack_info=False)
        except:
            logger.error("---断言失败 -> 请求检查!!", exc_info=True)
            raise

    @classmethod
    def json_les_xpath_as_cheng_gong_type(cls, jsonPath=None):
        response = json.loads(jsonPath.text)
        su_list = jsonpath.jsonpath(response, '$.msg')
        assert su_list == ['生成成功']
