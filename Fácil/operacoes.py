tipo = input().upper()
n1, n2 = map(float, input().split())

if tipo == "M":
    resultado = n1 * n2
elif tipo == "D":
    resultado = n1 / n2

print(f"{resultado:.2f}")