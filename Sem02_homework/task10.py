# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, 
# чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть

import random

quantity_coins = int(input("Введите число монеток: "))
coins = [] # только квадратные скобки, т.к. заполнять будем с помощью .append()

#append - заполнение списка
for i in range(quantity_coins):
    coins.append(random.randint(0, 1))  # монетка либо орел(0) либо решка(1) 

print(coins) #вывод списка

count_heads = 0 #счетчик монеток стороной "орел"
count_tails = 0 #счетчик монеток стороной "решка"

# заполнение счетчиков "орел" и "решка"
for i in range(quantity_coins):
    if coins[i] == 0:
        count_heads += 1
    elif coins[i] == 1:
        count_tails += 1

print(count_heads if count_heads < count_tails else count_tails)