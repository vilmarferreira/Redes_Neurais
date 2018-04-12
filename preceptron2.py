import numpy as np

entradas = np.array([1, 7, 5])
pesos = np.array([0.8, 0.1, 0])

def soma (e, p):
    return e.dot(p)
#dot product/produto escalar

def stepFunction(soma):
    if(soma >= 1):
        return 1
    else:
        return 0

s = soma(entradas, pesos)
print(s)

r = stepFunction(s)
print(r)
