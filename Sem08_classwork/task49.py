# Создать телефонный справочник с
# возможностью импорта и экспорта данных в
# формате .txt. Фамилия, имя, отчество, номер
# телефона - данные, которые должны находиться
# в файле

# заголовочное меню
def input_answer():
    print("\033c", end="") # очищаем терминал

    print('1. Добавить контакт')
    print('2. Считать информацию')
    print('3. Найти контакт')

    # принимаем на вход число action
    action = int(input("Что делаем: "))
    return action # возвращаем значение action

# основной цикл проги
def main_process(action):

    # если action = 1 то добавляем новый контакт
    if action == 1: 
        with open ('Sem08_classwork/Phonebook.txt', 'a', encoding='utf-8') as data:
            contact = [(), (), (), ()]

            print("\033c", end="") # очистка консоли

            contact[0] = input('Фамилия: ')
            contact[1] = input('Имя: ')
            contact[2] = input('Отчество: ')
            contact[3] = input('Номер телефона: ')

            contact_string = str(contact[0]) + ' ' + str(contact[1]) + ' ' + str(contact[2]) + ' ' + str(contact[3])

            data.write('\n' + contact_string)
    
    # если action = 2 то выводим список всех контактов из файла
    elif action == 2:
        with open ('Sem08_classwork/Phonebook.txt', 'r', encoding='utf-8') as data:
            print("\033c", end="") # очистка консоли
            
            # считываем весь текст из файла
            text = data.read()
            print(text)

            # делаем split текста
            text = text.split()

            contact_num = 0 # номер выбранного контакта
            i = 4 # это число - количество элементов контакта (1[фамилия] 2[имя] 3[отчество] 4[телефон])

            print("\nВсего контактов: ", int(len(text) / 4))
            contact_num = int(input("Номер контакта: ")) - 1 # -1 т.к. нумерация с нуля

            #создаем список конкретного выбранного контакта
            contact = list((text[0 + i * contact_num] + ' ' + text[1 + i * contact_num] + ' ' + text[2 + i * contact_num] + ' ' + text[3 + i * contact_num]).split())
            contact_string = str(contact[0]) + ' ' + str(contact[1]) + ' ' + str(contact[2]) + ' ' + str(contact[3])
            
            # вывод контакта
            print(contact_string)


    # поиск контакта по данным
    elif action == 3:
        with open ('Sem08_classwork/Phonebook.txt', 'r', encoding='utf-8') as data:
            print("\033c", end="") #очистка консоли
            text = data.read() #считывание данных

            # делаем split текста
            text = text.split()

            search_contact = input('Найти (имя/фамилия/отчество/номер телефона): ')

            # проверяем все элементы списка (каждые 4 элемента - 1 контакт) 
            # i = 0,1,2,3 - 1 контакт [фамилия][имя][отчество][номер телефона]
            for i in range(len(text)):

                # если значение которое ввел пользователь совпадает с каким-то элементом списка (будь то фамилия имя и т.п.)
                if search_contact == text[i]: 
                    contact_num = i // 4

                    contact = list((text[0 + 4 * contact_num] + ' ' + text[1 + 4 * contact_num] + ' ' + text[2 + 4 * contact_num] + ' ' + text[3 + 4 * contact_num]).split())
                    contact_string = str(contact[0]) + ' ' + str(contact[1]) + ' ' + str(contact[2]) + ' ' + str(contact[3])
                    
                    # вывод контакта
                    print(contact_num + 1, contact_string)

# ПРОГРАММА
# спрашиваем пользователя что делать
action = input_answer()

# и делаем)
main_process(action)