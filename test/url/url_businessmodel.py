#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: R.
# email: sy.mailbox@foxmail.com
"""
系统名称:产品运营系统
界面名称:业务模式配置页面
菜单位置:产品运营系统>产品管理>应用管理>业务模式配置
"""


class TestBusiness(object):  # 注意这里的开发必须以Test, 不然代码执行不了;

    @classmethod
    def setup(cls):
        cls.Dependent_function = globals()

    @property  # 增加
    def url_Business_model_add(self):
        urls_Business_model_add = "/operate/busModelConfig/insertDnBusModelConfig"
        return urls_Business_model_add

    @property  # 增加
    def function_data_add(self):
        data_Business_model_add = {"busModel": "ri",  # 业务模式(必填)
                                   "description": "",  # 备注
                                   "status": "1"  # 状态打开1 或关闭0
                                   }
        return data_Business_model_add

    @property  # 修改
    def url_Business_model_update(self):
        urls_Business_model_update = "/operate/busModelConfig/updateDnBusModelConfigById"
        return urls_Business_model_update

    @property  # 修改
    def function_data_update(self):
        data_Business_model_update = {"busModel": self.Dependent_function['ids'],  # 业务模式 #这里的参数依赖是因为不能固定,所以就使用一样的id就命名
                                      "description": "sopppp",  # 备注
                                      "id": self.Dependent_function['ids'],  # 主键
                                      "status": "1"  # 状态 打开1 关闭0
                                      }
        return data_Business_model_update

    @property  # 删除
    def urls_Business_model_delete(self):
        urls_Business_model_delete = "/operate/busModelConfig/deleteDnBusModelConfigById"
        return urls_Business_model_delete

    @property  # 删除
    def function_data_delete(self):
        data_Business_model_delete = {"idList": self.Dependent_function['ids'],  # idList(必填)
                                      }
        return data_Business_model_delete

    @property  # 查询
    def urls_Business_model_select(self):
        urls_Business_model_select = "/operate/busModelConfig/selectDnBusModelConfigByCondition"
        return urls_Business_model_select

    @property  # 查询
    def function_data_select(self):
        data_Business_model_select = {"limit": "50",  # 一页的数量(必填)
                                      "start": "1",  # 第几页(必填)
                                      "busModel": "",  # 业务模式
                                      "status": "",  # 状态 打开1 关闭0
                                      }
        return data_Business_model_select

    @property  # 导出
    def urls_Business_model_exit(self):
        urls_Business_model_exit = "/operate/busModelConfig/export"
        return urls_Business_model_exit

    @property  # 导出
    def function_data_exit(self):
        data_Business_model_exit = {"busModel": "",  # 业务模式
                                    "export_file_name": "",  # 备注
                                    "status": "1",  # 状态
                                    "value": "id,ID;busModel,业务模式;description,备注;status,状态;updateUser,编辑账号;updateTime,"
                                             "编辑时间;createUser,创建账号;createTime,创建时间",  # value(注意格式!!!!)
                                    }
        return data_Business_model_exit

    @property  # 查询--获取业务配置列表
    def urls_Business_model_selects(self):
        urls_Business_model_selects = "/operate/busModelConfig/getModelList"
        return urls_Business_model_selects

    @property  # 查询--获取业务配置列表
    def data_Business_model_selects(self):
        return False  # 传token即可
