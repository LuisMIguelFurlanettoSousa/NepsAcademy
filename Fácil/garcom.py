n = int(input())

somac = 0
for _ in range(n):
    l, c = map(int, input().split())
    if l > c:
        somac += c

print(somac)