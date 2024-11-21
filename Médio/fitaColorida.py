def colorir_fita(n, fita):
    # Lista para armazenar as distâncias mínimas
    distancias = [float('inf')] * n
    
    # Passo 1: Percorrer da esquerda para a direita
    ultima_posicao_0 = -1
    for i in range(n):
        if fita[i] == 0:
            ultima_posicao_0 = i
            distancias[i] = 0
        elif ultima_posicao_0 != -1:
            distancias[i] = min(distancias[i], i - ultima_posicao_0)
    
    # Passo 2: Percorrer da direita para a esquerda
    ultima_posicao_0 = -1
    for i in range(n - 1, -1, -1):
        if fita[i] == 0:
            ultima_posicao_0 = i
            distancias[i] = 0
        elif ultima_posicao_0 != -1:
            distancias[i] = min(distancias[i], ultima_posicao_0 - i)
    
    # Passo 3: Colorir a fita de acordo com as distâncias
    fita_colorida = [
        min(distancia, 9) if fita[i] == -1 else 0
        for i, distancia in enumerate(distancias)
    ]
    
    return fita_colorida

# Entrada
n = int(input())
fita = list(map(int, input().split()))

# Processar e imprimir saída
resultado = colorir_fita(n, fita)
print(" ".join(map(str, resultado)))