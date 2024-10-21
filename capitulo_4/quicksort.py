# 4.1 Função de soma
def soma_lista(lista):
    if len(lista) == 0:
        return 0
    elif len(lista) == 1:
        return lista[0]
    else:
        return lista.pop(0) + soma_lista(lista)

# Exemplo de uso
# print(soma_lista([1, 2, 3]))  # 6
# print(soma_lista([7]))  # 7
# print(soma_lista([]))  # 0

# 4.2 Contar número de itens em uma lista
def contar_itens(lista):
    if len(lista) == 0:
        return 0
    else:
        return 1 + contar_itens(lista[1:])  # [1:] significa do segundo item até o final

# Exemplo de uso
# print(contar_itens([1, 2, 3]))  # 3
# print(contar_itens([]))  # 0

# 4.3 Número máximo em uma lista
def maximo_lista(lista):
    if len(lista) == 0:
        return "erro: a lista deve conter pelo menos um número!"
    elif len(lista) == 1:
        return lista[0]
    else:
        sub_max = maximo_lista(lista[1:])
        return sub_max if sub_max > lista[0] else lista[0]

# Exemplo de uso
# print(maximo_lista([1, 5, 2, 0, 100]))  # 100
# print(maximo_lista([]))  # "erro: a lista deve conter pelo menos um número!"
# print(maximo_lista([9]))  # 9

# Código do Quicksort
def quicksort(lista):
    if len(lista) < 2:
        return lista
    else:
        pivô = lista[0]
        # criar novos sub-arrays consistindo de elementos restantes que são <= pivô
        menores = [i for i in lista[1:] if i <= pivô]
        # criar novos sub-arrays consistindo de elementos restantes que são > pivô
        maiores = [i for i in lista[1:] if i > pivô]
        return quicksort(menores) + [pivô] + quicksort(maiores)

# Exemplo de uso
# print(quicksort([2, 1, 109, 20, 40, 10]))  # [1, 2, 10, 20, 40, 109]
