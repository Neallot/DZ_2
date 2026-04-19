print('Приветствую в телефонном справочнике!')
print('Что возможно для Вас сделать?')


def main_menu():    # главное меню
    print("1. Показать все контакты",
          "2. Создать контакт",
          "3. Найти контакт",
          "4. Изменить контакт",
          "5. Удалить контакт",
          "0. Выход", sep="\n")
    print('Выберите пункт меню: ', end='')


def invalid_data():    # неверный ввод на этапе меню
    print('Неверный ввод, возврат к выбору пункта меню')
    print('')


def contact_creation(buffer_dict): # начинаем создавать контакт
    print('Введите данные для создания контакта.')
    while True:  # проверка того, что такого ID еще нет и что он корректно записан
        id_record = input("Введите ID (произвольно от 1 до 4 цифр): ")
        if not id_record.isdigit():
            print("Нужно ввести число")
        elif len(id_record) > 4:
            print("Нужно ввести до 4 цифр")
        elif id_record in buffer_dict:
            print("Такой ID уже существует")
        else:
            break
    while True:  # проверка на отсутствие ввода имени
        name = input("Введите имя: ")
        if name == "":
            print("Обязательно введите любое имя")
        else:
            break
    while True:  # проверка на корректный ввод номера
        number = input("Введите номер из 10 цифр (код страны указывать не нужно): ")
        if not number.isdigit():
            print("Нужно ввести число")
        elif len(number) != 10:
            print("Нужно ввести 10 цифр")
        else:
            break
    comment = input("Напишите комментарий о контакте (опционально): ")
    print(f'Был создан контакт ID:{id_record} {name.title()}: +7{number} (Заметка: {comment})')
    return id_record, name, f'+7{number}', comment


def find_contact(buffer_dict): # поиск по данным, кроме ID
    query = input('Введите данные для поиска контакта: ')
    search_list = []
    for contact_id, data in buffer_dict.items():
        if ((query in data['Имя'] or query in data['Номер'] or query in data['Комментарий'])
                and contact_id not in search_list):
            search_list.append(contact_id)
    print(f"Результаты поиска:")
    if  not search_list:
        print("Ничего не найдено.")
        print('')
        return search_list
    else:
        return search_list


def izm_contact(buffer_dict): # изменение контакта
    for contact_id, data in buffer_dict.items():
        print(f"ID:{contact_id} {data['Имя']}: {data['Номер']} (Заметка: {data['Комментарий']})")
    while True:
        change_input = input("Введите ID контакта для изменения: ")  # обязательно нужной найти ID в словаре
        if change_input not in buffer_dict:
            print("ID не найден")
        else:
            break
    while True:
        name = input("Введите новое имя: ")
        if  not name:
            print("Обязательно введите любое имя")
        else:
            break
    while True:
        number = input("Введите новый номер из 10 цифр (код страны указывать не нужно): ")
        if not number.isdigit():
            print("Нужно ввести число")
        elif len(number) != 10:
            print("Нужно ввести 10 цифр")
        else:
            break
    comment = input("Напишите новый комментарий о контакте (опционально): ")
    if comment == "":
        comment = "Отсутствует"
    return change_input, name, f'+{number}', comment


def del_contact(buffer_dict): # удаление контакта
    for contact_id, data in buffer_dict.items(): # выводим для пользователя все контакты
        print(f"ID:{contact_id} {data['Имя']}: {data['Номер']} (Заметка: {data['Комментарий']})")
    while True:
        del_input = input("Введите ID для удаления записи: ")  # проверяем, что такой ID существует
        if del_input in buffer_dict.keys():
            break
        else:
            print("ID не найден")
    for contact_id, data in buffer_dict.items():
        if del_input == contact_id:
            print(f"Удалить ID:{contact_id} {data['Имя']}: {data['Номер']} (Заметка: {data['Комментарий']})?",
                  f"1. Да",
                  f"2. Нет", sep="\n")
    confirmation_of_del = input("Выберите вариант ответа: ")
    if confirmation_of_del == "1":  # удаляем контакт, только если пользователь хочет
        del buffer_dict[del_input]
    else:
        print("Операция отменена")

    return buffer_dict

