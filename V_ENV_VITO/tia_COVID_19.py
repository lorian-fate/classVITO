import requests
import json
from statistics import My_Statistics
import threading
#from progress.bar import Bar
import time
import matplotlib.pyplot as plt


"""
def load_function(interval):
    bar1 = Bar('Procesando:', max=100)
    for num in range(interval):
        time.sleep(0.158)
        bar1.next()
    bar1.finish()

t1 = threading.Thread(target=load_function, args=(100,))
t1.start()
"""

class Process_DATA:


    """
    JSON 2:
        Escribir un nuevo json
        Obtener los confirmados totales por 
    semana
        Crear una gráfica con los mismos
        Calcular R pearson
        Calcular B

    """
    url = "https://datos.comunidad.madrid/catalogo/dataset/7da43feb-8d4d-47e0-abd5-3d022d29d09e/resource/\
ead67556-7e7d-45ee-9ae5-68765e1ebf7a/download/covid19_tia_muni_y_distritos.json"


    def my_REQUESTS(self):
        my_request = requests.get(self.url).json()
        with open("./DATAS/covid_19.json", "w") as json_file:
            json.dump(my_request, json_file, indent=4)

    @property
    def my_data(self):
        with open("./DATAS/covid_19_new.json", "r") as json_file:
            json_data = json.load(json_file)  
            return json_data['data']

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
        my_list = sorted({report_date["fecha_informe"] for report_date in self.my_data})
        
        #for item for self.my_data:
        #    yield item

        my_Dict = {counter:date_tia for counter, date_tia in enumerate(my_list, start=1)}
        return my_Dict
    


    @property
    def daily_TIA(self):
        my_Dict = {}
        #my_list = list(self.date_LIST.values())
        #my_list.reverse()

        for date_tia in self.date_LIST.values():
            counter = 0
            for daily_tia in self.my_data:
                if date_tia == daily_tia["fecha_informe"]:
                    if "casos_confirmados_totales" in daily_tia.keys():
                        counter += daily_tia["casos_confirmados_totales"]
                    elif "casos_confirmados_totales" not in daily_tia.keys():
                        counter += 0
            my_Dict[date_tia] = counter
        return my_Dict







objp = Process_DATA()
x = list(objp.date_LIST.keys())
y = list(objp.daily_TIA.values())
#x = list(objp.daily_TIA.keys())



print(objp.date_LIST)
print("=====================")
print(objp.daily_TIA)


obj = My_Statistics(x,  y)
print(obj.r_pearson)
print(obj.b)


plt.plot(x, y)
plt.show()


import numpy as np
import matplotlib.pyplot as plt

#plt.axis([0, 127, 0, 7000])
#plt.ion()
"""
xs = [0, 0]
ys = [1, 1]

for i, j in zip(x, y):
    #y = np.random.random()
    xs[0] = xs[1]
    ys[0] = ys[1]
    xs[1] = i
    ys[1] = j
    plt.plot(xs, ys)
    plt.pause(0.2)
"""


"""
#*=========================================================================
#*Creación de una serie de figuras
import numpy as np
import matplotlib.pyplot as plt
for i in range(2, 17):
    x = np.arange(1, i, .1)
    y = np.exp(x)
    plt.plot(x, y)
    plt.savefig("./figures/figure{0:03d}.png".format(i))
    plt.clf()

#*Creación final del video
import glob
file_list = sorted(glob.glob('./figures/*.png'))

import moviepy.editor as mpy
fps = 3
clip = mpy.ImageSequenceClip(file_list, fps=fps)
clip.write_gif('movie.gif')
"""
"""
import numpy as np
import matplotlib.pyplot as plt

#plt.axis([0, 100, 0, 1])
plt.axis([0, 100, 0, 500])
plt.ion()

xs = [0, 0]
ys = [1, 1]


#for i in range(100):
for i, j in zip(range(100), range(0, 500, 5)):
    #y = np.random.random()
    xs[0] = xs[1]
    ys[0] = ys[1]
    xs[1] = i
    ys[1] = j
    plt.plot(xs, ys)
    #plt.plot(i, j)
    plt.pause(0.1)
"""