def contagem_regressiva(numero):
    print(numero)
    if numero <= 0: 
        return
    else:
        contagem_regressiva(numero - 1) 

contagem_regressiva(3)

def fatorial(numero):
    if numero == 1:
        return 1
    else:
        return numero * fatorial(numero - 1) 

print(fatorial(3))