from datetime import datetime

from dateutil.parser import parser


def num2datetime(num):
    if num is None:
        return None
    d = datetime.fromtimestamp(num / 1000)
    str1 = d.strftime("%Y-%m-%d %H:%M:%S")
    return str1


header = ['id',
          'order_id',
          'customer',
          'product_name',
          'product_per_price',
          'product_num',
          'product_sum_price',
          'order_time',
          'cutting_time',
          'forg_company_name',
          'roughcast_price',
          'roughcast_processing_fee',
          'material_return_time',
          'manager_person_name',
          'processing_person_name',
          'priduct_processing_fee',
          'roughcast_weight',
          'product_new_weight',
          'iron_filings_weight',
          'addition_file_path',
          'notes', ]


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

    def query(self, sql):
        pass

    def alter_table_data(self, form):
        data_header = ['update orders set ',
                       'cutting_time = "{}",',
                       'forg_company_name = "{}",',
                       'roughcast_price = {},',
                       'roughcast_processing_fee = {},',
                       'material_return_time = "{}",',
                       'manager_person_name = "{}",',
                       'processing_person_name = "{}",',
                       'priduct_processing_fee = {},',
                       'roughcast_weight = {},',
                       'product_new_weight = {},',
                       'iron_filings_weight = {},',
                       'addition_file_path = "{}",',
                       'notes = "{}",',
                       ' where id = {};']
        tmp = []
        for key in header:
            tmp.append(form[key])
        sql = data_header[0]
        tmp = tmp[8:] + tmp[:1]
        tmp[0] = num2datetime(tmp[0])
        tmp[4] = num2datetime(tmp[4])
        for i in range(len(tmp)):
            if tmp[i] is not None:
                if i == len(tmp) - 1:
                    sql = sql[:-1] + data_header[i + 1].format(tmp[i])
                else:
                    sql += data_header[i + 1].format(tmp[i])
        print(sql)
        self.exec(sql)
        return form

    def count_table_data(self):
        sql = 'select count(*) from orders'
        return self.query(sql)

    def fetch_table_data(self, page, limit, filter_data):

        min_id = page * limit
        max_id = page * limit + limit
        filter_param = ''
        for key, value in filter_data.items():
            filter_param += ' {0} = "{1}" and'.format(key, value)

        if filter_param != '':
            filter_param = 'where %s' % filter_param[:-3]

        sql = 'select * from orders %s order by id desc limit %d,%d;' % (filter_param, min_id, max_id)
        print(sql)
        return self.query(sql)

    def insert_file(self, filepath, is_exist):
        if not is_exist:
            sql = 'insert into image(path)values("%s");' % filepath
            print(sql)
            self.exec(sql)

        sql = 'select id from image where path="%s";' % filepath

        return self.query(sql)

    def update_file_data(self, order_info, file_id):

        sql = 'select addition_file_path from orders where id = %s;' % order_info['id']
        print(sql)
        for addition_file_path in self.query(sql):
            addition = addition_file_path[0]
            if addition is None:
                addition = ''
            if addition != '':
                addition += ','

            addition += str(file_id)

            sql = 'update orders set addition_file_path ="%s" where id = %s;' % (addition, order_info['id'])
            print(sql)

            self.exec(sql)
        return

    def get_file_path(self, file_id):

        sql = 'select path from image where id="%s";' % file_id

        return self.query(sql)
