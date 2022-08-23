#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: R.
# email: sy.mailbox@foxmail.com
"""
系统名称:产品运营系统
界面名称:修图分类管理
菜单位置:产品运营系统>工具配置>修图模块>修图分类管理
"""
from realization.lib.library import TestLibrary


class TestRevision(TestLibrary):
    @classmethod
    def setup(cls):
        cls.Dependent_function = globals()

    @property  # 增加接口
    def urls_add_Revision(self):
        urls_add_Revision = "/img/type/handle"
        return urls_add_Revision

    @property  # 增加接口
    def data_add_Revision(self):
        data_add_Revision = {"handle": "add",  # 操作-add/del/edit(必填)
                             'createTime': "",  # 创建时间
                             "id": "",  # 资源id
                             "modifyTime": "",  # 修改时间
                             "modifyUser": "",  # 操作用户
                             "oldTypeSort": "",  # 旧的排序
                             "status": "1",  # 启用1 不启用0
                             "type": self.str_rands(),  # 名称(必填)
                             "typeSort": self.generate_code()}  # 排序(必填)
        return data_add_Revision

    @property  # 修改接口
    def urls_Revision_update(self):
        urls_edit_Revision = "/img/type/handle"
        return urls_edit_Revision

    @property  # 修改接口
    def data_Revision_update(self):
        data_edit_Revision = {"handle": "edit",  # 操作-add/del/edit(必填)
                              "id": self.Dependent_function['ids'],  # 资源id
                              "status": "1",  # 启用1 不启用0
                              "type": self.str_rands(),  # 名称(必填)
                              "typeSort": self.generate_code()}  # 排序(必填)
        return data_edit_Revision

    @property  # 删除接口
    def url_revision_delete(self):
        urls_del_Revision = "/img/type/handle"
        return urls_del_Revision

    @property  # 删除接口
    def data_revision_delete(self):
        data_del_Revision = {"handle": "del",  # 操作-add/del/edit(必填)
                             "id": self.Dependent_function["ids"]}  # 资源id
        return data_del_Revision

    @property  # 查询接口
    def url_revision_select(self):
        urls_select_Revision = "/img/type/selectImgTypeList"
        return urls_select_Revision

    @property  # 查询接口
    def data_revision_select(self):
        data_select_Revision = {"createTime": "",  # 创建时间
                                "id": "2",  # 资源id
                                "limit": "",  # 条数
                                "modifyTime": "",  # 修改时间
                                "modifyUser": "",  # 操作人
                                "oldTypeSort": "",  # 旧的排序
                                "start": "",  # 页码
                                "status": "1",  # 启用状态 1：启用 0：不启用
                                "type": "",  # 名称
                                "typeSort": ""  # 排序
                                }
        return data_select_Revision
