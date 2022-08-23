#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: R.
# email: sy.mailbox@foxmail.com
import jsonpath

d = {
    "error_code": 0,
    "stu_info": [
        {
            "id": 2059,
            "name": "亚索",
            "sex": "男",
            "age": 28,
            "addr": "德玛西亚",
            "grade": "天蝎座",
            "info": {
                "card": 434345432,
                "bank_name": '中国银行',
                'name': 'dddd'

            }

        },
        {
            "id": 2067,
            "name": "李青",
            "sex": "男",
            "age": 28,
            "addr": "虾子岛",
            "grade": "天蝎座",
        }
    ]
}

# $表示最外层的{},取出来的格式都是列表list，注意自行处理
# 指定查找 [2067] 等同于 d['stu_info'][1]['id']
print(jsonpath.jsonpath(d, '$.stu_info.1.id.name'))
# # 在第一层里面找是否有键值=name的，未找到返回False
# print(jsonpath.jsonpath(d, '$.name'))
# # 在第二层找是否有键值=name的,有2个['亚索', '李青']
# print(jsonpath.jsonpath(d, '$..name'))
# # 在第二层找是否有键值=card的,有一个[434345432]
# print(jsonpath.jsonpath(d, '$...card'))
#
# # 数字索引提取，适用于列表  $表示最外层的[]
# a = [1, 2, [3, 4, [5, 6]]]
# # 第一个2是[3,4,[5,6]]，第二个2是[5,6],0是5
# print(jsonpath.jsonpath(a, '$.2.2.0'))  # [5]

# # 过滤
# c = {'code': 200,
#      'data': [
#          {'create_time': '2016-01-29 13:49:13',
#           'link': 'http://www.ehoutai.com/', 'uid': 7, 'name': '易后台'},
#          {'create_time': '2016-01-29 13:42:15',
#           'link': 'http://www.sanjieke.com/', 'uid': 4, 'name': '三节课'},
#          {'create_time': '2016-01-29 13:40:53',
#           'link': 'https://www.aliyun.com/', 'uid': 1, 'name': '阿里云'},
#          {'create_time': '2016-01-29 14:01:59',
#           'link': 'http://xmanlegal.com/', 'uid': 8, 'name': '未来法律'}]}
# # 只筛选data下uid等于4的一条数据 ：[{'create_time': '2016-01-29 13:42:15', 'link': 'http://www.sanjieke.com/', 'uid': 4,
# # 'name': '三节课'}]
# print(jsonpath.jsonpath(c, '$.data[?(@.uid==4)]'))
# print(jsonpath.jsonpath(c, '$.data[?(@.uid==4)][name]'))  # ['三节课']
# print(jsonpath.jsonpath(c, '$.data[?(@.uid>4)]'))  # 大于4的有2条数据
# # 使用in也可以 [{'create_time': '2016-01-29 14:01:59', 'link': 'http://xmanlegal.com/', 'uid': 8, 'name': '未来法律'}]
# print(jsonpath.jsonpath(c, '$.data[?("xm" in @.link)]'))
