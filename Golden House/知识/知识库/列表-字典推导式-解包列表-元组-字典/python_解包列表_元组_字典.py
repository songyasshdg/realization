#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: R.
# email: sy.mailbox@foxmail.com
'''*解包 把 oo拆成3个值'''
oo=(1,2,3)
ll=[2,4,6]
def uu(a,b,c):
    print(a,b,c)
uu(*oo) #1 2 3
uu(*ll) #2 4 6
'''**解包 拆解字典解字典为这样的格式 a=1,b=2,c=3，*拆解字典的话只能得到键的值'''
dd={'a':1,'b':2,'c':3}
# 一个星解包字典只会把键拿出来 *dd 就是 'a','b','c'  uu()函数返回结果是 a b c
uu(*dd)
# **dd 相当于 a=1,b=2,c=3 传到uu()函数里面 uu()函数返回结果是 1 2 3
uu(**dd)


'''解包合并字典和列表'''
list1=[1,2,3]
list2=[4,5,6]
print([*list1,*list2])  #[1, 2, 3, 4, 5, 6]

dict1={1:1,2:2}
dict2={3:3,4:4}
print({**dict1,**dict2}) #{1: 1, 2: 2, 3: 3, 4: 4}
