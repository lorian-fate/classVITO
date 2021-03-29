import requests as req
import csv

#response = req.get("https://restcountries.eu/rest/v2/all").json()
#* Debe permitirnos buscar países por nombre y por continentes Cada uno de los países buscados debe quedar escrito en un archivo tipo csv que 
#* solo admitira  los siguientes valores: name, capital, region, population, area, idioma (el primero), flag A su vez estos valores acturán como encabezados


#name = input("Enter a country: ")
#response = req.get(f"https://restcountries.eu/rest/v2/name/spain").json()
#search_data = input("Enter country or continent: ")

#print(response)


def search_country(name):
    my_request = req.get("https://restcountries.eu/rest/v2/all").json()
    set_continents = {continent['region'] for continent in my_request}
    set_countries = {country['name'] for country in my_request}
    
    if name.capitalize() in set_countries:
        my_country = req.get(f"https://restcountries.eu/rest/v2/name/{name}").json()
        list_param = [my_country[0]['name'], my_country[0]['capital'], 
                        my_country[0]['population'], my_country[0]['area'], 
                        my_country[0]['languages'][0]['name']]
        try:
            country_file = open('countries.csv')
            read_line = csv.reader(country_file)
            try:
                assert [True for country in read_line if name.capitalize() in country]
                return f"The country {name} already exist"
                country_file.close()
            except AssertionError:
                with open('countries.csv', 'a', newline='') as file_co:
                    writer_line = csv.writer(file_co)
                    writer_line.writerow(list_param)
        except FileNotFoundError:
            with open("countries.csv", 'a', newline='') as country_file:
                writer_line = csv.writer(country_file)
                writer_line.writerow(list_param)
                return f"country saved succesfully"

        return ""
    elif name.capitalize() in set_continents:
        list_countries = [country['name'] for country in my_request if country['region'] == name.capitalize()]
        
        return list_countries
    else:
        return f"Name error"
        


print(search_country('benin'))
"""
with open('countries.csv') as file_da:
    read_file = csv.reader(file_da)
    try:
        assert [True for x in read_file if 'Spains' in x]
        print(True)
    except:
        print("is empty")
"""
    #for da in read_file:
    #    print(da)



