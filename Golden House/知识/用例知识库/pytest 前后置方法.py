#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: R.
# email: sy.mailbox@foxmail.com
import pytest
class TestFrontBack:
    def setup_class(self):
        print("前置条件(作用域：每个类执行之前)：创建日志对象，创建数据库连接")
    def setup(self):
        print("前置条件(作用域：每个用例执行之前)：打开谷歌，窗口最大化")

    def test_login(self):
        print('点击登录')
        print('输入账号')
        print('输入密码')
        print('点击登录')
    def test_buy(self):
        print('登录界面输入账号密码')
        print('点击登录')
        print('查看商品加入购物车')
        print('购物车购买支付商品')
        print('查看账户余额')

    def teardown(self):
        print('后置条件(作用域：每个用例执行之前后)：关闭谷歌')
    def teardown_class(self):
        print('后置条件(作用域：每个类执行之前后)：销毁日志对象，销毁数据库连接')

if __name__ == '__main__':
    pytest.main([r'D:\python新代码集\pytest_study\basics\test_front_back.py'])
