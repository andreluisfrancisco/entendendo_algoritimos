votantes = {}

def verificar_votante(nome):
    if votantes.get(nome):
        print("Expulsar!")
    else:
        votantes[nome] = True
        print("Deixar votar!")

# Exemplo de uso
# verificar_votante("Alice")  # Deixar votar!
# verificar_votante("Alice")  # Expulsar!
