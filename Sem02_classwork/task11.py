# Дано натуральное число A > 1. Определите, каким по
# счету числом Фибоначчи оно является, то есть
# выведите такое число n, что φ(n)=A. Если А не
# является числом Фибоначчи, выведите число -1.

number = int(input("Введите число А: "))
fibonachi_first_number = 0
fibonachi_second_number = 1
current_fibonachi = 0
count = 1


while current_fibonachi <= number:
    # 0 стоит на 0 месте в последовательности Фибоначчи
    if number == 0:
        print(f"Число {number} является числом Фибоначчи. Порядковый номер: 0")
        break
    #выход из цикла когда текуще число Фибоначчи будет равно введенному числу
    if number == current_fibonachi:
        print(f"Число {number} является числом Фибоначчи. Порядковый номер: {count}")
        break
    #если не равно то делаем эти махинации)
    else:
        current_fibonachi = fibonachi_first_number + fibonachi_second_number
        fibonachi_first_number = fibonachi_second_number
        fibonachi_second_number = current_fibonachi
        count += 1
    #если вышли цикла - выводим -1 (текущее стало больше введенного числа и не входит в последовательность Фибоначчи)
    if current_fibonachi > number:
        print(-1)