#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: R.
# email: sy.mailbox@foxmail.com
import requests
r = requests.get("https://blog.csdn.net/wuyoudeyuer", timeout=0.001)
print(r.elapsed)
print(r.elapsed.total_seconds())
print(r.elapsed.microseconds)
print(r.elapsed.seconds)
print(r.elapsed.days)
print(r.elapsed.max)
print(r.elapsed.min)
print(r.elapsed.resolution)

# total_seconds 总时长，单位秒
# days 以天为单位
# microseconds (>= 0 and less than 1 second) 获取微秒部分，大于0小于1秒
# seconds Number of seconds (>= 0 and less than 1 day) 秒，大于0小于1天
# max = datetime.timedelta(999999999, 86399, 999999) 最大时间
# min = datetime.timedelta(-999999999) 最小时间
# resolution = datetime.timedelta(0, 0, 1) 最小时间单位
