#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: R.
# email: sy.mailbox@foxmail.com
"""
系统名称:产品运营系统
界面名称:订阅模板参数配置
菜单位置:产品运营系统>产品管理>小游戏配置>订阅模板参数配置
"""


class TestSubsList(object):
    @classmethod
    def setup(cls):
        cls.Dependent_function = globals()

    @property  # 查询
    def url_SubsList_select(self):
        url_SubsLists = "/operate/subscriptionTemplateConfig/list"
        return url_SubsLists

    @property  # 查询
    def data_SubsList_select(self):
        data_SubsLists = {"appid": "",
                          "create_owner": "",
                          "create_time": "",
                          "handle": "",
                          "json": "",
                          "limit": "100",
                          "order": "",
                          "page": "",
                          "start": "0",
                          "template_id": "",
                          "update_owner": "",
                          "update_time": "",
                          }
        return data_SubsLists

    @property  # 增加
    def url_SubsList_add(self):
        url_SubsLists = "/operate/subscriptionTemplateConfig/handle"
        return url_SubsLists

    @property  # 增加
    def data_SubsList_add(self):
        data_SubsLists = {"appid": "10001",
                          "create_owner": "songya",
                          "create_time": "",
                          "handle": "add",
                          "json": "{}",
                          "limit": "100",
                          "order": "",
                          "page": "6",
                          "start": "0",
                          "template_id": "23",
                          "update_owner": "",
                          "update_time": "",
                          }
        return data_SubsLists

    @property  # 修改
    def url_SubsList_update(self):
        url_SubsLists = "/operate/subscriptionTemplateConfig/handle"
        return url_SubsLists

    @property  # 修改
    def data_SubsList_update(self):
        data_SubsLists = {"appid": "",
                          "create_owner": "",
                          "create_time": "",
                          "handle": "",
                          "json": "",
                          "limit": "100",
                          "order": "",
                          "page": "",
                          "start": "0",
                          "template_id": "",
                          "update_owner": "",
                          "update_time": "",
                          }
        return data_SubsLists

    @property  # 删除
    def url_SubsList_delete(self):
        url_SubsLists = "/operate/subscriptionTemplateConfig/handle"
        return url_SubsLists

    @property  # 删除
    def data_SubsList_delete(self):
        data_SubsLists = {"appid": "",
                          "create_owner": "",
                          "create_time": "",
                          "handle": "",
                          "json": "",
                          "limit": "100",
                          "order": "",
                          "page": "",
                          "start": "0",
                          "template_id": "",
                          "update_owner": "",
                          "update_time": "",
                          }
        return data_SubsLists
