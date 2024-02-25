# Создать телефонный справочник с
# возможностью импорта и экспорта данных в
# формате .txt. Фамилия, имя, отчество, номер
# телефона - данные, которые должны находиться
# в файле

# функция считывает текст из файла
def read_text_from_file():
    with open ('Sem08_classwork/Phonebook.txt', 'r', encoding='utf-8') as data:
            text = data.read() # считываем весь текст из файла
            text = text.split() # делаем split текста
    return text

# функция обработки текущего контакта из списка в строку
def treatment_current_contact(text, contact_num):
    elem = 4 # количество элементов в контакте (4 - фамилия, имя, отчество, телеф)
    current_contact = list((text[0 + elem * contact_num] + ' ' + text[1 + elem * contact_num] + ' ' + text[2 + elem * contact_num] + ' ' + text[3 + elem * contact_num]).split())
    current_contact_string = str(current_contact[0]) + ' ' + str(current_contact[1]) + ' ' + str(current_contact[2]) + ' ' + str(current_contact[3])
    return current_contact_string

# функция выводит список всех контактов
def print_list_contacts(text):
    counter_contacts = 1 # счетчик номера п/п контактов
    for i in range(0, len(text), 4):
        contact_num = i // 4
        current_contact_string = treatment_current_contact(text, contact_num)

        # печатеам контакт
        print(str(counter_contacts) + '.', current_contact_string)
        counter_contacts += 1

# функция удаляет контакт из книжки
def delete_contact():
    text = read_text_from_file() # считываем текст из файла
    print_list_contacts(text) # выводим список всех контактов

    print("\nВсего контактов: ", int(len(text) / 4))
    contact_number = int(input("Удалить контакт (введите порядковый номер контакта): ")) - 1 # -1 т.к. нумерация с нуля
    
    current_contact_string = treatment_current_contact(text, contact_number) # обрабатываем текущий контакт
            
    # вывод контакта
    print('\nУдалено: ', current_contact_string, '\n')

    # удаляем данные
    for i in range(4):
        text.pop(contact_number * 4)

    # заново заполняем книгу без удаленного контакта
    with open ('Sem08_classwork/Phonebook.txt', 'w', encoding='utf-8') as data:
        for i in range(int(len(text) / 4)):
            data.write('\n')
            contact_num = i
            current_contact_string = treatment_current_contact(text, contact_num) # обрабатываем текущий контакт
            #print(current_contact_string)
            data.write(current_contact_string) # записываем контакт в книгу

    text = read_text_from_file() # считываем текст из файла
    print_list_contacts(text) # выводим список всех контактов

# функция изменяет данные контакта
def edit_contact():
    text = read_text_from_file() # считываем текст из файла
    print_list_contacts(text) # выводим список всех контактов

    contact_number = int(input("Изменить контакт (введите порядковый номер контакта): ")) - 1 # -1 т.к. нумерация с нуля
    current_contact_string = treatment_current_contact(text, contact_number) # обрабатываем текущий контакт

#edit_contact()

# заголовочное меню
def input_answer():
    print("\033c", end="") # очищаем терминал

    print('1. Добавить контакт')
    print('2. Считать информацию')
    print('3. Найти контакт')
    print('4. Удалить контакт')

    # принимаем на вход число action - действие
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
        print("\033c", end="") #очистка консоли
        text = read_text_from_file() # считываем текст из файла
        print_list_contacts(text) # выводим контакты

    # поиск контакта по данным
    elif action == 3:
        print("\033c", end="") #очистка консоли
        text = read_text_from_file() # считываем текст из файла

        search_contact = input('Найти (введите имя/фамилию/отчество/номер телефона): ')

        # проверяем все элементы списка (каждые 4 элемента - 1 контакт) 
        for i in range(len(text)):
                
            # если значение которое ввел пользователь совпадает с каким-то элементом списка (будь то фамилия имя и т.п.)
            if search_contact == text[i]: 
                contact_num = i // 4

                current_contact_string = treatment_current_contact(text, contact_num) # обрабатываем текущий контакт
                    
                # вывод контакта
                print(contact_num + 1, current_contact_string)
    
    # удаление контакта из книжки
    elif action == 4:
        print("\033c", end="") # очистка консоли
        delete_contact() 

# ПРОГРАММА
# спрашиваем пользователя что делать
action = input_answer()

# и делаем)
main_process(action)