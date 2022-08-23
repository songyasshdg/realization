#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: R.
# email: 484002966@qq.com
from urllib import response

from jsonpath import jsonpath

book_dict = {
    "store": {
        "book": [
            {"category": "reference",
             "author": "Nigel Rees",
             "title": "Sayings of the Century",
             "price": 8.95
             }
            # {"category": "fiction",
            #  "author": "Evelyn Waugh",
            #  "title": "Sword of Honour",
            #  "price": 12.99
            #  },
            # {"category": "fiction",
            #  "author": "Herman Melville",
            #  "title": "Moby Dick",
            #  "isbn": "0-553-21311-3",
            #  "price": 8.99
            #  },
            # {"category": "fiction",
            #  "author": "J. R. R. Tolkien",
            #  "title": "The Lord of the Rings",
            #  "isbn": "0-395-19395-8",
            #  "price": 22.99
            #  }
        ],
        "bicycle": {
            "color": "red",
            "price": 19.95
        }
    }
}
d = {"ret": 1, "msg": "操作成功"}
# store.book下所有的author值
# print(jsonpath(book_dict, '$.store.book[*].author'))

# # # 所有author的值
# print(jsonpath(d, '$.*'))
#
# import jsonpath
#
#
# def test_authors():
#     author_list = jsonpath.jsonpath(d, '$.*')
#     asserts author_list == ["1", '操作成功']
#     print(author_list)
















