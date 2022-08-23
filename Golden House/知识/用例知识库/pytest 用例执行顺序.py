#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: R.
# email: sy.mailbox@foxmail.com
import pytest
def test1():
    print('登录')
def test4():
    print('取件')
def test2():
    print('存件')
def test3():
    print('发短信')
if __name__ == '__main__':
    pytest.main(['-vs',r'D:\python新代码集\pytest_study\basics\test_execution_sequence.py'])
import pytest
'''
默认执行顺序从上到下
'''
@pytest.mark.run(order=1)
def test1():
    print('登录')
@pytest.mark.run(order=4)
def test4():
    print('取件')

@pytest.mark.run(order=2)
def test2():
    print('存件')
@pytest.mark.run(order=3)
def test3():
    print('发短信')
if __name__ == '__main__':
    pytest.main(['-vs',r'D:\python新代码集\pytest_study\basics\test_execution_sequence.py'])
