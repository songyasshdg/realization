#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: R.
# email: sy.mailbox@foxmail.com
'''列表 和 字符串'''
import random

list1 = [1, '2', 3, 'kk']
print(str(list1))

'''
join()方法 是以字符串里面的内容分割每个列表的元素，然后变为字符串
需要注意的是该方法需要list中的元素为字符型，若是整型，则需要先转换为字符型后再转为str类型
'''

s = "".join([str(i) for i in list1])
print(s)

str1 = 'klo10'
l = list(str1)
print(l)

'''字典 和 字符串'''

d1 = {1: 1, 2: 2}
d2 = str(d1)
print('d2的值{}，类型为{}'.format(d2, type(d2)))  # d2的值{1: 1, 2: 2}，类型为<class 'str'>

'''把d2要重新转化为字典格式直接用dict(d2)是会报错的'''
# print(dict(d2))
d3 = eval(d2)
print('d3的值{}，类型为{}'.format(d3, type(d3)))  # d3的值{1: 1, 2: 2}，类型为<class 'dict'>

'''eval()函数 可以字符里面写表达式储存起来，再用eval()函数使用赋值给变量'''

# 随机文本
random_str = "'测试{}'.format(random.randint(100,99999))"
print(eval(random_str))

'''列表 和 字典'''

list1 = ['1', '2', '3']
list2 = [1, 2, 3, 1]
print('相同长度的列表(多余的会自动干掉)转换为字典（哪个列表在前面就是键）{}'.format(dict(zip(list2, list1))))

'''写个方法，当列表长度不一样是可以自动补充键值'''
def l_d(l1, l2):
    dict2 = {}
    if len(l1) == len(l2):
        for i in range(len(l1)):
            dict2[l1[i]] = l2[i]
        return dict2
    elif len(l1) > len(l2):
        for i in range(len(l1)):
            if i >= len(l2):
                dict2[l1[i]] = None
            else:
                dict2[l1[i]] = l2[i]
        return dict2
    else:
        k = 0
        for i in range(len(l2)):
            k += 1
            if i >= len(l1):
                dict2['k{}'.format(k)] = l2[i]
            else:
                dict2[l1[i]] = l2[i]
        return dict2


print(l_d(list1, list2))

dict0 = {'ll': 2, 'cc': 0, 'dd': '1'}
'''键转为列表'''
print([i for i in dict0.keys()])
'''值转为列表'''
print([i for i in dict0.values()])
