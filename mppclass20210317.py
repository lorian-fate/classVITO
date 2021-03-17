"""
listA = ['a', 'b', 'c', 'd']
listB = [1, 2, 3, 4]
listC = ['A', 'B', 'C', 'D']

for lA, lB, lC in zip(listA, listB, listC):
    print(lA, lC, lB)
"""
lista = [1, 2, 3, 4]
print([element*2 if element > 2 else element for element in lista])

listaC = []
for element in lista:
    if element > 2:
        listaC.append(element*2)
    else:
        listaC.append(element)
print(listaC)


