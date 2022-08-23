#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: R.
# email: sy.mailbox@foxmail.com
"""
系统名称:产品运营系统
界面名称:小游戏内购支付配置
菜单位置:产品运营系统>产品运营>小游戏配置>小游戏内购支付配置
"""


class TestSmaLgame(object):
    @classmethod
    def setup(cls):
        cls.Dependent_function = globals()

    @property  # 查询
    def url_game_select(self):
        url_Game_select = "/operate/inGamePaymentConfig/list"
        return url_Game_select

    @property  # 查询
    def data_Game_select(self):
        data_game = {"api_key": "",  # API 密钥
                     "appid": "",  # appid
                     "channel": "",  # 子渠道
                     "limit": "100",  # 页最大数
                     "machid": "",  # 商户号
                     "mch_serial": "",  # 商户证书序列号
                     "order": "",  # 排序字段
                     "start": "0",  # 当前页
                     "wxappid": "",  # 微信id
                     }
        return data_game

    @property  # 操作-查询小游戏内购支付配置
    def url_Game_add_del_exit(self):
        url_Game_select = "/operate/inGamePaymentConfig/handel"
        return url_Game_select

    @property  # 操作-查询小游戏内购支付配置
    def data_Game_add_del_exit(self):
        data_game = {"api_key": "54",  # API 密钥
                     "app_secret": "http://192.168.1.3/",  # 凭证秘钥
                     "appid": "9999",  # 应用id
                     "channel": "111",  # 渠道
                     "create_owner": "songya",  # 创建人
                     "create_time": "",  # 创建时间
                     "handle": "add",  # 操作方式(add/edit/del)
                     "machid": "545",  # 商户号
                     "mch_serial": "454",  # 商户证书序列号
                     "notify_url": "http://192.168.1.38/",  # 回调地址
                     "private_key": "58",  # 私钥
                     "update_owner": "",  # 更新人
                     "update_time": "",  # 更新时间
                     "wxappid": "45",  # 微信id
                     }
        return data_game
