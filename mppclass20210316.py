import random

"""
Siendo estas las siguientes listas, cree una función que permita crear una nueva lista que empiece por los alumnos del turno mañana

Python por las mañanas: ["Patricia", "Nicole", "Verónica", "Javier", "Guillermo", "Javier", "Pablo"]
Python por las tardes: ["Germán", "Sara", "José", "Claudio", "Rubén", "Sandra"]

"""
maniana = [
    {"name": "Patricia", "id" :  "001", 'gender': 'F'},
    {"name": "Nicole", "id" :  "002", 'gender': 'F'},
    {"name": "Javier", "id" :  "003", 'gender': 'M'},
    {"name": "Verónica", "id" :  "004", 'gender': 'F'},
    {"name": "Guillermo","id" :  "005", 'gender': 'M'},
    {"name": "Pablo", "id" :  "006", 'gender': 'M'},
    {"name": "Evander", "id" :  "007", 'gender': 'M'},
    {"name": "Isabel", "id" :  "008", 'gender': 'F'},
    ]

tarde =[
    {"name": "Germán", "id" :  "001", 'gender': 'M'},
    {"name": "Sara", "id" :  "002", 'gender': 'F'},
    {"name": "Jorge", "id" :  "003", 'gender': 'M'},
    {"name": "María", "id" :  "004", 'gender': 'F'},
    {"name": "Alicia", "id" :  "006", 'gender': 'F'},
    {"name": "Hernesto", "id" :  "006", 'gender': 'M'},
    ]
new_students = ["Miguel", "Pedro", "Sandra"]

"""

Ejercicio 1: Agregar al curso de la tarde los siguiente lista de alumnos, recordad que no pueden tener los mismos id's:
	new_students = ["Miguel", "Pedro", "Sandra"]
	* Debe trabajarse con una lista dada

"""

def addStudents(student_list, evening_students_list):
    list_Student_id = [i['id'] for i in evening_students_list]
    length_student_list = len(student_list)
    id_student = '00'
    counter = 0
    while counter < length_student_list:
        for x in student_list:
            id_ = len(evening_students_list) + 1
            evening_students = {
                    'name': x, 'id': id_student+str(id_)
                }
            student_list.remove(x)
            tarde.append(evening_students)
        counter += 1

#addStudents(new_students, tarde)


"""
Ejercicio 2: Crear una función que permita verificar que ningún id sea igual a otro
"""
def verifyRepeatedID(list_students):
    list_Student_id = [i['id'] for i in list_students]
    dict_repeated = {}
    for x in list_Student_id:
        if list_Student_id.count(x) > 1:
            dict_repeated[x] = list_Student_id.count(x)
    if len(dict_repeated) == 0:
        print("No Id are repeated")
    else:
        for key, value in dict_repeated.items():
            print(f"this id {key} is repeated {value} times")
    return ''      



"""
Ejercicio 4: Agregar a los id de los alumnos por la mañana la letra "M" y a los alumnos por la tarde la letra "T"

"""

def addIDLetter(evening_students_list, morning_student_list):
    for x in evening_students_list:
        for key, value in x.items():
            if key == 'id':
                x[key] = value + 'T'
    for x in morning_student_list:
        for key, value in x.items():
            if key == 'id':
                x[key] = value + 'M'

addIDLetter(tarde, maniana)


"""
Ejercicio 5: Crear una nueva lista con todos los estudiantes de Python
"""
all_python_Student = []
all_python_Student.extend(maniana)
all_python_Student.extend(tarde)
#print(all_python_Student)


"""
Ejercicio 6: De la última lista creada dividir por género
"""
female_list = [i for i in all_python_Student if i['gender'] == 'F']
male_list = [i for i in all_python_Student if i['gender'] == 'M']

#print(female_list)

"""

Ejercicio 7: Crear una función que además de agregar la clave courses a cada uno de los estudiantes, se le pueda indicar uno de los 		
cursos matriculados

"""
def addCourse(student_list):
    course_list = ['python', 'java', 'security IT']
    for x in all_python_Student:
        #choice = input(f'Enter a course for this student {x['name']}: ')
        choice = random.choice(course_list)
        x['course'] = choice

addCourse(all_python_Student)


def searchStudent(id_student):
    id_student_list = [i['id'] for i in all_python_Student]
    try:
        assert id_student in id_student_list
    except AssertionError:
        print(f"this id {id_student} doesn't exist")
    else:
        for i in all_python_Student:
            if i['id'] == id_student:
                print(f"Name: {i['name']} \nId: {i['id']} \nGender: {i['gender']}")
    return ''

"""
print(" ________________________________________________________________________________________")
print("|------------------------|-------------------------------|-------------------------------|")
print('|',"       NAME", '\t\t', '|','\t\t', "ID",'\t\t','|','\t', "     GENDER",'\t\t','|')
print("|------------------------|-------------------------------|-------------------------------|")
for i, x in enumerate(all_python_Student, start=1):
    if len(x['name']) < 8:
        print('|',i,'._', x['name'], '\t\t', '|', '\t\t', x['id'],'\t\t', '|', '\t\t', x['gender'], '\t\t', '|')
        print("|------------------------|-------------------------------|-------------------------------|")
    else:
        print('|',i,'._', x['name'], '\t','|', '\t\t', x['id'], '\t\t', '|', '\t\t', x['gender'], '\t\t', '|')
        print("|------------------------|-------------------------------|-------------------------------|")
print("|________________________________________________________________________________________|")
#print(all_python_Student)
"""
id_student = '001M'

a = lambda id_student: searchStudent(id_student)

print(a(id_student))
print(searchStudent(id_student))