#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: R.
# email: sy.mailbox@foxmail.com

# coding=utf-8
import os
from selenium import webdriver
import datetime
import time
from os import path
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# 此处chromedriver改为自己下载解压的chromedriver的路径
s = Service('C:/Users/wzyh/AppData/Local/Google/Chrome/Application/chromedriver')
driver = webdriver.Chrome(service=s)


# driver.maximize_window()

def login():
    # 打开淘宝首页，扫码登陆淘宝
    driver.get("https://www.taobao.com")
    time.sleep(3)
    if driver.find_element(by=By.LINK_TEXT, value='亲，请登录'):
        driver.find_element(by=By.LINK_TEXT, value='亲，请登录').click()
        print("请在30秒内完成扫码登录...")
        time.sleep(30)
        # 打开购物车列表首页
        driver.get("https://cart.taobao.com/cart.htm")
        time.sleep(3)
        # 全选购物车
    if driver.find_element(by=By.ID, value='J_SelectAll1'):
        driver.find_element(by=By.ID, value='J_SelectAll1').click()
    now = datetime.datetime.now()
    print("login success:", now.strftime("%Y-%m-%d %H:%M:%S"))


def buy(times):
    while True:
        # 记录当前时间，使用datatime内置模块
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(times)
        print(now)
        # 对比时间，时间到的话就点击结算
        if now == times:
            try:
                if driver.find_element(by=By.ID, value='J_Go'):
                    driver.find_element(by=By.ID, value='J_Go').click()
                    driver.find_element(by=By.LINK_TEXT, value='提交订单').click()
                    print('抢购成功，请尽快付款')
            except:
                print('请再次尝试提交订单')
        print(now)
        time.sleep(0.1)


if __name__ == "__main__":
    times = input("请输入抢购时间(例如格式：2022-08-11 12:00:00):")
    login()
    buy(times)
