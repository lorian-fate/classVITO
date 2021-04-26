import requests
import json



class Defibrellator:
    url = "https://datos.comunidad.madrid/catalogo/dataset/35609dd5-9430-4d2e-8198-3eeb277e5282/resource/c38446ec\
-ace1-4d22-942f-5cc4979d19ed/download/desfibriladores_externos_fuera_ambito_sanitario.json"
    
    def save_data(self):
        data = requests.get(self.url).json()
        with open("../DATAS/defibrillator.json", "w", encoding="utf8") as my_josn:
            json.dump(data, my_josn, ensure_ascii=False, indent=4)


    @property
    def get_data(self):
        with open("../DATAS/defibrillator.json", encoding="utf8") as my_json:
            my_file = json.load(my_json)
            return my_file["data"]
    
    @property
    def dea_Quantity(self):
        return len(self.get_data)
        



obj = Defibrellator()
print(obj.dea_Quantity)