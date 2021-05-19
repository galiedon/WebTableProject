import openpyxl


class ExcelHelper(object):
    def __init__(self, filepath):
        self._filepath = filepath
        self._workbook = openpyxl.load_workbook(filepath)
