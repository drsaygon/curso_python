# versão melhorada
class Ingresso:
    def __init__(self, estoque):
        self.estoque = estoque

    def comprar(self, quantidade):
        if quantidade > self.estoque:
            return "Ingressos esgotados"
        
        self.estoque -= quantidade
        return f"Você comprou: {quantidade}\nIngressos disponíveis: {self.estoque}"

if __name__ == '__main__':
    ingresso = Ingresso(10)
    print(ingresso.comprar(1))
    print(ingresso.comprar(1))


'''
# versão inicial
class Ingresso:
    def __init__(self, estoque):
        self.estoque = estoque

    def comprar(self, quantidade):
        self.quantidade = quantidade
        if (quantidade > self.estoque):
            print('Ingressos esgotados')
            return
        self.estoque -= quantidade
        print(f'Você comprou: {quantidade}')
        print(f'Ingressos disponíveis: {self.estoque}')

class Main:
    ingresso = Ingresso(10)
    ingresso.comprar(1)
    ingresso.comprar(1)

if __name__ == '__main__':
    Main()
'''

    