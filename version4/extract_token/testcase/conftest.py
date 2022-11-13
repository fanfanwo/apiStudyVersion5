import pytest

@pytest.fixture(autouse=True)
def data_token():
    return [
        {
            "request": {
                "headers": {
                    "content-type": "application/json"
                },
                "params": {
                    "s": "api/user/login",
                    "application": "app",
                    "application_client_type": "weixin"
                },
                "json": {
                    "accounts": "test_fcy",
                    "pwd": "test_fcy",
                    "type": "username"
                },
                "method": "post",
                "url": "http://shop-xo.hctestedu.com:80/index.php"
            },
            "extract_data": {
                "id": "$.data.id",
                "token": "$.data.token"
            },
            "assert_business": {
                "$.code": 0, "$.msg": "登录成功",
                "$.data.username": "test_fcy"
            },
            "assert_sql": {
                "dql": "select token from sxo_user where id=${id};",
                "sql_jsonpath": "$.token",
                "r_jsonpath": "$.data.token"
            }
        },
        {
            "request": {
                "headers": {
                    "content-type": "application/json"
                },
                "params": {
                    "s": "api/message/index",  # 查看消息列表
                    "application": "app",
                    "application_client_type": "weixin",
                    "token": "${token}"
                },
                "json": {
                    "page": 1
                },
                "method": "post",
                "url": "http://shop-xo.hctestedu.com:80/index.php"
            },
            "assert_business": {
                "$.code": 0, "$.msg": "success"
            }
        }
    ]


# @pytest.fixture(autouse=True)
# def data_token():
#     return [
#         {
#             "request": {
#                 "headers": {
#                     "content-type": "application/json"
#                 },
#                 "params": {
#                     "s": "api/user/login",
#                     "application": "app",
#                     "application_client_type": "weixin"
#                 },
#                 "json": {
#                     "accounts": "test_fcy",
#                     "pwd": "test_fcy",
#                     "type": "username"
#                 },
#                 "method": "post",
#                 "url": "http://shop-xo.hctestedu.com:80/index.php"
#             },
#             "extract_data": {
#                 "id": "$.data.id",
#                 "token": "$.data.token"
#             },
#             "assert_business": {
#                 "$.code": 0, "$.msg": "登录成功",
#                 "$.data.username": "test_fcy"
#             },
#             "assert_sql": {
#                 "dql": "select token from sxo_user where id=${id};",
#                 "sql_jsonpath": "$.token",
#                 "r_jsonpath": "$.data.token"
#             }
#         },
#         {
#             "request": {
#                 "headers": {
#                     "content-type": "application/json"
#                 },
#                 "params": {
#                     "s": "api/message/index",  # 查看消息列表
#                     "application": "app",
#                     "application_client_type": "weixin",
#                     "token": "${token}"
#                 },
#                 "json": {
#                     "page": 1
#                 },
#                 "method": "post",
#                 "url": "http://shop-xo.hctestedu.com:80/index.php"
#             },
#             "assert_business": {
#                 "$.code": 0, "$.msg": "success"
#             }
#         }
#     ]



