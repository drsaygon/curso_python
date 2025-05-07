class Ingresso:
    def __init__ (self, estoque):
        self.estoque = estoque

    def comprar(self, quantidade):
        if quantidade > self.estoque:
            return 'Ingressos esgotados'
        self.estoque -= quantidade
        return f'Estoque: {self.estoque} \nComprado: {quantidade}'
    
if __name__ == '__main__':
    ingresso = Ingresso(10)
    print(ingresso.comprar(1))
    print(ingresso.comprar(1))
    print(ingresso.comprar(1))