# по данному целому неотрицательному N вычислить N факториал

number = int(input("Введите N: "))
factorial_number = 1 #результирующая переменная
i = 1 #счетчик

#факториал 0 = 1
if number == 0:
    factorial_number = 1

#нахождение факториала
while i <= number:
    factorial_number *= i
    i += 1

#вывод результата
print(factorial_number)