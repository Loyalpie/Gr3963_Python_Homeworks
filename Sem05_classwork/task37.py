# Дано натуральное число N и последовательность из N элементов. Требуется вывести эту последовательность в обратном порядке.

def numbers(n):
    while n >= 0:
        print(f'{n}', end=" ")
        return numbers(n-1)
    return -1

number = int(input("Введите число: "))

numbers(number)