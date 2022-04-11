# quantidade de vagas e nota mínima de cada projeto
projectPreference = []
# lista de projetos dos estudantes por ordem de prioridade
studentPreference = []
# nota de cada estudante
studentGrade = []
# lista de espera
waitingList = []
# lista que associa cada estudante a um projeto
projectTaken = []
# lista que associa cada projeto aos estudantes
studentTaken = []
# contador para printar o número de iterações
counter = 0

def read_input_file(path):
    with open(path) as f:
        lines = f.readlines()

    for i in range(30):
        projectPreference.append([int(x) for x in lines[i][1:-2].split(', ')[1:]])

    for i in range(30, 130):
        studentPreference.append([int(x[1:]) - 1 for x in lines[i].split(':')[1][1:-6].split(', ')])
        studentGrade.append(int(lines[i].split(':')[1][-3:-2]))

def setup():
    for i in range(100):
        projectTaken.append(-1)

    for i in range(30):
        studentTaken.append([])

    for i in range(100):
        waitingList.append(i)

def print_answer():
    totalAcceptedStudents = 0
    print('\nResultado:')
    for i in range(30):
        totalAcceptedStudents+= len(studentTaken[i])
        if (len(studentTaken[i]) == 0):
            print(f'O projeto {i + 1} não terá alunos')
        else:
            print(f'O projeto {i + 1} terá os alunos {", ".join([str(x + 1) for x in studentTaken[i]])}')
    print(f'\nNúmero total de estudantes aceitos em algum projeto: {totalAcceptedStudents}')

read_input_file('entradaProj2TAG.txt')
setup()

while (waitingList != []):
    counter += 1

    student = waitingList[0]

    # remove o estudante da lista de espera
    waitingList = waitingList[1:]

    # verifica se o estudante ainda tem projetos não tentados
    if len(studentPreference[student]) == 0:
        continue

    # escolhe o primeiro projeto da lista do estudante
    project = studentPreference[student][0]

    # remove o projeto da lista de preferência dele
    studentPreference[student] = studentPreference[student][1:]

    # verifica se o projeto já atingiu o limite máximo de estudantes
    # compara a quantidade de estudantes que já estão no projeto com a quantidade de vagas disponiveis pra esse projeto
    # compara a nota do aluno com a nota mínima para entrar no projeto
    if (len(studentTaken[project]) < projectPreference[project][0] and (studentGrade[student] >= projectPreference[project][1])):
        # projeto aceita mais um estudante
        studentTaken[project].append(student)
        # estudante vai estar naquele projeto
        projectTaken[student] = project

        # printa resultado das primeiras 10 iterações
        if (counter < 10):
            print(f'O projeto {project + 1} aceitou o estudante {student + 1}')
    else:
        # se o estudante não conseguiu nenhum projeto, coloca ele de volta na lista de espera
        waitingList.append(student)

        # printa resultado das primeiras 10 iterações
        if (counter < 10):
            print(f'O projeto {project + 1} não aceitou o estudante {student + 1}')

# mostra na tela os estudantes que vão estar em cada projeto
print_answer()