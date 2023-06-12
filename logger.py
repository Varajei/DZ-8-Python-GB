import json

# Функция для чтения данных из файла
def read_data():
    try:
        with open('phonebook.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
    except FileNotFoundError:
        data = []
    return data

# Функция для записи данных в файл
def write_data(data):
    with open('phonebook.json', 'w', encoding='utf-8') as file:
        json.dump(data, file)

# Функция для добавления нового контакта
def add_contact():
    data = read_data()
    name = input('Введите имя: ')
    surname = input('Введите фамилию: ')
    phone = input('Введите номер телефона: ')
    city = input('Введите город проживания: ')
    contact = {'name': name, 'surname': surname, 'phone': phone, 'city': city}
    data.append(contact)
    write_data(data)
    print('Контакт успешно добавлен')

# Функция для поиска контакта по фамилии
def find_contact():
    data = read_data()
    surname = input('Введите фамилию: ')
    found_contacts = []
    for contact in data:
        if contact['surname'].lower() == surname.lower():
            found_contacts.append(contact)
    if found_contacts:
        for contact in found_contacts:
            print(contact)
    else:
        print('Контакт не найден')

# Функция для удаления контакта по фамилии
def delete_contact():
    data = read_data()
    surname = input('Введите фамилию: ')
    new_data = []
    for contact in data:
        if contact['surname'].lower() != surname.lower():
            new_data.append(contact)
    if len(new_data) != len(data):
        write_data(new_data)
        print('Контакт успешно удалён')
    else:
        print('Контакт не найден')

# Функция для изменения контакта по фамилии
def update_contact():
    data = read_data()
    surname = input('Введите фамилию: ')
    found_contacts = []
    for contact in data:
        if contact['surname'].lower() == surname.lower():
            found_contacts.append(contact)
    if found_contacts:
        for contact in found_contacts:
            print(contact)
        index = int(input('Введите номер контакта для изменения: ')) - 1
        contact = found_contacts[index]
        field = input('Введите поле для изменения (name, surname, phone, city): ')
        value = input('Введите новое значение: ')
        contact[field] = value
        write_data(data)
        print('Контакт успешно изменён')
    else:
        print('Контакт не найден')

# Функция для вывода списка всех контактов
def show_contacts():
    contact = read_data()
    if contact:
        print('Список контактов:')
        for surname, data in contact.items():
            print(f'{surname} {data["name"]}, тел.: {data["phone"]}, дата рождения: {data["birthday"]}, город: {data["city"]}')
    else:
        print('Нет контактов в телефонной книге')