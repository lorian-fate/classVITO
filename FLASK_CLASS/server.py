from flask import Flask
from flask_cors import CORS
import requests as req
import json


app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})


data = req.get("https://datos.comunidad.madrid/catalogo/dataset/35609dd5-9430-4d2e-8198-3eeb277e5282/resource/c38446ec-ace1-4d22-942f-5cc4979d19ed/download/desfibriladores_externos_fuera_ambito_sanitario.json").json()

def save_DATA():
    with open("c:/LORIAN/classVITO/FLASK_CLASS/my_json.json", "w", encoding="utf8") as my_file:
        json.dump(data, my_file, ensure_ascii=False, indent=4)

def get_data():
    with open("c:/LORIAN/classVITO/FLASK_CLASS/my_json.json", encoding="utf8") as my_file:
        return json.load(my_file)

@app.route("/api/all")
def api():
    return get_data()


#* move to current path to run server
#* set FLASK_APP=server
#* flask run

#* change flask run port
#* flask run --port=number_port