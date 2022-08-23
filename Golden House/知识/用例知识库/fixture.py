#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: R.
# email: sy.mailbox@foxmail.com
import pytest


# @pytest.fixture(scope="class")
# def execute_sql():
#     print("执行SQL语句")
#     print("关闭数据库连接")
#
#
# @pytest.mark.usefixtures("execute_sql")
# class TestApi:
#
#     def test_01_mashang(self):
#         print("1")
#
#     def test_02_jiaoyu(self):
#         print("2")
#
#
# class TestMashang:
#     def test_baili(self):
#         print("天草柑橘")
import pytest


# fixture函数(类中) 作为多个参数传入
@pytest.fixture()
def login():
    print("打开浏览器")
    a = "account"
    return a


@pytest.fixture()
def logout():
    print("关闭浏览器")


class TestLogin:
    # 传入lonin fixture
    def test_001(self, login):
        print("001传入了loging fixture")
        assert login == "account"

    # 传入logout fixture
    def test_002(self, logout):
        print("002传入了logout fixture")

    def test_003(self, login, logout):
        print("003传入了两个fixture")

    def test_004(self):
        print("004未传入仍何fixture哦")


if __name__ == '__main__':
    pytest.main()


