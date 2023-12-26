# Два различных натуральных числа n и m называются дружественными, 
# если сумма делителей числа n (включая 1, но исключая само n) равна числу m и наоборот. 
# Например, 220 и 284 – дружественные числа. По данному числу k выведите все пары дружественных чисел, 
# каждое из которых не превосходит k. Программа получает на вход одно натуральное число k, 
# не превосходящее 105. Программа должна вывести  все пары дружественных чисел, каждое из которых не превосходит k.

#функция находит сумму всех делителей числа number
def search_dividers_number(number):
    sum_dividers = 0
    for i in range(1, number):
        if number % i == 0:
            sum_dividers += i
    return sum_dividers #возвращает сумму всех делителей числа number

number = int(input("Введите число: "))

temp_i = 0

for i in range(1, number + 1):
    sum_dividers = search_dividers_number(i)
    if i == search_dividers_number(sum_dividers) and sum_dividers != search_dividers_number(sum_dividers) and temp_i != sum_dividers:
        temp_i = i
        print(i, sum_dividers)