import json

import jsonpath
from requests import request
# from version4.Package import database
from version4.extract_cookies.Package.database import Sql
from string import Template


class Argument:
    """存储提取的参数数据"""


class Request:

    def __init__(self):
        self.r = request
        self.d = {}  # 接收所有的请求数据
        self.respond = None  # 接收所有的响应数据

    def run(self, **kwargs):
        self.d.update(kwargs)  # 参数的传递，例如cookie、token
        # print(f"d:{self.d}")
        self.respond = self.r(**self.d)
        # print(f"self.respond: {self.respond}")
        return self

    def extract_cookie(self):
        """提取cookie"""
        setattr(Argument, "cookies", self.respond.cookies)
        get = getattr(Argument,"cookies")
        print(f"get_cookies:{get}")
        return self

    def add_cookie(self):
        """请求数据中添加cookies"""
        self.d = {"cookies": self.__argument["cookies"]}
        print(f"self.d:{self.d}")


    @property  # 将一个类方法 变更为一个类属性
    def json(self):
        """将响应数据转为json格式"""
        return self.respond.json()

    def argument(self, **kwargs):
        """提取数据"""
        for k, v in kwargs.items():
            data = jsonpath.jsonpath(self.json, v)
            print(f"data[0]:{data[0]}")
            setattr(Argument, k, data[0])
        return self

    def assert_business(self, assert_data):
        for k, v in assert_data.items():
            data = jsonpath.jsonpath(self.json, k)

            assert data[0] == v, f"业务断言失败，实际拿到的数据：{data[0]},预期的数据是：{v}"
        print(f"业务断言成功")
        return self

    def assert_sql(self, assert_data):
        """
        这块处理 没搞懂
        assert_sql:{
        "sql_jsonpath":"$.token",
         "r_jsonpath":"$.data.token"
         }
        :param assert_data:  数据断言
        :return:
        """
        dql = assert_data["dql"]  # 拿到sql 查询语句
        dql = Template(dql).substitute(**self.__argument)  # 将查询语句中的$id替换成 __argument中id的值
        data = Sql().execute(dql).fetchone()  # 执行数据库语句，得到查询结果 token
        expect_data = jsonpath.jsonpath(data, assert_data["sql_jsonpath"])[0]  # 从data中 提取token
        expect_value = jsonpath.jsonpath(self.json, assert_data["r_jsonpath"])[0]  # 从r.json()中提取token
        assert expect_data == expect_value, f"数据断言失败，实际拿到的是：{data}，预期值是：{expect_value}"
        print("数据断言成功")

    @property
    def __argument(self):
        argument_dict = dict(Argument.__dict__)
        argument_dict.pop("__module__")
        argument_dict.pop("__doc__")
        argument_dict.pop("__dict__")
        argument_dict.pop("__weakref__")
        print(f"argument_dict:{argument_dict}")
        return argument_dict
# if __name__ == '__main__':
#     request_data = {
#         "request": {
#             "headers": {
#                 "content-type": "application/json"
#             },
#             "params": {
#                 "s": "api/user/login",
#                 "application": "app",
#                 "application_client_type": "weixin",
#             },
#             "json": {
#                 "accounts": "test_changfeng",
#                 "pwd": "changfeng",
#                 "type": "username"
#             },
#             "method": "post",
#             "url": "http://shop-xo.hctestedu.com:80/index.php",
#         },
#         "assert_data":
#             {
#                 "$.code": 0, "$.msg": "登录成功",
#                 "$.data.username": "test_changfeng"
#             }
#     }
#     Request().run(**request_data["request"]).argument(id="$.data.id", username="$.data.username").assert_business(
#         request_data["assert_data"])
#
#     print(Argument.id)
#     print(Argument.username)
#
#     print(Argument.__dict__)