a, b = map(float, input().split())

media = (a + b) / 2

if media >= 7:
    print("Aprovado")
elif media >= 4:
    print("Recuperacao")
else:
    print("Reprovado")