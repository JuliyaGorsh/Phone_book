import view


phone_book = []

def get_phone_book() -> list:
    global phone_book
    return phone_book

def set_phone_book(new_phone_book: list):
    global phone_book
    phone_book = new_phone_book

def add_contact():
    global phone_book
    contact = view.input_new_contact()
    phone_book.append(contact)

def remove_contact():
    global phone_book
    id = view.input_remove_contact()
    confirm = input(f'Вы точно хотите удалить контакт {phone_book[id-1][0]}? (y/n)')
    if confirm.lower() == 'y':
        del_contact = phone_book.pop(id-1)

def find_contacts():
    global phone_book
    string = input('Для поиска введите необходимые значения: ')
    x = 0
    for contact in phone_book:
        for i in range(len(contact)):
            for j in range(len(contact[i])):
                if string.lower() in str(contact[i][j : j + len(string)]).lower():
                    x = 1
                    print(*contact)
                    break
    if x != 1:
        print('Ничего не найдено')
    print()


def change_contact():
    global phone_book
    id = int(input('Введите ID контакта, который хотите изменить: '))
    print(phone_book[id-1])
    change = int(input('Выберите, что хотите изменить (1-имя, 2-телефон, 3-комментарий): '))
    if change == 1:
        new_name = input('Введите новое имя: ')
        phone_book[id-1][0] = new_name
    if change == 2:
        new_phone = input('Введите новый телефон: ')
        phone_book[id-1][1] = new_phone
    if change == 3:
        new_comment = input('Введите новый комментарий: ')
        phone_book[id-1][2] = new_comment
    print('Не забудь сохранить изменения!')
    print()

