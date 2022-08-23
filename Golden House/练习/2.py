# import requests
# # from requests_toolbelt import MultipartEncoder
#
#
# class SendMsg():
#     def __init__(self, app_id, app_secret, web_hook_url):
#         self.app_id = app_id  # 发送图片时需要
#         self.app_secret = app_secret  # 发送图片时需要
#         self.web_hook_url = web_hook_url  # 机器人web_hook地址
#
#     # 获取token为上传图片时使用
#     def get_tenant_access_token(self):
#         url = "https://open.feishu.cn/open-R/auth/v3/tenant_access_token/internal"
#         body = {
#             "app_id": self.app_id,
#             "app_secret": self.app_secret
#         }
#         r = requests.request(method='post', url=url, json=body)
#         print(r.json())
#         return r.json()['tenant_access_token']
#
#     # 上传图片生成image id
#     def uploadImage(self, image_rb):
#         tenant_access_token = self.get_tenant_access_token()
#         url = "https://open.feishu.cn/open-R/im/v1/images"
#         form = {'image_type': 'message',
#                 'image': image_rb}  # image_rb:是以rb格式读的图片内容，也可以是ui自动截的图，直接传过来
#         multi_form = MultipartEncoder(form)
#         headers = {'Authorization': 'Bearer {}'.format(tenant_access_token), 'Content-Type': multi_form.content_type}
#         response = requests.request("POST", url, headers=headers, data=multi_form)
#         # print(response.headers['X-Tt-Logid'])  # for debug or oncall
#         print(response.json())  # Print Response
#         return response.json()['data']['image_key']
#
#     def send_post(self, title, content):
#         """
#         title: 发送消息的标题
#         content: 使用富文本格式:https://open.feishu.cn/document/uAjLw4CM/ukTMukTMukTM/im-v1/message/create_json
#         """
#         body = {
#             "msg_type": "post",
#             "content": {
#                 "post": {
#                     "zh_cn": {
#                         "title": title,
#                         "content": content
#                     }
#                 }
#             }
#         }
#         r = requests.request(method='post', url=self.web_hook_url, json=body)
#         print(r.json())
# for letter in 'Python':
#    if letter == '':
#       continue
#    print('当前字母 :%s' %letter)
# row = 1
# while row <= 9:
#     col = 1
#     while col <= row:
#         print('%d * %d = %d\t' % (row, col, col * row), end='')
#         col += 1
#     print('')
#     row += 1
# import pytest
# import pytest_check as check
#
# #
# # def test_example():
# #     a = 1
# #     b = 2
# #     c = [2, 4, 6]
# #     check.greater(a, b)
# #     check.less_equal(b, a)
# #     check.is_in(a, c, "111")
# #     check.is_not_in(b, c, "222")
# #
# #
# # if __name__ == "__main__":
# #     pytest.main()
# import requests
# r = requests.get("https://blog.csdn.net/wuyoudeyuer", timeout=0.001)
# print(r.elapsed)
# print(r.elapsed.total_seconds())
# print(r.elapsed.microseconds)
# print(r.elapsed.seconds)
# print(r.elapsed.days)
# print(r.elapsed.max)
# print(r.elapsed.min)
# print(r.elapsed.resolution)
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: R.
# email: sy.mailbox@foxmail.com

"""
UI名称:业务模式配置
"""
import json

import allure
import pytest
from R.Common.Url_Base_Changping.url_Business_model import Business_model, TestBusiness_model_sss
from R.Common.my_Base_Changping.my_Base_Chanping import Test_Chan_ping
from R.Common.my_Base_Changping.my_assart_info_Changping import TestCsmAAssertionLibrary
from R.Common.my_Base_Changping.my_jsonpath_Changping import jsonpathAssertionLibrary
from R.Common.my_Base_Changping.my_assart_info_Changping import TesterHekAse
from R.Common.my_Base_Changping.my_hamcrest_Changping import TesAsserThat
from R.Common.my_Base_Changping.my_Fileopen_Changping import Testfile
from R.loggins.my_logins import logger


