#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: R.
# email: sy.mailbox@foxmail.com
class TestfilePng(object):
    @classmethod
    def filePng(self, filename, filepath, filetype):  # 注意上传png的图片, 请求头 不能携带Content-Type
        """
        :param filename: 文件的名称+格式
        :param filepath: 文件的路径
        :param filetype: 文件的媒体类型
        :return: rb 表示二进制方式读取
        上传文件格式
        """
        filPng = {"file": (filename, open(filepath, mode="rb"), filetype)}  # 如果需要编码转码, 可以在括号里加上encoding="utf8"
        return filPng
