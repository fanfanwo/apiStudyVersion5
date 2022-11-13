# -*- coding: utf-8 -*-
import jsonpath
from requests import request
from ..package.database import Sql
from string import Template


class Argument:
    """存储提取的参数数据"""


class Request:

    def __init__(self):
        self.r = request
        self.d = None
        self.respond = None

    def run(self, **kwargs):
        self.d = kwargs
        self.respond = self.r(**self.d)  # respond = request(**self.kwargs)
        return self

    @property  # 将一个类方法 变更为一个；类属性的调用方式
    def json(self):
        return self.respond.json()  # respond.json()

    def argument(self, **kwargs):
        for k, v in kwargs.items():
            # print(f"k为：{k} , v为：{v}")
            # print(f"self.json:{self.json}")
            data = jsonpath.jsonpath(self.json,v)  # jsonpath.jsonpath(self.respond.json(),v) #从respond.json()中提取字段$.data.id 和$.data.username的值 放到Agrgument类中
            setattr(Argument, k, data[0])  # k为id  和 username
        return self

    '''
    "assert_business"={"$.code": 0, "$.msg": "登录成功",
                      "$.data.username": "test_fcy"}
    '''

    def assert_business(self, assert_data):
        for k, v in assert_data.items():
            data = jsonpath.jsonpath(self.json, k)  # $.msg $.data.username
            assert data[0] == v, f"业务断言失败，实际拿到的数据为：{data[0]}，预期的数据是：{v}"
        print("业务断言成功")
        return self
    '''
    "assert_sql"={"dql": "select token from sxo_user where id=${id};",
                    "sql_jsonpath": "$.token",
                    "r_jsonpath": "$.data.token"}
    '''
    def assert_sql(self, assert_data):
        """
        :param assert_data: 数据断言数据
        :return:
        """
        dql = assert_data["dql"]  # 拿到sql查询语句 ="select token from sxo_user where id=${id};"
        dql = Template(dql).substitute(**self.__argument)  # 把查询语句的${id} 替换成**self.__argument
        # print(dql)
        data = Sql().execute(dql).fetchone()
        # print(data)
        expect_data = jsonpath.jsonpath(data, assert_data["sql_jsonpath"])[0]  # 得到数据库响应数据
        real_data = jsonpath.jsonpath(self.json, assert_data["r_jsonpath"])[0]
        assert expect_data == real_data, f"数据断言失败，实际拿到的数据是：{real_data},预期的数据是：{expect_data}"
        print("数据断言成功")


    @property
    def __argument(self):
        argument_dict = dict(Argument.__dict__)
        argument_dict.pop("__module__")
        argument_dict.pop("__doc__")
        argument_dict.pop("__dict__")
        argument_dict.pop("__weakref__")
        #函数属性只留下id、username == {'id': '94', 'username': 'test_changfeng'}
        print(argument_dict)
        return argument_dict

'''
if __name__ == '__main__':
    request_data = {
        "request": {
            "headers": {
                "content-type": "application/json"
            },
            "params": {
                "s": "api/user/login",
                "application": "app",
                "application_client_type": "weixin",
            },
            "json": {
                "accounts": "test_changfeng",
                "pwd": "changfeng",
                "type": "username"
            },
            "method": "post",
            "url": "http://shop-xo.hctestedu.com:80/index.php",
        },
        "assert_data":
            {
                "$.code": 0, "$.msg": "登录成功",
                "$.data.username": "test_changfeng"
            },
        "assert_sql":
            {
                "dql": "select token from sxo_user where id=${id};",
                "sql_jsonpath": "$.token",
                "r_jsonpath": "$.data.token"
            }
    }
    Request().run(**request_data["request"]).argument(id="$.data.id", username="$.data.username").assert_business(
        request_data["assert_data"]).assert_sql(request_data["assert_sql"])

    # print(Argument.id)
    # print(Argument.username)
    #
    # print(Argument.__dict__)
'''