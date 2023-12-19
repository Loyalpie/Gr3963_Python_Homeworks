# Найдите сумму цифр трехзначного числа.

number = int(input("Введите 3-значное число: "))

result = int(number / 100) + int(number % 100 / 10) + int(number % 100 % 10)

print(f"{int(number / 100)} + {int(number % 100 / 10)} + {int(number % 100 % 10)} = {result}")