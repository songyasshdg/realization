#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: R.
# email: sy.mailbox@foxmail.com
"""
系统名称:产品运营系统
界面名称:微信分享内容配置
菜单位置:产品运营系统>产品管理>小游戏配置>微信分享内容配置
"""
from realization.lib.library import TestLibrary


class TestWecTshRing(TestLibrary):
    @classmethod
    def setup(cls):
        cls.Dependent_function = globals()

    @property  # 查询
    def url_wecTshRing_select(self):
        url_wecTshRing = "/operate/shareContentConfig/list"
        return url_wecTshRing

    @property  # 查询
    def data_wecTshRing_select(self):
        data_wecTshRing = {"limit": "100",  # 页最大数
                           "order": "",  # 排序
                           "remark": "",  # 备注
                           "start": "0",  # 当前页
                           }
        return data_wecTshRing

    @property  # 增加
    def url_wecTshRing_add(self):
        url_wecTshRing = "/operate/shareContentConfig/add"
        return url_wecTshRing

    @property  # 增加
    def data_wecTshRing_add(self):
        data_wecTshRing = {"image_number": self.generate_code(),  # 图片编号
                           "image_url": self.generate_code(),  # 图片地址
                           "remark": "",  # 备注
                           "title": self.str_rands(),  # 标题
                           }
        return data_wecTshRing

    @property  # 修改
    def url_wecTshRing_update(self):
        url_wecTshRing = "/operate/shareContentConfig/update"
        return url_wecTshRing

    @property  # 修改
    def data_wecTshRing_update(self):
        data_wecTshRing = {"id": self.Dependent_function['ids'],  # id
                           "image_number": self.generate_code(),  # 图片编号
                           "image_url": self.generate_code(),  # 图片地址
                           "remark": "",  # 备注
                           "title": self.str_rands(),  # 标题
                           }
        return data_wecTshRing

    @property  # 删除
    def url_wecTshRing_delete(self):
        url_wecTshRing = "/operate/shareContentConfig/delete"
        return url_wecTshRing

    @property  # 删除
    def data_wecTshRing_delete(self):
        data_wecTshRing = {"id": self.Dependent_function['ids']
                           }
        return data_wecTshRing

    @property  # 导出
    def url_wecTshRing_export(self):
        url_wecTshRing = "/operate/shareContentConfig/export"
        return url_wecTshRing

    @property  # 导出
    def data_wecTshRing_export(self):
        data_wecTshRing = {"order": "",  # 排序
                           "remark": "",  # 备注
                           "report": "",  # 页面名称
                           "value": "image_number,图片编号;image_url,图片地址;title,标题;remark,备注;create_owner,"
                                    "创建人;create_time,创建时间;update_owner,更新人;update_time,更新时间",  # 自定义列参数 ,示例值(appid,
                           # 产品id;channel,渠道)
                           }
        return data_wecTshRing
