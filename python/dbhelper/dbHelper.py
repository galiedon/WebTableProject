class DBHelper(object):
    def __init__(self, db_type):
        self._db_type = db_type
        self._host = None
        self._username = None
        self._password = None
        self._db_name = None
        self._conn = None

    @property
    def db_type(self):
        return self._db_type

    @db_type.setter
    def db_type(self, new_db_type):
        self._db_type = new_db_type

    @property
    def host(self):
        return self._host

    @host.setter
    def host(self, new_host):
        self._host = new_host

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, new_username):
        self._username = new_username

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, new_password):
        self._password = new_password

    @property
    def db_name(self):
        return self._db_name

    @db_name.setter
    def db_name(self, new_db_name):
        self._db_name = new_db_name

    @property
    def conn(self):
        return self._conn

    @conn.setter
    def conn(self, new_conn):
        self._conn = new_conn

    def connect(self, host, username, password, db_name):
        pass

    def close(self):
        pass

    def exec(self, sql):
        pass
