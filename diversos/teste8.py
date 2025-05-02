# Melhor exemplo de classe e herança

class Pessoa:
    def __init__(self, altura, peso, cor):
        self.altura = altura
        self.peso = peso
        self.cor = cor

    def Caracteristicas(self):
        return(self.altura, self.peso, self.cor)
    
class Aluno(Pessoa):
    def __init__(self, altura, peso, cor, matricula):
        super().__init__(altura, peso, cor)
        self.matricula = matricula

    def InfoAluno(self):
        return f'Matrícula: {self.matricula}, Altura: {self.altura}, Peso: {self.peso}, Cor: {self.cor}'
    
aluno = Aluno('172', '70', 'Branca', '27367482')
print(aluno.InfoAluno())