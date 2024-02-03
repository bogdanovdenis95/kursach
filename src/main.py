from utils import load_operations, get_last_operations, print_last_operations


def redact_info(operation):
    redacted_info = operation.copy()

    if 'from' in redacted_info:
        redacted_info['from'] = redacted_info['from'][-4:].rjust(len(redacted_info['from']), '*')

    if 'to' in redacted_info:
        redacted_info['to'] = redacted_info['to'][-4:].rjust(len(redacted_info['to']), '*')

    return redacted_info


def main():
    filename = input("Введите путь к файлу с операциями: ")
    operations_data = load_operations(filename)

    if operations_data:
        last_operations = get_last_operations(operations_data)

        if last_operations:
            redacted_operations = [redact_info(operation) for operation in last_operations if
                                   operation.get('state') == 'EXECUTED']
            print_last_operations(redacted_operations)
        else:
            print("Нет выполненных операций.")
    else:
        print("Не удалось загрузить данные операций.")


if __name__ == "__main__":
    main()

