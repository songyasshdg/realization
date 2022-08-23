#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: R.
# email: sy.mailbox@foxmail.com
import threading
import time


# 函数里面不能写变量
def run():
    ##这里直接写主体内容
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))  # 输出当地时间

    timer = threading.Timer(2, run)  # 设置一个定时器，循环输出时间,单位秒
    timer.start()  # 启动线程
run()
