def pesquisa_binaria(lista, item):
    limite_inferior = 0
    limite_superior = len(lista) - 1

    while limite_inferior <= limite_superior:
        indice_meio = (limite_inferior + limite_superior) // 2
        valor_meio = lista[indice_meio]
        
        if valor_meio == item:
            return indice_meio
        elif valor_meio > item:
            limite_superior = indice_meio - 1
        else:
            limite_inferior = indice_meio + 1

    return None 

minha_lista = [1, 3, 5, 7, 9]

resultado_encontrado = pesquisa_binaria(minha_lista, 9) 
resultado_nao_encontrado = pesquisa_binaria(minha_lista, -1)

print(resultado_encontrado) 
print(resultado_nao_encontrado) 