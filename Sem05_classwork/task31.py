# Требуется найти N-е число Фибоначчи через рекурсию.

def fib(number_index):
    if number_index in [0, 1]:
        return number_index
    return fib(number_index - 1) + fib(number_index - 2)


number_index = int(input("Введите номер числа Фибоначчи: "))
print(f"{number_index}-е число Фибоначчи равно: {fib(number_index)}")