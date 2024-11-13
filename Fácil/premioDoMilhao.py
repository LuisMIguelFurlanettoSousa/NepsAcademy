N = int(input())
acessos_diarios = [int(input()) for _ in range(N)]

somaAcessos = 0
dias = 0

for acesso in acessos_diarios:
    somaAcessos += acesso
    dias += 1
    if somaAcessos >= 1000000:
        break

print(dias)