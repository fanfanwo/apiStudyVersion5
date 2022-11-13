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
def test01(method_url,params,headers,username,password,assert_data):

    json = {
        "accounts": username,
        "pwd": password,
        "type": "username"
    }
    '''
    实现请求业务
    '''
    r = request(params=params, headers=headers, json=json,**method_url)
    print("r",r.json()) #调试 -->提取测试业务所需数据

    '''
    断言-->业务断言
    '''


    '''
    jsonpath是提取json格式里面的数据，类似于jmeter里的json 提取器
     $.code 即是jsonpath的提取方式
     a={
     "code":0
     }
     $.code -->jsonpath 提取方式
     jsonpath.jsonpath(a,"$.code") -->包含提取值的列表，所以需要给下标
    '''

    for k,v in assert_data.items():
        data = jsonpath.jsonpath(r.json(),k)[0]
        assert data == v,f'业务断言失败，实际拿到的数据分别为：{data},预期的值为{v}'
    print("业务断言成功")

    '''
    断言---> 数据断言
    '''


    '''
    连接数据库
    '''
    # db = pymysql.connect(host="shop-xo.hctestedu.com",
    #                      port=3306,
    #                      user="api_test",
    #                      password="Aa9999!",
    #                      database="shopxo_hctested", )
    # #访问数据库的对象， 构建游标cursor实例
    # cursor = db.cursor(pymysql.cursors.DictCursor)
    #传递数据的查询语句
    uid = r.json()["data"]["id"]
    # cursor.execute(f"select token from sxo_user where id ={uid};")
    data = Sql().execute(f"select token from sxo_user where id ={uid};").fetchone()
    # data = cursor.fetchone() #查看游标的执行结果,返回第一条数据，元组类型
    print("token:",data)
    assert data["token"]==r.json()["data"]["token"],f'数据断言失败，实际拿到的结果为:{r.json()["data"]["token"]},预期为：{data["token"]}'
    print("数据断言成功")