# -*- coding: utf-8 -*-
from version4.extract_token.Package.Request import Request


def execute(data):
    r = Request()  # 实例化对象
    for i in data:
        r.run(**i["request"])  # 发送请求
        if i.get("cookies", False):
            r.extract_cookie().add_cookie()
        if i.get("extract_data", False):  # 如果需要提取则提取数据
            r.argument(**i["extract_data"])  # 提取数据
        if i.get("assert_business", False):
            r.assert_business(i["assert_business"])  # 断言业务正确性
        if i.get("assert_sql"):
            r.assert_sql(i["assert_sql"])  # 断言数据正确性
