
import data_base
import view
import phone_book as pb

def choice_menu(choice):
    match choice:
        case 1:
            view.print_phone_book()
        case 2:
            data_base.load_contacts()
        case 3:
            data_base.save_contacts()
        case 4:
            pb.add_contact()
        case 5:
            pb.change_contact()
        case 6:
            pb.remove_contact()
        case 7:
            pb.find_contacts()
        case 0:
            a = input('Вы уверены, что хотите выйти? Перед выходом не забудьте сохранить изменения. (y/n)')
            if a == 'y':
                print('Вы вышли!')
                return True

while True:
    choice = view.main_menu()
    if choice_menu(choice):
        break
