

for x in range(1,100):
    y = str(x)[::-1]
    t = x + float(y)
    if t == 100:
        print(x, y)


#print(dir(str))