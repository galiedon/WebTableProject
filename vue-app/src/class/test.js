let table_data = [
	{
		order_id: '1',
		customer: '2',
		product_name: '3',
		product_per_price: '4',
		product_num: '5',
		product_sum_price: '6',
		order_time: '7',
		cutting_time: '8',
		forg_company_name: '9',
		roughcast_price: '10',
		roughcast_processing_fee: '11',
		material_return_time: '12',
		manager_person_name: '13',
		processing_person_name: '14',
		priduct_processing_fee: '15',
		roughcast_weight: '16',
		product_new_weight: '17',
		iron_filings_weight: '18',
		addition_file_path: '19',
		notes: '20',
	},
	{
		order_id: '1',
		customer: '2',
		product_name: '3',
		product_per_price: '4',
		product_num: '5',
		product_sum_price: '6',
		order_time: '7',
		cutting_time: '8',
		forg_company_name: '9',
		roughcast_price: '10',
		roughcast_processing_fee: '11',
		material_return_time: '12',
		manager_person_name: '13',
		processing_person_name: '14',
		priduct_processing_fee: '15',
		roughcast_weight: '16',
		product_new_weight: '17',
		iron_filings_weight: '18',
		addition_file_path: '19',
		notes: '20',
	},
	{
		order_id: '1',
		customer: '2',
		product_name: '3',
		product_per_price: '4',
		product_num: '5',
		product_sum_price: '6',
		order_time: '7',
		cutting_time: '8',
		forg_company_name: '9',
		roughcast_price: '10',
		roughcast_processing_fee: '11',
		material_return_time: '12',
		manager_person_name: '13',
		processing_person_name: '14',
		priduct_processing_fee: '15',
		roughcast_weight: '16',
		product_new_weight: '17',
		iron_filings_weight: '18',
		addition_file_path: '19',
		notes: '20',
	},
	{
		order_id: '1',
		customer: '2',
		product_name: '3',
		product_per_price: '4',
		product_num: '5',
		product_sum_price: '6',
		order_time: '7',
		cutting_time: '8',
		forg_company_name: '9',
		roughcast_price: '10',
		roughcast_processing_fee: '11',
		material_return_time: '12',
		manager_person_name: '13',
		processing_person_name: '14',
		priduct_processing_fee: '15',
		roughcast_weight: '16',
		product_new_weight: '17',
		iron_filings_weight: '18',
		addition_file_path: '19',
		notes: '20',
	},
	{
		order_id: '1',
		customer: '2',
		product_name: '3',
		product_per_price: '4',
		product_num: '5',
		product_sum_price: '6',
		order_time: '7',
		cutting_time: '8',
		forg_company_name: '9',
		roughcast_price: '10',
		roughcast_processing_fee: '11',
		material_return_time: '12',
		manager_person_name: '13',
		processing_person_name: '14',
		priduct_processing_fee: '15',
		roughcast_weight: '16',
		product_new_weight: '17',
		iron_filings_weight: '18',
		addition_file_path: '19',
		notes: '20',
	},
]

let table_header = {
	id: '???????????????',
	order_id: '????????????',
	customer: '????????????',
	product_name: '????????????-????????????',
	product_per_price: '????????????-????????????',
	product_num: '????????????-????????????',
	product_sum_price: '????????????-??????',
	order_time: '??????/????????????',
	cutting_time: '????????????',
	forg_company_name: '????????????',
	roughcast_price: '????????????',
	roughcast_processing_fee: '???????????????',
	material_return_time: '????????????',
	manager_person_name: '????????????',
	processing_person_name: '????????????',
	priduct_processing_fee: '???????????????',
	roughcast_weight: '????????????',
	product_new_weight: '????????????',
	iron_filings_weight: '????????????',
	addition_file_path: '??????',
	notes: '??????',
}
// ['id',
// 'order_id',
// 'customer',
// 'product_name',
// 'product_per_price',
// 'product_num',
// 'product_sum_price',
// 'order_time',
// 'cutting_time',
// 'forg_company_name',
// 'roughcast_price',
// 'roughcast_processing_fee',
// 'material_return_time',
// 'manager_person_name',
// 'processing_person_name',
// 'priduct_processing_fee',
// 'roughcast_weight',
// 'product_new_weight',
// 'iron_filings_weight',
// 'addition_file_path',
// 'notes',]

