import json


class Phone_Direrctory():
    """Создаем некий буфер для данных которые потом будем записывать в справочник"""
    def __init__(self):
        """При инициализации будем создавать словарь как переменную класса"""
        self.directory = {

        }

    def __str__(self):
        """Пробегается по данным в справочнике и выводит их пользователю"""
        with open("phone_directory.json", "r", encoding='utf-8') as f:
            print("Все контакты:")
            json_data = json.load(f)
            for contact_id, data in json_data.items():
                print(f"ID:{contact_id} {data['Имя']}: {data['Номер']} (Заметка: {data['Комментарий']})")
        return ''


    def get_phone_directory(self):
        """Получаем все данные из файла-справочника для дальнейшей обработки"""
        with open('phone_directory.json', 'r', encoding='utf-8') as f:
            self.directory = json.load(f)
            return 'Считывание прошло успешно!'


    def add_contact(self, id_for_file, name_for_file, number_for_file, comment_for_file):
        """Добавляем в наш буфер контакт"""
        self.directory[id_for_file] = {'Имя': name_for_file, 'Номер': number_for_file, 'Комментарий': comment_for_file}


    def save_phone_directory(self):
        """Записываем все из буфера в файл"""
        with open('phone_directory.json', 'w', encoding='utf-8') as f:
            json.dump(self.directory, f)


class Contact():
    """Класс контакта"""
    def __init__(self, human_id, name, phone, comment):
        """Создание информации о контакте"""
        self.data = {human_id: {'Имя': name,
                                'Номер': phone,
                                'Комментарий': comment,}}


    def __str__(self):
        """Вывод для пользователя контакта на экран"""
        for contact_id, data in self.data.items():
            print(f"ID:{contact_id} {data['Имя']}: {data['Номер']} (Заметка: {data['Комментарий']})")
        return ' '

