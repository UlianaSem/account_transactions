from random import choice


def partition(sortable_array, left, right):
    """
    Процедура разбиения массива в алгоритме Быстрой сортировки
    :param sortable_array: массив с данными
    :param left: индекс начала массива
    :param right: индекс конца массива
    :return: индексы для функции quicksort
    """
    support_element = choice(sortable_array[left:right + 1])
    left_array_index = left

    for array_index in range(left, right + 1):
        if sortable_array[array_index].operation_date < support_element.operation_date:
            sortable_array[array_index], sortable_array[left_array_index] = sortable_array[left_array_index],\
                sortable_array[array_index]

            left_array_index += 1

    right_array_index = left_array_index

    for array_index in range(left_array_index, right + 1):
        if sortable_array[array_index].operation_date == support_element.operation_date:
            sortable_array[array_index], sortable_array[right_array_index] = sortable_array[right_array_index],\
                sortable_array[array_index]

            right_array_index += 1

    return left_array_index, right_array_index


def quicksort(sortable_array, left, right):
    """
    Реализует рекурсивный алгоритм Быстрой сортировки
    :param sortable_array: массив с данными
    :param left: индекс начала массива
    :param right: индекс конца массива
    :return: отсортированный массив
    """
    if left < right:
        left_array_index, right_array_index = partition(sortable_array, left, right)

        quicksort(sortable_array, left, left_array_index)
        quicksort(sortable_array, right_array_index, right)

    return sortable_array
