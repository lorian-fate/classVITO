## Comprobación de una ley
"""
* Para poder realizar este ejercicio deberán descargar el archivo JSON en éste mismo repositorio
* De ahora en mas al valor de la clave "densidad_por_km2" la llamaremos densidad
* Ejercicio 1: Obtender la densidad media de los municipios de Madrid
* Ejercicio 2: Obtener municipio por codigo ine // Extra: utilizando función filter
* Ejercicio 3: Obtener el municipio más grande
* Ejercicio 4: Obtener los 10 municipios con mayor densidad poblacional
* Ejercicio Bonus: Crea una función que reciba como parametro el dataset y devuelva tres listas con la siguiente condición:
	* la lista 1 tendrá todos los valores de densidad que empiecen por 1
	* la lista 2 tendrá todos los valores de densidad que empiecen por 2
	ej:
	lista_1 = ["134324", "1354211", "349.34"]

"""
"""
def multiple(numero):    # Primero declaramos una función condicional
    if numero % 5 == 0:  # Comprobamos si un numero es múltiple de cinco
        return True      # Sólo devolvemos True si lo es

numeros = [2, 5, 10, 23, 50, 33]

filter(multiple, numeros)
"""

#==========================================   EXERCICE 1  ==========================================
# Obtender la densidad media de los municipios de Madrid
from mppclass20210318 import get_json_data

def getAverageDensity():
    data = get_json_data()
    density_data = [density['densidad_por_km2'] for density in data]
    return f"The average of density is: {sum(density_data) / len(density_data)}"

#print(getAverageDensity())


#==========================================   EXERCICE 2  ==========================================
# Obtener municipio por codigo ine // Extra: utilizando función filter
def get_municipality(data_required='municipio_codigo_ine', ine_m='280035'):
    data = get_json_data()
    #ine_m = '280035'
    def filter_by_ine(ine):
        ine_allowed = [ine_muni for ine_muni in data if ine_muni[data_required] == ine]
        try:
            assert len(ine_allowed)
        except AssertionError:
            print("The ine typed doesn't exist")
        else:
            return ine_allowed
    
    #data_by_id = list(filter(filter_by_ine, ine_m))
    #return data_by_id

    data_by_ine = filter_by_ine(ine_m)
    return data_by_ine
#print(get_municipality())

#==========================================   EXERCICE 3  ==========================================
# Obtener el municipio más grande

def get_the_biggest_municipality():
    data = get_json_data()
    the_biggest = max([biggest_muni['superficie_km2'] for biggest_muni in data])
    return the_biggest

#print(get_the_biggest_municipality())



#==========================================   EXERCICE 4  ==========================================
# Obtener los 10 municipios con mayor densidad poblacional

def get_the_10_highest_density_municipality():
    den = 'densidad_por_km2'
    data = get_json_data()
    biggest_density = [biggest_den['densidad_por_km2'] for biggest_den in data]
    highest_density_municipality_list = []
    while len(highest_density_municipality_list) != 10:
        for i in range(0, 10):
            print(True)
            max_den = max(biggest_density)
            highest_density_municipality_list.append(max_den)
            biggest_density.pop(biggest_density.index(max_den))
    
    for density in highest_density_municipality_list:
        print(get_municipality(den, density))
    #return len(highest_density_municipality_list)
    return ''


#print(get_the_10_highest_density_municipality())



#==========================================   EXERCICE BONO  ==========================================
# Crea una función que reciba como parametro el dataset y devuelva tres listas con la siguiente condición:
#	* la lista 1 tendrá todos los valores de densidad que empiecen por 1
#	* la lista 2 tendrá todos los valores de densidad que empiecen por 2
#	ej:
#	lista_1 = ["134324", "1354211", "349.34"]

def bonus(dataset):
    listStartwith1, listStartwith2, listStartwith3 = [], [], []
    for condition in dataset:
        if str(condition['densidad_por_km2']).startswith('1'):
            listStartwith1.append(condition['densidad_por_km2'])
        elif str(condition['densidad_por_km2']).startswith('2'):
            listStartwith2.append(condition['densidad_por_km2'])
        elif str(condition['densidad_por_km2']).startswith('3'):
            listStartwith3.append(condition['densidad_por_km2'])

    return listStartwith1, listStartwith2, listStartwith3
#data = get_json_data()
#print(bonus(data))


def percentage(dataset):
    data = get_json_data()
    density_list = [density['densidad_por_km2'] for density in data]
    x, y, z = bonus(data)
    
    return f"The percentage of the density startwith 1 is: {round((len(x) * 100) / len(density_list), 2)}% \
             \nThe percentage of the density startwith 2 is: {round((len(y) * 100) / len(density_list), 2)}% \
             \nThe percentage of the density startwith 3 is: {round((len(z) * 100) / len(density_list), 2)}%"

#print(percentage())




