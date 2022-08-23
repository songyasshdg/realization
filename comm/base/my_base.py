#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: R.
# email: sy.mailbox@foxmail.com
import requests
from realization.log.logger.my_log import logger


class TestPublicLibrary(object):
    tokens = None  # 全局token  #全项目token失效时间为5~9分钟
    rep_ss = requests.session()  # 全局session
    base_urls = "http://192.168.1.38:6105"  # 全局域名

    @classmethod
    def setup(cls):  # 前置准备
        """
        globals()  # 全局依赖函数
        """
        cls.Dependent_function = globals()
        logger.info(
            '\n''==================================================接口自动化测试开始==========================================')

    @classmethod
    def teardown(cls):  # 后置退出
        logger.info(
            "\n""=================================================接口自动化测试结束===========================================")

    @classmethod  # 使用类方法
    def setup_class(cls):  # setup_class 为前置
        base_urls = cls.base_urls + "/all/login"  # 基于pytest框架，所以使用pytest中的setup，实现操作前先登录
        data = {"value": "eyJ1bmFtZSI6InNvbmd5YSIsInB3ZCI6InNvbmd5YTA2MTAifQ=="}
        r = cls.rep_ss.post(url=base_urls, data=data)
        cls.tokens = r.json()['token']

    @classmethod
    def teardown_class(cls):
        cls.rep_ss.close()  # teardown_class为后置 不管有多少用例, 执行完后 自动关闭session()会话

    @classmethod
    def headers(self):
        Header = {"token": self.tokens, 'charset': 'utf-8'}
        return Header

    @classmethod
    def jsonHeaders(self):
        Header = {"token": self.tokens, 'Content-Type': 'application/json', 'charset': 'utf-8'}
        return Header

    @classmethod
    def fromHeader(self):
        Header = {"token": self.tokens, 'Content-Type': 'application/x-www-form-urlencoded', 'charset': 'utf-8'}
        return Header

    @classmethod
    def requests(self, method: str, url, params=None, data=None, json=None, headers=None, files=None, timeout=None, **kwargs):  # 自定义发送请求
        method = method.upper()  # 将请求方法转换成大写
        if method == "GET":
            res = self.rep_ss.get(url, params=params, headers=headers, files=files, timeout=3, **kwargs)
            logger.info(
                '\n'f"请求方法：{method}\n请求地址：{url}\n请求参数:{data}\n发送请求：{res.request.body}\n请求头:{headers}\n响应未超过3秒:{timeout}\n上传文件:{files}\n\n\n响应结果：{res.text}\n\n")
            return res
        elif method == "POST":
            # 由于导出数据量大的文件,需要延迟时间至10秒
            res = self.rep_ss.post(url, data=data, json=json, headers=headers, files=files, timeout=10, **kwargs)
            logger.info(
                '\n'f"请求方法：{method}\n请求地址：{url}\n请求参数:{data}\n发送请求：{res.request.body}\n请求头:{headers}\n响应未超过10秒:{timeout}\n上传文件:{files}\n\n\n响应结果：{res.text}\n\n")
            return res
        elif method == "PUT":
            res = self.rep_ss.put(url, data=data, json=json, headers=headers, files=files, timeout=3, **kwargs)
            logger.info(
                '\n'f"请求方法：{method}\n请求地址：{url}\n请求参数:{data}\n发送请求：{res.request.body}\n请求头:{headers}\n响应未超过3秒:{timeout}\n上传文件:{files}\n\n\n响应结果：{res.text}\n\n")
            return res
        elif method == "DELETE":
            res = self.rep_ss.delete(url, data=data, json=json, headers=headers, files=files, timeout=3, **kwargs)
            logger.info(
                '\n'f"请求方法：{method}\n请求地址：{url}\n请求参数:{data}\n发送请求：{res.request.body}\n请求头:{headers}\n响应未超过3秒:{timeout}\n上传文件:{files}\n\n\n响应结果：{res.text}\n\n")
            return res
        else:  # 如果不是以上4种请求方法，则提示"请求方法未定义，请检查！"
            logger.error("请求方法未来定义, 请检查!!!!")
            print("请求方法未定义，请检查！")
