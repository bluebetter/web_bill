# coding=utf-8
import json

class Bill:
    """
    Bill Service
    """
    def get_list(start_time='', end_time='', order_by='', limit=''):
        bill_list = [
            {
                'id': 1,
                'date': '2020-01-01 00:00:00',
                'amount': 100.00,
                'remark': '',
            },
            {
                'id': 2,
                'date': '2020-01-01 00:00:00',
                'amount': -100.00,
                'remark': '',
            }
        ]
        return json.dumps(bill_list)
    
    def add(date, amount ,remark=''):
        raise Exception('todo')

    def delete(id):
        raise Exception('todo')

    def update(id, date, amount, remark=''):
        raise Exception('todo')


if __name__ == "__main__":
    pass
