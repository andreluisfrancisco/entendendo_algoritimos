estados_necessarios = set(["ac", "al", "ap", "ba", "ce", "df", "es", "go", "ma", "mt", "ms", "mg", "pa", "pb", "pr", "pe", "pi", "rj", "rn", "rs", "ro", "rr", "sc", "se", "sp", "to"])

estacoes = {
    "estacao1": set(["ac", "ro", "am"]),
    "estacao2": set(["ap", "pa", "ma"]),
    "estacao3": set(["ce", "pb", "pe"]),
    "estacao4": set(["ba", "mg", "es"]),
    "estacao5": set(["sp", "rj", "pr"]),
    "estacao6": set(["rs", "sc", "to"]),
    "estacao7": set(["df", "go", "ms"]),
}

estacoes_finais = set()

def encontrar_melhor_estacao(estados_necessarios, estacoes):
    """Encontra a estação que cobre o maior número de estados não cobertos."""
    melhor_estacao = None
    estados_cobertos = set()
    
    for estacao, estados_cobertos_por in estacoes.items():
        cobertos = estados_necessarios & estados_cobertos_por 
        if len(cobertos) > len(estados_cobertos):
            melhor_estacao = estacao
            estados_cobertos = cobertos
            
    return melhor_estacao, estados_cobertos

while estados_necessarios: 
    melhor_estacao, estados_cobertos = encontrar_melhor_estacao(estados_necessarios, estacoes)
    if melhor_estacao is None:
        break
    estados_necessarios -= estados_cobertos
    estacoes_finais.add(melhor_estacao)

print(estacoes_finais) 
