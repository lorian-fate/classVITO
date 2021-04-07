import requests
import json
import datetime


class Process_DATA:
    url = "https://datos.comunidad.madrid/catalogo/dataset/7da43feb-8d4d-47e0-abd5-3d022d29d09e/resource/\
ead67556-7e7d-45ee-9ae5-68765e1ebf7a/download/covid19_tia_muni_y_distritos.json"


    def my_REQUESTS(self):
        my_request = requests.get(url).json()
        my_json = {'datas':[]}
    
        for response in my_request['data']:
            if "casos_confirmados_totales" and "casos_confirmados_ultimos_14dias" not in list(response.keys()):
                my_json['datas'].append({
                    "municipio_distrito": response["municipio_distrito"],
                    "codigo_geometria": response["codigo_geometria"],
                    "tasa_incidencia_acumulada_ultimos_14dias": response["tasa_incidencia_acumulada_ultimos_14dias"],
                    "tasa_incidencia_acumulada_total": response["tasa_incidencia_acumulada_total"],
                    "fecha_informe": response["fecha_informe"]
                })
            elif "casos_confirmados_ultimos_14dias" not in list(response.keys()):
                my_json['datas'].append({
                    "municipio_distrito": response["municipio_distrito"],
                    "codigo_geometria": response["codigo_geometria"],
                    "tasa_incidencia_acumulada_ultimos_14dias": response["tasa_incidencia_acumulada_ultimos_14dias"],
                    "tasa_incidencia_acumulada_total": response["tasa_incidencia_acumulada_total"],
                    "casos_confirmados_totales": response["casos_confirmados_totales"],
                    "fecha_informe": response["fecha_informe"]
                })
            else:
                my_json['datas'].append({
                    "municipio_distrito": response["municipio_distrito"],
                    "codigo_geometria": response["codigo_geometria"],
                    "tasa_incidencia_acumulada_ultimos_14dias": response["tasa_incidencia_acumulada_ultimos_14dias"],
                    "tasa_incidencia_acumulada_total": response["tasa_incidencia_acumulada_total"],
                    "casos_confirmados_totales": response["casos_confirmados_totales"],
                    "casos_confirmados_ultimos_14dias": response["casos_confirmados_ultimos_14dias"],
                    "fecha_informe": response["fecha_informe"]
                })
        

        with open("./DATAS/covid_19.json", "w") as json_file:
            json.dump(my_json, json_file, indent=4)

    @property
    def my_data(self):
        with open("./DATAS/covid_19.json", "r") as json_file:
            json_data = json.load(json_file)  
            return json_data['datas']

    @property
    def municipality_QUANTITY(self):
        return len({municipality["municipio_distrito"] for municipality in self.my_data})


    def get_TIA(self):  
        counterA, counterB = 0, 0
        init_TIA = 0
        final_TIA = 0
        for tia in self.my_data:
            if "2020/07/01" in tia["fecha_informe"]:
                if "casos_confirmados_totales" in tia.keys():
                    final_TIA += tia["casos_confirmados_totales"]
                    counterA += 1
            elif "2020/02/26" in tia["fecha_informe"]:
                if "casos_confirmados_totales" not in tia.keys():
                    init_TIA += 0
                    counterB += 1      
        return f"The initial TIA is: {init_TIA} over {counterB} municipalities\
        \nThe final TIA is: {final_TIA} over {counterA} municipalities"


    @property
    def date_LIST(self):
        my_list = sorted(list({datetime.date(int(report_date["fecha_informe"].split(" ")[0].split("/")[0]),
                int(report_date["fecha_informe"].split(" ")[0].split("/")[1]),
                int(report_date["fecha_informe"].split(" ")[0].split("/")[2])).
                strftime("%Y/%m/%d") for report_date in self.my_data}))
        
        my_Dict = {counter:date_tia for counter, date_tia in enumerate(my_list, start=1)}
        return my_Dict


    @property
    def daily_TIA(self):
        my_Dict = {}

        for date_tia in self.date_LIST.values():
            counter = 0
            for daily_tia in self.my_data:
                if date_tia in daily_tia["fecha_informe"]:
                    if "casos_confirmados_totales" in daily_tia.keys():
                        counter += daily_tia["casos_confirmados_totales"]
                    elif "casos_confirmados_totales" not in daily_tia.keys():
                        counter += 0
            my_Dict[date_tia] = counter
        return my_Dict



