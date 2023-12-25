# Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные оценки на максимальные. 
# Напишите программу, которая заменяет оценки Василия, но наоборот: все максимальные – на минимальные.

import random

list_grade = [] # журнал оценок
list_length = 10 #кол-во оценок

#генерация оценок в журнале
for i in range(list_length):
    list_grade.append(random.randrange(1,6))

print(list_grade)

#поиск минимальной и максимальной оценки
max_grade = max(list_grade)
min_grade = min(list_grade)

#замена максимальных на минимальные
for i in range(list_length):  
    if list_grade[i] == max_grade: list_grade[i] = min_grade

print(list_grade)