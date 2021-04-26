import json



class Users:
    
    def __init__(self, name, password):
        self.name = name
        self.password = password
    

    def saveUser(self):
        my_file = open("../DATAS/users.json")
        my_userFile = json.load(my_file)
        my_file.close()

        my_user = {
            "name": self.name,
            "password": self.password
        }
        if my_user not in my_userFile["users"]:
            my_userFile.append(my_user)
            with open("../DATAS/users.json", "w") as my_json:
                json.dump(my_userFile, my_json, indent=4)