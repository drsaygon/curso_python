class TesteA:
    def __init__(self):
        print('Início A')

    def gerar_texto(self, texto):
        return f'Você digitou: {texto}'
    
class TesteB(TesteA):
    def __init__(self):
        super().__init__()
        #print('Início B')

testea = TesteA()
print(testea.gerar_texto('123'))

testeb = TesteB()
print(testeb.gerar_texto('123'))
