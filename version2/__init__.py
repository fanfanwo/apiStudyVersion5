'''
版本二：
将request参数的 请求方法、url、请求头、必要参数 放到conftest.py文件中，并分别用pytest.fixture装饰器修饰
请求数据内容 的username、password 和 断言数据，都别参数化 --通过pytest.mark.parametrize 装饰器
连接数据库、构建游标实例、数据查询、查看查询结果 都封装到package包中
把业务断言封装成函数 assert_operator
把数据断言封装成函数 assert_sql_data
用到的技术：
pytest
requests
pyyaml
pymysql
jsonpath
'''