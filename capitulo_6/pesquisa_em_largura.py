from collections import deque

grafo = {
    "vendedor_1": ["vendedor_2", "vendedor_3", "vendedor_4"],
    "vendedor_2": ["vendedor_6"],
    "vendedor_3": ["vendedor_5", "vendedor_6"],
    "vendedor_4": ["vendedor_7", "vendedor_8"],
    "vendedor_5": [],
    "vendedor_6": [],
    "vendedor_7": [],
    "vendedor_8": []
}

def eh_vendedor_de_manga(nome):
    return nome[-1] == "1"

def busca_vendedor(inicio_pessoa):
    fila_de_busca = deque() 
    fila_de_busca += grafo[inicio_pessoa]
    pesquisados = set()

    while fila_de_busca:
        pessoa = fila_de_busca.popleft()
        if pessoa not in pesquisados:
            if eh_vendedor_de_manga(pessoa):
                print(f"{pessoa} é um vendedor de manga!")
                return True
            fila_de_busca += grafo[pessoa]
            pesquisados.add(pessoa)
    
    print("Nenhum vendedor de manga foi encontrado.")
    return False

busca_vendedor("vendedor_1")