let info_type = {
	text: 'text',
	time: 'time',
	label: 'label',
	file: 'file',
}

let table_info = {
	id: {
		enable_search: true,
		type: info_type.label,
	},
	order_id: {
		enable_search: true,
		type: info_type.label,
	},
	customer: {
		enable_search: true,
		type: info_type.label,
	},
	product_name: {
		enable_search: true,
		type: info_type.label,
	},
	product_per_price: {
		enable_search: true,
		type: info_type.label,
	},
	product_num: {
		enable_search: true,
		type: info_type.label,
	},
	product_sum_price: {
		enable_search: true,
		type: info_type.label,
	},
	order_time: {
		enable_search: true,
		type: info_type.label,
	},
	cutting_time: {
		enable_search: false,
		type: info_type.time,
	},
	forg_company_name: {
		enable_search: false,
		type: info_type.text,
	},
	roughcast_price: {
		enable_search: false,
		type: info_type.text,
	},
	roughcast_processing_fee: {
		enable_search: false,
		type: info_type.text,
	},
	material_return_time: {
		enable_search: false,
		type: info_type.time,
	},
	manager_person_name: {
		enable_search: false,
		type: info_type.text,
	},
	processing_person_name: {
		enable_search: false,
		type: info_type.text,
	},
	priduct_processing_fee: {
		enable_search: false,
		type: info_type.text,
	},
	roughcast_weight: {
		enable_search: true,
		type: info_type.text,
	},
	product_new_weight: {
		enable_search: true,
		type: info_type.text,
	},
	iron_filings_weight: {
		enable_search: true,
		type: info_type.text,
	},
	addition_file_path: {
		enable_search: true,
		type: info_type.file,
	},
	notes: {
		enable_search: true,
		type: info_type.text,
	},
}
let search_config = {
	// id: {
	// 	enable_search: false,
	// 	type: info_type.label,
	// 	value:""
	// },
	order_id: {
		enable_search: false,
		type: info_type.label,
		value:""
	},
	customer: {
		enable_search: false,
		type: info_type.label,
		value:""
	},
	product_name: {
		enable_search: false,
		type: info_type.label,
		value:""
	},
	// product_per_price: {
	// 	enable_search: false,
	// 	type: info_type.label,
	// 	value:""
	// },
	// product_num: {
	// 	enable_search: false,
	// 	type: info_type.label,
	// 	value:""
	// },
	// product_sum_price: {
	// 	enable_search: false,
	// 	type: info_type.label,
	// 	value:""
	// },
	order_time: {
		enable_search: false,
		type: info_type.time,
		value:""
	},
	cutting_time: {
		enable_search: false,
		type: info_type.time,
		value:""
	},
	forg_company_name: {
		enable_search: false,
		type: info_type.text,
		value:""
	},
	// roughcast_price: {
	// 	enable_search: false,
	// 	type: info_type.text,
	// 	value:""
	// },
	// roughcast_processing_fee: {
	// 	enable_search: false,
	// 	type: info_type.text,
	// 	value:""
	// },
	material_return_time: {
		enable_search: false,
		type: info_type.time,
		value:""
	},
	manager_person_name: {
		enable_search: false,
		type: info_type.text,
		value:""
	},
	processing_person_name: {
		enable_search: false,
		type: info_type.text,
		value:""
	},
	// priduct_processing_fee: {
	// 	enable_search: false,
	// 	type: info_type.text,
	// 	value:""
	// },
	// roughcast_weight: {
	// 	enable_search: false,
	// 	type: info_type.text,
	// 	value:""
	// },
	// product_new_weight: {
	// 	enable_search: false,
	// 	type: info_type.text,
	// 	value:""
	// },
	// iron_filings_weight: {
	// 	enable_search: false,
	// 	type: info_type.text,
	// 	value:""
	// },
	// addition_file_path: {
	// 	enable_search: false,
	// 	type: info_type.text,
	// 	value:""
	// },
	notes: {
		enable_search: false,
		type: info_type.text,
		value:""
	},
}

// ?????????????????????????????????????????????????????????????????????????????????
var warming_days = 5

let test = {
	table_data,
	table_header,
	table_info,
	info_type,
	search_config,
	warming_days
}
export default test
