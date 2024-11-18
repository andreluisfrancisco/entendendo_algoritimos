class Aula:
    def __init__(self, nome, duracao, professor):
        self.nome = nome
        self.duracao = duracao 
        self.professor = professor

class Sala:
    def __init__(self, nome, capacidade):
        self.nome = nome
        self.capacidade = capacidade

class Cronograma:
    def __init__(self):
        self.aulas = []
        self.salas = []
        self.agendamentos = {}
    
    def adicionar_aula(self, aula):
        self.aulas.append(aula)

    def adicionar_sala(self, sala):
        self.salas.append(sala)
    
    def agendar_aula(self, aula, sala, horario):
        if sala.nome not in self.agendamentos:
            self.agendamentos[sala.nome] = {}
        
        if horario not in self.agendamentos[sala.nome]:
            self.agendamentos[sala.nome][horario] = aula
            print(f'Aula "{aula.nome}" agendada na sala "{sala.nome}" para o horário {horario}.')
        else:
            print(f'Conflito: A sala "{sala.nome}" já está agendada para o horário {horario}.')
    
if __name__ == "__main__":
    aula_matematica = Aula("Matemática", 1.5, "Prof. Silva")
    aula_fisica = Aula("Física", 1.0, "Prof. Souza")
    aula_quimica = Aula("Química", 2.0, "Prof. Lima")

    sala_a = Sala("Sala A", 30)
    sala_b = Sala("Sala B", 25)

    cronograma = Cronograma()

    cronograma.adicionar_aula(aula_matematica)
    cronograma.adicionar_aula(aula_fisica)
    cronograma.adicionar_aula(aula_quimica)

    cronograma.adicionar_sala(sala_a)
    cronograma.adicionar_sala(sala_b)

    cronograma.agendar_aula(aula_matematica, sala_a, "07:00")
    cronograma.agendar_aula(aula_fisica, sala_a, "09:30")
    cronograma.agendar_aula(aula_quimica, sala_b, "10:00")
    
    cronograma.agendar_aula(aula_fisica, sala_a, "09:30")

#config token 