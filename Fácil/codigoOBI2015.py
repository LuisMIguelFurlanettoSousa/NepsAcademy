n = int(input())

lista = list(input().split())
stringUnica = ''.join(lista)

ocorrencias = stringUnica.count("100")
print(ocorrencias)