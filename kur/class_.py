import re

from datetime import datetime


class Operation:
    def __init__(self, id_, date_1, state, operation_amount, description, to, from_=''):
        self.id_ = id_
        self.date_1 = self.correct_data(date_1)
        self.state = state
        self.operation_amount = operation_amount
        self.description = description
        self.from_ = self.hide_number(from_) if from_ else ''
        self.to = self.hide_number(to)

    @staticmethod
    def correct_data(date_2):
        str_date = datetime.strptime(date_2, '%Y-%m-%dT%H:%M:%S.%f')
        return datetime.strftime(str_date, '%d-%m-%Y')

    @staticmethod
    def hide_number(way):
        if way.startswith('Счет'):
            delete_word = re.sub(r'[a-z]+\s?', '', way.lower()).strip()
            delete_digit = re.sub(r'\d+\s?', '', way).strip()
            replace_stars = (len(delete_word[:2]) * '*') + delete_word[-4:]
            return f"{delete_digit} {replace_stars}"
        delete_word = re.sub(r'[a-z]+\s?', '', way.lower()).strip()
        delete_digit = re.sub(r'\d+\s?', '', way).strip()
        git_asterisk_for_from = delete_word[:6] + (len(delete_word[6:-4]) * '*') + delete_word[-4:]
        replace_stars = " ".join([git_asterisk_for_from[i:i + 4] for i in range(0, len(git_asterisk_for_from), 4)])
        return f"{delete_digit} {replace_stars}"

    def __repr__(self):
        return f'{self.date_1} {self.description}\n ' \
               f'{self.from_} -> {self.to}\n' \
               f'{self.operation_amount["amount"]} {self.operation_amount["currency"]["name"]}\n'

    def __str__(self):
        return f'{self.date_1} {self.description}\n'\
               f'{self.from_} -> {self.to}\n' \
               f'{self.operation_amount["amount"]} {self.operation_amount["currency"]["name"]}\n'
