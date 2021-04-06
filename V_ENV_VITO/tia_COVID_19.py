import requests
import json
import datetime

url = "https://datos.comunidad.madrid/catalogo/dataset/7da43feb-8d4d-47e0-abd5-3d022d29d09e/resource/\
ead67556-7e7d-45ee-9ae5-68765e1ebf7a/download/covid19_tia_muni_y_distritos.json"

def my_REQUESTS():
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


def my_data():
    with open("./DATAS/covid_19.json", "r") as json_file:
        json_data = json.load(json_file)  
        return json_data['datas']


def municipality_QUANTITY():
    return len({municipality["municipio_distrito"] for municipality in my_data()})


def get_TIA():
    init_TIA = [tia["tasa_incidencia_acumulada_total"] for tia in my_data() if "2020/02/26" in tia["fecha_informe"]]
    final_TIA = [tia["tasa_incidencia_acumulada_total"] for tia in my_data() if "2020/07/01" in tia["fecha_informe"]]
    return f"The initial TIA is: {sum(init_TIA)}\nThe final TIA is: {sum(final_TIA):.2f}"


def date_LIST():
    my_list = sorted(list({datetime.date(int(report_date["fecha_informe"].split(" ")[0].split("/")[0]),
                int(report_date["fecha_informe"].split(" ")[0].split("/")[1]),
                int(report_date["fecha_informe"].split(" ")[0].split("/")[2])).
                strftime("%Y/%m/%d") for report_date in my_data()}))
    return len(my_list)

def daily_TIA():
    my_list = [sum([daily_tia["tasa_incidencia_acumulada_total"] for daily_tia in my_data() if date_tia in daily_tia["fecha_informe"]]) for date_tia in date_LIST()]
    return my_list



#print(municipality_QUANTITY())
#print(get_TIA())
#print(date_LIST())
print(daily_TIA())
