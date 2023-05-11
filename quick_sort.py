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
    m = left
    for i in range(left, right + 1):
        if sortable_array[i].operation_date < support_element.operation_date:
            sortable_array[i], sortable_array[m] = sortable_array[m], sortable_array[i]
            m += 1
    n = m
    for j in range(m, right + 1):
        if sortable_array[j].operation_date == support_element.operation_date:
            sortable_array[j], sortable_array[n] = sortable_array[n], sortable_array[j]
            n += 1
    return m, n


def quicksort(sortable_array, left, right):
    """
    Реализует рекурсивный алгоритм Быстрой сортировки
    :param sortable_array: массив с данными
    :param left: индекс начала массива
    :param right: индекс конца массива
    :return: отсортированный массив
    """
    if left < right:
        lt, gt = partition(sortable_array, left, right)
        quicksort(sortable_array, left, lt)
        quicksort(sortable_array, gt, right)
    return sortable_array
