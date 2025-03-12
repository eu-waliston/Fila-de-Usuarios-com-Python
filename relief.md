# Explicação do Código

### Fila de Usuários:
Utilizamos a classe Queue para armazenar os usuários na ordem de chegada.

### Função trabalhador:
Cada thread executa essa função, retirando usuários da fila e processando-os. Se não houver usuário disponível por 3 segundos (indicando que a fila está esvaziando), a thread encerra.

### Função monitorar_fila:
Essa função verifica periodicamente o tamanho da fila. Se o número de usuários na fila ultrapassar o limite definido (nesse exemplo, 5) e ainda não atingimos o número máximo de threads (10), ela cria uma nova thread para ajudar no processamento, "desafogando" a fila.

### Execução Principal:
Inicialmente, criamos 3 threads para processar os usuários. Em seguida, uma thread de monitoramento é iniciada para dinamicamente adicionar mais threads se a fila estiver congestionada.