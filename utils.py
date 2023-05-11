import json
from operations_class import Operation
from quick_sort import quicksort


def formate_data_to_dictionary(file_name):
    """
    Считает данные из формата JSON и добавляет их в словарь
    :param file_name: путь к файлу
    :return: словарь с данными по операциям
    """
    with open(file_name, 'r', encoding='UTF-8') as file:
        data_from_file = file.read()

    operations_data = json.loads(data_from_file)
    return operations_data


def add_in_class(operations_data):
    """
    Добавляет данные из словаря с операциями в класс Operation
    :param operations_data: словарь с данными по операциям
    :return: список с экземплярами класса Operation
    """
    operations_data_list = []
    for operation in operations_data:
        if len(operation) == 0:
            continue

        else:
            if operation.get('from') is None:
                operations_data_list.append(Operation(operation['id'], operation['date'], operation['state'],
                                                      operation['operationAmount'], operation['description'],
                                                      operation['to']))
            else:
                operations_data_list.append(Operation(operation['id'], operation['date'], operation['state'],
                                                      operation['operationAmount'], operation['description'],
                                                      operation['to'], operation['from']))

    return operations_data_list


def get_last_five_operations(operations_data_list):
    """
    Возвращает список с пятью последними успешными операциями
    :param operations_data_list: список с экземплярами класса Operation
    :return: список с пятью последними успешными операциями в нужном формате
    """
    i = 0
    last_five_operations = []

    sorted_operations_data_list = quicksort(operations_data_list, 0, len(operations_data_list) - 1)

    for operation in reversed(sorted_operations_data_list):
        if operation.transfer_state == "EXECUTED":
            last_five_operations.append(operation.build_response())
            i += 1
            if i == 5:
                break
        else:
            continue

    return last_five_operations
