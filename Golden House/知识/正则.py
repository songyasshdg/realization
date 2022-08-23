#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: R.
# email: sy.mailbox@foxmail.com
import re

# s = 'a regular expression'
# print(re.findall(r"re(?=gular)", s))
# assert re.findall(re.findall(r"re(?=gular)", s)
# 匹配re 匹配的是 后面又 gular 的re  只会匹配到一个re
# 断言部分 (?=xxx) 只是用来确定位置的
# 零宽正向断言 就在我想匹配的字符的后面设置 匹配位置
#  - 输出结果： ['re']
# {"ret":1,"msg":"操作成功","data":[]}
# s = {"ret": 1, "msg": "操作成功", "data": []}
#
# print(re.findall(r"(?<!re)gular", s))
# 匹配 左边不是re 的 gular
#  - 输出结果： ['gular2', 'gular3']
import requests
import re

# 登录接口
# login_url = 'http://47.112.233.130:8888/users/login/'


# # 请求登录接口，进行登录
# params = {
#     "username": "test",
#     "password": "123456"
# }
# response = requests.post(url=login_url, json=params)
# #使用正则表达式提取token
# result = re.search(r'msg":"(.+?)"',response.text)
# token = result.group(1)
# print(result)
# print(token)
# # assert True
# print(response.text)
import re
# import re
#
# zen = "ret:1,msg:30"
# m = re.search("\\d+", zen)
# m.group(0)
# print(m)
import re
#
# zen = "ret:1,msg:30"
# ms = re.search("\\d+", zen).group(0)  # 123abc456,返回整体
# print(ms)
# mss = re.search("\\d+", zen).group(1)
# print(mss)
# # ma = re.search("([0-9]*)([a-z]*)([0-9]*)", zen).group(1)  # 123
# # print(ma)
# # ak = re.search("([0-9]*)([a-z]*)([0-9]*)", zen).group(2)  # abc
# # print(ak)
# # ss = re.search("([0-9]*)([a-z]*)([0-9]*)", zen).group(3)  # 456
# # print(ss)
import re
#
# pattern = re.compile(r'\d+')  # 查找数字
# result1 = pattern.findall('runoob 123 google 456')
# result2 = pattern.findall('run88oob123google456', 0, 10)
#
# print(result1)
# print(result2)
import re

#
# # 定义了两个group,因为包含两个括号
# s = "Isaac:Newton,b:physicist"
# m = re.search("(\\w+)", s)
#
# # group(0)就是匹配的整个结果
# print(m.group(1))  # 输出结果为Isaac Newton

# group(1)是第一个group的值
# print(m.group(1))  # 输出结果为Isaac

# group(2)是第二个group的值
# print(m.group(2))  # 输出结果为Newton

# groups返回所有的group,以元组的形式
# print(m.groups())  # 输出结果为('Isaac','Newton')
# us = "ret,1,msg,10,s,12"
# m = re.search("\\d+", us)
# print(m)
