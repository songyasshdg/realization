#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: R.
# email: sy.mailbox@foxmail.com
# 定义
list1 = [1, "2", "进阶"]
print(list1)

# 嵌套
list2 = [1, "2", "进阶", [1, 2]]
print(list2)
# 取值(细节)
list3 = ['c', 'a', 'd', 'g']
print(list3[1])  # 取索引为1的值，结果为字符串 'a'
print(list3[1:2])  # 取索引为1的值，结果为列表 ['a']

# 增删改查拼乘
list4 = ['c+'] + ['+']
print(list4)
list5 = ['2', '1', 2, 4, "dd"]
print(list5 * 3)
# 新增 末尾新增
list5.append(1)
print(list5)
# insert(index, x)在列表lst指定位置index处添加元素x，该位置后面的所有元素后移一个位置
list5.insert(1, 'xl')

# pop方法 删除并返回列表lst中下标为index（默认为-1）的元素
list5.pop()
list5.pop(0)
print(list5)  # ['1']
# index()方法 返回列表lst中第一个值为x的元素的下标，若不存在值为x的元素则抛出异常
print(list5.index(2))

# count(x) 统计元素出现的次数
print(list5.count(1))
print(list5)
# reverse() 对列表lst所有元素进行逆序
list5.reverse()  # 这个运行结果没有返回值
print(list5)
print(list5[::-1])  # 这个是有返回值，其实是取值

'''写个方法 校验列表是否有相同的元素'''
def chan(l):
    for i in l:
        if  l.count(i)>1:
            return i
