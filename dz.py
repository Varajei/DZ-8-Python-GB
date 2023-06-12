import json

# Функция для чтения данных из файла
def read_data():
    try:
        with open('PB.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
    except FileNotFoundError:
        data = []
    return data

# Функция для записи данных в файл
def write_data(data):
    with open('PB.json', 'w', encoding='utf-8') as file:
        json.dump(data, file)

# Функция для добавления нового контакта
def add_contact():
    data = read_data()
    name = input('Введите имя: ')
    surname = input('Введите фамилию: ')
    phone = input('Введите номер телефона: ')
    city = input('Введите город проживания: ')
    contact = {'Имя': name, 'Фамилия': surname, 'Телефон': phone, 'Город': city}
    data.append(contact)
    write_data(data)
    print('Контакт успешно добавлен')

# Функция для поиска контакта по фамилии
def find_contact():
    data = read_data()
    surname = input('Введите фамилию: ')
    found_contacts = []
    for contact in data:
        if contact['Фамилия'].lower() == surname.lower():
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
        if contact['Фамилия'].lower() != surname.lower():
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
        if contact['Фамилия'].lower() == surname.lower():
            found_contacts.append(contact)
    if found_contacts:
        for contact in found_contacts:
            print(contact)
        index = int(input('Введите номер контакта для изменения: ')) - 1
        contact = found_contacts[index]
        field = input('Введите поле для изменения (Имя, Фамилия, Телфон, Город): ')
        value = input('Введите новое значение: ')
        contact[field] = value
        write_data(data)
        print('Контакт успешно изменён')
    else:
        print('Контакт не найден')

# Главное меню программы
while True:
    print('Меню:')
    print('1. Добавить новый контакт')
    print('2. Найти контакт по фамилии')
    print('3. Удалить контакт по фамилии')
    print('4. Изменить контакт по фамилии')
    print('5. Выйти из программы')
    choice = input('Выберите пункт меню: ')
    if choice == '1':
        add_contact()
    elif choice == '2':
        find_contact()
    elif choice == '3':
        delete_contact()
    elif choice == '4':
        update_contact()
    elif choice == '5':
        break
    else:
        print('Некорректный ввод')