class Multiplicar:
    def __init__(self, funcao):
        self.funcao = funcao

    def __call__(self, *args):
        return self.funcao(*args)

@Multiplicar
def soma(x, y):
    return x + y

teste = soma(10, 20)
print(teste)
