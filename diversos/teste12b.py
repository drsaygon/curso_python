# Definição dos módulos de cálculo
class ModuloA:
    def __soma(self, a, b):
        return a + b

    def acessar_soma(self, a, b):
        # Regra de controle: evita somas acima de 10.000
        if a + b > 10000:
            raise ValueError("Valor muito alto!")
        return self.__soma(a, b)

# Classe principal que herda diretamente ModuloA
class Calculations(ModuloA):
    def calcular(self, num1, num2):
        return self.acessar_soma(num1, num2)  # Agora chama diretamente o método herdado

# Testando
calc = Calculations()
print(f'Cálculo: {calc.calcular(5, 5)}')

# Testando acesso direto a acessar_soma
teste = calc.acessar_soma(5, 5)
print(f'Teste direto: {teste}')
