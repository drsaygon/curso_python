from time import sleep
from threading import Thread

class MeuThread(Thread):
    def __init__(self, texto, tempo):
        self.texto = texto
        self.tempo = tempo

        # Se não chamássemos super().__init__(), a instância de MeuThread não seria
        # corretamente registrada como uma thread, e os métodos próprios de Thread 
        # (como start()) poderiam não funcionar como esperado.
        super().__init__()

    def run(self):
        sleep(self.tempo)
        print(self.texto)

thread1 = MeuThread('Thread 1', 5)
thread1.start()

for i in range(20):
    print(i)
    sleep(1)