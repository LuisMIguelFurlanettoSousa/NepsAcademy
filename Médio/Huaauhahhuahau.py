def risada_engracada(risada):
    # Filtra apenas as vogais da risada
    vogais = [char for char in risada if char in 'aeiou']
    
    # Verifica se as vogais formam um palíndromo
    if vogais == vogais[::-1]:
        return "S"  # É uma risada engraçada
    else:
        return "N"  # Não é uma risada engraçada

# Entrada
risada = input().strip()

# Saída
print(risada_engracada(risada))