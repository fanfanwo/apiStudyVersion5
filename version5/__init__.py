'''

一个完整的用例分为4个部分：
1.请求的参数： Headers params json method url
2.提取参数： token id
3.业务断言：业务断言的路径 jsonpath的路径、断言的预期值
4.断言数据库：数据库查询语句，jsonpath提取查询结果 ，要拿提取的数据 和什么东西做对比

多接口 用列表嵌套 --token
从上一个接口中 将token 的提取方式写出来
在下一个接口中 置换token

生成测试报告：
pytest --report/report.html --self-containd-html
生产测试总结
'''