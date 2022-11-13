# -*- coding: utf-8 -*-
'''
业务流程的测试 编辑购物车的商品数量
'''

'''
步骤1:登录
'''
from requests import request
import pymysql
import random

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
r = request(method="post", url="http://shop-xo.hctestedu.com/index.php", params=params, headers=headers, json=json)
# print("r.json:",r.json())
'''
步骤2:获取所有商品数据(搜索)
'''
params = {
    "s": "api/search/index",
    "application": "app",
    "application_client_type": "weixin"
}

r1 = request(method="post", url="http://shop-xo.hctestedu.com/index.php", params=params, headers=headers)
# print(r1.json())  #所有商品数据
'''
步骤3:得出商品分类（有无规格）
'''
# 通过有无规格分类商品Id
f_data_id_list = []  # 有规格的商品
u_data_id_list = []  # 无规格的商品
goods_id_list = []

for i in r1.json()["data"]["data"]:
    if i["is_shelves"] == "1" and i["is_deduction_inventory"] == "1":
        if i["is_exist_many_spec"] == "1":
            f_data_id_list.append({"id": i["id"]})
        else:
            u_data_id_list.append({"id": i["id"]})

goods_id_list.append({"f_data_id": f_data_id_list})
goods_id_list.append({"u_data_id": u_data_id_list})
# print(goods_id_list)
'''有无规格分类分别处理业务'''
goods = random.choice(goods_id_list)  # 随机选择有规格数据或无规格数据
# print(goods)#有规格或者无规格的商品id 字典
'''
步骤4:根据不同规格，构建商品加入购物车的实现
'''
if "u_data_id" in goods.keys():  #根据关键字判断 有规格还是无规格
    good_id = random.choice(goods["u_data_id"]) #从无规格的商品ID中随机挑选 id
    '''步骤4-1、添加购物车'''
    json = {
        "goods_id": good_id["id"],
        "stock": 1  # 加入购物车的商品数量
    }
    params = {
        "s": "api/cart/save",
        "application": "app",
        "application_client_type": "weixin",
        "token":r.json()["data"]["token"]
    }
    r2 = request(method="post", url="http://shop-xo.hctestedu.com/index.php", params=params, json=json, headers=headers)
    # print("r2.json",r2.json())
else:
    '''步骤4-2、商品详情'''
    good_id = random.choice(goods["f_data_id"]) #从有规格的商品中随机选择id
    json = {
        "goods_id": good_id["id"]
    }
    params = {
        "s": "api/goods/detail",
        "application": "app",
        "application_client_type": "weixin"
    }
    r3 = request(method="post", url="http://shop-xo.hctestedu.com/index.php", params=params, json=json, headers=headers)
    # print("r3.response",r3.json()) #获取商品详情
    specifications = r3.json()["data"]["goods"]["specifications"]["choose"] #choose是一个列表，里面存放了各种尺码或颜色或套餐
    # 获得随机商品规格的数据
    spc = []
    for i in specifications: #i代表了列表存放 尺码、颜色或套餐的字典，套餐，颜色或尺码 的key都为value，值为字典，套餐里的每个值都有key为name,值为套餐几
        spc.append({"type":i["name"],"value":random.choice(i["value"])["name"]})
    # print(spc) #商品的尺寸、颜色等规格值
    '''步骤4-3、添加购物车'''
    json = {
        "goods_id": good_id["id"],
        "stock": 4,
        "spc": spc
    }
    params = {
        "s": "api/cart/save",
        "application": "app",
        "application_client_type": "weixin",
        "token": r.json()["data"]["token"]
    }
    r4 = request(method="post", url="http://shop-xo.hctestedu.com/index.php", params=params, json=json, headers=headers)
    # print(r4.json())

'''
步骤5:查看购物车，获取购物车的ID和对应商品ID
'''
params = {
    "s": "api/cart/index",
    "application": "app",
    "application_client_type": "weixin",
    "token": r.json()["data"]["token"]
}
r5 = request(method="get", url="http://shop-xo.hctestedu.com/index.php", params=params, headers=headers)
# print(r5.json())
'''
步骤6:根据步骤5所得数据，编辑购物车ID
'''
cart = random.choice(r5.json()["data"]["data"])
good_number = "1"
json = {
    "id": cart["id"],
    "goods_id": cart["goods_id"],
    "stock": good_number
}

params = {
    "s": "api/cart/stock",
    "application": "app",
    "application_client_type": "weixin",
    "token": r.json()["data"]["token"]

}
r6 = request(method="get", url="http://shop-xo.hctestedu.com/index.php", params=params, json=json, headers=headers)

# 业务断言
assert r6.json()["msg"] == "更新成功" and r6.json()["code"] == 0, "错误语句，错误描述"
print(r6.json())

# 数据断言  ---》 确定数据被编辑成功
'''
连接数据库
'''
db = pymysql.connect(host="shop-xo.hctestedu.com",
                     port=3306,
                     user="api_test",
                     password="Aa9999!",
                     database="shopxo_hctested", )
cursor = db.cursor(pymysql.cursors.DictCursor)
cursor.execute(f"select stock from sxo_cart where id ='{cart['id']}' and goods_id = '{cart['goods_id']}';")
data_one = cursor.fetchone()  # 拿第一条数据
assert data_one["stock"]==int(good_number),f"数据断言失败，实际数据是{data_one['stock']}"
print("数据断言成功")