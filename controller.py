import view
from model import *


try:        # пытаемся открыть файл, если его нет то создаем его и записываем туда Пример
    with open("phone_directory.json", "r", encoding='utf-8', ) as file:
        buffer = Phone_Direrctory()
        buffer.get_phone_directory()
except FileNotFoundError:
    with open("phone_directory.json", "w", encoding='utf-8') as file:
        data = {
            '1':{'Имя': 'Пример', 'Номер': '+79999999999', 'Комментарий': 'Отсутствует'},
        }
        json.dump(data, file, indent=4, ensure_ascii=False)
    buffer = Phone_Direrctory()
    buffer.get_phone_directory()

menu_input = 9
while True:
    if menu_input == 9: # переходим в главное меню
        view.main_menu()
        try:
            menu_input = int(input()) # ждем от пользователя ввода пункта меню
        except ValueError:
            view.invalid_data()
            continue

    elif menu_input == 1: # печатаем пользователю весь телефонный справочник
        print(buffer)
        menu_input = 9 # главное меню

    elif menu_input == 2: # начинаем создание контакта
        buffer.get_phone_directory() # получаем данные из файла
        id_for_record, name_for, number_for, comment_for = view.contact_creation(buffer.directory) # получаем уже проверенные данные из view
        buffer.add_contact(id_for_record, name_for, number_for, comment_for) # добавляем контакт в буфер
        buffer.save_phone_directory() # записываем контакт в файл
        menu_input = 9  # главное меню

    elif menu_input == 3: # ищем контакт
        buffer.get_phone_directory() # получаем данные из файла
        search_rez =  view.find_contact(buffer.directory) # поиск
        if not search_rez: # если ничего нет
            menu_input = 9  # главное меню
        for contact_id, data in buffer.directory.items(): # если есть - выводим построчно каждый контакт
            for data_in_list in search_rez:
                if data_in_list in contact_id or data_in_list in data:
                    print(f"ID:{contact_id} {data['Имя']}: {data['Номер']} (Заметка: {data['Комментарий']})")
        print('')
        menu_input = 9  # главное меню

    elif menu_input == 4:
        buffer.get_phone_directory()  # получаем данные из файла
        changing_input_new, name_new, number_new, comment_new = view.izm_contact(buffer.directory) # изменяем контакт
        buffer.add_contact(changing_input_new, name_new, number_new, comment_new) # перезаписываем контакт в буфере
        buffer.save_phone_directory() # записываем буфер в файл
        menu_input = 9  # главное меню

    elif menu_input == 5:
        buffer.get_phone_directory()  # получаем данные из файла
        view.del_contact(buffer.directory) # удаление контакта
        buffer.save_phone_directory() # записываем буфер в файл
        menu_input = 9 # главное меню

    elif menu_input == 0: # выходим из программы
        print('До свидания!')
        break



