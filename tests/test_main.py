from kursach.src.main import get_last_operations, format_date, mask_card_number, mask_account_number

def test_get_last_operations():
    # Подготовим тестовые данные
    sample_operations = [
        {
            "date": "08.12.2019",
            "description": "Открытие вклада",
            "from": "XXXX XXXX XXXX 1234",
            "to": "**5907",
            "operationAmount": "0 RUB"
        },
        {
            "date": "07.12.2019",
            "description": "Перевод организации",
            "from": "XXXX XXXX XXXX 9012",
            "to": "**3655",
            "operationAmount": "0 RUB"
        },
        # Добавьте другие операции по аналогии
    ]

    # Вызовем тестируемую функцию
    last_operations = get_last_operations(sample_operations)

    # Проведем проверки
    assert len(last_operations) == 2  # Предполагаем, что в тестовых данных 2 операции
    assert last_operations[0]['date'] == '12.08.2019'

    assert last_operations[1]['description'] == 'Перевод организации'

def test_format_date():
    # Проверим форматирование даты
    formatted_date = format_date("2019-12-08T22:46:21.935582")
    assert formatted_date == "08.12.2019"

def test_mask_card_number():
    # Проверим маскирование номера карты
    masked_card = mask_card_number("1234 5678 9012 3456")
    assert masked_card == "XXXX XXXX XXXX 3456"

def test_mask_account_number():
    # Проверим маскирование номера счета
    masked_account = mask_account_number("1234567890123456")
    assert masked_account == "**3456"

