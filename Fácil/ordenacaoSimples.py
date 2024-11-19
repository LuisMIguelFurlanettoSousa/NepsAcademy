n = int(input())

lista = list(map(int, input().split()))

listaOrdenada = sorted(lista, reverse=False)

for value in listaOrdenada:
    print(value, end=" ")


# teste algoritimo
# n = int(input())

# lista = list(map(int, input().split()))

# escolhido = lista[2]
# lista_escolhido = [escolhido]
# menor_escolhido = list()
# maior_escolhido = list()

# for value in lista:
#     if value < escolhido:
#         menor_escolhido.append(value)
#     if value > escolhido:
#         maior_escolhido.append(value)

# for i in menor_escolhido: 
#     if menor_escolhido[0] > menor_escolhido[1]:
#         menor_escolhido[0], menor_escolhido[1] = menor_escolhido[1], menor_escolhido[0]

# for i in maior_escolhido:
#     if maior_escolhido[0] > maior_escolhido[1]:
#         maior_escolhido[0], maior_escolhido[1] = maior_escolhido[1], maior_escolhido[0]

# listaOrdenada = menor_escolhido + lista_escolhido + maior_escolhido
# print(listaOrdenada)