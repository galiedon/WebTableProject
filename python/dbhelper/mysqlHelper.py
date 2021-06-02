from const import const
from dbhelper.dbHelper import DBHelper
from mysql import connector
from mysql.connector import errorcode


class MysqlHelper(DBHelper):
    def __init__(self):
        super(MysqlHelper, self).__init__(const.DB_TYPE)
        self._cursor = None

    @property
    def cursor(self):
        return self._cursor

    @cursor.setter
    def cursor(self, new_cursor):
        self._cursor = new_cursor

    def reconnect(self):
        self.close()
        self.connect(self.host, self.username, self.password, self.db_name)

    def connect(self, host, username, password, db_name):
        self.host = host
        self.username = username
        self.password = password
        self.db_name = db_name

        config = {
            'user': self.username,
            'password': self.password,
            'host': self.host,
            'database': self.db_name,
        }
        try:
            self.conn = connector.connect(**config)
            self.cursor = self.conn.cursor()
            print('连接数据库成功')
        except connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)

    def close(self):
        if self.conn is None:
            print('没有连接到数据库')
            return

        try:
            self.conn.close()
        except connector.Error as err:
            print(err)

    def query(self, sql):
        try:
            self.cursor.execute(sql)
        except connector.Error as err:
            print(err)

        return self.cursor

    def exec(self, sql):
        try:
            self.cursor.execute(sql)
            self.conn.commit()
        except connector.Error as err:
            print(err)

        return self.cursor
