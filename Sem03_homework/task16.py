# Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

length = int(input("Введите длину последовательности: "))

numbers = []

#заполнение списка с клавы
for i in range(length):
    num = int(input(f"Элемент {i}: "))
    numbers.append(num)

print(numbers)

num = int(input("Введите число: "))

count = 0

for i in range(length):
    if numbers[i] == num:
        count += 1
    
print(count)