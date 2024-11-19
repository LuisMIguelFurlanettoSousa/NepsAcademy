n = int(input())

p, c ,q = map(str, input().split())

p, q = int(p), int(q)

if c == "+":
    soma = p + q
    if soma > n:
        print("OVERFLOW")
    elif soma <= n:
        print("OK")
if c == "*":
    multi = p * q
    if multi > n:
        print("OVERFLOW")
    elif multi <= n:
        print("OK")
