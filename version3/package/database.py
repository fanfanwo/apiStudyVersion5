
import pymysql

DictCursor=pymysql.cursors.DictCursor

class Sql:

    def __init__(self,host="shop-xo.hctestedu.com",
                 port=3306,
                 user="api_test",
                 password="Aa9999!",
                 database="shopxo_hctested"
                 ):
        #连接数据库
        self.db = pymysql.connect(
            host = host,
            port=port,
            user=user,
            password=password,
            database=database
        )
        #实例化游标对象
        self.__cursor=self.db.cursor(DictCursor)

    def execute(self,dql):
        #执行查询语句
        self.__cursor.execute(dql)
        return self

    def fetchone(self):
        #查询一一条的结果
        return self.__cursor.fetchone()

    def fetchall(self):
        return self.__cursor.fetchall()

