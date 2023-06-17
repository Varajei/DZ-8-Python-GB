import json

# Создаем пустой словарь - наш телефонный справочник
phonebook = {}

# Функция для чтения телефонного справочника из файла
def load_phonebook():
    global phonebook
    try:
        with open('phonebook.json', 'r') as file:
            phonebook = json.load(file)
    except FileNotFoundError:
        print('Файл с телефонным справочником не найден')

# Функция для записи телефонного справочника в файл
def save_phonebook():
    with open('phonebook.json', 'w') as file:
        json.dump(phonebook, file)

# Функция для просмотра всех контактов в телефонном справочнике
def view_phonebook():
    for contact in phonebook.values():
        print(f'{contact["last_name"]} {contact["first_name"]}, телефон: {contact["phone_number"]}, город: {contact["city"]}')

# Функция для добавления нового контакта в телефонный справочник
def add_contact():
    last_name = input('Введите фамилию: ')
    first_name = input('Введите имя: ')
    phone_number = input('Введите номер телефона: ')
    city = input('Введите город: ')
    phonebook[last_name] = {
        'last_name': last_name,
        'first_name': first_name,
        'phone_number': phone_number,
        'city': city
    }
    print(f'Контакт {last_name} {first_name} добавлен в телефонный справочник')

# Функция для удаления контакта из телефонного справочника по фамилии
def delete_contact():
    last_name = input('Введите фамилию контакта, которого хотите удалить: ')
    if last_name in phonebook:
        del phonebook[last_name]
        print(f'Контакт {last_name} удален из телефонного справочника')
    else:
        print(f'Контакт {last_name} не найден в телефонном справочнике')

# Функция для частичного изменения контакта по фамилии
def update_contact():
    last_name = input('Введите фамилию контакта, которого хотите изменить: ')
    if last_name in phonebook:
        print('Введите новые данные:')
        first_name = input(f'Имя ({phonebook[last_name]["first_name"]}): ')
        phone_number = input(f'Номер телефона ({phonebook[last_name]["phone_number"]}): ')
        city = input(f'Город ({phonebook[last_name]["city"]}): ')
        phonebook[last_name].update({
            'first_name': first_name or phonebook[last_name]['first_name'],
            'phone_number': phone_number or phonebook[last_name]['phone_number'],
            'city': city or phonebook[last_name]['city']
        })
        print(f'Контакт {last_name} обновлен')
    else:
        print(f'Контакт {last_name} не найден в телефонном справочнике')

# Загружаем телефонный справочник из файла при запуске программы
load_phonebook()

# Главный цикл программы
while True:
    print('\nВыберите действие:')
    print('1 - Просмотреть все контакты')
    print('2 - Добавить новый контакт')
    print('3 - Удалить контакт')
    print('4 - Частично изменить контакт')
    print('5 - Выйти из программы')
    choice = input('Введите номер действия: ')
    if choice == '1':
        view_phonebook()
    elif choice == '2':
        add_contact()
        save_phonebook()
    elif choice == '3':
        delete_contact()
        save_phonebook()
    elif choice == '4':
        update_contact()
        save_phonebook()
    elif choice == '5':
        print('До свидания!')
        break
    else:
        print('Неверный выбор')