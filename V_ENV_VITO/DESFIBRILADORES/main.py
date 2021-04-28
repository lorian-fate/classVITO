from user import User
from manage import Manage


def menu():
    exit_command = True
    my_manage = Manage()

    while exit_command:

        option = input("1._Create user \n2._Access \n3._Admin \n4._Exit \nSelect an option: ")
        if option == '1': my_manage.save_User()
        elif option == '2': my_manage.access()
        elif option == "3": my_manage.admin()
        elif option == '4':
            exit_command = False

