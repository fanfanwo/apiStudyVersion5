# -*- coding: utf-8 -*-
'''
Requests: 构建接口测试的业务实现，--业务验证
pymysql：连接数据库 --数据验证
'''
# 业务实现：单接口测试
'''
登录接口的测试
'''
import pytest
from requests import request
import pymysql
import jsonpath
from ..package.database import Sql
'''
数据伪造 18-33行
'''
#{"$.code":0 } $.code代表 提取方式， 0代表预期的值
@pytest.mark.parametrize(["username","password","assert_data"],[
                         ["test_fcy","test_fcy",{"$.code":0,"$.msg":"登录成功","$.data.username":"test_fcy"}]])
def test02(method_url,params,headers,username,password,assert_data,assert_operator,assert_sql_data):

    json = {
        "accounts": username,
        "pwd": password,
        "type": "username"
    }
    """实现请求业务"""
    r = request(params=params, headers=headers, json=json,**method_url)
    # print("r",r.json()) #调试 -->提取测试业务所需数据

    '''
    jsonpath是提取json格式里面的数据，类似于jmeter里的json 提取器
     $.code 即是jsonpath的提取方式
     a={
     "code":0
     }
     $.code -->jsonpath 提取方式
     jsonpath.jsonpath(a,"$.code") -->包含提取值的列表，所以需要给下标
    '''
    """业务断言"""
    assert_operator(assert_data, r.json())

    """数据断言"""
    uid = r.json()["data"]["id"]
    assert_data = {
        "sql":f"select token from sxo_user where id ={uid};",
    }
    expect_data = jsonpath.jsonpath(r.json(),"$.data.token")[0]
    assert_sql_data(assert_data,expect_data)

