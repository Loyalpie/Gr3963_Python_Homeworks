# Дан список чисел. Определите, сколько в нем встречается различных чисел.

length = int(input("Введите количество элементов: "))

numbers = []

#заполнение списка с клавы
for i in range(length):
    num = int(input(f"Элемент {i}: "))
    numbers.append(num)

print(numbers)

set_from_my_list = set(numbers) #список превращается в множество (в множестве нет одинаковых значений)
print(len(set_from_my_list))