import json
import time

import pytest

RESULT = (r"D:\Files\pypro1\apistudy2\version5\result.json")


# 钩子函数 固定写法
@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    out = yield
    # print("测试主体：",out)  #预置条件、执行主体、后置处理
    result = out.get_result()  # 当result.when为call的时候，运行的时用例主体
    print(result)
    # print(result.__dict__)
    if result.when == "call":
        outcome = result.outcome  # result.outcome 为测试结果
        name = result.nodeid  # Yongli 名称
        times = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))  # 时间单位

        f = open(RESULT, "r", encoding='utf-8')  # 有数据更新，没数据定义  保存持久性数据 用json数据体存储数据
        d = f.read()
        if d:
            result_ = json.loads(d)  # 有数据的操作  --将字符串转换成json格式
            f.close()
        else:
            result_ = {}
            f.close()
        f = open(RESULT, "w", encoding='utf-8')  # 覆盖写
        keys = name.replace("::","-").replace("/","-").replace(".py","-")+times.replace(" ","").replace("-","").replace(":","") #时间换成存数据
        result_.update({keys:{"name":name,"result":outcome,"time":times}}) #更新数据
        f.write(json.dumps(result_))
        f.close()
