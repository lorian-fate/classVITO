import requests as req

response = req.get("https://restcountries.eu/rest/v2/all")
print(response)