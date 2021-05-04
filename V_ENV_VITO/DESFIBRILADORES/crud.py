import json



class My_CRUD:
    
    def add_DEA(self):
        info_DEA = {}
        
        key_list = ["direccion_puerta", "direccion_via_codigo", "direccion_piso",
                    "municipio_codigo", "municipio_nombre", "direccion_ubicacion",
                    "direccion_via_nombre", "direccion_portal_numero", "tipo_establecimiento",
                    "direccion_codigo_postal", "horario_acceso", "codigo_dea",
                    "tipo_titularidad", "direccion_coordenada_y", "direccion_coordenada_x"]
        for data in key_list:
            data_DEA = input(f"Type {data}: ")
            info_DEA[data] = data_DEA
        
        my_file = open("../DATAS/defibrillator.json", encoding="utf8")
        my_data = json.load(my_file)
        my_file.close()
        
        if info_DEA not in my_data["data"]:
            my_data["data"].append(info_DEA)
            with open("../DATAS/defibrillator.json", "w", encoding="utf8") as my_josn:
                json.dump(my_data, my_josn, ensure_ascii=False, indent=4)
        

    def modify_DEA(self):
        my_file = open("../DATAS/defibrillator.json", encoding="utf8")
        my_data = json.load(my_file)
        my_file.close()

        dea_code = input("type the dea code: ")
        dea_to_update = list(filter((lambda dea: dea["codigo_dea"] == dea_code), my_data["data"]))[0]
        if dea_to_update:
            exit_key = True
            while exit_key:
                for ind, opt in enumerate(dea_to_update.keys(), start=0):
                    print(f"{ind}._ {opt}")

                option = input("15._Nothing \nWhat do you want to modify?: ")
                if int(option) in range(0, 15):
                    new_value = input(f"Type the new {list(dea_to_update.keys())[int(option)]}: ")
                    my_data["data"].remove(dea_to_update)
                    
                    
                    dea_to_update[list(dea_to_update.keys())[int(option)]] = new_value
                    my_data["data"].append(dea_to_update)
                    with open("../DATAS/defibrillator.json", "w", encoding="utf8") as my_josn:
                        json.dump(my_data, my_josn, ensure_ascii=False, indent=4)
                elif option == '15':
                    exit_key = False
                else:
                    print("not allowed option...")
                
        else:
            print(f"{dea_code} this Dea doesn't exist")

        


    def delete_DEA(self):
        my_file = open("../DATAS/defibrillator.json", encoding="utf8")
        my_data = json.load(my_file)
        my_file.close()

        dea_code = input("type the dea code: ")
        dea_to_update = list(filter((lambda dea: dea["codigo_dea"] == dea_code), my_data["data"]))[0]
        if dea_to_update:
            my_data["data"].remove(dea_to_update)
            with open("../DATAS/defibrillator.json", "w", encoding="utf8") as my_josn:
                json.dump(my_data, my_josn, ensure_ascii=False, indent=4)
        else:
            print(f"{dea_code} this Dea doesn't exist")


