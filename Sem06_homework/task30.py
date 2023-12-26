# Заполните список элементами арифметической прогрессии. 
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

#функция заполнения списка по формуле an = a1 + (n-1) * d.
def append_list(first_elem, step, quantity, list = []):
    while quantity > 0:
        list.append(first_elem)
        return append_list(first_elem + step, step, quantity - 1, list)
    return list

print(append_list(7, 2, 5, my_list := []))