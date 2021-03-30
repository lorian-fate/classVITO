import requests as req
import csv
import json
import os




def myRequest(name=None):
    if name == None:
        return req.get("https://restcountries.eu/rest/v2/all").json()
    else:
        return req.get(f"https://restcountries.eu/rest/v2/name/{name}").json() 


def population_continent(name):
    try:
        file_json = open(f"{name}.json")
        population = json.load(file_json)
        total_population = [popus['population'] for popus in population['countries']]
        return f"The total population of {name} is {sum(total_population)}"
    except FileNotFoundError:
        return "The region typed doesnt exist"
    

def historical_searching():
    
    pass

def search_country(name):
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
                return f"The country {name} already exist"
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
                    return f"Country saved successfully"

        except FileNotFoundError:
            with open("countries.csv", 'a', newline='') as country_file:
                writer_line = csv.writer(country_file)
                writer_line.writerow(list_param)
                return f"country saved successfully"

    elif name.capitalize() in set_continents:
        currentDirectory = os.path.dirname(os.path.realpath(__file__))
        diretories = os.listdir(currentDirectory)
        if str(f'{name}.json') in diretories:
            return list_countries
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
            return list_countries
    else:
        return f"Invalid name"
        


def menu():
    print("PENDING")


print(search_country('spain'))
#print(population_continent('americas'))
