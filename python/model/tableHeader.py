
class TableHeader(object):
    def __init__(self):
        self._col = {}
        self._num = 0

    @property
    def col(self):
        return self._col

    @property
    def num(self):
        return self._num

    @num.setter
    def num(self, new_num):
        self._num = new_num
