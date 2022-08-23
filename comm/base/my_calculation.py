#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: R.
# email: sy.mailbox@foxmail.com
import random
import string
from datetime import timedelta, date
from product.log.logger.my_log import logger


class TestAluLaTion(object):
    @classmethod
    def mobiles(self):
        tel = random.choice(['134', '139', '137', '135', '150', '151', '157', '130', '132', '133', '153'])
        list1 = []
        for i in range(8):
            list1.append(random.choice('0123456789'))
        part = ''.join(list1)
        mobile = tel + part
        with open(r"C:\PycharmProjects\R\Common\yaml\test_Business_model.yaml", "a") as f:
            f.seek(0)  # 从0位置开始读取
            f.truncate()
            f.write(mobile)
            return mobile

    @classmethod
    def read_mbiles(self):
        f = open(r"C:\PycharmProjects\R\Common\yaml\test_Business_model.yaml")
        data = f.readlines()  # 按行读取list
        f.close()  # 关闭
        return data

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

    # 校验身份证最后一位是否正确
    @classmethod
    def check_last_idnum(self, id=None):
        """
        @param id: 传入18位身份证号码
        @return: 返回通过校验True/False
        """
        lis = list(id)
        ten = ['X', 'x', 'Ⅹ']
        ID = ["10" if i in ten else i for i in lis]  # 将罗马数字Ⅹ和字母X替换为10
        W = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
        Checkcode = [1, 0, 'X', 9, 8, 7, 6, 5, 4, 3, 2]
        sum = 0
        for i in range(17):
            sum = sum + int(ID[i]) * W[i]
        if Checkcode[sum % 11] == int(ID[17]):
            print('输入正确')
            return True
        else:
            print('输入错误')
            return False

    @classmethod
    # 生成18位身份证号码，测试过程中发现1000次有87次无法通过校验，老脚本舍弃
    def generate_old_id(self):
        '''
        1.随机生成身份证号,现行身份证号为18位
        2.组成部分为6位地址码，8位生日，3位顺序码（最后一位奇数为男，偶数为女），
        3.一位校验码，并作为返回值
        '''
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
        id = id + check  # 组合生成身份证号
        return id

    @classmethod
    # 自动生成手机号
    def generate_mobile(self):
        tel = random.choice(['134', '139', '135', '150', '151', '157', '130', '132', '133', '153'])
        list1 = []
        for i in range(8):
            list1.append(random.choice('0123456789'))
        part = ''.join(list1)
        mobile = tel + part
        return mobile

    @classmethod
    def rands(self):
        name = ["12", "23", "45", "78", "45", "22"]  # 可多加
        int_list = ["1", "5", "8", "6", "9", "4"]  # 可多加
        random.shuffle(int_list)
        font_string = ''
        for i in range(0, random.randint(1, 3)):  # 从0开始
            font_string += random.choice(int_list)
        names = random.choice(name)
        return names + font_string

    @classmethod
    # 写入文本，注意修改路径
    def write_fourinfomation_txt(self, filename, user_info, mode="a+"):
        filepath = "D:\\Mytest\\Python3\\Python3\\"
        # 写入新文件（如果没有文件后缀.txt，默认文本文件）
        with open(filepath + f'{filename}', mode=mode, encoding="utf8") as wfile:
            wfile.write(user_info)
            wfile.write("\n")
            wfile.seek(0, 0)
            new = wfile.read()
            print(str(new))

    @classmethod
    # 老脚本（生成银行卡，无法通过银行校验）
    def generate_oldbank_id(self):
        """随机生成建行银行卡，并作为返回值"""
        head = '621284'
        list1 = []
        for i in range(11):
            list1.append(random.choice('0123456'))
        part = ''.join(list1)
        end = '10'
        code = head + part + end
        return code

    @classmethod
    def rand(self):
        name = ["任", "李", "张", "宋", "奥", "是"]  # 可多加
        str_list = ["爱", "婷", "聪", "亚", "二", "王"]  # 可多加
        random.shuffle(str_list)
        font_string = ''
        for i in range(0, random.randint(1, 3)):  # 从0开始
            font_string += random.choice(str_list)
        names = random.choice(name)
        return names + font_string

    @classmethod  # 生成8位必含数字、大小写字母的字符串（密码）
    def new_password_rand(cls):
        src_digits = string.digits  # string_数字
        src_uppercase = string.ascii_uppercase  # string_大写字母
        src_lowercase = string.ascii_lowercase  # string_小写字母
        count = 1
        for i in range(count):  # 随机生成数字、大写字母、小写字母的组成个数（可根据实际需要进行更改）
            digits_num = random.randint(1, 6)
            uppercase_num = random.randint(1, 8 - digits_num - 1)
            lowercase_num = 8 - (digits_num + uppercase_num)
            password = random.sample(src_digits, digits_num) + random.sample(src_uppercase,
                                                                             uppercase_num) + random.sample(
                src_lowercase, lowercase_num)  # 生成字符串
            random.shuffle(password)  # 打乱字符串
            new_password = ''.join(password)  # 列表转字符串
            return new_password

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
    def random_str(cls, numLength=4, stringLength=6):
        strs = ""
        letters = string.ascii_letters
        digits = string.digits
        for i in range(stringLength):
            strs += letters[random.randint(0, len(letters) - 1)]
        for i in range(numLength):
            strs += digits[random.randint(0, len(digits) - 1)]
        str_in = list(strs)
        random.shuffle(str_in)
        return ''.join(str_in)

    @classmethod  # 生成8位必含数字、大小写字母的字符串（密码）
    def password_rand(cls):
        random.seed(0x1010)
        s = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*"
        ls = []  # 存取密码的列表
        FirstPsw = ""  # 存取第一个密码的字符
        while len(ls) < 50:  # 50个随机密码
            pwd = ""
            for i in range(10):
                pwd += s[random.randint(0, len(s)) - 1]
            if pwd[0] in FirstPsw:
                continue
            else:
                ls.append(pwd)
                FirstPsw += pwd[0]
            f = open("./随密码.txt", "w", encoding="utf-8")
            f.truncate()
            f.write("\n".join(ls))
            f.close()
