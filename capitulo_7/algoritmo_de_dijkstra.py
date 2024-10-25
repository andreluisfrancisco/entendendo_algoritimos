grafo = {}
grafo["inicio"] = {}
grafo["inicio"]["a"] = 6
grafo["inicio"]["b"] = 2
grafo["a"] = {}
grafo["a"]["fim"] = 1
grafo["b"] = {}
grafo["b"]["a"] = 3
grafo["b"]["fim"] = 5
grafo["fim"] = {}

infinito = float("inf") 
custos = {}
custos["a"] = 6
custos["b"] = 2
custos["fim"] = infinito

pais = {}
pais["a"] = "inicio"
pais["b"] = "inicio"
pais["fim"] = None

processados = []

def encontrar_no_com_menor_custo(custos):
    menor_custo = float("inf")
    no_menor_custo = None
    for no in custos:
        custo = custos[no]
        if custo < menor_custo and no not in processados:
            menor_custo = custo
            no_menor_custo = no
    return no_menor_custo

no_atual = encontrar_no_com_menor_custo(custos)  
while no_atual is not None: 
    custo_atual = custos[no_atual] 
    vizinhos = grafo[no_atual] 
    for vizinho in vizinhos.keys():
        novo_custo = custo_atual + vizinhos[vizinho]  
        if custos[vizinho] > novo_custo: 
            custos[vizinho] = novo_custo 
            pais[vizinho] = no_atual 
    processados.append(no_atual) 
    no_atual = encontrar_no_com_menor_custo(custos)

print(custos["fim"]) 
