#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: R.
# email: sy.mailbox@foxmail.com
"""
系统名称:产品运营系统
界面名称:单机兑换码V1
菜单位置:产品运营系统>产品管理>产品设置>单机兑换码V1
"""


class TestExchange(object):
    @classmethod
    def setup(cls):
        cls.Dependent_function = globals()

    @property  # 单个生成
    def url_exchange_code_add(self):
        base_exchange_code = "/operate/exchangeCode/add"
        return base_exchange_code

    @property  # 单个生成
    def data_exchange_code_add(self):
        data_exchange_code = {"expire_time": "2022-06-20 00:00:00",  # 过期时间
                              "num": 1,  # 兑换次数
                              "type": 1,  # 类型1是代表一次使用, 类型2是代表多次使用
                              "value": 0  # 兑换值
                              }
        return data_exchange_code

    @property  # 查询兑换
    def url_exchange_code_select(self):
        base_exchange_code_s = "/operate/exchangeCode/list"
        return base_exchange_code_s

    @property  # 查询兑换
    def data_exchange_code_select(self):
        data_exchange_code_s = {"code": "",  # 兑换码
                                "code_value": "",  # 兑换值
                                "limit": 100,  # 一页的数量
                                "order": "2",  # 排序
                                "start": "",  # 当前页
                                "status": ""  # 状态
                                }
        return data_exchange_code_s

    @property  # 批量生成
    def url_code_adds(self):
        base_exchange_code_ss = "/operate/exchangeCode/batchAdd"
        return base_exchange_code_ss

    @property  # 批量生成
    def data_exchange_code_adds(self):
        data_exchange_code_ss = {"expire_time": "2022-07-20",  # 过期时间
                                 "generate_num": 3,  # 生成数量
                                 "num": "1",  # 兑换次数
                                 "type": "2",  # 类型1一次使用,2多次使用
                                 "value": "2"  # 兑换值
                                 }
        return data_exchange_code_ss

    @property  # 使用测试接口
    def url_code_debuGapi(self):
        base_exchange_code_sss = "/operate/exchangeCode/usetest"
        return base_exchange_code_sss

    @property  # 使用测试接口 参数
    def data_code_debuGapi(self):
        data_exchange_code_sss = {"appid": "19075",  # 产品id
                                  "code": "4717091549",  # 兑换码
                                  "deviceId": "test",  # 设备id
                                  "ver": "v1"  # 版本
                                  }
        return data_exchange_code_sss
