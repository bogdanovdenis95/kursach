

import json
from datetime import datetime
from operator import itemgetter
from dateutil import parser

def load_operations(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        operations_data = json.load(file)
    return operations_data

def mask_card_number(card_number):
    masked_number = f"XXXX XXXX XXXX {card_number[-4:]}"
    return masked_number

def mask_account_number(account_number):
    masked_number = f"**{account_number[-4:]}"
    return masked_number

def format_date(date_string):
    try:
        date_obj = parser.parse(date_string)
        formatted_date = date_obj.strftime('%d.%m.%Y')
        return formatted_date
    except ValueError:
        return "Invalid Date"



def get_last_operations(operations):
    # Отсортировать операции по дате в обратном порядке
    sorted_operations = sorted(operations, key=lambda x: x.get('date', ''), reverse=True)[:5]

    result = []

    for operation in sorted_operations:
        # Использовать get для избежания ошибки, если поле 'operationAmount' отсутствует
        amount_currency = operation.get('operationAmount')
        if isinstance(amount_currency, str):
            amount, currency = map(str.strip, amount_currency.split()[:2])
        else:
            amount, currency = '0', 'RUB'

        date = format_date(operation.get('date', ''))
        description = operation.get('description', '')
        from_account = mask_card_number(operation.get('from', ''))
        to_account = mask_account_number(operation.get('to', ''))

        result.append({
            'date': date,
            'description': description,
            'from_account': from_account,
            'to_account': to_account,
            'amount': amount,
            'currency': currency
        })

    return result




if __name__ == "__main__":
    file_path = "operations.json"
    operations_data = load_operations(file_path)
    last_operations = get_last_operations(operations_data)
    for operation in last_operations:
        print(operation)
