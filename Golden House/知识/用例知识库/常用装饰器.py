#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: R.
# email: sy.mailbox@foxmail.com
import pytest

age = 18


@pytest.mark.skip(reason="跳过01用例")
def test_01():
    print("day02------test_day01")


@pytest.mark.skipif(age >= 18, reason="age大于18跳过")
def test_02():
    print("day02------test_day02")


@pytest.mark.run(order=2)
def test_03():
    print("day02------test_day03")


@pytest.mark.smoke
def test_smoke():
    print("冒烟测试。。。")


@pytest.mark.run(order=1)
@pytest.mark.userlogin
def test_login():
    print("用户登录。。")
# @pytest.mark.skip(reason=“跳过01用例”) 跳过用例
# @pytest.mark.skipif(age>=18,reason=“age大于18跳过”) 满足条件跳过
# @pytest.mark.run(order=2) 指定用例执行顺序
# @pytest.mark.smoke (自定义标识,smoke为自己定义)
