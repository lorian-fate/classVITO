#from DJANGO_CLASS.my_FIRST_PROJECT.my_FIRST_APP.views import closest_DEA
import utm
import json
import geocoder



def utm_TO_gps(latitude_DEA, longitude_DEA, zone_number=30, zone_letter="T"):
    #*Convert a (latitude, longitude) tuple into an UTM coordinates:
    #my_loc = utm.from_latlon(latitude_DEA, longitude_DEA)

    #* Convert an UTM coordinate into a (latitude, longitude) tuple:
    my_loc = utm.to_latlon(latitude_DEA, longitude_DEA, zone_number, zone_letter)
    return my_loc

#*C:\Users\ta010\Documents\MY_CODE\classMPP\classVITO\DJANGO_CLASS\my_FIRST_PROJECT>python
def get_distance(list_DEA):
    user_point = (443142.7, 4474998.8)
    #directory = "C:\Users\ta010\Documents\MY_CODE\classMPP\classVITO\DJANGO_CLASS\my_FIRST_PROJECT\my_FIRST_APP\defibrillator.json"
    
    #my_json = open(directory, encoding="utf8")
    #my_data = json.load(my_json)["data"]
    my_dic = {}

    #more_DEA = [m_dea for m_dea in list_DEA]

    my_dic1 = {}
    for my_DEA in list_DEA:
        dea_POSITION = search_BYDISTANCE(user_point, [my_DEA.x_utm, my_DEA.y_utm])
        my_dic1[dea_POSITION] = my_DEA
    
    minimun_distance = min(list(my_dic1.keys()))
    closest_DD = my_dic1[minimun_distance]
    dea_S_coordinates = utm_TO_gps(float(closest_DD.x_utm), float(closest_DD.y_utm))
    user_S_coordinates = utm_TO_gps(user_point[0], user_point[1])
    return [dea_S_coordinates, user_S_coordinates, minimun_distance, closest_DD]

    """
    for my_DEA in my_data:
        dea_POSITION = search_BYDISTANCE(user_point, [float(my_DEA["direccion_coordenada_x"]),
                                                    float(my_DEA["direccion_coordenada_y"])])
        my_dic[dea_POSITION] = my_DEA
    
    minimun_distance = min(list(my_dic.keys()))
    closest_D = my_dic[minimun_distance]
    user_S_coordinates = utm_TO_gps(float(closest_D["direccion_coordenada_x"]), float(closest_D["direccion_coordenada_y"]))
    return [user_S_coordinates, minimun_distance, closest_D, closest_DD]
    """
    
    

def search_BYDISTANCE(obj_user, B):
    x_DEA, y_DEA = obj_user[0], obj_user[1]
    x_USER, y_USER = B[0], B[1]
    return ((x_USER - x_DEA)**2 + (y_USER - y_DEA)**2)**0.5


"""
g = geocoder.ip("me")
print(g.latlng)

print(get_distance())


window.navigator.geolocation.getCurrentPosition((position) => {
    console.log(position.coords)
})

"""