
import json

from kur.class_ import Operation
from kur.settings import DATA


class SortedList:
    def __init__(self):
        self.data_json = DATA

    def read_json(self):
        with open(self.data_json, encoding='utf-8') as f:
            return json.load(f)

    def true_list(self):
        q = self.read_json()
        q.remove({})
        return q

    def true_five_dict(self):
        q = self.true_list()
        return sorted(q,
                      key=lambda operation_data: (operation_data['state'], operation_data['date']),
                      reverse=True
                      )[:5]

    def new_true_five_dict(self):
        q = self.true_five_dict()
        list_ = []
        for i in q:
            list_.append(Operation(id_=i['id'],
                                   date_1=i['date'],
                                   state=i['state'],
                                   operation_amount=i['operationAmount'],
                                   description=i['description'],
                                   to=i['to'],
                                   from_=i.get('from')
                                   ))
        return list_
