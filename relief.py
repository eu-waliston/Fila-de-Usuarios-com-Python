import time
import queue
import threading
import random

def processar_usuario(usuario):
    print(f"Iniciando o processamento de {usuario}...")
    # Simula o tempo de processamento (entre 1 e 3 segundos)
    time.sleep(random.uniform(1, 3))
    print(f"{usuario} processado com sucesso!")

def trabalhador(fila):
    while True:
        try:
            # Tenta pegar um usuário da fila; se não houver por 3 segundos, encerra a thread
            usuario = fila.get(timeout=3)
        except queue.Empty:
            break
        processar_usuario(usuario)
        fila.task_done()

def monitorar_fila(fila, trabalhadores, limite_fila, max_trabalhadores):
    while not fila.empty():
        tamanho_atual = fila.qsize()
        if tamanho_atual > limite_fila and len(trabalhadores) < max_trabalhadores:
            # Cria uma nova thread para ajudar no processamento
            nova_thread = threading.Thread(target=trabalhador, args=(fila,))
            nova_thread.start()
            trabalhadores.append(nova_thread)
            print(f"Nova thread adicionada! Total de threads: {len(trabalhadores)}")
        time.sleep(1)  # Verifica a cada 1 segundo

if __name__ == "__main__":
    # Cria a fila e adiciona 20 usuários
    fila_usuarios = queue.Queue()
    for i in range(1, 21):
        fila_usuarios.put(f"Usuário {i}")

    trabalhadores = []
    num_inicial_threads = 3      # Número inicial de threads
    limite_fila = 5              # Se a fila tiver mais que 5 itens, adiciona nova thread
    max_trabalhadores = 10       # Limite máximo de threads

    # Inicia as threads iniciais
    for _ in range(num_inicial_threads):
        t = threading.Thread(target=trabalhador, args=(fila_usuarios,))
        t.start()
        trabalhadores.append(t)

    # Inicia uma thread monitor para verificar a fila e desafogá-la se necessário
    monitor_thread = threading.Thread(target=monitorar_fila, args=(fila_usuarios, trabalhadores, limite_fila, max_trabalhadores))
    monitor_thread.start()

    # Aguarda o processamento completo de todos os usuários
    fila_usuarios.join()
    monitor_thread.join()
    for t in trabalhadores:
        t.join()

    print("Todos os usuários foram processados!")
