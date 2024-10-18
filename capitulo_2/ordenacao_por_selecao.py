def encontrar_menor(indice_lista):
    menor_valor = indice_lista[0]
    indice_menor = 0
    for i in range(1, len(indice_lista)):
        if indice_lista[i] < menor_valor:
            menor_valor = indice_lista[i]
            indice_menor = i
    return indice_menor

def ordenar_por_selecao(lista):
    lista_ordenada = []
    while lista:
        indice_menor = encontrar_menor(lista)
        lista_ordenada.append(lista.pop(indice_menor))
    return lista_ordenada

resultado = ordenar_por_selecao([5, 3, 6, 2, 10])
print(resultado)