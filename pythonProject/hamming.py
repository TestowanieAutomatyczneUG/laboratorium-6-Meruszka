def distance(x: str, y: str):
    if len(x) == len(y):
        if len(x) == 0 or len(y) == 0:
            return 0
        x = x.split('')
        y = y.split('')
        suma = 0
        for i in range(len(x)):
            if x[i] == y[i]:
                suma +=1
        return suma
    else:
        raise ValueError