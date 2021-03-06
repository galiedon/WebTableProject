import os.path

# ip
LOCALHOST = '127.0.0.1'

API_PORT = '5000'

# dbname
DB_TYPE = 'mysql'

USERNAME = 'root'

PASSWORD = '123456'

DB_NAME = 'test'

APP_PATH = os.getcwd()

RES_PATH = os.path.join(APP_PATH, '../res')

EXCEL_FILE_NAME = 'data_from_deal.xlsx'

EXCEL_FILE_PATH = os.path.join(RES_PATH, EXCEL_FILE_NAME)

ADDITION_FILE_PATH = os.path.join(RES_PATH, "pics/")


CREATE_SOURCE_TABLE_DEMO = \
    'create table src_data(C1 Text, C2 Text, C3 Text, C4 Text, C5 Text, C6 Text, C7 Text, C8 Text, ' \
    'C9 Text, C10 Text, C11 Text, C12 Text, C13 Text, C14 Text, C15 Text, C16 Text, C17 Text, ' \
    'C18 Text, C19 Text, C20 Text, C21 Text, C22 Text, C23 Text, C24 Text, C25 Text, C26 Text, ' \
    'C27 Text, C28 Text, C29 Text, C30 Text, C31 Text, C32 Text, C33 Text, C34 Text, C35 Text, ' \
    'C36 Text, C37 Text, C38 Text, C39 Text, C40 Text, C41 Text, C42 Text, C43 Text, C44 Text, ' \
    'C45 Text, C46 Text, C47 Text, C48 Text, C49 Text, C50 Text, C51 Text, C52 Text, C53 Text, ' \
    'C54 Text, C55 Text, C56 Text, C57 Text, C58 Text, C59 Text, C60 Text, C61 Text, C62 Text, ' \
    'C63 Text, C64 Text, C65 Text, C66 Text, C67 Text, C68 Text, C69 Text, C70 Text, C71 Text, ' \
    'C72 Text, C73 Text, C74 Text, C75 Text, C76 Text, C77 Text, C78 Text, C79 Text, C80 Text, ' \
    'C81 Text, C82 Text, C83 Text);'
INSERT_TABLE_DEMO = 'insert into src_data values("C1","C2","C3","C4","C5","C6","C7","C8","C9","C10","C11","C12","C13",' \
                    '"C14","C15","C16","C17","C18","C19","C20","C21","C22","C23","C24","C25","C26","C27","C28","C29",' \
                    '"C30","C31","C32","C33","C34","C35","C36","C37","C38","C39","C40","C41","C42","C43","C44","C45",' \
                    '"C46","C47","C48","C49","C50","C51","C52","C53","C54","C55","C56","C57","C58","C59","C60","C61",' \
                    '"C62","C63","C64","C65","C66","C67","C68","C69","C70","C71","C72","C73","C74","C75","C76","C77",' \
                    '"C78","C79","C80","C81","C82","C83");'
INSERT_TABLE_SQL = ('insert into src_data values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,'
                    '%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,'
                    '%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);')
INSERT_TABLE_DATA = (
    "C1", "C2", "C3", "C4", "C5", "C6", "C7", "C8", "C9", "C10", "C11", "C12", "C13", "C14", "C15", "C16", "C17", "C18",
    "C19", "C20", "C21", "C22", "C23", "C24", "C25", "C26", "C27", "C28", "C29", "C30", "C31", "C32", "C33", "C34",
    "C35",
    "C36", "C37", "C38", "C39", "C40", "C41", "C42", "C43", "C44", "C45", "C46", "C47", "C48", "C49", "C50", "C51",
    "C52",
    "C53", "C54", "C55", "C56", "C57", "C58", "C59", "C60", "C61", "C62", "C63", "C64", "C65", "C66", "C67", "C68",
    "C69",
    "C70", "C71", "C72", "C73", "C74", "C75", "C76", "C77", "C78", "C79", "C80", "C81", "C82", "C83")
INSERT_TABLE_HEAD = 'insert into src_data values('
INSERT_TABLE_END = ');'
