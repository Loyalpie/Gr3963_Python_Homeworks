# Дан список, состоящий из целых чисел. 
# Напишите программу, которая подсчитает количество элементов списка, больших предыдущего (элемента с предыдущим номером)

length = int(input("Введите длину последовательности: "))

numbers = []

#заполнение списка с клавы
for i in range(length):
    num = int(input(f"Элемент {i}: "))
    numbers.append(num)

print(numbers)

for i in range(len(numbers)):
    count = 0
    for j in range(len(numbers)):
        if numbers[j] > numbers[i]:
            count += 1
    print(f"Больше {numbers[i]} - {count} чисел")