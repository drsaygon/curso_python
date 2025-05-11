class Meta(type):
    def __call__(cls, *args, **kwargs):
        print('1')
        return super().__call__(*args, **kwargs)

class Pessoa(metaclass=Meta):
    def __new__(cls, *args, **kwargs):
        print('2')
        return super().__new__(cls)

    def __init__(self, nome):
        print('3')
        self.nome = nome

    def __call__(self, x, y):
        print('Call chamado', self.nome, x + y)

if __name__ == '__main__':
    teste = Pessoa('José')
    teste(10, 10)