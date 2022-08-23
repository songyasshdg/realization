#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: R.
# email: sy.mailbox@foxmail.com
"""
系统名称:产品运营系统
界面名称:小游戏事件上报统计-大数据
菜单位置:产品运营系统>运营数据>新手>小游戏事件上报统计-大数据
"""


class TestEvenTre(object):

    @classmethod
    def setup(cls):
        cls.Dependent_function = globals()

    @property  # 查询
    def url_evenTure_select(self):
        urls_evenTure = "/game/mgEventReport/get"
        return urls_evenTure

    @property  # 查询
    def data_evenTure_select(self):
        data_evenTure = {"appid": "38778",  # 应用id(必填)
                         "end_date": "2022-08-19",  # 结束时间(必填)
                         "start_date": "2022-05-21",  # 开始时间(必填)
                         "event_id": "",  # 事件id
                         "export_file_name": "",  # 文件名
                         "group": "tdate,appid,event_id",  # 维度
                         "limit": "100",  # 条数
                         "order_str": "",  # 排序 ,示例值(可排序字段tdate,new_user_cnt,old_user_cnt)
                         "start": "0",  # 页码
                         "value": "",  # 自定义列参数：value,key;value2,key2
                         }
        return data_evenTure

    @property  # 导出
    def url_evenTure_export(self):
        urls_evenTure = "/game/mgEventReport/export"
        return urls_evenTure

    @property  # 导出
    def data_evenTure_export(self):
        data_evenTure = {"appid": "38778",  # 应用id(必填)
                         "end_date": "2022-08-19",  # 结束时间(必填)
                         "start_date": "2022-05-21",  # 开始时间(必填)
                         "event_id": "",  # 事件id
                         "export_file_name": "",  # 文件名
                         "group": "tdate,appid,event_id",  # 维度
                         "limit": "100",  # 条数
                         "order_str": "",  # 排序 ,示例值(可排序字段tdate,new_user_cnt,old_user_cnt)
                         "start": "0",  # 页码
                         "value": "tdate,日期;appname,应用名称;appid,应用id;event_id,事件id;new_user_cnt,新用户上报人数;old_user_cnt,"
                                  "老用户上报人数",  # 自定义列参数：value,key;value2,key2
                         }
        return data_evenTure

    @property  # 获取事件id下拉列表
    def url_evenTure_post_id(self):
        urls_evenTure = "/game/mgEventReport/getMGEventList"
        return urls_evenTure

    @property  # 获取事件id下拉列表
    def data_evenTure_post_id(self):
        data_evenTure = {"appid": "38778",  # 应用id(必填)
                         "end_date": "2022-08-19",  # 结束时间(必填)
                         "start_date": "2022-05-21",  # 开始时间(必填)
                         }
        return data_evenTure
