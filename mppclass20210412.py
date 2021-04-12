

#* Operadores ternarios
#order_typed = input("Enter something: ")

#result = "you typed a number" if isinstance(order_typed, int) else "you typed a string" #if isinstance(float(order_typed), float) else "you typed a float"
#print(result)


"""
va = 'victor'
print(hex(id(va)))

def vas():
    return "victor"

valor = vas
print(valor)
print(hex(id(valor)))
"""

#* GENERATOR

def get_sqr(list_given):
    for item in list_given:
        yield item**2

l = [1, 3, 2, 8, 7]
func = get_sqr(l)

print(func)
print(hex(id(func)))