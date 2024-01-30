

import pytest
from main import load_operations, get_last_operations

@pytest.fixture
def sample_operations():
    # Вместо этого вы можете использовать реальные тестовые данные
    return [
        {"date": "01.01.2023", "description": "Payment", "from": "1234567890123456", "to": "9876543210987654", "operationAmount": "100 USD"},
        {"date": "02.01.2023", "description": "Transfer", "from": "1234567890123456", "to": "9876543210987654", "operationAmount": "50 EUR"},
        {"date": "03.01.2023", "description": "Deposit", "from": "", "to": "9876543210987654", "operationAmount": "2000 RUB"},
        {"date": "04.01.2023", "description": "Withdrawal", "from": "1234567890123456", "to": "", "operationAmount": "5000 JPY"},
        {"date": "05.01.2023", "description": "Purchase", "from": "1234567890123456", "to": "9876543210987654", "operationAmount": "150 GBP"},
    ]

def test_get_last_operations(sample_operations):
    last_operations = get_last_operations(sample_operations)

    assert len(last_operations) == 5

    expected_dates = ["05.01.2023", "04.01.2023", "03.01.2023", "02.01.2023", "01.01.2023"]
    for i, operation in enumerate(last_operations):
        assert operation['date'] == expected_dates[i]



