#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: R.
# email: sy.mailbox@foxmail.com
import os
import yaml


class YamlUsage(object):
    def __init__(self, filepath):
        self.filepath = filepath

    def write_yaml(self, filename, mode):
        self.__check()
        file = open(self.filepath, mode, encoding='utf-8')
        yaml.dump(filename, file, Dumper=yaml.Dumper)

    def rend_yaml(self):
        self.__check()
        file = open(self.filepath, mode='r', encoding='utf-8')
        with file as f:
            com = yaml.load(f, Loader=yaml.Loader)
            return com

    def __check(self):
        if os.path.exists(self.filepath):
            pass
        else:
            files = open(self.filepath, 'w')
            files.truncate()
            files.close()


if __name__ == '__main__':
    yam = YamlUsage("./a.yaml")
    data1 = {"1": "3",
             "2": "2",
             "3": "8"

             }
    data = [data1]
    yam.write_yaml(filename=data, mode='a')
    print(yam.rend_yaml())


