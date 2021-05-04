import json
from mppclass20210426 import Defibrillator
from user import User
import utm
from geopy.geocoders import Nominatim
from pygeocoder import Geocoder
import webbrowser
from crud import My_CRUD



class Manage:
    obj_defibrillator = Defibrillator()
    obj_crud = My_CRUD()

    @property
    def get_data(self):
        with open("../DATAS/users.json") as my_json:
            my_file = json.load(my_json)
            return my_file["users"]


    def save_User(self):
        name = input("Enter a name: ")
        password = input("Enter a password: ")
        my_user = {
            "name": name,
            "password": password
        }

        if my_user not in self.get_data:
            my_userFile["users"].append(my_user)
            with open("../DATAS/users.json", "w") as my_json:
                json.dump(my_userFile, my_json, indent=4)
                print("A user was created")
        else:
            print("This user already exist")


    @classmethod
    def print_data(self, data):
        print("|================================|=======================================================================================|")
        for key, value in data[0].items():
            if len(key) < 11:
                print(f"| {key}", '\t\t\t', f"| {value}")
                print("|================================|=======================================================================================|")
            elif len(key) > 20:
                print(f"| {key}", '\t', f"| {value}")
                print("|================================|=======================================================================================|")
            else:
                print(f"| {key}", '\t\t', f"| {value}")
                print("|================================|=======================================================================================|")


    #* This function convert UTM coordinates into latitude, longitude and viceversa
    @classmethod
    def utm_TO_gps(self, latitude_DEA, longitude_DEA, zone_number=30, zone_letter="T"):
        
        #*Convert a (latitude, longitude) tuple into an UTM coordinates:
        #my_loc = utm.from_latlon(latitude_DEA, longitude_DEA)

        #* Convert an UTM coordinate into a (latitude, longitude) tuple:
        my_loc = utm.to_latlon(latitude_DEA, longitude_DEA, zone_number, zone_letter)
        return my_loc


    #* This function convert coordinates into address
    """
    @classmethod
    def get_Address(self, lat_D, long_D):
        my_coordinates = Manage.utm_TO_gps(lat_D, long_D)
        geolocator = Nominatim(user_agent="my-application")
        my_ADDRESS = geolocator.reverse(str(my_coordinates[0]), str(my_coordinates[1]))
        return my_ADDRESS.address
    


    @classmethod
    def get_Address(self, lat_D, long_D):
        my_coordinates = Manage.utm_TO_gps(lat_D, long_D)
        my_ADDRESS = Geocoder.reverse_geocode(my_coordinates[0], my_coordinates[1])
        return my_ADDRESS[0]
    """

    @classmethod
    def show_UBICATIOM(self, url_D):
        return webbrowser.open(url_D, new=2, autoraise=True)


    @classmethod
    def get_UBICATION(self, user_lat, user_long, lat_D, long_D):
        #my_ubication = "https://www.google.com/maps/search/?api=1&query={},{}".format(lat_D, long_D)
        my_ubication = f"https://www.google.com/maps/dir/{user_lat},+{user_long}/{lat_D},{long_D}"
        
        return my_ubication


    @classmethod
    def get_distance(self, user_point):
        my_dic = {}
        for my_DEA in self.obj_defibrillator.get_data:
            dea_POSITION = self.obj_defibrillator.search_BYDISTANCE(user_point, [float(my_DEA["direccion_coordenada_x"]),
                                                                                float(my_DEA["direccion_coordenada_y"])])
            my_dic[dea_POSITION] = my_DEA
        
        minimun_distance = min(list(my_dic.keys()))

        return [minimun_distance, my_dic[minimun_distance]]
    
    



    def access(self):
        name = input("Enter a name: ")
        password = input("Enter a password: ")
        my_user = {
            "name": name,
            "password": password
        }
        if my_user in self.get_data:
            print("Access Granted!!!")
            exit_command = True

            while exit_command:
                option = input("1._SEARCH DEA BY CODE \n2._SEARCH DEA BY DISTANCE \n3._EXIT \nSelect an option: ")
                if option == '1':
                    code = input("Type the code: ")
                    my_DEA = self.obj_defibrillator.search_BYCODE(code)
                    Manage.print_data(my_DEA)
                elif option == '2':
                    user_position = input("Type the user position: ")
                    user_point = User(float(user_position.split(",")[0]), float(user_position.split(",")[1]))
                    my_DEA = Manage.get_distance(user_point)
                    transform_TO_gps = Manage.utm_TO_gps(float(my_DEA[1]['direccion_coordenada_x']), float(my_DEA[1]['direccion_coordenada_y']))
                    transform_TO_gps_user = Manage.utm_TO_gps(float(user_position.split(",")[0]), float(user_position.split(",")[1]))
                    my_ubication = Manage.get_UBICATION(transform_TO_gps_user[0], transform_TO_gps_user[1], transform_TO_gps[0], transform_TO_gps[1])
                    print(f"The closest DEA is at this ubication {my_ubication}")
                    
                    print(Manage.show_UBICATIOM(my_ubication))

                elif option == '3':
                    exit_command = False
            
        else:
            print("Access denied")


    def admin(self):
        name = input("Enter a name: ")
        password = input("Enter a password: ")
        
        if (name == self.get_data[0]["name"]) and (password == self.get_data[0]["password"]):
            exit_command = True
            while exit_command:
                option = input("1._ADD \n2._MODIFY \n3._DELETE \n4._EXIT\nSelect an option: ")
                if option == '1':
                    self.obj_crud.add_DEA()
                elif option == '2':
                    self.obj_crud.modify_DEA()
                elif option == '3':
                    self.obj_crud.delete_DEA()
                elif option == '4':
                    exit_command = False
        else:
            print("Incorrect data")
        



"""
f"https://www.google.com/maps/search/?api=1&query={},{}"
f"https://www.google.com/maps/dir/{user_lat},+{user_long}/{nearest_dea.latitude},{nearest_dea.longitude}"
"""