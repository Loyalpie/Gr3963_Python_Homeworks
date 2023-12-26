# Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

#функция генерации списка с рандомными  целыми числами
def gen_list_random(length, min_value, max_value):
    import random
    my_list = []
    for _ in range(length):
        my_list.append(random.randrange(min_value, max_value))
    return my_list

#функция находит индексы списка, под которыми числа удовлетворяют условию (min < list[i] < max)
def search_indexes(min_value, max_value, list = []):
    list_result = []
    for i in range(len(list)):
        if min_value < list[i] < max_value: list_result.append(i)
    return list_result

min_value = int(input("Введите минимальное значение: "))
max_value = int(input("Введите максимальное значение: "))

print(list_1 := gen_list_random(10, -10, 10))
print(answer_list := search_indexes(min_value, max_value, list_1))