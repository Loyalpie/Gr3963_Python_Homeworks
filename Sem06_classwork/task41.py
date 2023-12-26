# Дан список, состоящий из целых чисел. 
# Напишите программу, которая в данном списке определит количество элементов, 
# у которых два соседних и, при этом, оба соседних элемента меньше данного.

#функция генерации списка с рандомными  целыми числами
def gen_list_random(length, min_value, max_value):
    import random
    my_list = []
    for _ in range(length):
        my_list.append(random.randrange(min_value, max_value))
    return my_list

#функция подсчета тех элементов в списке, у которых 2 соседа-числа и оба меньше этого элемента
def count_elems(list):
    count = 0
    for i in range(1, len(list) - 1):
        if list[i - 1] < list[i] and list[i + 1] < list[i]: count += 1 
    return count

my_list = gen_list_random(10, -10, 10)
print(my_list)
print(count_elems(my_list))