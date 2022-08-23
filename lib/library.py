#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: R.
# email: sy.mailbox@foxmail.com
import random
import string
from datetime import timedelta, date
from realization.log.logger.my_log import logger


class TestLibrary(object):
    @classmethod
    # 自动生成手机号
    def generate_mobile(self):
        tel = random.choice(['134', '139', '135', '150', '151', '157', '130', '132', '133', '153'])
        list1 = []
        for i in range(8):
            list1.append(random.choice('0123456789'))
        part = ''.join(list1)
        mobile = tel + part
        logger.info(f"生成随机11手机号:{mobile}")
        return mobile  # 11位

    @classmethod
    # 自动生成验证码
    def generate_code(self):
        tel = random.choice(['1', '3', '0', '8', '5', '6', '9', '7', '2', '4'])
        list1 = []
        for i in range(3):
            list1.append(random.choice('78915401236'))
        part = ''.join(list1)
        mobile = tel + part
        logger.info(f"生成随机4位验证码:{mobile}")
        return mobile  # 4位

    @classmethod
    def code_int(self):
        tel = random.choice(['1', '3', '0', '8', '5', '6', '9', '7', '2', '4'])
        list1 = []
        for i in range(5):
            list1.append(random.choice('78915401236'))
        part = ''.join(list1)
        mobile = tel + part
        logger.info(f"生成随机3-4位数字;{mobile}")
        return mobile  # 3到4位

    @classmethod
    def str_rands(self):
        name = ["汤", "唐", "小", "元", "明", "清", "帼", "固", "逗", "伊", "越泽", "天佑", "雨泽", "哲瀚", "志泽", "修洁", "修涯", "无根",
                "无名"]  # 可多加
        int_list = ["二", "王", "大", "智", "聪", "强", "耳", "阿", "女", "无", "鹏涛", "峻熙", "弘文", "弘文", "炎彬", "煜城"]  # 可多加
        random.shuffle(int_list)
        font_string = ''
        for i in range(0, random.randint(1, 2)):  # 从0开始
            font_string += random.choice(int_list)
        names = random.choice(name) + font_string
        logger.info(f"生成随机2-3位名字;{names}")
        return names  # 生成名字2-3位

    @classmethod
    def password_random(cls, numLength=5, stringLength=3):
        strs = ""
        letters = string.ascii_letters
        digits = string.digits
        for i in range(stringLength):
            strs += letters[random.randint(0, len(letters) - 1)]
        for i in range(numLength):
            strs += digits[random.randint(0, len(digits) - 1)]
        str_in = list(strs)
        random.shuffle(str_in)
        logger.info(f"随机生成大写+小写+数字8位密码;{''.join(str_in)}")
        return ''.join(str_in)  # 生成随机大写+小写+数字密码(8位)

    @classmethod
    def generate_number_name(self, change_num="0001"):
        """
        @param change_num: 传入数字"0001",自动填充为4位
        @return: 返回中文"零零零一"
        """
        change_num = f"{change_num:0>4}"
        old_list, new_list = list(change_num), []
        str_num, str_chinese = "0123456789", "零一二三四五六七八九"
        for i in old_list:
            new_list.append(str_chinese[eval(i)])
        # new_str = "李" + "".join(new_list)
        new_str = "".join(new_list)
        # print(new_str)
        return new_str

    @classmethod
    # 生成18位身份证号码，测试过程中发现1000次有87次无法通过校验，老脚本舍弃
    def generate_id(self):
        """
        1.随机生成身份证号,现行身份证号为18位
        2.组成部分为6位地址码，8位生日，3位顺序码（最后一位奇数为男，偶数为女），
        3.一位校验码，并作为返回值
        """
        area_id = str(510000)
        year = str(random.randint(1990, 1999))
        # 生成月份日期 方法为当前日期+随机时间
        da = date.today() + timedelta(days=random.randint(1, 366))  # 月份和日期项
        da = da.strftime('%m%d')
        code = str(random.randrange(100, 999, 2))  # 生成顺序码，女性
        id = area_id + year + da + code  # 除最后一位的身份证
        # 生成校验码
        count = 0
        weight = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]  # 权重项
        checkcode = {'0': '1', '1': '0', '2': 'X', '3': '9', '4': '8', '5': '7', '6': '6', '7': '5', '8': '5', '9': '3',
                     '10': '2'}  # 校验码映射
        for i in range(0, len(id)):
            count = count + int(id[i]) * weight[i]
        check = checkcode[str(count % 11)]  # 算出校验码
        ids = id + check  # 组合生成身份证号
        logger.info(f"随机生成身份证:{ids}")
        return ids

    @staticmethod
    def random_phone_num():
        """随机一个电话号码"""
        num_start = ['134', '135', '136', '137', '138',
                     '139', '150', '151', '152', '158',
                     '159', '157', '182', '187', '188',
                     '147', '130', '131', '132', '155',
                     '156', '185', '186', '133', '153',
                     '180', '189']
        start = random.choice(num_start)
        end = ''.join(random.sample(string.digits, 8))
        phone_number = start + end
        logger.info('生成的随机手机号码：{}'.format(phone_number))
        return phone_number

    @classmethod
    def create_string_number(cls, n):  # n可以自定义生成指定多少位数
        """生成一串指定位数的字符+数组混合的字符串"""  # 有大写,小写,数字(9位)
        m = random.randint(1, n)
        a = "".join([str(random.randint(0, 9)) for _ in range(m)])
        b = "".join([random.choice(string.ascii_letters) for _ in range(n - m)])
        ls = ''.join(random.sample(list(a + b), n))
        return ls

    @classmethod
    def create_random_string(cls):  # 生成一个大小写字母
        """随机生成一个大写或小写的英文字母"""
        ls = random.choice(string.ascii_letters)
        return ls

    @classmethod
    def create_random_0_1_number(cls):
        """随机返回一个0-1之间的浮点数"""
        ls = random.random()
        return ls

    @classmethod
    def create_random_float_number(cls):
        """随机返回从0-9999之间的浮点数"""
        ls = random.uniform(0, 9999)
        return ls

    @classmethod
    def create_random_int_number(cls):
        """随机返回从0-9之间的整数"""
        ls = random.randint(0, 10000)  # 可以自定义填里面的值比如 0,10/0,1000/0,999
        return ls
        # 也可以根据续修返回其他长度的数字，这里我返回1000-9999中的任意一个数字
        # return random.randint(1000, 9999)

    @classmethod
    def captcha(cls, n=10):  # n决定生成位数,如果n=5,那么生成的就是5位, 也可以其他,可以自定义
        ascii_str = string.ascii_letters  # 获取大小写字母串
        ascii_int = string.digits  # 获取数字串
        code_list = random.sample(ascii_int + ascii_str, n)  # 随机取字符
        ls = ''.join(code_list)  # 列表转为字符串
        return ls
