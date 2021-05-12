import requests
import json



class Defibrillator:
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

    @property
    def postal_CODE_M30(self):
        m30_postal_CODE = [
                            "28029", "28036", "28046", "28039", "28016", "28020", 
                            "28002", "28003", "28015", "28010", "28006", "28028", 
                            "28008", "28004", "28001", "280013", "28014", "28009", 
                            "28007", "28012", "28005", "28045"
                            ]
        my_lambda = filter((lambda parameter: parameter["direccion_codigo_postal"] in m30_postal_CODE), self.get_data)
        return len(list(my_lambda))


    @property
    def public_defibrillator(self):
        for defibrillator in self.get_data:
            if defibrillator["tipo_titularidad"] == "Público":
                yield defibrillator


    @property
    def private_defibrillator(self):
        for defibrillator in self.get_data:
            if defibrillator["tipo_titularidad"] == "Privado":
                yield defibrillator


    def search_BYCODE(self, code):
        my_DEA = filter((lambda parameter: parameter["codigo_dea"] == code), self.get_data)
        return list(my_DEA)


    def search_BYDISTANCE(self, obj_user, B):
        x_DEA, y_DEA = obj_user.x, obj_user.y
        x_USER, y_USER = B[0], B[1]
        return ((x_USER - x_DEA)**2 + (y_USER - y_DEA)**2)**0.5





