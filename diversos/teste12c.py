# Definição dos módulos de cálculo
class ModuloA:
    def __init__(self):
        self.limite = 10000  # Definindo um limite como exemplo

    def __soma(self, a, b):
        return a + b

    def acessar_soma(self, a, b):
        # Regra de controle: evita somas acima do limite definido
        if a + b > self.limite:
            raise ValueError("Valor muito alto!")
        return self.__soma(a, b)

# Classe principal que herda diretamente ModuloA
class Calculations(ModuloA):
    def __init__(self):
        super().__init__()  # Chama o __init__ da classe mãe
        print("Calculations inicializada!")  # Apenas para ilustrar

    def calcular(self, num1, num2):
        return self.acessar_soma(num1, num2)

# Testando
calc = Calculations()
print(f'Cálculo: {calc.calcular(5, 5)}')

# Testando acesso direto
print(f'Teste direto: {calc.acessar_soma(5, 5)}')
