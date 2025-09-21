'''
Primeira Avaliação

'''

N, T = map(int, input().split())

alunos = []
for _ in range(N):
    nome, habilidade = input().split()
    alunos.append((nome, int(habilidade)))

alunos.sort(key=lambda x: x[1], reverse=True)

times = [[] for _ in range(T)]
indice_time = 0

for aluno in alunos:
    times[indice_time].append(aluno[0])
    indice_time = (indice_time + 1) % T

for i, time in enumerate(times):
    print(f"Time {i + 1}")
    time.sort()
    for jogador in time:
        print(jogador)
    print()