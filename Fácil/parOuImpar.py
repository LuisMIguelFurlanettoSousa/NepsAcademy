bino = int(input())
cino = int(input())

if bino <= 10 and cino <= 10:
    somaDedos = bino + cino
    if somaDedos % 2 != 0:
        print("Cino")
    elif somaDedos % 2 == 0:
        print("Bino")
else:
    exit()