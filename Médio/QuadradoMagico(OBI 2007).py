def is_magic_square(matrix, n):
    # Soma da primeira linha como referência
    target_sum = sum(matrix[0])
    
    # Verifica se todas as linhas têm a mesma soma
    for row in matrix:
        if sum(row) != target_sum:
            return -1
    
    # Verifica se todas as colunas têm a mesma soma
    for col in range(n):
        for row in range(n):
            if sum(matrix[row][col]) != target_sum:
                return -1
    
    # Verifica a soma das diagonais
    if sum(matrix[i][i] for i in range(n)) != target_sum:
        return -1
    if sum(matrix[i][n - i - 1] for i in range(n)) != target_sum:
        return -1
    
    # Se passou por todas as verificações
    return target_sum

# Leitura da entrada
n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]

# Determina se é um quadrado mágico
result = is_magic_square(matrix, n)

# Exibe o resultado
print(result)
