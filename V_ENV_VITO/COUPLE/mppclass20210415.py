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
        sample1 = filter((lambda x: x["inscripcion_año"] <= "2010"), self.get_data)
        sample2 = filter((lambda x: x["inscripcion_año"] > "2010"), self.get_data)
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
        cound = 0
        for year in list_years:
            for sample in self.get_data:
                if sample["inscripcion_año"] == year:
                    if sample["pareja_tipo"] == "heterosexual":
                        counter += int(sample["num_inscripciones"])
                    elif "homosexual" in sample["pareja_tipo"]:
                        counter1 += int(sample["num_inscripciones"])
            coun = counter + counter1
            cound += coun
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

def graphic1(obj):
    my_items = obj.proportion_by_YEAR
    year = [i for i, year in enumerate(my_items, start=1)]
    homo_couple = [homo['homosexual'] for homo in my_items]
    hetero_couple = [hetero['heterosexual'] for hetero in my_items]
    labels_name = ['year', 'homosexual']
    plt.plot(year, homo_couple, label=labels_name)
    plt.plot(year, hetero_couple)
    plt.show()

def z_funct(obj):
    total_couples1 = sum([int(num_couples["num_inscripciones"]) for num_couples in obj.separe_sample[0]])
    total_couples2 = sum([int(num_couples["num_inscripciones"]) for num_couples in obj.separe_sample[1]])
    homo_proportion1 = round((sum([int(num_couples["num_inscripciones"]) for num_couples in obj.separe_sample[0] 
                        if num_couples["pareja_tipo"] != "heterosexual"])*100)/total_couples1, 2)/100
    homo_proportion2 = round((sum([int(num_couples["num_inscripciones"]) for num_couples in obj.separe_sample[1] 
                        if num_couples["pareja_tipo"] != "heterosexual"])*100)/total_couples2, 2)/100
    
    p1, p2, n1, n2 = homo_proportion1, homo_proportion2, total_couples1, total_couples2
    P = round(((n1*p1) + (n2*p2))/(n1 + n2), 2)
    p1_p2_sus = round(p2 - p1, 2)
    denominator = (P*(1 - P)*((1/n1)+(1/n2)))
    Z = round((p2 - p1)/((P*(1-P)*((1/n1)+(1/n2)))**(1/2)), 2)
    return Z


def broken_couples(couple_list):
    for couple in couple_list:
        yield int(couple["num_inscripciones_cancelacion"])


def proportion_broken_couples(broken):
    total = sum([int(couple["num_inscripciones"]) for couple in broken])
    broken_coup = sum(list(broken_couples(broken)))
    return ((broken_coup*100)/total)/100




obj = Unamed_CLASS()
fun = proportion_broken_couples(obj.get_data)
print(fun)


































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
