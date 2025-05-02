# def texto_decorador(func):
#     def gerador(self, texto):
#         return f'Você digitou: {func(self, texto)}'
#     return gerador

# class TesteA:
#     def __init__(self):
#         print('Início A')

#     @texto_decorador
#     def gerar_texto(self, texto):
#         return texto
    
# class TesteB:
#     def __init__(self):
#         print('Início B')

#     @texto_decorador
#     def gerar_texto(self, texto):
#         return texto

# testea = TesteA()
# print(testea.gerar_texto('123'))

# testeb = TesteB()
# print(testeb.gerar_texto('456'))


from functools import wraps

def texto_decorador(func):
    @wraps(func)
    def gerador(self, texto):
        return f'Você digitou: {func(self, texto)}'
    return gerador

class TesteA:
    def __init__(self):
        print('Início A')

    @texto_decorador
    def gerar_texto(self, texto):
        return texto

class TesteB:
    def __init__(self):
        print('Início B')

    @texto_decorador
    def gerar_texto(self, texto):
        return texto

testea = TesteA()
print(testea.gerar_texto('123'))

testeb = TesteB()
print(testeb.gerar_texto('456'))
