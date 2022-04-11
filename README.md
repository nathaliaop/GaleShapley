# Execução do projeto
`python galeShapley.py`

# Gale-Shapley
Implementação do algoritmo para achar o emparelhamento estável máximo
O algoritmo usa uma lista de espera para armazenar os estudantes que ainda não foram alocado em algum projeto.
Enquanto a lista de espera não estiver vazia, analiso o primeiro estudante da lista de espera se ele ainda tiver algum projeto não tentado.
Se o estudante tiver a nota mínima para aquele projeto e o projeto ainda tiver vagas disponíveis, o estudante é aceito no projeto.
Caso contrário, ele volta para a fila de espera.
