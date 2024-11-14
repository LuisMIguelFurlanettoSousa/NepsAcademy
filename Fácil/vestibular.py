q = int(input())

respostas = input().upper()
candidato = input().upper()
Lrespostas = list(respostas)
LCandidato = list(candidato)

cont = 0
for i in range(len(Lrespostas)):
    if LCandidato[i] == Lrespostas[i]:
        cont += 1
print(cont)