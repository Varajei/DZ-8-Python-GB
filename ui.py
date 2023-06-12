from logger import add_contact, find_contact, delete_contact, update_contact, show_contacts

# Главное меню программы
def interface():
    while True:
        print('Меню:')
        print('1. Добавить новый контакт')
        print('2. Найти контакт по фамилии')
        print('3. Удалить контакт по фамилии')
        print('4. Изменить контакт по фамилии')
        print('5. Показать список контактов')
        print('6. Выйти из программы')
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
          show_contacts()
        elif choice == '6':
          break
        else:
           print('Некорректный ввод')
        
