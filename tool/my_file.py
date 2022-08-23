#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: R.
# email: sy.mailbox@foxmail.com
from pathlib import Path
import yaml


class TestRedaFile(object):
    path_obtain = str(Path(__file__).parent.parent) + '/'

    @classmethod
    def read_yaml(cls, path):
        path = cls.path_obtain + path
        file = open(path, 'r', encoding='utf-8')
        with file as f:
            value = yaml.load(stream=f, Loader=yaml.Loader)
            return value


if __name__ == '__main__':
    # 读取配置文件里面的数据
    print(TestRedaFile.read_yaml('config/environment.yaml'))
