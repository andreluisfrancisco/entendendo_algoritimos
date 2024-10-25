def quicksort(lista):
    if len(lista) < 2:
        return lista
    else:
        pivô = lista[0]
        menores = [i for i in lista[1:] if i <= pivô]
        maiores = [i for i in lista[1:] if i > pivô]
        return quicksort(menores) + [pivô] + quicksort(maiores)
