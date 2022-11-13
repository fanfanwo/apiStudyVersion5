# -*- coding: utf-8 -*-
# author: 华测-长风老师

from version4.extract_token.Package.Request import Request


def test06(data_token):
    """多接口测试tooken"""
    r = Request()  # 实例化对象
    b = 1
    for i in data_token:
        r.run(**i["request"])  # 请求
        print(b)
        if i.get("extract_data", False):  # i.get(value1,value2); i["value1"]
            r.argument(**i["extract_data"])  # 提取数据
        if i.get("assert_business", False):
            r.assert_business(i["assert_business"])  # 断言业务正确性
        if i.get("assert_sql"):
            r.assert_sql(i["assert_sql"])  # 断言数据正确性
        b = b + 1
    # print(r.json)
