# Напишите программу, которая принимает на вход строку, и отслеживает, сколько раз каждый символ уже встречался. 
# Количество повторов добавляется к символам с помощью постфикса формата _n
# Input: a a a b c a a d c d d Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2

my_string = input("Введите строку: ")
my_list = list(my_string)
my_dictionary = {}

print(my_list)

#заполнение словаря
for letter in my_list:
    #если символ есть в словаре увеличиваем счетчик на 1
    if letter in my_dictionary: 
        my_dictionary[letter] += 1
    #если нет то создаем счетчик и присваиваем значение 1
    else: 
        my_dictionary[letter] = 1
    count_of_repeats = my_dictionary[letter] #переменная - количество повторов
    print(f"{letter}_{count_of_repeats - 1}" if count_of_repeats > 1 else letter, end = ' ')