"""
	

## OOP
* Ejercicio 5: Crear una clase de tipo municipality/municipio
	* Debe tener tantas propiedas como claves en el diccionario
* Ejercicio 7: Crear una función que acepte un solo parámetro (municipio) y que devuleva un objecto con las propiedades (nombre, densidad, superfice)
* Ejercicio 8: Modificar el tipo de impresión (print) para que se vea así --> nombre: valor
										 densidad: float con tres decimales
										 superficie: float con tres decimales
* Ejercicio 9: Crear una función que acepte como parámetro toda la lista de diccionarios y devuelva una lista de objetos
* Ejercicio 10: Considerando que en cada objeto tenemos la superficie y densidad ambas por km2, crear un MÉTODO 
	(una función dentro del objeto) que devuelva la densidad total del municipio dado
* Ejercicio 11: Ya que tenemos una lista con todos los objetos, con su método "get_total_density()" 
	obtener la densidad total de la comunidad de Madrid

* Ejercicio 12: Crea un contador de modo que cada vez que se cree una nueva instancia, el mencionado contador aumente en 1
* Ejercicio 13: Crea un classmethod llamado from_str que crea una instancia de la siguiente cadena --> "test-3.54-23.86"
* Ejercicio 14: Estable una tasa de crecimiento anual del 2%
* Ejercicio 15: Define un método que aplique el crecimiento anual sobre un objeto
* Ejercicio 16: Convertir el método del ejercicio 10 en propiedad
* Ejercicio 17: Modificiar el print() para que también devuelva la población
* Ejercicio 18: Define un set_anual_growth que permita modificar la tasa de crecimiento
* Ejercicio 19: Agregar un Error Handeling para verficar que el type pasado como argumento en from_string sea un float

"""


#==========================================   EXERCICE 5  ==========================================


#* Ejercicio 5:
class Municipality:
    counter = 0

    def __init__(self, density_per_km2, municipality_name, surface_km2):
        self.density_per_km2 = density_per_km2
        self.municipality_name = municipality_name
        self.surface_km2 = surface_km2
        self.counter += 0 #*Ejercicio 12:


    #* Ejercicio 7:
    #* Ejercicio 8:								
    def return_municipality(self, municipality):
        data = get_json_data()
        ine_allowed = [ine_muni for ine_muni in data if ine_muni['municipio_nombre'] == municipality]
        try:
            assert len(ine_allowed)
        except AssertionError:
            print("The ine typed doesn't exist")
        else:
            for ine in ine_allowed:
                print(f"name: {ine['municipio_nombre']}\ndensity: {float(ine['densidad_por_km2'])}\nsurface: {float(ine['superficie_km2'])}")
        return ''
    
    #* Ejercicio 10:
    #* Ejercicio 11: 
    def total_density(self, municipality):
        data = get_json_data()
        ine_allowed = [ine_muni for ine_muni in data if ine_muni['municipio_nombre'] == municipality]
        all_population = [den["densidad_por_km2"]*den['superficie_km2'] for den in data]
        all_surface = [sur['superficie_km2'] for sur in data]
        
        #population_density = ine_allowed[0]['densidad_por_km2']
        #surface_km2 = ine_allowed[0]['superficie_km2']
        #population = population_density * surface_km2

        density = sum(all_population) /  sum(all_surface)
        return f"the Total Density is: {density:.2f}, {sum(all_population)}"


    #* Ejercicio 13: Crea un classmethod llamado from_str que crea una instancia de la siguiente cadena --> "test-3.54-23.86"
    @classmethod
    def from_str(cls, string_):
        name, density, surface = string_.split('-')
        return cls(name, density, surface) 


    #* Ejercicio 14: Estable una tasa de crecimiento anual del 2% before year (6.377.040)
    def annual_Growing(self):

        pass


    #* Ejercicio 15: Define un método que aplique el crecimiento anual sobre un objeto


#* Ejercicio 9:
def convertToObject(dict_list):
    object_list = []
    for dictionary in dict_list:
        obj = Municipality(
                        dictionary["densidad_por_km2"],
                        dictionary["municipio_nombre"],
                        dictionary["superficie_km2"])
    
        object_list.append(obj)
    return object_list






    



data = get_json_data()
obj_municipality = Municipality('','','')
obj_municipality.return_municipality('Ajalvir')
print(obj_municipality.total_density('Madrid '))
print(obj_municipality.from_str("Madrid-3.54-23.86"))
#print(convertToObject(data))


    









#==========================================   EXERCICE 7  ==========================================


#==========================================   EXERCICE 8  ==========================================


#==========================================   EXERCICE 9  ==========================================


#==========================================   EXERCICE 10  ==========================================



#==========================================   EXERCICE 11  ==========================================

#==========================================   EXERCICE 12  ==========================================

#==========================================   EXERCICE 13  ==========================================

#==========================================   EXERCICE 14  ==========================================

#==========================================   EXERCICE 15  ==========================================