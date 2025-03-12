# Como o Código Funciona

### Interface Gráfica (Tkinter):
A janela exibe uma lista (Listbox) com os usuários enfileirados, um rótulo de status e um botão para iniciar a simulação.

### Enfileiramento e Processamento:
Ao clicar no botão, 20 usuários são adicionados a uma fila. Três threads iniciais são criadas para processar esses usuários. Cada thread retira um usuário da fila, simula o processamento (com uma pausa aleatória) e, após o processamento, atualiza a contagem de usuários processados.

### Monitoramento e "Desafogamento":
Uma thread monitor observa o tamanho da fila e, se o número de itens ultrapassar um limite definido (5 neste exemplo) e o total de threads for menor que o máximo permitido (10), uma nova thread é iniciada para acelerar o processamento.

### Atualização da Interface:
O método update_ui atualiza periodicamente o título da janela com informações sobre o número de usuários processados, quantos ainda estão na fila e quantas threads estão ativas. A função remove_user_from_list remove de forma segura os itens da lista visual à medida que são processados.