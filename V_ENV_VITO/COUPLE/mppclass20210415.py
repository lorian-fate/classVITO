import requests 
import json
import itertools
import matplotlib.pyplot as plt




class Unamed_CLASS:

    def my_REQUEST(self):
        url = "https://datos.comunidad.madrid/catalogo/dataset/eb0c86dc-743d-4220-a53f-da43a8cbc955/\
resource/d12f9a6d-aa9c-404f-82a8-9dcaaffebc28/download/uniones_hecho_parejas.json"

        my_request = requests.get(url).json()
        with open('../DATAS/couples.json', 'w', encoding="utf8") as my_file:
            json.dump(my_request, my_file, indent=4, ensure_ascii=False)


    @property
    def get_data(self):
        with open("../DATAS/couples.json", encoding="utf8") as my_file:
            my_json = json.load(my_file)
            my_data = my_json["data"]
            return my_data


    @property
    def separe_sample(self):
        sample1 = filter((lambda x: x["inscripcion_año"] <= "2005"), self.get_data)
        sample2 = filter((lambda x: x["inscripcion_año"] > "2005"), self.get_data)
        return [sample1, sample2]


    @property
    def proportion(self):
        proportion_Dict = {}
        proportion_Dict1 = {}
        kinds_of_couple = {couple["pareja_tipo"] for couple in self.get_data}
        counter1 = 0
        for couple in kinds_of_couple:
            for sample in self.separe_sample[0]:
                if sample["pareja_tipo"] == couple:
                    counter1 += int(sample["num_inscripciones"])
            proportion_Dict[couple] = counter1
            counter1 = 0
        for couple in kinds_of_couple:
            for sample in self.separe_sample[1]:
                if sample["pareja_tipo"] == couple:
                    counter1 += int(sample["num_inscripciones"])
            proportion_Dict1[couple] = counter1
            counter1 = 0
        
        porcentage1 = sum([value for value in proportion_Dict.values()])
        porcentage2 = sum([value for value in proportion_Dict1.values()])
        proportion = {}
        proportion1 = {}
        
        for key, value in proportion_Dict.items():
            porc = (value*100)/porcentage1
            proportion[key] = round(porc, 2)
        for key, value in proportion_Dict1.items():
            porc = (value*100)/porcentage2
            proportion1[key] = round(porc, 2)
        return proportion, proportion1


    @property
    def proportion_couple(self):
        proportion_sample_1 = self.proportion[0]
        proportion_sample_2 = self.proportion[1]
        return [proportion_sample_1, proportion_sample_2]


    @property
    def proportion_by_YEAR(self):
        list_years = sorted({year["inscripcion_año"] for year in self.get_data})
        proportion_couple_by_year = {}
        counter, counter1 = 0, 0
        for year in list_years:
            for sample in self.get_data:
                if sample["inscripcion_año"] == year:
                    if sample["pareja_tipo"] == "heterosexual":
                        counter += int(sample["num_inscripciones"])
                    elif "homosexual" in sample["pareja_tipo"]:
                        counter1 += int(sample["num_inscripciones"])
            proportion_couple_by_year[year] = {"heterosexual": counter, "homosexual": counter1}
            counter, counter1 = 0, 0
        
        porcentage_couple_by_year = []
        for year, couple in proportion_couple_by_year.items():
            total_couple = couple['heterosexual'] + couple['homosexual']
            porcentage_hetero = (couple['heterosexual']*100)/total_couple
            porcentage_homo = (couple['homosexual']*100)/total_couple
            porcentage_couple_by_year.append({
                                        'year': year,
                                        'heterosexual': round(porcentage_hetero, 2),
                                        'homosexual': round(porcentage_homo, 2)
                                    })
        return porcentage_couple_by_year


def graphic(obj):
    couples = obj.proportion_couple[1]
    female_homo = couples['homosexual femenina']
    male_homo = couples['homosexual masculina']
    hetero = couples['heterosexual']
    couples = [female_homo, male_homo, hetero]
    names = ['homosexual femenina', 'homosexual masculina', 'heterosexual']
    plt.pie(couples, labels=names, autopct="%0.1f %%")
    plt.show()


obj = Unamed_CLASS()
print(obj.proportion_by_YEAR)
#print(len(obj.get_data))
#graphic(obj)
















#print(obj.get_data)
"""
l, m = [1,2,3,4,4], [2,1,3,2,4,2,2]
s = []
for i, x in itertools.zip_longest(l,m):
    if type(i) == int and type(x) == int:
        t = i*x
        s.append(t)
    elif type(x) == int:
        s.append(x)
    elif type(i) == int:
        s.append(i)
    print(i, x)
print(s)
"""
