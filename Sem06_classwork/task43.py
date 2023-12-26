# Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу. 
# Считается, что любые два элемента, равные друг другу образуют одну пару, которую необходимо посчитать. 

#функция генерации списка с рандомными  целыми числами
def gen_list_random(length, min_value, max_value):
    import random
    my_list = []
    for _ in range(length):
        my_list.append(random.randrange(min_value, max_value))
    return my_list

#создание словаря, в котором ключ - число (элемент списка), значение - сколько раз встречается этот элемент в списке
def count_pair_numbers(list):
    count_dict = {} #словарь
    pair_counter = 0 #счетчик пар
    
    #заполнение словаря
    for i in range(len(list)):
        if list[i] not in count_dict: count_dict[list[i]] = 1 #если данного i элемента нет в словаре, добавляем и считаем как 1 шт
        else: count_dict[list[i]] += 1 #если уже есть - увеличиваем на 1 шт

    set_dict = set(count_dict) #создаем множество, в котором ключи словаря

    #подсчет количества пар
    for i in range(min(set_dict), max(set_dict) + 1 ): #диапазон чисел от минимального до максимального значения в этом множестве (i - число в словаре, КЛЮЧ)
        if i in set_dict: #проверка, есть ли i в множестве (допустим, список [1, 4, 6, 8], чисел 3, 5, 7 НЕТ в списке, поэтому их надо пропустить)
            pair_counter += count_dict[i] // 2 # делим нацело количество чисел i в словаре на 2 (т.к. пара - 2 числа)
    
    return pair_counter 

print(my_list :=gen_list_random(10, -5, 5))
print('Всего пар чисел: ', my_counter := count_pair_numbers(my_list))