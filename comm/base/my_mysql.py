#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: R.
# email: sy.mailbox@foxmail.com
import pymysql as pymysql


class TestMysql(object):
    def __init__(self, hostname, username, passwords, ab):
        self.myldb = pymysql.connect(host=hostname,user=username,password=passwords,database=ab,charset='utf-8')
        self.sqlc = self.myldb.cursor()
    def close_db(self):
        self.sqlc.close()

    def select_db(self):
        pass
