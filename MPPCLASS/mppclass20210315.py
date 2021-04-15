"""
listB = [a for a in [1,2,3,4,5,6,7,8,9,10] if a%2==0  ]
listC = [a.capitalize() for a in ['jose', 'maria', 'alicia']]


listE = []


listD = [2, 9, 1, 29, 3, 45, 19, 47, 4, 98, 25]
print(f"original list: {listD}")
for i in range(0, len(listD)):
    if len(listD) == 0:
        pass
    else:
        a = min(listD)
        listE.append(a)
        listD.pop(listD.index(a))

print(f"Ordered list: {listE}")
#print(listD)
#print(listB)
#print(listC)
"""
course = [
    {
        "name": "Viktor Navorski",
        "grade": 10
    },
    {
        "name": "Leo Di Caprio",
        "grade": 3
    },
    {
        "name": "John Williams",
        "grade": 10
    },
    {
        "name": "Meryl Streep" ,
        "grade": 4
    },
    {
        "name": "Jack Black",
        "grade": 1
    },
    {
        "name": "Jennifer Lopez",
        "grade": 7
    },
    {
        "name": "Nicole Kidman",
        "grade": 8
    },
]

def classMPP(listCourse):
    above7 = []
    bellow7 = []
    for dicCourse in listCourse:
        for key, value in dicCourse.items():
            if isinstance(value, int):
                if value < 7:
                    bellow7.append(dicCourse['name'])
                else:
                    above7.append(dicCourse['name'])
    return (bellow7, above7)

def classMPP1(listCourse):
    above7 = []
    bellow7 = []
    for dicCourse in listCourse:
        if dicCourse['grade'] < 7:
            bellow7.append(dicCourse)
        else:
            above7.append(dicCourse)
    return f"Approved students: {bellow7}", f"Suspended students: {above7}"



print(classMPP1(course))
