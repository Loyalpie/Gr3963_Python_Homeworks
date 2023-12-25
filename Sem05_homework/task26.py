# Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.

def power_number(a, b, temp):
    while b > 1:
        return power_number(a * temp, b - 1, temp)
    return a

number_one = int(input("Введите число A: "))
number_two = int(input("Введите число B: "))

temp = number_one #на нее будем домножать

print(power_number(number_one, number_two, temp))