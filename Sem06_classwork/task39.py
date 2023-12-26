# Даны два списка чисел. Требуется вывести те элементы первого списка (в том порядке, в каком они идут в первом списке), которых нет во втором массиве

import random

list_1 = []
list_2 = []
list_result = []

length_list_1 = int(input("Длина первого списка: "))
length_list_2 = int(input("Длина второго списка: "))

#первый список будет длинее второго)
if length_list_2 > length_list_1: 
    length_list_1, length_list_2 = length_list_2, length_list_1

#заполнение 1 списка
for i in range(length_list_1):
    list_1.append(random.randrange(-10, 10))

#заполнение 2 списка
for i in range(length_list_2):
    list_2.append(random.randrange(-10, 10))

#нахождение элементов которые есть в 1 списке но нет во 2
for i in range(length_list_1):
    if list_1[i] not in list_2:
        list_result.append(list_1[i])

print(list_1)
print(list_2)
print(list_result)