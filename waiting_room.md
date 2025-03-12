# Explicação do Código:

### Fila de usuários:
Usamos a classe Queue do módulo queue para criar uma fila que armazena os usuários na ordem de chegada.

### Processamento do usuário:
A função processar_usuario simula o tempo de processamento (usando time.sleep) e exibe mensagens indicando quando o processamento inicia e termina.

### Trabalhador:
A função trabalhador é executada por cada thread (simbolizando um servidor). Ela retira usuários da fila e os processa enquanto a fila não estiver vazia.

### Threads:
Criamos 3 threads para simular que o site possui 3 "servidores" processando as requisições simultaneamente. Cada thread pega um usuário da fila e o processa.

### Sincronização:
Utilizamos fila_usuarios.join() para garantir que o programa só termine após todos os usuários terem sido processados, e t.join() para aguardar o término de cada thread.

