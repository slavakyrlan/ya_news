# test_pdb.py
def integers_counter(data):
    # Создаем счётчик для целых чисел.
    integers_found = 0
    # Перебираем в цикле элементы входного списка.
    for item in data:
        # Если элемент - целое число, то увеличиваем счётчик.
        if isinstance(item, int):
            integers_found += 1
    # Возвращаем счётчик.
    return integers_found


def test_counter():
    # Произвольные данные для анализа.
    data = [False, 1.0, "some_string", 3, True, 1, [], False]
    # Вызываем функцию:
    integers = integers_counter(data)
    # Целых чисел должно быть 2.
    assert integers == 2