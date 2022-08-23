#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: R.
# email: sy.mailbox@foxmail.com
import pytest


@pytest.mark.run(order=2)
def test_1():
    print(11111111111)


@pytest.mark.run(order=3)
def test_2():
    print(22222)


@pytest.mark.run(order=1)
def test_3():
    print(33333333)


@pytest.mark.run(order=4)
def test_4():
    print(44444)


if __name__ == "__main__":
    pytest.main()
