#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: R.
# email: sy.mailbox@foxmail.com

"""
系统名称:产品运营系统
界面名称:黑名单管理
菜单位置:产品运营系统>用户管理>用户运营>黑名单管理
"""


class TestLackList(object):
    @classmethod
    def setup(cls):
        cls.Dependent_function = globals()

    @property  # 查询是否被封禁
    def url_blacklist(self):
        url_blacklist = "/test/forbidden/get"
        return url_blacklist

    @property  # 查询是否被封禁
    def data_blacklist(self):
        data_blacklist = {"appid": "11265",  # 应用id	(必填)
                          "timestamp": 21,  # 客户端13位时间戳	(必填)
                          "userid": 2222,  # 用户id(必填)
                          "aid": None,  # androidid安卓设备标识
                          "idfa": None,  # idfa苹果设备标识
                          "lsn": None,  # 动能设备id
                          "pid": None  # 项目id
                          }
        return data_blacklist
