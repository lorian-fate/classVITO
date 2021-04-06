import requests
import json

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
        

    with open("./DATAS/covit_19.json", "w") as json_file:
        json.dump(my_json, json_file, indent=4)
    