@allure.epic("业务模式配置模块")  # 一个模块构建一个类
class TestBus(Test_Chan_ping, Testfile, Business_model, TestCsmAAssertionLibrary, TesAsserThat,
              TesterHekAse, jsonpathAssertionLibrary, TestBusiness_model_sss):

    def setup(self):  # 前置准备
        self.Dependent_function = globals()  # 全局依赖函数
        logger.info(
            '\n''==================================================接口自动化测试开始==========================================')

    def teardown(self):  # 后置退出
        logger.info(
            "\n""=================================================接口自动化测试结束===========================================")

    @allure.feature("业务模式配置-增加")
    @allure.title('增加-用例1-正向')
    @allure.description('接口地址:/operate/busModelConfig/insertDnBusModelConfig')
    # @pytest.mark.flaky(reruns=2, reruns_delay=2.5)  # 如果用例执行失败,则重跑两次,每次延迟2.5秒
    def test_001(self):
        urls = self.base_urls + self.urls_Business_model_add
        data_Business_model_add = {"busModel": "145..45445",  # 业务模式(必填)
                                   "description": "",  # 备注
                                   "status": "1"  # 状态打开1 或关闭0
                                   }
        r = self.request_tets(method='post', url=urls, data=data_Business_model_add, headers=self.headers_form_())
        self.str_id = str(r.json()['data'])
        self.Dependent_function['ids'] = self.str_id
        print(self.str_id)

    # @allure.feature("业务模式配置-修改")
    # @allure.title('修改-用例1-正向')
    # @allure.description('接口地址:/operate/busModelConfig/updateDnBusModelConfigById')
    # # @pytest.mark.flaky(reruns=2, reruns_delay=2.5)  # 如果用例执行失败,则重跑两次,每次延迟2.5秒
    # def test_002(self):
    #     urls = self.base_urls + self.urls_Business_model_update
    #     data_Business_model_update = {"busModel": self.glo['ids'],  # 业务模式
    #                                   "description": "songya21111",  # 备注
    #                                   "id": self.glo['ids'],  # 主键
    #                                   "status": "1"  # 状态 打开1 关闭0
    #                                   }
    #     r = self.request_tets(method='post', url=urls, data=data_Business_model_update, headers=self.headers_form_())

    def test_002(self):
        urls = self.base_urls + self.urls_Business_model_update
        r = self.request_tets(method='post', url=urls, data=self.data_Business_update(), headers=self.headers_form_())
        print(r.text)
    # @allure.feature("业务模式配置-查询")
    # @allure.title('查询-用例1-正向')
    # @allure.description('接口地址:/operate/busModelConfig/selectDnBusModelConfigByCondition')
    # # @pytest.mark.flaky(reruns=2, reruns_delay=2.5)  # 如果用例执行失败,则重跑两次,每次延迟2.5秒
    # def test_003(self):
    #     urls = self.base_urls + self.urls_Business_model_select
    #     r = self.request_tets(method='post', url=urls, data=self.data_Business_model_select,
    #                           headers=self.headers_form_())
    #     print(r.text)

    #
    # @allure.feature("业务模式配置-删除")
    # @allure.title('删除-用例1-正向')
    # @allure.description('接口地址:/operate/busModelConfig/deleteDnBusModelConfigById')
    # # @pytest.mark.flaky(reruns=2, reruns_delay=2.5)  # 如果用例执行失败,则重跑两次,每次延迟2.5秒
    # def test_004(self):
    #     urls = self.base_urls + self.urls_Business_model_delete
    #     r = self.request_tets(method='post', url=urls, data=self.data_Business_model_delete,
    #                           headers=self.headers_form_())
    #     print(r.text)
    #
    # @allure.feature("业务模式配置-获取业务配置列表")
    # @allure.title('获取业务配置列表-用例1-正向')
    # @allure.description('接口地址:/operate/busModelConfig/getModelList')
    # # @pytest.mark.flaky(reruns=2, reruns_delay=2.5)  # 如果用例执行失败,则重跑两次,每次延迟2.5秒
    # def test_005(self):
    #     urls = self.base_urls + self.urls_Business_model_selects
    #     r = self.request_tets(method='post', url=urls, headers=self.headers_form_())
    #     print(r.text)
    #
    # @allure.feature("业务模式配置-导出文件数据")
    # @allure.title('导出文件数据-用例1-正向')
    # @allure.description('接口地址:/operate/busModelConfig/export')
    # # @pytest.mark.flaky(reruns=2, reruns_delay=2.5)  # 如果用例执行失败,则重跑两次,每次延迟2.5秒
    # def test_006(self):
    #     urls = self.base_urls + self.urls_Business_model_exit
    #     r = self.request_tets(method='post', url=urls, data=self.data_Business_model_exit, headers=self.headers_form_())
    #     self.with_open(_r_=r.content, filepath="C:\\PycharmProjects\\R\\Test_Case\\File_api\\业务模式配置.xlsx")
    #     print(r.text)


if __name__ == '__main__':
    pytest.main(['-vs', 'test_Business_model.py'])
