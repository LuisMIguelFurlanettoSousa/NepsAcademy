# Características dos Quadrantes:
# Quadrante I: x > 0, y > 0
# Quadrante II: x < 0, y > 0
# Quadrante III: x < 0, y < 0
# Quadrante IV: x > 0, y < 0

def quadrante(x, y):
    if x > 0 and y > 0:
        return "Q1"
    elif x < 0 and y > 0:
        return "Q2"
    elif x < 0 and y < 0:
        return "Q3"
    elif x > 0 and y < 0:
        return "Q4"
    else:
        return "eixos"


x = int(input())
y = int(input())

quad = quadrante(x, y)
print(quad)