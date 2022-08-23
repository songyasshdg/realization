#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: R.
# email: sy.mailbox@foxmail.com
"""
系统名称:产品运营系统
界面名称:新-V2锁屏配置
菜单位置:产品运营系统>工具配置>应用外功能配置>新-V2锁屏配置
"""


class TestLockscreen(object):  # 注意这里的开发必须以Test, 不然代码执行不了;

    @classmethod
    def setup(cls):
        cls.Dependent_function = globals()

    @property  # 增加
    def url_Lockscreen_Add(self):
        urls_Lockscreen = "/superLock/insertSuperLockGroup"
        return urls_Lockscreen

    @property  # 增加
    def data_Lockscreen_Add(self):
        data_Lockscreen = {"appid": "10002",  # 产品id
                           "bat_fas": "0",
                           "buy_act": "",  # 投放账户
                           "buy_id": "",  # 投放渠道
                           "cha": "2",  # 渠道标识
                           "chongdianStyle": [
                               {"path": ["pop#1", "ldyBefore#plaque", "", ""], "xIconZoom": "100", "style": "chongdian",
                                "deeplink": "", "per": "100", "close": "0"}],
                           "chongdianSwitch": "1",
                           "city": "all",
                           "cityStatus": "1",
                           "creatTime": "",
                           "cuser": "",
                           "dayTotalNum": "50",
                           "dianLiangModel": "1",
                           "dianLiangPer": "80#60#40#20",
                           "dianLiangStyle": [
                               {"path": ["pop#1", "ldyBefore#plaque", "", ""], "xIconZoom": "100", "style": "dianLiang",
                                "deeplink": "", "per": "100", "close": "0"}],
                           "dianLiangSwitch": "1",
                           "ejectInterval": "120",
                           "firstHome": "0",
                           "firstLock": "3600",
                           "firstLockNew": "0",
                           "firstUnLock": "0",
                           "h_fas": "0",
                           "homeAuto": "2",
                           "homeCity": "all",
                           "homeInterval": "120",
                           "homeNum": "50",
                           "homeStatus": "1",
                           "homeStyle": "[]",
                           "homeSwitch": "0",
                           "id": "",
                           "ldyAuto": "2",
                           "limit": "",  # 条数
                           "lockCity": "all",
                           "lockStatus": "1",
                           "lockStyle": "news_100,card_0,outNews_0",
                           "lockSwitch": "1",
                           "lockTotalNum": "50",
                           "modifyTime": "",
                           "modifyUser": "",
                           "nqDt": "5184000",
                           "outNewsSw": "0",
                           "pEt": "00:00:00",
                           "pFas": "0",
                           "pIt": "60",
                           "pSt": "00:00:00",
                           "pSw": "1",
                           "power_fas": "0",
                           "prjid": "20",  # 项目id######################################
                           "start": "",  # 页码
                           "status": "1",
                           "taCity": "all",
                           "taEt": "00:00:00",
                           "taFd": "0",
                           "taIt": "60",
                           "taNum": "50",
                           "taPointStyle": "[]",
                           "taSt": "00:00:00",
                           "taSta": "1",
                           "taSty": "[]",
                           "taSw": "1",
                           "ta_fas": "0",
                           "ul_fas": "0",
                           "unLockCity": "all",
                           "unLockInterval": "180",
                           "unLockStatus": "1",
                           "unLockStyle": "[]",
                           "unLockSwitch": "1",
                           "unlockTotalNum": "50",
                           "userGroup": "all",
                           "wf_fas": "0",
                           "wifiStyle": [
                               {"path": ["pop#1", "ldyBefore#plaque", "", ""], "xIconZoom": "100", "style": "wifi",
                                "deeplink": "", "per": "100", "close": "0"}],
                           "wifiSwitch": "1"
                           }
        return data_Lockscreen

    @property  # 修改
    def url_Lockscreen_update(self):
        urls_Lockscreen = "/superLock/updateSuperLockGroupByIdList"
        return urls_Lockscreen

    @property  # 修改
    def data_Lockscreen_update(self):
        data_Lockscreen = {"": "",
                           "": "",
                           "": "",
                           "": "",
                           "": "",
                           "": "",
                           "": "",
                           "": "",

                           }
        return data_Lockscreen

    @property  # 删除
    def url_Lockscreen_delete(self):
        urls_Lockscreen = "/superLock/deleteSuperLockGroupByIdList"
        return urls_Lockscreen

    @property  # 删除
    def data_Lockscreen_delete(self):
        data_Lockscreen = {"": "",
                           "": "",
                           "": "",
                           "": "",
                           "": "",
                           "": "",
                           "": "",
                           "": "",

                           }
        return data_Lockscreen

    @property  # 查询
    def url_Lockscreen_select(self):
        urls_Lockscreen = "/superLock/selectSuperLockGroup"
        return urls_Lockscreen

    @property  # 查询
    def data_Lockscreen_select(self):
        data_Lockscreen = {"": "",
                           "": "",
                           "": "",
                           "": "",
                           "": "",
                           "": "",
                           "": "",
                           "": "",

                           }
        return data_Lockscreen

    @property  # 修改状态(开关)
    def url_Lockscreen_updates(self):
        urls_Lockscreen = "/superLock/updateOnOff"
        return urls_Lockscreen

    @property  # 修改开关(状态)
    def data_Lockscreen_updates(self):
        data_Lockscreen = {"": "",
                           "": "",
                           "": "",
                           "": "",
                           "": "",
                           "": "",
                           "": "",
                           "": "",

                           }
        return data_Lockscreen
