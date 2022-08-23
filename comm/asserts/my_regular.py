#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: R.
# email: sy.mailbox@foxmail.com
import re


class TestResult(object):
    @classmethod
    def regular_expression_Assert(cls, regular_group=None):
        """
        正则表达式匹配相等值
        msg使用了json()[]匹配相等
        """
        try:
            result = re.search(r'"msg":"(.+?)"', regular_group.text).group(1)
            assert result == regular_group.json()['msg'] == "操作成功"  # msg使用了json()[]定位匹配
            return True
        except:
            result = re.search(r'"msg":"(.+?)"', regular_group.text).group(1)
            assert result != regular_group.json()['msg'] == "操作成功"
            raise

    @classmethod
    def regular_expression_Assert_int(cls, regular_group=None):  # ret使用了 text定位匹配
        """
        正则表达式匹配相等值
        ret:使用了text[]位置进行匹配相等
        """
        try:
            results = re.search("\\d+", regular_group.text).group(0)  # 项目统一ret返回为1,msg为"操作成功" ,group表示从某个位置开始
            assert results == regular_group.text[7] == "1"  # 匹配相等值, 如果匹配不一致则False, 文本匹配到第7个位置就是ret的value值
            return True
        except:
            results = re.search("\\d+", regular_group.text).group(0)
            assert results != regular_group.text[7] == "1"
            raise
