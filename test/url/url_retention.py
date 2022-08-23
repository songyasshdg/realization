#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: R.
# email: sy.mailbox@foxmail.com
"""
系统名称:产品运营系统
界面名称:应用内真实留存
菜单位置:产品运营系统>运营数据>留存数据>应用内真实留存
"""


class TestRetention(object):
    @classmethod
    def setup(cls):
        cls.Dependent_function = globals()

    @property  # 查询
    def url_retention_select(self):
        url_retentions = "/retainedData/selectByCondition"
        return url_retentions

    @property  # 查询
    def data_retention_select(self):
        data_retentions = {"appid": "",  # 应用id
                           "downloadChannel": "",  # 下载渠道
                           "end_date": "2022-08-15",  # 结束时间
                           "export_file_name": "",  # 文件名
                           "group": "",  # 维度
                           "limit": "100",  # 条数
                           "order_str": "",  # 排序字段
                           "pid": "",  # 项目id
                           "start": "1",  # 页码
                           "start_date": "2022-08-15",  # 开始时间
                           "value": "",  # 自定义列参数：value,key;value2,key2
                           "ver": ""  # 项目id

                           }
        return data_retentions

    @property  # 导出
    def url_retention_export(self):
        url_retentions = "/retainedData/exportAdsToolAppInRetentionDaily"
        return url_retentions

    @property  # 导出
    def data_retention_export(self):
        data_retentions = {"appid": "",  # 应用id
                           "downloadChannel": "",  # 下载渠道
                           "end_date": "2022-08-15",  # 结束时间
                           "export_file_name": "",  # 文件名
                           "group": "tdate,downloadChannel,pid,ver",  # 维度
                           "limit": "100",  # 条数
                           "order_str": "",  # 排序字段
                           "pid": "",  # 项目id
                           "start": "1",  # 页码
                           "start_date": "2022-08-09",  # 开始时间
                           "value": "tdate,日期;appid,应用ID;pid,项目ID;downloadChannel,下载渠道;ver,版本号;appName,"
                                    "应用名称;proportionOfUsers,真实用户占比;regUserCnt,当天新增;realRegUserCnt,"
                                    "当天新增真实用户;realRetention1dayUserCnt,1日后;realRetention2dayUserCnt,"
                                    "2日后;realRetention3dayUserCnt,3日后;realRetention4dayUserCnt,"
                                    "4日后;realRetention5dayUserCnt,5日后;realRetention6dayUserCnt,"
                                    "6日后;realRetention7dayUserCnt,7日后;realRetention14dayUserCnt,"
                                    "14日后;realRetention30dayUserCnt,30日后;", # 自定义列参数：value,key;value2,key2
                           "ver": "",  # 版本号

                           }
        return data_retentions
