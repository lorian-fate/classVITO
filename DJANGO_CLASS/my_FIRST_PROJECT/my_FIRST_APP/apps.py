from types import prepare_class
from django.apps import AppConfig
import os
import json


class MyFirstAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'my_FIRST_APP'
    
    def ready(self):
        """
        print("I m here")
        from .models import Dea

        dinamic_path = os.path.realpath(__file__)[0:-8]

        def get_data():
            with open(f"{dinamic_path}\defibrillator.json", encoding="utf8") as my_file:
                return json.load(my_file)["data"]
        my_data = get_data()
        print(len(my_data))
        
        
        for my_dea in my_data:
            Dea.objects.create(
                    codigo_dea = my_dea["codigo_dea"],
                    direccion_ubicacion = my_dea["direccion_ubicacion"],
                    direccion_portal_numero = my_dea["direccion_portal_numero"],
                    horario_acceso = my_dea["horario_acceso"],
                    x_utm = my_dea["direccion_coordenada_x"],
                    y_utm = my_dea["direccion_coordenada_y"]
            )
        """
        pass

            
