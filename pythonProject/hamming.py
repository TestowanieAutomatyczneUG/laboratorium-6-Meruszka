def distance(x: str, y: str):
    x = x.split('')
    y = y.split('')
    suma = 0
    for i in range(len(x)):
        if x[i] == y[i]:
            suma +=1
    return suma