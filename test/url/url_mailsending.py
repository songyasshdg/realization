#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: R.
# email: sy.mailbox@foxmail.com
"""
系统名称:产品运营系统
界面名称:礼包补发
菜单位置:产品运营系统>产品管理>产品设置>礼包补发
"""


class TestMailsend(object):
    @classmethod
    def setup(cls):
        cls.Dependent_function = globals()

    @property  # 获取邮件接口
    def url_MaiLsEnDing(self):
        url_MaiLenDing = "/test/mail/get"
        return url_MaiLenDing

    @property  # 邮件单独服务 此接口在发送之后只会下发一次结果, 重复获取返回为data:[]
    def data_POST_Mail(self):
        data_MaiLenDing = {"appid": 11265,  # 应用id	(必填)
                           'timestamp': 24,  # 客户端13位时间戳(必填)
                           "userid": 11111111111,  # 用户id(必填)
                           "aid": None,  # androidid安卓设备标识
                           "idfa": None,  # idfa苹果设备标识
                           "lsn": None,  # 动能设备id
                           "pid": None  # 项目id
                           }
        return data_MaiLenDing
