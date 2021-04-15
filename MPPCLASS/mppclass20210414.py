
#! Funciones anonimas
#? Funciones lambdas
c = lambda b, a: b + a
d = lambda name, gender: f"Sr. {name}" if gender == 'm' else f"Sra. {name}"
print(c)


#? Función map
#* Por cada valor de un iterable se le aplicará una función 
#* devolviendo cada resultado
#* map(funcion, iterable)

def func(x):
    return x**2

def get_sqr(x):
    return x**(1/2)

x = map(func, range(4))
w = map((lambda x, y: x**(1/2)+y), range(4), range(5))

print(list(w))

#? Función filter

w1 = filter((lambda x: x if x%2==0 else None), range(10))
#print(list(w1))

#? Funcion 