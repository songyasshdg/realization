#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: R.
# email: sy.mailbox@foxmail.com
import random

a = 1
while a < 3:
    print('进来时a={}'.format(a))
    a += 1
    print('出去时a={}'.format(a))

print('循环运行完的a={}'.format(a))

count = 0
while a <= 7:
    count += 1
    a += random.randint(2, 9)
else:
    print('a运行了{}次就大于7了，a={}'.format(count, a))
