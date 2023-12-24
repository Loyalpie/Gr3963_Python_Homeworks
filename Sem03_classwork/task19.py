# Дана последовательность из N целых чисел и число K. 
# Необходимо сдвинуть всю последовательность (сдвиг - циклический) на K элементов вправо, K – положительное число.

length = int(input("Введите длину последовательности: "))

numbers = []

#заполнение списка с клавы
for i in range(length):
    num = int(input(f"Элемент {i}: "))
    numbers.append(num)

print(numbers)

number = int(input("На сколько сдвигаем вправо? "))

#сдвиг вправо списка на number элементов
for i in range(len(numbers) - number):
    numbers.append(numbers[0]) #добавляем в конец списка элемент [0]
    numbers.pop(0) #удаляем элемент [0]
    
print(numbers)