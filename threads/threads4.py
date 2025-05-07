from time import sleep
from threading import Thread, Lock

class Ingressos:
    def __init__(self, estoque):
        self.estoque = estoque
        self.lock = Lock()

    def comprar(self, quantidade):
        with self.lock:
            if self.estoque < quantidade:
                print('Não temos ingressos suficientes')
                return
            
            sleep(1)

            self.estoque -= quantidade
            print(f'Você comprou {quantidade} ingresso(s). '
                  f'Ainda temos {self.estoque}')

    def verificar_estoque(self):
        while True:
            with self.lock:
                print(f'Estoque atual: {self.estoque}')
            sleep(2)

if __name__ == '__main__':
    ingressos = Ingressos(10)

    # Thread para verificar o estoque constantemente
    t_verificacao = Thread(target=ingressos.verificar_estoque, daemon=True)
    t_verificacao.start()

    # Thread para comprar ingressos
    for i in range(1, 6):  # Ajustado para comprar ingressos até acabar
        t_compra = Thread(target=ingressos.comprar, args=(1,))
        t_compra.start()
        sleep(0.5)  # Pequeno delay para melhor visualização da execução
