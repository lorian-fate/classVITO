import requests as req

#response = req.get("https://restcountries.eu/rest/v2/all").json()
#* Debe permitirnos buscar países por nombre y por continentes Cada uno de los países buscados debe quedar escrito en un archivo tipo csv que 
#* solo admitira  los siguientes valores: name, capital, region, population, area, idioma (el primero), flag A su vez estos valores acturán como encabezados


#name = input("Enter a country: ")
#response = req.get(f"https://restcountries.eu/rest/v2/name/{name}").json()
search_data = input("Enter country or continent: ")

print(response)