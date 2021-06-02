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
						<el-button round>搜索</el-button>
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
					stripe
					height="400"
					max-height="400"
					style="width: 100%"
				>
					<el-table-column
						prop="id"
						label="行号"
						float="left"
						sortable
						width="180"
					>
					</el-table-column>
					<el-table-column
						v-for="(value, key, index) in table_headers"
						:key="index"
						:prop="key"
						:label="value"
						sortable
						width="180"
					>
					</el-table-column>
					<el-table-column fixed="right" label="操作" width="100%">
						<template slot-scope="scope">
							<el-button
								@click="handleClick(scope.row, scope.$index)"
								type="text"
								size="small"
								>编辑</el-button
							>
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
							v-model="cur_row[key]"
							autocomplete="off"
						></el-input>

						<el-date-picker
							v-if="table_info[key].type == info_type.time"
							v-model="cur_row[key]"
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
			cur_id: 0,
			upload_data_dialog_visiable: false,
			file_list: [],
		}
	},
	computed: {
		table_data() {
			return this.table_datas
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
	},
	methods: {
		upload_success() {
			this.message_box('上传成功，正在重新获取数据...')
			this.change_page(1)
		},
		submitUpload() {
			this.upload_data_dialog_visiable = false
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
			if (date == null) {
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
		handleClick(row, index) {
			this.cur_id = index
			this.dialog_from_visible = true
			this.cur_row = Object.assign({}, row)
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
				temp[key] = item[i]
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

				cur_row['cutting_time'] = this.sec2date(cur_row['cutting_time'])
				cur_row['material_return_time'] = this.sec2date(
					cur_row['material_return_time']
				)

				// console.log(this.cur_row)
				this.message_box('修改成功')
				for (let key in this.table_header) {
					this.$set(this.table_datas, this.cur_id, cur_row)
					if (
						this.cur_row[key] != null &&
						this.table_info[key].type == this.info_type.time
					) {
						this.cur_row[key] = this.date2time_string(this.cur_row[key])
					}
				}
				this.dialog_from_visible = false
			})
		},
		fetch_data: function (page, limit) {
			Vue.axios({
				method: 'get',
				url: 'http://127.0.0.1:5000/get_data',
				headers: {
					'Access-Control-Allow-Origin': '*',
				},
				params: {
					page: page,
					limit: limit,
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
</style>
