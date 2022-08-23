#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: R.
# email: sy.mailbox@foxmail.com
from realization.log.logger.my_log import logger


class TestTime(object):
    @classmethod
    def elapsed_total_response_time(cls, __elapsed__=None):  # 接口响应时间封装
        """
        __elapsed__ 自定义取名:可以为空None
        total_seconds 总时长，单位秒
        """
        try:
            root = __elapsed__.elapsed.total_seconds()
            logger.info(f"响应时间:{root}", stack_info=False)
            return root
        except:
            logger.error("-----接口未响应,请检查!-----", exc_info=True)
            raise
