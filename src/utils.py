
import json
from datetime import datetime

def load_operations(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        operations_data = json.load(file)
    return operations_data

def encrypt_account(account):
    # Шифруем только последние 4 цифры
    encrypted_digits = '*' * (len(account) - 4) + account[-4:]
    return encrypted_digits

def format_date(date_str):
    # Преобразуем формат даты
    date_obj = datetime.fromisoformat(date_str)
    return date_obj.strftime('%d.%m.%Y')

def get_last_operations(operations, n=5):
    sorted_operations = sorted([op for op in operations if op.get('state') == 'EXECUTED'],
                               key=lambda x: x.get('date', ''), reverse=True)
    return sorted_operations[:n]

def print_last_operations(operations):
    print("Последние 5 операций:")
    for operation in operations:
        date = format_date(operation.get('date', 'N/A'))
        description = operation.get('description', 'N/A')
        from_account = encrypt_account(operation.get('from', 'N/A'))
        to_account = encrypt_account(operation.get('to', 'N/A'))
        amount = operation.get('operationAmount', {}).get('amount', 'N/A')
        currency = operation.get('operationAmount', {}).get('currency', {}).get('code', 'N/A')

        print(f"{date} {description}")
        print(f"{from_account} -> {to_account}")
        print(f"{amount} {currency}\n")


