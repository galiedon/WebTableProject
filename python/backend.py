import json
import os

from flask import Flask, url_for, request
from flask_cors import CORS, cross_origin

from const import const
from ado.data import Selection
from dbhelper.mysqlHelper import MysqlHelper
from import_data import importTable


class Backend(object):
    def __init__(self):
        self.app = Flask(__name__)
        CORS(self.app, supports_credentials=True)
        self.db_helper = MysqlHelper()
        self.db_helper.connect(const.LOCALHOST, const.USERNAME, const.PASSWORD, const.DB_NAME)

    def run(self):
        self.func_list()
        self.app.run(const.LOCALHOST, const.API_PORT, debug=True)

    def func_list(self):
        @self.app.route('/', methods=['GET', "POST"])
        @cross_origin(supports_credentials=True)
        def hello_world():
            return 'HelloWorld'

        @self.app.route('/get_data', methods=['GET'])
        @cross_origin(supports_credentials=True)
        def get_table_datas():
            page = request.args.get('page', 0)
            limit = request.args.get('limit', 100)
            page = int(page)
            limit = int(limit)
            filter_data = request.args.get('filter_data', '')
            filter_data = json.loads(filter_data)

            result = self.db_helper.fetch_table_data(page, limit, filter_data)
            ret = []
            for item in result:
                # print(item)
                ret.append(item)

            result = self.db_helper.count_table_data()
            count = result.fetchone()
            return {'data': ret, 'count': count[0]}


        @self.app.route('/alter_data', methods=['POST'])
        @cross_origin(supports_credentials=True)
        def alter_table_data():
            data = request.get_json()
            if len(data) == 0:
                return {'status': 204}

            result = self.db_helper.alter_table_data(data)
            return {'data': result, 'status': 200}

        @self.app.route('/put_file', methods=['POST'])
        @cross_origin(supports_credentials=True)
        def post_file():
            if 'file' not in request.files:
                return {'status': 403}
            file = request.files['file']

            file_path = os.path.join(const.RES_PATH, file.filename)
            file.save(file_path)
            importTable(file_path)
            self.db_helper.reconnect()
            return {'status': 200}

        @self.app.route('/put_addition_file', methods=['POST'])
        @cross_origin(supports_credentials=True)
        def put_addition_file():
            if 'file' not in request.files:
                return {'status': 403}

            data = request.get_json()
            file = request.files['file']

            file_path = os.path.join(const.ADDITION_FILE_PATH, file.filename[:-4]+"/")
            os.mkdir(file_path)
            file_path = os.path.join(file_path, file.filename)

            file.save(file_path)
            # self.db_helper.alter_table_data()

            print(data)

            return {'status': 200}



