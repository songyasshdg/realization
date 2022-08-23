#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: R.
# email: sy.mailbox@foxmail.com
"""
系统名称:产品运营系统
界面名称:新手引导-大数据
菜单位置:产品运营系统>运营数据>新手>新手引导-大数据
"""


class TestNoviceG(object):
    @classmethod
    def setup(cls):
        cls.Dependent_function = globals()

    @property  # 查询
    def url_NoviceG_select(self):
        url_NoviceGs = "/operate/newGuide/list"
        return url_NoviceGs

    @property  # 查询
    def data_NoviceG_select(self):
        data_NoviceGs = {"appid": ["9999"],  # appid
                         "channel": "",  # 子渠道
                         "endTime": "",  # 结束时间
                         "group": "appid,t_date,download_channel,pid",  # 分组
                         "limit": "100",  # 页最大数
                         "order": "",  # 排序
                         "pid": "",  # 项目id
                         "report": "",  # 页面名称
                         "start": "0",  # 当前页
                         "startTime": "",  # 开始时间
                         }
        return data_NoviceGs

    @property  # 导出
    def url_NoviceG_export(self):
        url_NoviceGs = "/operate/newGuide/export"
        return url_NoviceGs

    @property  # 导出
    def data_NoviceG_export(self):
        data_NoviceGs = {"appid": "",  # appid
                         "channel": "",  # 子渠道
                         "endTime": "2022-08-16",  # 结束时间
                         "group": "",  # 分组
                         "limit": "",  # 页最大数
                         "order": "",  # 排序
                         "pid": "",  # 项目id
                         "report": "",  # 页面名称
                         "start": "",  # 当前页
                         "startTime": "2022-05-18",  # 开始时间
                         "value": "appid,产品id;channel,渠道;",  # 自定义列参数 ,示例值(appid,产品id;channel,渠道)
                         }
        return data_NoviceGs

    @property  # 新手引导柱形图表
    def url_NoviceG_from(self):
        url_NoviceGs = "/operate/newGuide/view"
        return url_NoviceGs

    @property  # 新手引导柱形图表
    def data_NoviceG_from(self):
        data_NoviceGs = {"appid": "",  # appid
                         "channel": "",  # 子渠道
                         "endTime": "",  # 结束时间
                         "group": "",  # 分组
                         "limit": "",  # 页最大数
                         "order": "",  # 排序
                         "pid": "",  # 项目id
                         "report": "",  # 页面名称
                         "start": "",  # 当前页
                         "startTime": "",  # 开始时间
                         }
        return data_NoviceGs
