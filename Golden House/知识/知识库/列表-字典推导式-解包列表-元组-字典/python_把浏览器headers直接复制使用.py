#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: R.
# email: sy.mailbox@foxmail.com
from copyheaders import headers_raw_to_dict
x=b'''
{
    "hasThird":false,
    "thirdCarrierName":"",
    "thirdCarrierNo":true,
    "thirdPlatForm":null,
    "thirdContractNo":"",
    "thirdContractName":"",
    "shiftWaybillDTOList":[
        {
            "waybillId":xxx
        }
    ]
}
'''

r=headers_raw_to_dict(x)
print(r)
print(type(r))
