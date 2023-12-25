# Дано натуральное число N и последовательность из N элементов. Требуется вывести эту последовательность в обратном порядке.

def numbers(n, s = ''):
    if n > 0:
        s += str(n) + ' '
        return numbers(n-1, s)
    return s

number = int(input("Введите число: "))

print(numbers(number))