#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: R.
# email: sy.mailbox@foxmail.com
import json
import yaml
from realization.log.logger.my_log import logger
from realization.config.config import environment


class Testfile(object):
    @classmethod
    def r_open(cls, key=None, filepath=None):  # 读取yaml格式
        with open(filepath, mode='r', encoding='utf-8') as f:
            value = yaml.load(stream=f.read(), Loader=yaml.FullLoader)  # Loader=yaml.FullLoader 加载所有内容的意思
            # read() 函数默认读取全部文件内容
            return value[key]

    @classmethod
    def a_open(cls, data=None, filepath=None):  # 写入yaml格式
        with open(filepath, mode='a', encoding='utf-8') as f:  # allow_unicode = True 如果添加的数据包含中文，避免写入的数据出现乱码
            w = yaml.dump(data, stream=f, allow_unicode=True)
            return w

    @classmethod
    def clear_open(cls):
        pass

    @classmethod
    def with_open(cls, filename=None, filepath=None):  # xlsx文件流 可以不用带encoding='utf-8'
        paths = environment + filepath  # 从config文件获取路径进行拼接
        with open(paths, mode="wb") as f:
            logger.info(f"导出路径 -> 请往此路径查看数据:{paths}")
            f.truncate()  # 清空文件内容
            f.write(filename)  # write写入的意思
            w = f.close()
            return w

    @classmethod
    def yaml_file(self, filename):  # 打开yaml文件并读取数据
        with open(filename, mode="r", encoding="utf8") as f:  # read() 函数默认读取全部文件内容
            art_data_yaml = yaml.load(f.read(), Loader=yaml.FullLoader)  # Loader=yaml.FullLoader 加载所有内容的意思
        return art_data_yaml

    @classmethod
    def json_file(self, filename):  # 打开json文件并读取数据
        # art_data_json = json.load(open(filename, mode="r", encoding="utf8")) # 这种方式也可以  下面的方式也可以
        # return art_data_json
        file = open(filename, mode='r', encoding='utf8')
        data = json.load(file)  # 把json文件的内容转化为python的字典
        file.close()
        return data

    @classmethod
    def upload_file(self, filename, filepath, filetype):
        """
        :param filename: 文件的名称+格式
        :param filepath: 文件的路径
        :param filetype: 文件的媒体类型
        :return: rb 表示二进制方式读取
        上传文件格式
        """
        files_data = {"file": (filename, open(filepath, mode="rb"), filetype)}  # 如果需要编码转码, 可以在括号里加上encoding="utf8"
        return files_data

    @classmethod  # 写入 单组数据
    def yaml_open(self, filepath=None, data=None):
        with open(filepath, encoding="utf-8", mode='w') as f:
            yaml.dump(data, stream=f, allow_unicode=True)

    @classmethod  # 写入  多组数据
    def write_yaml(self, filepath=None, response=None):
        with open(filepath, encoding='utf-8', mode='w') as f:
            yaml.dump_all(documents=[response], stream=f, allow_unicode=True)  # 单组为dump 多组为dump_all

    @classmethod  # 清空
    def clear_yaml(self, filepath=None):
        with open(filepath, mode='w', encoding='utf-8') as f:
            f.truncate()  # 清空
            f.close()  # 关闭

    @classmethod  # 读取元组
    def read_yaml(self, filepath=None):
        with open(filepath, encoding='utf-8') as f:
            data = yaml.load_all(f.read(), Loader=yaml.FullLoader)  # 用load方法转字典
            return data

    @classmethod  # 读取列表
    def read_yaml_ful(self, filepath=None):
        with open(filepath, encoding='utf-8') as f:
            data = yaml.load(f.read(), Loader=yaml.FullLoader)
            return data
