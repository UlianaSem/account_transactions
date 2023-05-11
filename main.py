import utils


def main():
    """
    Задает основной алгоритм программы
    """
    operations_data = utils.formate_data_to_dictionary(FILE_NAME)
    operations_data_list = utils.add_in_class(operations_data)
    last_five_operations = utils.get_last_five_operations(operations_data_list)

    print('\n\n'.join(last_five_operations))


FILE_NAME = 'operations.json'

if __name__ == '__main__':
    main()
