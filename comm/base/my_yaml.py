#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: R.
# email: sy.mailbox@foxmail.com
import yaml


def yaml_file(self, filename):  # 打开yaml文件并读取数据
    with open(filename, "r", encoding="utf8") as f:
        art_data = yaml.load(f.read(), Loader=yaml.FullLoader)
    return art_data