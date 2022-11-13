import pytest
import jsonpath
from ..package.database import Sql
@pytest.fixture(autouse=True)
def headers():
    return {
        "content-type": "application/json"
    }

@pytest.fixture(autouse=True)
def params():
    return {
        "s": "api/user/login",
        "application": "app",
        "application_client_type": "weixin"
    }

@pytest.fixture(autouse=True)
def method_url():
    return {
        "method":"post",
        "url":"http://shop-xo.hctestedu.com:80/index.php"
    }

# @pytest.fixture(autouse=True)
# def assert_operator(assert_data, response_data):
#     for k, v in assert_data.items():
#         data = jsonpath.jsonpath(response_data, k)[0]
#         assert data == v, f'业务断言失败，实际拿到的数据分别为：{data},预期的值为{v}'
#     print("业务断言成功")
#给response传参的时候传了assert_operator,相当于是assert_operator=assert_operator()，没有带参数，所以需要下面的写法
@pytest.fixture(autouse=True)
def assert_operator():
    def func(assert_data,response_data):
        for k,v in assert_data.items():
            data = jsonpath.jsonpath(response_data,k)[0]
            assert data == v,f'业务断言失败，实际拿到的数据分别为：{data},预期的值为{v}'
        print("业务断言成功")
    return func

@pytest.fixture(autouse=True)
def assert_sql_data():
    def func(assert_data, expect_data):
        data = Sql().execute(assert_data["sql"]).fetchone() #预期值
        assert data["token"] == expect_data,f'数据断言失败，实际拿到的结果为:{expect_data},预期为：{data}'
        print("数据断言成功")
    return func
