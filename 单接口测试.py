# -*- coding: utf-8 -*-
'''
Requests: 构建接口测试的业务实现，--业务验证
pymysql：连接数据库 --数据验证
'''
# 业务实现：单接口测试
'''
登录接口的测试
'''

from requests import request
'''
数据伪造 18-33行
'''
# methon和url是必要参数
# url=协议+域名+port+文件路径
# 还有个不定长参数params(字典或json格式类型--键值对的数据)--存放必要的参数
params = {
    "s": "api/user/login",
    "application": "app",
    "application_client_type": "weixin"
}
# 请求头  规定接受数据的类型content-type
headers = {
    "content-type": "application/json"
}
username = "test_fcy"
# 请求数据的内容json
json = {
    "accounts": username,
    "pwd": "test_fcy",
    "type": "username"
}
'''
实现请求业务
'''
r = request(method="post", url="http://shop-xo.hctestedu.com:80/index.php", params=params, headers=headers, json=json)
print(r.json()) #调试 -->提取测试业务所需数据

'''
断言-->业务断言
'''
#构建断言
# if r.json()["code"]==0 and r.json()["msg"]=='登录成功' and r.json()["data"]["username"]==username:
#     print("业务断言成功")
# else:
#     print(f'业务断言失败，是拿到的数据分别为：code --》{r.json()["code"]};msg-->{r.json()["msg"]};username-->{r.json()["data"]["usernname"]}')
#断言失败打印
assert r.json()["code"]==0 and r.json()["msg"]=='登录成功' and r.json()["data"]["username"]==username,\
    f'业务断言失败，是拿到的数据分别为：code --》{r.json()["code"]};msg-->{r.json()["msg"]};username-->{r.json()["data"]["username"]}'
print("业务断言成功")

'''
断言---> 数据断言
'''
#导包
import pymysql
'''
连接数据库
'''
#构建连接数据库的实例，需要主机（域名）、端口、用户名，密码，数据库名
db = pymysql.connect(host="shop-xo.hctestedu.com",
                     port=3306,
                     user="api_test",
                     password="Aa9999!",
                     database="shopxo_hctested", )
#访问数据库的对象， 构建游标cursor实例
cursor = db.cursor(pymysql.cursors.DictCursor)
#传递数据的查询语句
uid = r.json()["data"]["id"]
cursor.execute(f"select token from sxo_user where id ={uid};")
# data = cursor.fetchall() #查看游标的执行结果,元组类型,序列化后 列表里套字典
data = cursor.fetchone() #查看游标的执行结果,返回第一条数据，元组类型
print("token:",data)
#字典的交互性 是最强的 所以将元组转换为字典类型 取值,两种转换为字典格式的思路
#1.自己构造一个dict，将值传进去
#2.使用pymysql 自带的数据序列化功能，pymysal.cursors.DictCursor--将其传给游标实例:cursor = db.cursor(pymysql.cursors.DictCursor)
assert data["token"]==r.json()["data"]["token"],f'数据断言失败，实际拿到的结果为:{r.json()["data"]["token"]},预期为：{data["token"]}'
print("数据断言成功")