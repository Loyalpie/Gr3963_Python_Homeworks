# Напишите рекурсивную функцию sum(a, b), 
# возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

def sum(a, b):
    while b > 0:
        return sum(a+1, b-1)
    return a

number_one = int(input("Введите число A: "))
number_two = int(input("Введите число B: "))

print(sum(number_one, number_two))