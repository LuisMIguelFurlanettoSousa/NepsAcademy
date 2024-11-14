from math import sqrt

n = int(input())

numeros = list(map(float, input().split()))

for n in numeros:
    print(f"{n ** 0.5:.4f}")