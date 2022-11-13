# -*- coding: utf-8 -*-
# author: 华测-长风老师

from version4.extract_cookies.Package.Request import Request

def test05(data_cookies):
    """多接口测试cookies"""
    r = Request() #实例化对象
    for i in data_cookies:
        r.run(**i["request"]).extract_cookie().add_cookie()
        # print(r.json)
        if i.get("extract_data",False):
            r.argument(**i["extract_data"])
        if i.get("assert_business",False):
            r.assert_business(i["assert_business"])
        if i.get("assert_sql"):
            r.assert_sql(i["assert_sql"])
        print(r.json)
