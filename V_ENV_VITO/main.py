import requests as req
import csv
import json
import os
from os import system
import time
from progress.bar import Bar



def myRequest(name=None):
    if name == None:
        return req.get("https://restcountries.eu/rest/v2/all").json()
    else:
        return req.get(f"https://restcountries.eu/rest/v2/name/{name}").json() 

def clear_SCREAN():
    return system("cls")

def population_continent(name):
    try:
        file_json = open(f"{name}.json")
        population = json.load(file_json)
        total_population = [popus['population'] for popus in population['countries']]
        print(f"The total population of {name} is {sum(total_population)}")
    except FileNotFoundError:
        print("The region typed doesnt exist")


def load_function(interval):
    bar1 = Bar('Procesando:', max=20)
    for num in range(interval):
        time.sleep(0.2)
        bar1.next()
    bar1.finish()


def historical_searching():
    try:
        with open("countries.csv", "r") as countrie_file:
            csv_reader = csv.reader(countrie_file)
            list_flag = []
            print("||-----------------------||-----------------------||")
            print("||", "\t","COUNTRY","\t", "||", "\t", "POPULATION", "\t"," ||")
            print("||=======================||=======================||")
            for country_in_csv_file in csv_reader:
                list_flag.append(country_in_csv_file[-1])
                if len(country_in_csv_file[0]) <= 5:
                    print("||","\t",country_in_csv_file[0], "\t\t", "||", "\t", country_in_csv_file[3], "\t"," ||")
                    print("||=======================||=======================||")

                elif len(country_in_csv_file[0]) >= 6:
                    print("||","\t",country_in_csv_file[0], "\t", "||", "\t", country_in_csv_file[3], "\t"," ||")
                    print("||=======================||=======================||")
            
            option = input("Do you wish to download the flags of these countries (y/n):") 
            if option == 'y':
                url_flag = "https://restcountries.eu/data/{}"
                diretories = os.listdir("../images_countries")
                for flag_country in list_flag:
                    flag_extension = flag_country.split("/")[-1]
                    if flag_extension not in diretories:
                        imag = req.get(f"https://restcountries.eu/data/{flag_extension}")
                        with open(f"../images_countries/{flag_extension}", "wb") as imag_file:
                            imag_file.write(imag.content)
            return ""

    except FileNotFoundError:
        return "The file doesn't exist"

def search_country_or_continent(name):
    my_request = myRequest()
    set_continents = {continent['region'] for continent in my_request}
    set_countries = {country['name'] for country in my_request}
    list_countries = [country['name'] for country in my_request if country['region'] == name.capitalize()]
    
    if name.capitalize() in set_countries:
        my_country = myRequest(name)
        list_param = [my_country[0]['name'], my_country[0]['capital'], my_country[0]['region'],
                        my_country[0]['population'], my_country[0]['area'], 
                        my_country[0]['languages'][0]['name'], my_country[0]['flag']]
        try:
            country_file = open('countries.csv')
            read_line = csv.reader(country_file)
            try:
                assert [True for country in read_line if name.capitalize() in country]
                print(f"The country {name} already exist")
                country_file.close()

            except AssertionError:
                option = input("Do you wish to save the flag (y/n): ")
                if option == 'y':
                    imag = req.get(my_country[0]['flag'])
                    image_name = my_country[0]['flag'].split('/')[-1]
                    image_dir = f"../images_countries/{image_name}"
                    with open(image_dir, 'wb') as im:
                        im.write(imag.content)
                with open('countries.csv', 'a', newline='') as file_co:
                    writer_line = csv.writer(file_co)
                    writer_line.writerow(list_param)
                    print(f"Country saved successfully")

        except FileNotFoundError:
            with open("countries.csv", 'a', newline='') as country_file:
                writer_line = csv.writer(country_file)
                writer_line.writerow(list_param)
                print(f"country saved successfully")

    elif name.capitalize() in set_continents:
        currentDirectory = os.path.dirname(os.path.realpath(__file__))
        diretories = os.listdir(currentDirectory)
        if str(f'{name}.json') in diretories:
            print("The region already exist")
        else:
            
            json_data = {
                'countries':[{
                        'name': country['name'],
                        'capital': country['capital'],
                        'region': country['region'],
                        'population': country['population'],
                        'language': country['languages'][0]['name']
                        } for country in my_request if country['region'] == name.capitalize()]      
                }
            with open(f"{name}.json", "w") as json_file:
                json.dump(json_data, json_file, indent=4)
            print("Region saved successfully")
    else:
        return f"Invalid name"
        


class Country:
    total_population = 0

    def __init__(self, name, capital, population):
        self.name = name
        self.capital = capital
        self.total_population += int(population)

    

def menu():


    exit_command = True
    while exit_command == True:
        print("=============================================================================")
        print("============================      MENU        ===============================")
        print("=============================================================================")
        option = input("1._COUNTRIES \n2._REGION \n3._POPULATION \n4._SHOW RECORD \
        \n5._CONVERT COUNTRIES IN OBJECT \n6._EXIT\nCHOOSE AN OPTION: ")

        if option == '1': 
            country_NAME = input("Type the country name: ")
            search_country_or_continent(country_NAME)
            time.sleep(2)
            load_function(20)
            clear_SCREAN()

        elif option == '2':
            region_NAME = input("Type the region name: ")
            search_country_or_continent(region_NAME)
            time.sleep(2)
            load_function(20)
            clear_SCREAN()

        elif option == '3':
            region_NAME = input("Type the region name: ")
            population_continent(region_NAME)
            time.sleep(2)
            load_function(20)
            clear_SCREAN()

        elif option == '4': 
            historical_searching()
            time.sleep(2)
            load_function(20)
            clear_SCREAN()

        elif option == '5':
            with open("countries.csv", "r") as countries_file:
                csv_reader = csv.reader(countries_file)
                for country in csv_reader:
                    obj_Country = Country(country[0], country[1], country[3])
                    class_ATTRIBUTE = input("Do you wish to access to the class attribute (y/n): ")
                    if class_ATTRIBUTE == 'y':
                        print(obj_Country.total_population)
            time.sleep(2)
            clear_SCREAN()

        elif option == '6':
            exit_command = False
        else:
            print("This option doesn't exist")
        


menu()
print("==============================================================================")
print("===========================  PROGRAM SHUTDOWN   ==============================")
print("==============================================================================")