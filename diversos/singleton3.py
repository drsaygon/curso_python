# voltou a ser singleton

def singleton(the_class):
    instances = {}

    def get_class(*args, **kwargs):
        if the_class not in instances:
            instances[the_class] = the_class(*args, **kwargs)
        return instances[the_class]

    return get_class

@singleton
class AppSettings:
    def __init__(self):
        self.tema = 'azul'
        self.font = '18px'

@singleton
class Teste:
    def __init__(self):
        print('oi')
        
if __name__ == "__main__":
    as1 = AppSettings()
    print(as1)
    print(as1.tema)

    as2 = AppSettings()
    print(as1 == as2)

    as1.tema = 'claro'
    print(as1.tema)
    print(as2.tema)

    # Só vai iniciar uma vez
    teste1 = Teste()
    teste2 = Teste()
    teste3 = Teste()