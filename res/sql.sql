-- 创建表
create table orders(id int primary key not null auto_increment,  
order_id text, 
customer text, 
product_name text, 
product_per_price float,
product_num text,
product_sum_price float,
order_time date);

create table data_src_tmp(id int primary key not null auto_increment,  order_id text, customer text, product_name text, product_per_price float,product_num text,product_sum_price float,order_time date);

create table test.orders(id int primary key not null auto_increment,  
order_id text, 
customer text, 
product_name text, 
product_per_price float,
product_num text,
product_sum_price float,
order_time date,
cutting_time timestamp,
forg_company_name text,
roughcast_price float,
roughcast_processing_fee float,
material_return_time timestamp,
manager_person_name text,
processing_person_name text,
priduct_processing_fee float,
roughcast_weight float,
product_new_weight float,
iron_filings_weight float,
addition_file_path text,
notes text
);

-- 查询src_data
select C1, C3, C5, C8, C9, C10, C20 from src_data;

-- 插入
insert into orders(order_id, customer, product_name, product_per_price, product_num, product_sum_price, order_time) values("%s","%s","%s", "%f", "%f", "%f", DATE("2017-06-15"));

insert into orders(order_id, customer, product_name, product_per_price, product_num, product_sum_price, order_time) values("{}","{}","{}", {}, "{}", {}, DATE("{}"));

-- 修改列表
update orders set 
cutting_time = DATE("{}"),
forg_company_name = "{}",
roughcast_price = {},
roughcast_processing_fee = {},
material_return_time = DATE("{}"),
manager_person_name = DATE("{}"),
processing_person_name = "{}",
priduct_processing_fee = {},
roughcast_weight = {},
product_new_weight = {},
iron_filings_weight = {},
addition_file_path = "{}",
notes = "{}"
where id = {};

['update orders set ',
'cutting_time = DATE("{}"),',
'forg_company_name = "{}",',
'roughcast_price = {},',
'roughcast_processing_fee = {},',
'material_return_time = DATE("{}"),',
'manager_person_name = DATE("{}"),',
'processing_person_name = "{}",',
'priduct_processing_fee = {},',
'roughcast_weight = {},',
'product_new_weight = {},',
'iron_filings_weight = {},',
'addition_file_path = "{}",',
'notes = "{}"',
'where id = {};']
update orders set cutting_time = DATE("2021-04-05T16:00:00.000Z"),forg_company_name = "1",roughcast_price = 1,roughcast_processing_fee = 2,material_return_time = DATE("2021-05-26T16:00:00.000Z"),manager_person_name = DATE("2"),processing_person_name = "2",priduct_processing_fee = 2,roughcast_weight = 2,product_new_weight = 2,iron_filings_weight = 2,addition_file_path = "2",notes = "2"where id = 26879;



sql = 'update orders set cutting_time = DATE("%s"), forg_company_name = "%s", roughcast_price = %d, ' \
        'roughcast_processing_fee = %d,material_return_time = DATE("%s"), manager_person_name = DATE("%s"), ' \
        'processing_person_name = "%s", priduct_processing_fee = %d, roughcast_weight = %d, product_new_weight ' \
        '= %d, iron_filings_weight = %d, addition_file_path = "%s", notes = "%s" where id = %d; '

update orders set  cutting_time = DATE("{0}"), forg_company_name = "{1}", roughcast_price = {2}, roughcast_processing_fee = {3}, material_return_time = DATE("{4}"), manager_person_name = DATE("{5}"), processing_person_name = "{6}", priduct_processing_fee = {7}, roughcast_weight = {8}, product_new_weight = {9}, iron_filings_weight = {10}, addition_file_path = "{11}", notes = "{12}"  where id = {13};

 ["", "", "", "", "", "", "", "", "", "", "", "", "", 26879]

--  插入附件
insert into image(path)values("123");

-- 查询id
select id from image where path="%s";