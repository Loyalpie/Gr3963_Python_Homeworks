# Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.

# Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества. 
# Затем пользователь вводит сами элементы множеств.

import random

length_first_list = int(input("Введите количество элементов первой последовательности: "))
length_second_list = int(input("Введите количество элементов второй последовательности: "))

first_list = []
second_list = []

#заполнение первого списка
for i in range(length_first_list):
    first_list.append(random.randrange(-20,20)) #случайными числами

#заполнение второго списка
for i in range(length_second_list):
    second_list.append(random.randrange(-20,20)) #случайными числами

result_list = []

#заполнение результирующего списка 
for i in range(length_first_list): #перебор всех элементов первого списка
    for j in range(length_second_list): #перебор всех элементов второго списка
        #добавление элемента (который и в 1 и во 2 списке) только если его нет в результирующем списке (чтобы избежать повторов)
        if first_list[i] == second_list[j]: 
            if first_list[i] not in result_list:
               result_list.append(first_list[i])

print(first_list)
print(second_list)
print(result_list)

for i in range(len(result_list)):
    for j in range(len(result_list)-1):
        if result_list[j + 1] < result_list[j]:
            result_list[j + 1], result_list[j] = result_list[j], result_list[j + 1] 

print(result_list)