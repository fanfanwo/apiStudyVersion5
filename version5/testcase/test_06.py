# -*- coding: utf-8 -*-
# author: 华测-长风老师
import pytest
import yaml

from version5.Package.execute import execute
from version5.Package.Request import Request

f = open(r"D:\Files\pypro1\apistudy2\version5\testcase\test_02.yaml","r",encoding="UTF-8")
data_token = yaml.safe_load(f)

@pytest.mark.parametrize("data",[data_token])
def test07(data):
    """多接口测试tooken"""
    r = Request()  # 实例化对象
    for i in data_token:
        r.run(**i["request"])  # 请求
        if i.get("extract_data", False):  # i.get(value1,value2); i["value1"]
            r.argument(**i["extract_data"])  # 提取数据
        if i.get("assert_business", False):
            r.assert_business(i["assert_business"])  # 断言业务正确性
        if i.get("assert_sql"):
            r.assert_sql(i["assert_sql"])  # 断言数据正确性


def test08(data_token1):
    execute(data_token1)