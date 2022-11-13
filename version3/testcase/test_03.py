#-*- coding: utf-8 -*-
from ..package.Request import Request

from ..package.database import Sql
def test03():
    data = {
        "request":
            {
                "headers":{
                    "content-type": "application/json"
                },
                "params":{
                    "s": "api/user/login",
                    "application": "app",
                    "application_client_type": "weixin",
                },
                "json":{
                    "accounts": "test_fcy",
                    "pwd": "test_fcy",
                    "type": "username"
                },
                "method":"post",
                "url":"http://shop-xo.hctestedu.com:80/index.php"
            },
        "assert_business":
            {
                "$.code": 0, "$.msg": "登录成功",
                "$.data.username": "test_fcy"
            },
        "assert_sql":
            {
                "dql": "select token from sxo_user where id=${id};",
                "sql_jsonpath": "$.token",
                "r_jsonpath": "$.data.token"
            }
    }

    r=Request()
    r.run(**data["request"])
    r.assert_business(data["assert_business"])
    r.argument(id="$.data.id",username="$.data.username")
    r.assert_sql(data["assert_sql"])