import pymysql

DictCursor = pymysql.cursors.DictCursor


class Sql:

    def __init__(self, host='shop-xo.hctestedu.com',
                 port=3306,
                 user='api_test',
                 password='Aa9999!',
                 database='shopxo_hctested'):
        self.db = pymysql.connect(
            host=host,
            port=port,
            user=user,
            password=password,
            database=database
        )
        # 私有属性，游标
        self.__cursor = self.db.cursor(DictCursor)

    def execute(self, dql):
        self.__cursor.execute(dql)
        return self

    def fetchone(self):
        return self.__cursor.fetchone()

    def fetchall(self):
        return self.__cursor.fetchall()
