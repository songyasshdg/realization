#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: R.
# email: 484002966@qq.com
import re
# from hamcrest import *
# s = "a regular1 expgular2 reegular3"
# print(re.findall(r"(?<!re)gular", s))
# # 匹配 左边不是re 的 gular
#
# # assertThat(333, hasToString(equalTo("333")))
# # assert_that(333,h)

from hamcrest import *
import unittest

#
# class HamcrestTest(unittest.TestCase):
#     def testEquals(self):
#         theString = 'Hello Hamcrest'
#         myString = 'Hello Hamcrest'
#         assert_that(theString, equal_to(myString))
#
#
# if __name__ == '__main__':
#     unittest.main()

import re
#
# # .：匹配任意1个字符
# re1 = r'.'
# res1 = re.findall(re1, '\nj8?0\nbth\nihb')
# print(res1)  # 运行结果：['j', '8', '?', '0', 'b', 't', 'h', 'i', 'h', 'b']
#
# # []：匹配列举中的其中一个
# re2 = r"[abc]"
# res2 = re.findall(re2, '1iugfiSHOIFUOFGIDHFGFD2345a6a78b99cc')
# print(res2)  # 运行结果：['a', 'a', 'b', 'c', 'c']
#
# # \d:匹配一个数字
# re3 = r"\d"
# res3 = re.findall(re3, "dfghjkl32212dfghjk")
# print(res3)  # 运行结果：['3', '2', '2', '1', '2']
#
# # \D:匹配一个非数字
# re4 = r"\D"
# res4 = re.findall(re4, "d212dk？\n$%3;]a")
# print(res4)  # 运行结果：['d', 'd', 'k', '？', '\n', '$', '%', ';', ']', 'a']
#
# # \s：匹配一个空白键或tab键（tab键实际就是两个空白键）
# re5 = r"\s"
# res5 = re.findall(re5, "a s d a  9999")
# print(res5)  # 运行结果：[' ', ' ', ' ', ' ', ' ']
#
# # \S: 匹配非空白键
# re6 = r"\S"
# res6 = re.findall(re6, "a s d a  9999")
# print(res6)  # 运行结果：['a', 's', 'd', 'a', '9', '9', '9', '9']
#
# # \w：匹配一个单词字符(数字、字母、下划线)
# re7 = r"\w"
# res7 = re.findall(re7, "ce12sd@#a as_#$")
# print(res7)  # 运行结果：['c', 'e', '1', '2', 's', 'd', 'a', 'a', 's', '_']
#
# # \W：匹配一个非单词字符(不是数字、字母、下划线)
# re8 = r"\W"
# res8 = re.findall(re8, "ce12sd@#a as_#$")
# print(res8)  # 运行结果：['@', '#', ' ', '#', '$']

# # 匹配指定字符
# re9 = r"python"
# res9 = re.findall(re9, "cepy1thon12spython123@@python")
# print(res9)  # 运行结果：['python', 'python']
import re

# s = "a123abc123aaa1234bbb888ccc"
s = "1生成成功"
# match：只匹配字符串的开头，开头不符合就返回None
res1 = re.match(r"生成成功", s)
print(res1)  # 运行结果：<re.Match object; span=(0, 4), match='a123'>