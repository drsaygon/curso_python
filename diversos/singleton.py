class AppSettings:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance
    
    def __init__(self):
        self.tema = 'azul'
        self.font = '18px'
        
if __name__ == "__main__":
    as1 = AppSettings()
    print(as1)
    print(as1.tema)
    as1.nome = 'Teste'

    as2 = AppSettings()
    print(as1 == as2)
    print(as2.nome)

    as1.tema = 'claro'
    print(as1.tema)
    print(as2.tema)