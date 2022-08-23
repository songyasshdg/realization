# -*- coding: utf-8 -*-
import requests


def push_report(web_hook):
    header = {
        "Content-Type": "application/json;charset=UTF-8"
    }
    message_body = {
        "msg_type": "text",
        "content": {
            "text": "消息推送展示项目：飞书\n" +
                    ">>环境：测试环境 \n" +
                    ">>类型：%s \n" % "消息推送" +
                    ">>测试结果：%s \n" % "通过"
        }

    }

    ChatRob = requests.post(url=web_hook, json=message_body, headers=header)
    opener = ChatRob.json()
    print("opener:{}".format(opener))
    if opener["StatusMessage"] == "success":
        print(u"%s 通知消息发送成功！" % opener)
    else:
        print(u"通知消息发送失败，原因：{}".format(opener))


if __name__ == '__main__':
    # webhook 来自于 获取机器人webhook：复制webhook 中的那个值
    webhook = "https://open.feishu.cn/open-R/bot/v2/hook/5e8a4d55-139e-4f15-b50a-cb60b36a4f23"
    push_report(webhook)
