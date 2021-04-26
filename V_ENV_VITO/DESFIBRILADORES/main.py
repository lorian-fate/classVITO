from user import Users


def menu():
    exit_command = True

    while exit_command:
        option = input("1._Create user \n2._Access \n3._Admin \n4._Exit \nSelect an option: ")
        
        if option == '1': 
            name = input("Enter a name: ")
            password = input("Enter a password: ")
            my_user = Users(name, password)
            my_user.saveUser()
            print("A user was created")
        
        elif option == '4':
            exit_command = False

