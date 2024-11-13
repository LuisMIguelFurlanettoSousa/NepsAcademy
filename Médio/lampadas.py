N = int(input())

sequencia = list(map(int, input().split()))

A = 0
B = 0

for interruptor in sequencia:
    if interruptor == 1:
        A = 1 - A  
    elif interruptor == 2:
        A = 1 - A  
        B = 1 - B  

print(A)
print(B)