from utils import load_operations, get_last_operations

def print_last_operations(last_operations):
    for operation in last_operations:
        date = operation.get('date', 'N/A')
        state = operation.get('state', 'N/A')
        description = operation.get('description', 'N/A')
        from_account = operation.get('from', 'N/A')
        to_account = operation.get('to', 'N/A')

        operation_amount = operation.get('operationAmount', {})
        amount = operation_amount.get('amount', 'N/A')
        currency = operation_amount.get('currency', {}).get('name', 'N/A')

        if state == 'EXECUTED':
            print(
                f"{date} {description}\n"
                f"{from_account} -> {to_account}\n"
                f"{amount} {currency}\n"
            )
        else:
            print(
                f"{date} {description}\n"
                f"Состояние: {state}\n"
            )

if __name__ == "__main__":
    filename = input("Введите путь к файлу с операциями: ")
    operations_data = load_operations(filename)
    last_operations = get_last_operations(operations_data)
    print_last_operations(last_operations)
