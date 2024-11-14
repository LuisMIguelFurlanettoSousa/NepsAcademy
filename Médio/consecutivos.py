n = int(input())

listaV = list(map(int, input().split()))

maior_sequecia = 1
sequencia_atual = 1 

for i in range(1, n):
    if listaV[i] == listaV[i - 1]:
        sequencia_atual += 1
    else:
        maior_sequecia = max(sequencia_atual, maior_sequecia)
        sequencia_atual = 1

maior_sequecia = max(sequencia_atual, maior_sequecia)
print(maior_sequecia)