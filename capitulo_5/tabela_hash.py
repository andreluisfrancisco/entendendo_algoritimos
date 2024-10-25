votantes = {}

def verificar_votante(nome):
    if votantes.get(nome):
        print("Expulsar!")
    else:
        votantes[nome] = True
        print("Deixar votar!")
