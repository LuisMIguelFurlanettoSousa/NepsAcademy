dici = {
    0: 1,
    1: 1
}

def fib(num):
    if num in dici:
        return dici[num]
    dici[num] = fib(num - 1) + fib(num - 2)
    return dici[num]


n = int(input())

result = fib(n)
print(dici)
print(result)

# from functools import lru_cache

# @lru_cache(maxsize=None)
# def fib(num):
#     if num == 0:
#         return 1
#     if num == 1:
#         return 1
#     else:
#         return fib(num - 1) + fib(num - 2)
    
# n = int(input())

# result = fib(n)
# print(result)
