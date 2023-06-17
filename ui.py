from logger import view_phonebook, add_contact, save_phonebook, delete_contact, update_contact

# Главный цикл программы
def interface():
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