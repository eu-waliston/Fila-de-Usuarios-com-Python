import time
import queue
import threading
import random

def processar_usuario(usuario):
    print(f"Iniciando o processamento de {usuario}...")
    # Simula o tempo de processamento do usuário (entre 1 e 3 segundos)
    time.sleep(random.uniform(1, 3))
    print(f"{usuario} processado com sucesso!")

def trabalhador(fila):
    while not fila.empty():
        usuario = fila.get()
        processar_usuario(usuario)
        fila.task_done()

if __name__ == "__main__":
    # Cria a fila de usuários
    fila_usuarios = queue.Queue()

    # Simula 10 usuários tentando acessar o site
    for i in range(1, 11):
        fila_usuarios.put(f"Usuário {i}")

    # Cria 3 "servidores" que irão processar os usuários na fila
    threads = []
    for _ in range(3):
        t = threading.Thread(target=trabalhador, args=(fila_usuarios,))
        t.start()
        threads.append(t)

    # Aguarda até que todos os usuários sejam processados
    fila_usuarios.join()

    for t in threads:
        t.join()

    print("Todos os usuários foram processados!")
