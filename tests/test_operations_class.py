import pytest
from src import operations_class


@pytest.fixture
def get_object_for_test():
    object_for_test = operations_class.Operation(51314762, "2018-08-25T02:58:18.764678", 'EXECUTED', {
        "amount": "52245.30",
        "currency": {
            "name": "USD",
            "code": "USD"
        }
    }, "Перевод с карты на карту", "Visa Platinum 7825450883088021", "Visa Classic 4040551273087672")

    return object_for_test


def test_get_encrypted_to_number(get_object_for_test):
    object_for_test_ = operations_class.Operation(464419177, "2018-07-15T18:44:13.346362", "CANCELED", {
      "amount": "71024.64",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    }, "Перевод с карты на счет", "Счет 19213886662094884261", "Visa Gold 9657499677062945")

    assert get_object_for_test.get_encrypted_to_number() == 'Visa Platinum 7825 45** **** 8021'
    assert object_for_test_.get_encrypted_to_number() == 'Счет **4261'


def test_get_encrypted_from_number(get_object_for_test):
    object_for_test_ = operations_class.Operation(464419177, "2018-07-15T18:44:13.346362", "CANCELED", {
      "amount": "71024.64",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    }, "Перевод с карты на счет", "Visa Gold 9657499677062945", "Счет 19213886662094884261")

    object_for_test_additional = operations_class.Operation(464419177, "2018-07-15T18:44:13.346362", "CANCELED", {
      "amount": "71024.64",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    }, "Перевод с карты на счет", "Visa Gold 9657499677062945")

    assert get_object_for_test.get_encrypted_from_number() == 'Visa Classic 4040 55** **** 7672'
    assert object_for_test_.get_encrypted_from_number() == 'Счет **4261'
    assert object_for_test_additional.get_encrypted_from_number() == 'Нет данных об исходящем счете'


def test_format_date(get_object_for_test):
    assert get_object_for_test.format_date() == '25.08.2018'


def test_build_response(get_object_for_test):
    assert get_object_for_test.build_response() == '''25.08.2018 Перевод с карты на карту
Visa Classic 4040 55** **** 7672 -> Visa Platinum 7825 45** **** 8021
52245.30 USD'''
