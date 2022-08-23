#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: R.
# email: sy.mailbox@foxmail.com
import json


class FileTools():
    def json_file(self, filename):  # 打开json文件并读取数据
        art_data = json.load(open(filename, "r", encoding="utf8"))
        return art_data
