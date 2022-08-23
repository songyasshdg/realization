#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: R.
# email: sy.mailbox@foxmail.com
import pytest

# @pytest.mark.dependency(depends=["test_01"])
# def test_02():
#     print('function hello')
#     asserts 1 == 1
#
#
# @pytest.mark.dependency()
# def test_01():
#     print('function hello')
#     asserts 1 == 1
#
#
# if __name__ == '__main__':
#     pytest.main(['-sv'])
# import pytest
#
#
# def test_02():
#     print('function test_02')
#     asserts 1 == 1
#
#
# class Testdep2():
#     @pytest.mark.dependency()
#     def test_01(self):
#         print('class test_01')
#         asserts 1 == 1
#
#     @pytest.mark.dependency()
#     def test_02(self):
#         print('class test_02')
#
#
# class Testdep1():
#     @pytest.mark.dependency()
#     def test_01(self):
#         print('class test_01')
#         asserts 1 == 1
#
#     @pytest.mark.dependency(depends=["test_01"], scope='class')
#     def test_02(self):
#         print('class test_02')
#
#
# @pytest.mark.dependency()
# def test_01():
#     print('function test_01')
#     asserts 1 == 1
#
#
# if __name__ == '__main__':
#     pytest.main(['-sv'])


# 类
import pytest


def test_02():
    print('function test_02')
    assert 1 == 1


class Testdep2():
    @pytest.mark.dependency()
    def test_01(self):
        print('class test_01')
        assert 1 == 1

    @pytest.mark.dependency()
    def test_02(self):
        print('class test_02')


class Testdep1():
    @pytest.mark.dependency()
    def test_01(self):
        print('class test_01')
        assert 1 == 1

    @pytest.mark.dependency(depends=["Testdep2::test_01"], scope='module')
    def test_02(self):
        print('class test_02')


@pytest.mark.dependency()
def test_01():
    print('function test_01')
    assert 1 == 1


if __name__ == '__main__':
    pytest.main(['-sv'])
