#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: R.
# email: 484002966@qq.com
# from pygal.style import *
# people=data['人员'].unique()
# label=data['月份'].unique()
# radar_chart = pygal.Radar(style=LightStyle)
# radar_chart.title = '520寝室2020年生活费花销情况'
# radar_chart.x_labels = label
# for i in people:
#     radar_chart.add(i, data[data.人员==i]['花销'].values.tolist())
# HTML(base_html.format(rendered_chart=radar_chart.render(is_unicode=True)))#图片渲染
# class Decorate(object):
#     def __init__(self, func):
#         self.__func = func
#
#     def __call__(self, name):
#         print("我能够多加上功能了")
#         self.__func(name)
#
#
# @Decorate
# def say(name):
#     print("我%s很饿的" % name)
#
#
# # say("小明")
# def my_decorator(func):
#     def wrapper():
#         print('wrapper of decorator')
#         func()
#     return wrapper
#
# @my_decorator
# def greet():
#     print('hello world')
#
from random import random
import random
import string
from datetime import timedelta, date


class s(object):
    @classmethod
    def rand(cls):
        name = ["任", "李", "张", "宋"]  # 可多加
        str_list = ["爱", "婷", "聪", "亚"]  # 可多加
        random.shuffle(str_list)
        font_string = ''
        for i in range(0, random.randint(1, 3)):  # 从0开始
            font_string += random.choice(str_list)
        names = random.choice(name)
        return names + font_string


ls = s.rand()
print(ls)
