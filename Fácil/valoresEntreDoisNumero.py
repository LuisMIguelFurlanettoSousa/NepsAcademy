a = int(input())
b = int(input())

if a > b:
    a, b = b, a
for i in range(a, b + 1):
    print(i, end=' ')