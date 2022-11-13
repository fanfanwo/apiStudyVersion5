import pytest




# app没有cookie,cookie只有web里有
@pytest.fixture(autouse=True)
def data_cookies():
    return [
        {
            "request": {
                "headers": {
                    "content-type": "application/json"
                },
                "params": {
                    "s": "api/user/login",
                    "application": "web",
                    "application_client_type": "pc"
                },
                "json": {
                    "accounts": "test_fcy",
                    "pwd": "test_fcy",
                    "type": "username"
                },
                "method": "post",
                "url": "http://shop-xo.hctestedu.com:80/index.php"
            },
            "assert_business": {
                "$.code": 0, "$.msg": "登录成功"
            }
        },
        {
            "request": {
                "headers": {
                    "content-type": "application/json"
                },
                "params": {
                    "s": "api/message/index",  # 查看消息列表
                    "application": "web",
                    "application_client_type": "pc"
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
