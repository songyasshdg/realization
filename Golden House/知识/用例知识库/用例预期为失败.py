#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: R.
# email: sy.mailbox@foxmail.com
"""
1.学习目标
    了解预期失败方法
2.操作步骤
    2.1 xfail(condition,reason)
        condition:当condition条件为真,用例标记失败
        reason: 原因

3.使用xfail标识用例可能出现的情况：
    条件     用例执行结果   测试结果
    True     False          FAILED
    True     True           PASSED
    False    False          XFAIL
    False    True           XPASS

"""
# 1.导入pytest
import pytest


# 2.编写测试用例
# 预期失败,结果失败
@pytest.mark.xfail(True, reason="该功能尚未完成")
def test_case_1():
    print("预期失败,结果失败")
    pytest.xfail()
    assert False


# 预期失败,结果成功
@pytest.mark.xfail(True, reason="该功能尚未计划")
def test_case_2():
    print("预期失败,结果成功")
    assert True


# 预期成功,结果失败
@pytest.mark.xfail(False, reason="")
def test_case_3():
    print("预期成功,结果失败")
    assert False


# 预期成功,结果成功
@pytest.mark.xfail(False, reason="")
def test_case_4():
    print("预期成功,结果成功")
    assert True


if __name__ == '__main__':
    pytest.main()

"""
运行结果：
test_01.py::test_case_1 预期失败,结果失败
XFAIL
test_01.py::test_case_2 预期失败,结果成功
XPASS (该功能尚未计划)
test_01.py::test_case_3 预期成功,结果失败
FAILED
test_01.py::test_case_4 预期成功,结果成功
PASSED

============== 1 failed, 1 passed, 1 xfailed, 1 xpassed in 0.09s ==============


用例表单说明.txt：
x(小写x)预期失败,结果失败   1 xfailed（预期失败）
X（大写X）预期失败,结果成功   1 xpassed（预期成功）
F预期成功,结果失败   1 failed
.预期成功,结果成功   1 passed
在测试执行过程中,会将xpassed状态的用例直接转成failed状态
"""


@pytest.mark.xfail(raises=AssertionError)
def test_03():
    assert 3 == 4


@pytest.mark.xfail(raises=ValueError)
def test_04():
    if isinstance('1234', int) is False:
        raise TypeError("传入参数非整数")
