r1 = 10
r2 = 20


def somar(r1,r2):
    resultado = r1 + r2
    return resultado
print('soma em série:', somar(r1, r2))

def somar(r1,r2):
    paralelo = (r1*r2)/(r1+r2)
    return paralelo
print('soma em paralelo:', somar(r1, r2))

