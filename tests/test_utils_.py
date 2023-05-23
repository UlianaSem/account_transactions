import contextlib, io
import pytest
from src import utils


@pytest.fixture
def get_list_for_test():
    data_to_be_processed = [{"id": 522357576, "state": "EXECUTED", "date": "2019-07-12T20:41:47.882230",
                             "operationAmount": {"amount": "51463.70", "currency": {"name": "USD", "code": "USD"}},
                             "description": "Перевод организации", "from": "Счет 48894435694657014368",
                             "to": "Счет 38976430693692818358"},
                            {"id": 895315941, "state": "EXECUTED", "date": "2018-08-19T04:27:37.904916",
                             "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
                             "description": "Перевод с карты на карту", "from": "Visa Classic 6831982476737658",
                             "to": "Visa Platinum 8990922113665229"},
                            {"id": 596171168, "state": "EXECUTED", "date": "2018-07-11T02:26:18.671407",
                             "operationAmount": {"amount": "79931.03", "currency": {"name": "руб.", "code": "RUB"}},
                             "description": "Открытие вклада", "to": "Счет 72082042523231456215"},
                            {"id": 716496732, "state": "EXECUTED", "date": "2018-04-04T17:33:34.701093",
                             "operationAmount": {"amount": "40701.91", "currency": {"name": "USD", "code": "USD"}},
                             "description": "Перевод организации", "from": "Visa Gold 5999414228426353",
                             "to": "Счет 72731966109147704472"},
                            {"id": 863064926, "state": "EXECUTED", "date": "2019-12-08T22:46:21.935582",
                             "operationAmount": {"amount": "41096.24", "currency": {"name": "USD", "code": "USD"}},
                             "description": "Открытие вклада", "to": "Счет 90424923579946435907"},
                            {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689",
                             "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
                             "description": "Перевод организации", "from": "Visa Platinum 1246377376343588",
                             "to": "Счет 14211924144426031657"}]

    return utils.add_in_class(data_to_be_processed)


def test_formate_data_to_dictionary():
    path_to_test_file = 'tests/test_operations.json'

    assert utils.formate_data_to_dictionary(path_to_test_file) == [{'date': '2019-08-26T10:50:58.294041',
                                                                    'description': 'Перевод организации',
                                                                    'from': 'Maestro 1596837868705199',
                                                                    'id': 441945886, "state": "EXECUTED",
                                                                    "operationAmount": {"amount": "31957.58",
                                                                                        "currency": {"name": "руб.",
                                                                                                     "code": "RUB"
                                                                                                     }
                                                                                        },
                                                                    "to": "Счет 64686473678894779589"},
                                                                   {'date': '2019-07-03T18:35:29.512364',
                                                                    'description': 'Перевод организации',
                                                                    'from': 'MasterCard 7158300734726758',
                                                                    'id': 41428829, "state": "EXECUTED",
                                                                    "operationAmount": {"amount": "8221.37",
                                                                                        "currency": {"name": "USD",
                                                                                                     "code": "USD"
                                                                                                     }
                                                                                        },
                                                                    "to": "Счет 35383033474447895560"}]


def test_add_in_class():
    test_list = [{'date': '2019-08-26T10:50:58.294041', 'description': 'Перевод организации',
                  'from': 'Maestro 1596837868705199', 'id': 441945886, "state": "EXECUTED",
                  "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
                  "to": "Счет 64686473678894779589"},
                 {'date': '2019-07-03T18:35:29.512364', 'description': 'Перевод организации',
                  'from': 'MasterCard 7158300734726758', 'id': 41428829, "state": "EXECUTED",
                  "operationAmount": {"amount": "8221.37", "currency": {"name": "USD", "code": "USD"}},
                  "to": "Счет 35383033474447895560"}]

    s = io.StringIO()

    with contextlib.redirect_stdout(s):
        print(utils.add_in_class(test_list))

    assert s.getvalue() == """[Operation (441945886, "2019-08-26T10:50:58.294041", "EXECUTED", {'amount':""" \
                           """ '31957.58', 'currency': {'name': 'руб.', 'code': 'RUB'}}, "Перевод организации",""" \
                           """ "Maestro 1596837868705199", "Счет 64686473678894779589"), Operation (41428829, "2""" \
                           """019-07-03T18:35:29.512364", "EXECUTED", {'amount': '8221.37', 'currency': {'name': """ \
                           """'USD', 'code': 'USD'}}, "Перевод организации", "MasterCard 7158300734726758", "Сче""" \
                           """т 35383033474447895560")]\n"""


def test_get_last_five_operations(get_list_for_test):
    assert utils.get_last_five_operations(get_list_for_test) == ['08.12.2019 Открытие вклада\n'
                                                                 'Нет данных об исходящем счете -> Счет **5907\n'
                                                                 '41096.24 USD',
                                                                 '12.07.2019 Перевод организации\n'
                                                                 'Счет **4368 -> Счет **8358\n51463.70 USD',
                                                                 '19.08.2018 Перевод с карты на карту\n'
                                                                 'Visa Classic 6831 98** **** 7658 -> Visa Platinum '
                                                                 '8990 92** **** 5229\n'
                                                                 '56883.54 USD',
                                                                 '11.07.2018 Открытие вклада\n'
                                                                 'Нет данных об исходящем счете -> Счет **6215\n'
                                                                 '79931.03 руб.',
                                                                 '04.04.2018 Перевод организации\n'
                                                                 'Visa Gold 5999 41** **** 6353 -> Счет **4472\n'
                                                                 '40701.91 USD']
