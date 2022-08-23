#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: R.
# email: sy.mailbox@foxmail.com
'''使用python3.6以上版本才有数据类型定义    '''
import math  # 数学函数

i: int = 1
f: float = 1.22
s: str = '字符串'
print(f'{i, f, s}')
'''int和float转化'''
# 整数转小数
print(float(i))
# 四舍五入保留2位小数
print(round(3.526, 2))
# 向下取整
print(math.floor(3.526))
# 向上取整
print(math.ceil(3.526))
# 将整数和小数分开打印输出，格式元组
print(math.modf(3.526))

'''数字类型和str'''
# 只有字符串里面的数据类型是数字类型或者浮点型类型就可以用对应的方法转化
print(int('12'))
print(float('12.1'))
