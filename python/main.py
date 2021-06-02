import time

import openpyxl
import warnings
from dbhelper.mysqlHelper import MysqlHelper
from const import const
from backend import Backend

if __name__ == '__main__':
    start = time.time()
    backend = Backend()
    backend.run()

    # excel_read_test()
    # sql_test()
    # read_data_from_excel_to_mysql()
    # read_src_data_2_orders()
    end = time.time()
    delta = end - start
    print('%d:%d:%d' % (delta // 3600, (delta // 60) % 60, delta % 60))
