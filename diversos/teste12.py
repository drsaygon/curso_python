# Definição dos módulos de cálculo
class ModuloA:
    def __soma(self, a, b):
        return a + b

    def acessar_soma(self, a, b):
        # Regra de controle: evita somas acima de 10.000
        if a + b > 10000:
            raise ValueError("Valor muito alto!")
        return self.__soma(a, b)

# ✅ Mais flexível: ModuloA pode ser substituído ou modificado sem impactar Calculations. 
# ✅ Segue o princípio de composição sobre herança (recomendado por boas práticas). 
# ✅ Facilita testes e manutenção, pois cada classe tem um papel bem definido. 
# 🚫 Pode exigir um pouco mais de código para acessar métodos herdados.

# Classe principal que reúne os módulos
class Calculations:
    def __init__(self):
        self.moduloA = ModuloA()

    def calcular(self, num1, num2):
        return self.moduloA.acessar_soma(num1, num2)  # Controle garantido

# Testando
calc = Calculations()
print(f'Cálculo: {calc.calcular(5,5)}')

# teste = ModuloA().__soma(5,5)
teste = ModuloA().acessar_soma(5,5)

