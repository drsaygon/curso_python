# contorna o problema anterior, onde a definição de um tema valia para todas as instâncias
# desse jeito, cada instância tem seus valores
# assim não é singleton

def singleton(the_class):
    print(the_class)
    return the_class

@singleton
class AppSettings:
    def __init__(self):
        self.tema = 'azul'
        self.font = '18px'
        
if __name__ == "__main__":
    as1 = AppSettings()
    print(as1)
    print(as1.tema)

    as2 = AppSettings()
    print(as1 == as2)

    as1.tema = 'claro'
    print(as1.tema)
    print(as2.tema)