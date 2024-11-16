# Entrada dos tempos
T1 = int(input())  
T2 = int(input())  
T3 = int(input())  

tempos = [(T1, 1), (T2, 2), (T3, 3)]

tempos_ordenados = sorted(tempos)

print(tempos_ordenados[0][1])  
print(tempos_ordenados[1][1])  
print(tempos_ordenados[2][1])  