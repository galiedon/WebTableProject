<template>
	<div id="app">
		<el-container>
			<!-- Header -->
			<el-header>
				<el-row>
					<el-col :span="temp">
						<el-button
							@click="upload_data_dialog_visiable = true"
							type="warning"
							round
							>导入</el-button
						>
					</el-col>
					<el-col :span="temp">
						<el-button @click="handle_search" round>搜索</el-button>
					</el-col>
					<el-col :span="temp">
						<el-button type="info" round>筛选</el-button>
					</el-col>
				</el-row>
			</el-header>

			<!-- Content -->
			<el-main>
				<el-table
					:data="table_data"
					border
					height="700"
					max-height="700"
					style="width: 100%"
					@header-dragend="save_table_width"
					:row-class-name="show_warming_data"
				>
					<el-table-column
						prop="id"
						label="行号"
						float="left"
						sortable
						width="50"
					>
					</el-table-column>
					<el-table-column
						v-for="(value, key, index) in table_headers"
						:key="index"
						:prop="key"
						:label="value"
						:index="index"
						sortable
						:width="table_width_list[index]"
					>
					</el-table-column>
					<el-table-column fixed="right" label="操作" width="100%">
						<template slot-scope="scope">
							<el-row>
								<el-col :span="8">
									<el-button
										@click="handleClick(scope.row, scope.$index, false)"
										type="text"
										size="small"
										>查看</el-button
									></el-col
								>
								<el-col :span="8">
									<el-button
										@click="handleClick(scope.row, scope.$index, true)"
										type="text"
										size="small"
										>编辑</el-button
									></el-col
								>
								<el-col :span="8">
									<el-button
										@click="upload_file_switch(scope.row, scope.$index)"
										type="text"
										size="small"
										>附件添加</el-button
									>
								</el-col>
							</el-row>
						</template>
					</el-table-column>
				</el-table>
			</el-main>
			<el-dialog title="订单详情" :visible.sync="dialog_from_visible">
				<el-form :model="cur_row">
					<el-form-item
						v-for="(value, key, index) in table_header"
						:key="index"
						:label="value"
						:label-width="formLabelWidth"
					>
						<el-input
							v-if="table_info[key].type == info_type.label"
							disabled
							v-model="cur_row[key]"
							autocomplete="off"
						></el-input>
						<el-input
							v-if="table_info[key].type == info_type.text"
							:disabled="!can_edit"
							v-model="cur_row[key]"
							autocomplete="off"
						></el-input>
						<template
							v-if="table_info[key].type == info_type.file">
								<el-image 
									style="width: 100px; height: 100px"
									v-for="(src_value, key) in image_src_list"
									:key="key"
									:src="src_value"
									:preview-src-list="[src_value]"
									:z-index="img_z_index">
								</el-image>
						</template>
						<el-date-picker
							v-if="table_info[key].type == info_type.time"
							v-model="cur_row[key]"
							:disabled="!can_edit"
							type="datetime"
							placeholder="选择日期时间"
						>
						</el-date-picker>
					</el-form-item>
				</el-form>
				<div slot="footer" class="dialog-footer">
					<el-button @click="dialog_from_visible = false">取 消</el-button>
					<el-button type="primary" @click="change_table_item(cur_row)"
						>确 定</el-button
					>
				</div>
			</el-dialog>

			<el-dialog title="搜索内容" :visible.sync="search_data_visible">
				<el-form>
					<el-form-item
						v-for="(value, key, index) in search_config"
						:key="index"
						:label-width="formLabelWidth"
					>
						<el-row v-if="check_search_null(search_config[key])">
							<el-col :span="6">
								<el-checkbox
									v-model="search_config[key].enable_search"
									:label="table_headers[key]"
								></el-checkbox>
							</el-col>
							<el-col :span="12">
								<el-input
									v-if="search_config[key].type == info_type.label"
									:disabled="!search_config[key].enable_search"
									v-model="search_config[key].value"
									autocomplete="off"
								></el-input>
								<el-input
									v-if="search_config[key].type == info_type.text"
									:disabled="!search_config[key].enable_search"
									v-model="search_config[key].value"
									autocomplete="off"
								></el-input>

								<el-date-picker
									v-if="search_config[key].type == info_type.time"
									:disabled="!search_config[key].enable_search"
									v-model="search_config[key].value"
									type="datetime"
									placeholder="选择日期时间"
								>
								</el-date-picker>
							</el-col>
						</el-row>
					</el-form-item>
				</el-form>
				<div slot="footer" class="dialog-footer">
					<el-button @click="search_data_visible = false">取 消</el-button>
					<el-button type="primary" @click="search_data(cur_row)"
						>确 定</el-button
					>
				</div>
			</el-dialog>

			<el-dialog title="导入Excel" :visible.sync="upload_data_dialog_visiable"
				><el-upload
					class="upload-demo"
					accept=".xlsx"
					drag
					action="http://127.0.0.1:5000/put_file"
					multiple
					ref="upload"
					:file-list="file_list"
					:auto-upload="false"
					:on-success="upload_success"
					:data="cur_row"
				>
					<i class="el-icon-upload"></i>
					<div class="el-upload__text">将文件拖到此处，或<em>点击上传</em></div>
					<div class="el-upload__tip" slot="tip">
						只能上传xlsx文件，且不超过500kb
					</div>
				</el-upload>
				<div slot="footer" class="dialog-footer">
					<el-button @click="upload_data_dialog_visiable = false"
						>取 消</el-button
					>
					<el-button @click="submitUpload()">上传</el-button>
				</div>
			</el-dialog>


			<el-dialog title="上传附件" :visible.sync="upload_file_visible"
				><el-upload
					class="upload-demo"
					accept=".jpg,.png,.bmp"
					action="http://127.0.0.1:5000/put_addition_file"
					drag
					multiple
					ref="upload"
					:data="cur_row"
					:file-list="file_list"
					:auto-upload="false"
					:on-success="upload_success"
				>
					<i class="el-icon-upload"></i>
					<div class="el-upload__text">将图片拖到此处，或<em>点击上传</em></div>
					<div class="el-upload__tip" slot="tip">
						只能上传jpg,png,bmp文件，且不超过500kb
					</div>
				</el-upload>
				<div slot="footer" class="dialog-footer">
					<el-button @click="upload_file_visible = false"
						>取 消</el-button
					>
					<el-button @click="upload_pics()">上传</el-button>
				</div>
			</el-dialog>
			<!-- Footer -->
			<el-footer>
				<el-pagination
					@current-change="change_page"
					@size-change="change_limit"
					background
					layout="total, sizes, prev, pager, next, jumper"
					:page-sizes="limit_nums"
					:page-size="limit"
					:total="count"
				>
				</el-pagination
			></el-footer>
		</el-container>
	</div>
