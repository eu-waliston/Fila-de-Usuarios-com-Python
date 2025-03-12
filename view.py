import tkinter as tk
import threading
import queue
import time
import random

class QueueSimulator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Simulação de Fila de Usuários")
        self.geometry("550x450")

        # Configurações da simulação
        self.queue = queue.Queue()
        self.trabalhadores = []
        self.num_inicial_threads = 3      # Número inicial de threads
        self.limite_fila = 5              # Se a fila tiver mais que 5 itens, adiciona nova thread
        self.max_trabalhadores = 10       # Limite máximo de threads
        self.processed_count = 0

        # Interface gráfica
        tk.Label(self, text="Fila de Usuários:").pack(pady=5)
        self.listbox = tk.Listbox(self, width=50, height=10)
        self.listbox.pack(pady=5)

        self.status_label = tk.Label(self, text="Status: Aguardando início")
        self.status_label.pack(pady=5)

        self.start_button = tk.Button(self, text="Iniciar Simulação", command=self.start_simulation)
        self.start_button.pack(pady=10)

        # Atualiza a interface a cada 1 segundo
        self.after(1000, self.update_ui)

    def start_simulation(self):
        self.start_button.config(state=tk.DISABLED)
        # Adiciona 20 usuários na fila e na lista visual
        for i in range(1, 21):
            usuario = f"Usuário {i}"
            self.queue.put(usuario)
            self.listbox.insert(tk.END, usuario)

        self.status_label.config(text="Simulação iniciada")

        # Inicia as threads iniciais para processamento
        for _ in range(self.num_inicial_threads):
            t = threading.Thread(target=self.worker, daemon=True)
            t.start()
            self.trabalhadores.append(t)

        # Inicia uma thread monitor para verificar a fila e adicionar novas threads se necessário
        monitor_thread = threading.Thread(target=self.monitor_queue, daemon=True)
        monitor_thread.start()

    def worker(self):
        while True:
            try:
                # Tenta obter um usuário da fila (timeout de 3s para encerrar se a fila esvaziar)
                usuario = self.queue.get(timeout=3)
            except queue.Empty:
                break
            # Atualiza a interface: remove o usuário da lista visual
            self.remove_user_from_list(usuario)
            self.status_label.config(text=f"Processando {usuario}...")
            # Simula o tempo de processamento
            time.sleep(random.uniform(1, 3))
            self.processed_count += 1
            self.status_label.config(text=f"{usuario} processado!")
            self.queue.task_done()

    def monitor_queue(self):
        while not self.queue.empty():
            if self.queue.qsize() > self.limite_fila and len(self.trabalhadores) < self.max_trabalhadores:
                # Cria uma nova thread para ajudar no processamento
                t = threading.Thread(target=self.worker, daemon=True)
                t.start()
                self.trabalhadores.append(t)
                self.status_label.config(text=f"Nova thread adicionada! Total de threads: {len(self.trabalhadores)}")
            time.sleep(1)

    def remove_user_from_list(self, usuario):
        # Garante que a atualização da interface seja feita na thread principal
        def remover():
            items = self.listbox.get(0, tk.END)
            for idx, item in enumerate(items):
                if item == usuario:
                    self.listbox.delete(idx)
                    break
        self.after(0, remover)

    def update_ui(self):
        # Atualiza o título da janela com informações atuais
        self.title(f"Processados: {self.processed_count} | Na fila: {self.queue.qsize()} | Threads: {len(self.trabalhadores)}")
        self.after(1000, self.update_ui)

if __name__ == "__main__":
    app = QueueSimulator()
    app.mainloop()
