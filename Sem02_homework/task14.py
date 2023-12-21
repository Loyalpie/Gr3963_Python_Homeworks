# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

number = int(input("Введите N: "))

power = 0
result = None
result = 2 ** power

while result < number:
    print(result)
    result = 2 ** power
    power += 1