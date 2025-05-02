class TesteArgs:
    def __init__(self, *args):
        if len(args) >= 3:
            self.a = args[0]
            self.b = args[1]
            self.c = args[2]
        else:
            self.a = 1
            self.b = 2
            self.c = 3

class TesteKwargs:
    def __init__(self, **kwargs):
        self.a = kwargs.get('a', 1)
        self.b = kwargs.get('b', 2)
        self.c = kwargs.get('c', 3)
    
teste_args = TesteArgs(10, 20, 30)
teste_kwargs = TesteKwargs(a=11, b=21, c=31)

print(teste_args.a)
print(teste_args.b)
print(teste_args.c)
print(teste_kwargs.a)
print(teste_kwargs.b)
print(teste_kwargs.c)
