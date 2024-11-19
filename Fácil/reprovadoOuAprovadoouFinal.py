def resultado(n1, n2): 
    mediaP = (n1 * 2 + n2 * 3) / (5)
    if mediaP >= 7:
        return "Aprovado"
    elif mediaP < 3:
        return "Reprovado"
    else:
        return "Final"

n1 = int(input())
n2 = int(input())

situacao = resultado(n1, n2)
print(situacao)
