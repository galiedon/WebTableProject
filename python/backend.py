import json
import os

from flask import Flask, url_for, request
from flask_cors import CORS, cross_origin

from const import const
from ado.data import Selection
from dbhelper.mysqlHelper import MysqlHelper
from import_data import importTable


def return_img_stream(img_local_path):
    """
    工具函数:
    获取本地图片流
    :param img_local_path:文件单张图片的本地绝对路径
    :return: 图片流
    """
    import base64
    img_stream = ""
    with open(img_local_path, "rb") as img_f:
        img_stream = img_f.read()
        img_stream = base64.b64encode(img_stream)
        return str(img_stream)[2:-1]

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

            data = request.form
            print(data)
            file = request.files['file']

            file_path = os.path.join(const.ADDITION_FILE_PATH, file.filename[:-4] + "/")
            if not os.path.exists(file_path):
                os.mkdir(file_path)
            file_path = os.path.join(file_path, file.filename)
            file_rela_path = file.filename[:-4] + "/" + file.filename

            is_exist = False
            if os.path.exists(file_path):
                is_exist = True
            else:
                file.save(file_path)
            file_id = 0
            for file_id_tmp in self.db_helper.insert_file(file_rela_path, is_exist):
                file_id = file_id_tmp[0]
            self.db_helper.update_file_data(data, file_id)

            return {'status': 200}

        @self.app.route('/get_image', methods=['Get'])
        @cross_origin(supports_credentials=True)
        def get_image():
            if len(request.args) == 0:
                return {'status': 403}

            file_id = request.args['file_id']
            result = self.db_helper.get_file_path(file_id)
            file_path = ''
            for file_path_tmp in result:
                file_path = file_path_tmp[0]

            # return 'data:image/jpeg;base64,'+return_img_stream(os.path.join(const.ADDITION_FILE_PATH, file_path))
            return {'data': 'data:image/jpeg;base64,'+return_img_stream(os.path.join(const.ADDITION_FILE_PATH, file_path)), 'status': 200}
