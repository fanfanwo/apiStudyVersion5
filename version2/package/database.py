import pymysql

DictCursor = pymysql.cursors.DictCursor


class Sql:
    # 给构造函数传参
    def __init__(self, host='shop-xo.hctestedu.com',
                 port=3306,
                 user="api_test",
                 password="Aa9999!",
                 database="shopxo_hctested"):
        # 连接数据库,由db保存数据库连接状态
        self.db = pymysql.connect(
            host=host,
            port=port,
            user=user,
            password=password,
            database=database
        )
        # 私有属性的写法__cursor 实例化游标对象 ---执行数据库操作是有游标完成
        self.__cursor = self.db.cursor(DictCursor)

    def execute(self, dql):
        '''执行数据库语句'''
        self.__cursor.execute(dql)
        return self

    def fetchone(self):
        return self.__cursor.fetchone()

    def fetchall(self):
        return self.__cursor.fetchall()

# if __name__ == '__main__':
#     print(Sql().execute("select token from sxo_user where id=94").fetchone())