</template>

<script>
import Vue from 'vue'
import test from './class/test.js'

export default {
	name: 'app',
	components: {},
	data() {
		return {
			temp: 8,
			page: 1,
			limit_nums: [100, 500, 1000],
			limit: 100,
			table_datas: [],
			table_header: test.table_header,
			count: 10000,
			dialog_from_visible: false,
			cur_row: {},
			formLabelWidth: '200px',
			table_info: test.table_info,
			info_type: test.info_type,
			search_config: test.search_config,
			cur_id: 0,
			// 更新数据显示界面
			upload_data_dialog_visiable: false,
			file_list: [],
			table_width_list: [],
			data_filter: [],
			// 搜索显示界面
			search_data_visible: false,
			tmp: null,
			can_edit: false,
			// 上传附件界面
			upload_file_visible : false,
			image_src_list: [],
			img_z_index: 9999,
		}
	},
	computed: {
		table_data() {
			var table_data_first = []
			var table_data_second = []
			// 需要处理置顶内容
			for (var i = 0; i < this.table_datas.length; ++i) {
				if (this.is_overdue_item(this.table_datas[i])) {
					table_data_first.push(this.table_datas[i])
				} else {
					table_data_second.push(this.table_datas[i])
				}
			}

			return table_data_first.concat(table_data_second)
		},
		max_page() {
			return this.count / this.limit + 1
		},
		cur_page() {
			return this.page - 1
		},
		table_headers() {
			let tmp = Object.assign({}, test.table_header)
			delete tmp['id']
			return tmp
		},
		data_search() {
			let keys = Object.keys(this.table_header)
			var param = {}

			for (var i = 0; i < keys.length; i++) {
				if (this.search_config[keys[i]] != null) {
					if (this.search_config[keys[i]].enable_search) {
						if(this.search_config[keys[i]].type == this.info_type.time){
							param[keys[i]] = this.date2sec(this.search_config[keys[i]].value) 
						}else{
							param[keys[i]] = this.search_config[keys[i]].value
						}
					}
				}
			}
			return param
		},
	},
	methods: {

		upload_file_switch(row, index) {
			this.cur_row = Object.assign({}, row)
			this.upload_file_visible = true
		},
		is_overdue_item(row) {
			var date = null
			if (row['material_return_time'] == null) {
				date = row['material_return_time']
			} else if (row['cutting_time'] != null) {
				date = row['cutting_time']
			} else {
				date = row['order_time']
			}

			date = this.time_string2date(date)
			var curDate = new Date()
			var days = (curDate - date) / (1000 * 3600 * 24)
			if (days - test.warming_days >= 0) {
				return true
			} else {
				return false
			}
		},
		show_warming_data({ row, rowIndex }) {
			if (this.is_overdue_item(row)) {
				return 'warning-row'
			} else {
				return ''
			}
		},
		search_data() {
			console.log(this.data_search)
			this.fetch_data(this.cur_page, this.limit)
			this.save_search_config()
			this.search_data_visible = false
		},
		save_table_width(newWidth, oldWidth, column, event) {
			this.$set(this.table_width_list, column.index, newWidth)
			console.log('Save table width!')
			localStorage.width_list = JSON.stringify(this.table_width_list)
		},
		save_other_datas() {
			localStorage.limit_nums = this.limit_nums
			localStorage.limit = this.limit
			localStorage.page = this.page
			localStorage.count = this.count
		},
		load_other_datas() {
			if (localStorage.limit_nums != null) {
				this.limit_nums = localStorage.limit_nums
			}
			if (localStorage.limit != null) {
				this.limit = localStorage.limit
			}
			if (localStorage.page != null) {
				this.page = localStorage.page
			}
			if (localStorage.count != null) {
				this.count = localStorage.count
			}
		},
		load_table_width() {
			if (
				localStorage.width_list == null ||
				localStorage.width_list.length == 0
			) {
				this.table_width_list = Array(Object.keys(this.table_headers).length)
				this.table_width_list.fill(180)
			} else {
				this.table_width_list = JSON.parse(localStorage.width_list)
			}
		},
		load_search_config() {
			if (localStorage.search_config == null) {
				this.search_config = test.search_config
			} else {
				this.search_config = JSON.parse(localStorage.search_config)
			}
		},
		// 保存过滤配置
		save_search_config() {
			console.log('Save search config')
			localStorage.search_config = JSON.stringify(this.search_config)
		},
		upload_success() {
			this.message_box('上传成功，正在重新获取数据...')
			this.change_page(1)
		},
		submitUpload() {
			this.upload_data_dialog_visiable = false
			this.$refs.upload.submit()
		},
		upload_pics(){
			this.upload_file_visible = false
			this.$refs.upload.submit()
		},
		change_table_item(rows) {
			let cur_row = Object.assign({}, rows)
			cur_row['cutting_time'] = this.date2sec(cur_row['cutting_time'])

			cur_row['material_return_time'] = this.date2sec(
				cur_row['material_return_time']
			)
			this.post_new_row(cur_row)
		},
		date2sec(date) {
			if (date != null) {
				date = new Date(date)
				return date.getTime()
			}
			return null
		},
		sec2date(sec) {
			if (sec == null) {
				return ''
			}
			return new Date(sec)
		},
		message_box(str) {
			this.$message(str)
		},
		date2time_string(date) {
			if (date == null || date.getTime() == 0) {
				return ''
			}
			return (
				date.getFullYear() +
				'年' +
				(date.getMonth() + 1) +
				'月' +
				date.getDate() +
				'日 ' +
				date.getHours() +
				':' +
				date.getMinutes() +
				':' +
				date.getSeconds()
			)
		},
		time_string2date(date) {
			return new Date(
				Date.parse(date.replace('年', '-').replace('月', '-').replace('日', ''))
			)
		},
		handleClick(row, index, can_edit) {
			this.cur_id = index
			this.dialog_from_visible = true
			this.cur_row = Object.assign({}, row)

			this.cur_row['cutting_time'] = this.time_string2date(
				this.cur_row['cutting_time']
			)

			this.cur_row['material_return_time'] = this.time_string2date(
				this.cur_row['material_return_time']
			)
			this.can_edit = can_edit
			this.fetch_files()

		},
		fetch_files(){
			this.image_src_list = undefined
			this.image_src_list = []
			if(this.cur_row['addition_file_path'] == null){
				return;
			}
			var file_id_list = this.cur_row['addition_file_path'].split(",")
			console.log(file_id_list)
			for(let id in file_id_list){
				Vue.axios({
					method: 'get',
					url: 'http://127.0.0.1:5000/get_image',
					headers: {
						'Access-Control-Allow-Origin': '*',
					},
					params: {
						file_id: file_id_list[id],
					},
				}).then((response) => {
					if (response.data.status != 200) {
						return
					}
					// console.log(response.data.data)
					this.image_src_list.push(response.data.data)
				})
			}
		},
		handle_search() {
			this.search_data_visible = true
			// console.log(this.search_config)
		},
		change_page: function (new_page) {
			this.page = new_page
			this.fetch_data(this.cur_page, this.limit)
		},
		change_limit: function (new_limit) {
			this.limit = new_limit
			this.fetch_data(this.cur_page, this.limit)
		},
		parse_data: function (item) {
			if (item == undefined) {
				return null
			}
			var temp = {}
			var i = 0
			for (let key in this.table_header) {
				if (
					this.table_header[key] == this.table_header.order_time ||
					this.table_header[key] == this.table_header.cutting_time ||
					this.table_header[key] == this.table_header.material_return_time
				) {
					temp[key] = this.date2time_string(new Date(item[i]))
				} else {
					temp[key] = item[i]
				}
				i++
			}
			return temp
		},
		post_new_row: function (new_row) {
			Vue.axios({
				method: 'post',
				url: 'http://127.0.0.1:5000/alter_data',
				headers: {
					'Access-Control-Allow-Origin': '*',
				},
				data: new_row,
			}).then((response) => {
				if (response.data.status != 200) {
					return
				}
				var cur_row = Object.assign({}, response.data.data)

				cur_row['cutting_time'] = this.date2time_string(
					new Date(cur_row['cutting_time'])
				)
				cur_row['material_return_time'] = this.date2time_string(
					new Date(cur_row['material_return_time'])
				)

				// console.log(this.cur_row)
				this.message_box('修改成功')
				for (let key in this.table_header) {
					this.$set(this.table_datas, this.cur_id, cur_row)
					if (
						this.cur_row[key] != null &&
						this.table_info[key].type == this.info_type.time
					) {
						this.cur_row[key] = this.date2time_string(
							new Date(this.cur_row[key])
						)
						console.log(this.cur_row[key])
					}
				}

				this.dialog_from_visible = false
			})
		},
		check_search_null(data) {
			if (data == null || data.type == null || data.value == null) {
				return false
			}
			return true
		},
		fetch_data: function (page, limit) {
			var filter_data = this.data_search
			Vue.axios({
				method: 'get',
				url: 'http://127.0.0.1:5000/get_data',
				headers: {
					'Access-Control-Allow-Origin': '*',
				},
				params: {
					page: page,
					limit: limit,
					filter_data: filter_data,
				},
			}).then((response) => {
				this.table_datas = undefined
				this.table_datas = []
				for (var i = 0; i < limit; ++i) {
					let result = this.parse_data(response.data.data[i])
					if (result != null) {
						this.table_datas.push(result)
					}
				}
				this.count = response.data.count
			})
		},
		edit(row, index) {
			row.iseditor = true
		},
		save(row, index) {
			row.iseditor = false
		},
	},
	beforeMount() {
		this.load_table_width()
		this.load_search_config()
		this.fetch_data(this.cur_page, this.limit)
	},
}
</script>

<style>
#app {
	font-family: 'Avenir', Helvetica, Arial, sans-serif;
	-webkit-font-smoothing: antialiased;
	-moz-osx-font-smoothing: grayscale;
	text-align: center;
	color: #2c3e50;
	margin-top: 60px;
}

.el-header,
.el-footer {
	background-color: #b3c0d1;
	color: #333;
	text-align: center;
	line-height: 60px;
}

.el-aside {
	background-color: #d3dce6;
	color: #333;
	text-align: center;
	line-height: 200px;
}

.el-main {
	background-color: #e9eef3;
	color: #333;
	text-align: center;
	/* line-height: 160px; */
}

body > .el-container {
	margin-bottom: 40px;
}

.el-container:nth-child(5) .el-aside,
.el-container:nth-child(6) .el-aside {
	line-height: 260px;
}

.el-container:nth-child(7) .el-aside {
	line-height: 320px;
}

.el-table .warning-row {
	background: hsla(0, 87%, 71%, 0.557);
	color: #555555;
}
</style>
