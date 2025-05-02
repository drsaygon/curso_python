from time import sleep
from threading import Thread

class MeuThread(Thread):
    def __init__(self, texto, tempo):
        self.texto = texto
        self.tempo = tempo

        super().__init__()

    def run(self):
        sleep(self.tempo)
        print(self.texto)
'''
thread1 = MeuThread('Thread 1', 5)
thread1.start()

for i in range(20):
    print(i)
    sleep(1)
'''
def vai_demorar(texto, tempo):
    sleep(tempo)
    print(texto)

t1 = Thread(target=vai_demorar, args=('Ólá mundo 1!', 5))
t1.start()

t2 = Thread(target=vai_demorar, args=('Ólá mundo 2!', 2))
t2.start()

while t1.is_alive():
    print('Esperando a execução da thread...')
    sleep(2)