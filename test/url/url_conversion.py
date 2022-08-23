#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: R.
# email: sy.mailbox@foxmail.com
"""
系统名称:产品运营系统
界面名称:业务模式配置页面
菜单位置:产品运营系统>产品管理>应用管理>业务模式配置
"""


class TestConversion(object):  # 注意这里的开发必须以Test, 不然代码执行不了;

    @classmethod
    def setup(cls):
        cls.Dependent_function = globals()

    @property  # 查询外广转换漏斗
    def url_conversion_select(self):
        urls_conversion_select = "/operate/outConvertFunnel/list"
        return urls_conversion_select

    @property  # 查询外广转换漏斗
    def data_conversion_select(self):
        data_conversionc = {"appid": "",  # appid
                            "category": "",  # 分类
                            "channel": "",  # 子渠道
                            "endTime": "2022-08-16",  # 结束时间
                            "event_name": "",  # 触发来源
                            "group": "ds,appid,ver,channel,event_name",  # 分组
                            "limit": "",  # 页最大数
                            "order": "",  # 排序
                            "start": "",  # 当前页
                            "startTime": "2022-05-18",  # 开始时间
                            "version": "",  # 版本号
                            }
        return data_conversionc

    @property  # 导出
    def url_conversion_export(self):
        urls_conversion = "/operate/outConvertFunnel/export"
        return urls_conversion

    @property  # 导出
    def data_conversion_export(self):
        data_conversionc = {"appid": "",  # appid
                            "category": "",  # 分类
                            "channel": "",  # 子渠道
                            "endTime": "2022-05-06",  # 结束时间
                            "event_name": "",  # 触发来源
                            "group": "ds,appid,ver,channel,event_name",  # 分组
                            "order": "",  # 排序
                            "report": "",  # 页面名称
                            "startTime": "2022-05-05",  # 开始时间
                            "value": "ds,日期;app,应用名称;channel,子渠道;ver,版本号;act_users,活跃;new_users,新增;add_rate,"
                                     "新增占比;event_name,触发来源;pull_rate,应弹渗透率;",  # 自定义列参数 ,示例值(appid,产品id;channel,渠道)
                            "version": ""  # 版本号
                            }

        return data_conversionc
