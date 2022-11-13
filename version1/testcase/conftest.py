import pytest

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

