entradas = [1, 7, 5]
pesos = [0.8, 0.1, 0]

def soma (e, p):
    s = 0
    for i in range(3):
        s += e[i] * p[i]
    return s

def stepFunction(soma):
    if(soma >= 1):
        return 1
    else:
        return 0

s = soma(entradas, pesos)
print(s)

r = stepFunction(s)
print(r)
