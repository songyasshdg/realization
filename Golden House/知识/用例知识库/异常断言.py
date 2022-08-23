#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: R.
# email: sy.mailbox@foxmail.com
# !/usr/bin/python3.6
# coding=utf-8
# Author: 文

import pytest


def exc(x):
    if x == 0:
        raise ValueError("value not 0 or None")
    return 2 / x


def test_raises():
    with pytest.raises(ValueError, match="value not 0 or None"):
        exc(0)
    assert eval("1 + 2") == 4


if __name__ == '__main__':
    pytest.main(["异常断言.py", "-s"])