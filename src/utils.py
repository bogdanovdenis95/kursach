# utils.py

import json


def load_operations(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        operations_data = json.load(file)
    return operations_data


def get_last_operations(operations, n=5):
    # Функция сортировки операций
    def get_date(operation):
        date = operation.get('date', '')
        return date or '9999-12-31'  # Значение по умолчанию для сортировки

    sorted_operations = sorted(operations, key=get_date, reverse=True)
    return sorted_operations[:n]

