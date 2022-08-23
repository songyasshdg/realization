#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: R.
# email: sy.mailbox@foxmail.com
import time

import requests
import timeout_decorator


@timeout_decorator.timeout(0.001)  # 这个模块在Linux里面常用   windows下使用会有限制
def test():
    r = requests.get("https://www.baidu.com/")
    print(r)


