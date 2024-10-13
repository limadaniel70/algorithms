from typing import Generator

# fibo seq
# 0, 1, 1, 2, 3, 5, 8, 13, ...


def fibo_generator(n: int) -> Generator[int, None, None]:
    a = 0
    b = 1
    aux = 0
    for i in range(n + 1):
        yield a
        aux = a
        a += b
        b = aux


def ifibo(n: int) -> int:
    a = 0
    b = 1
    aux = 0
    for i in range(n):
        aux = a
        a += b
        b = aux
    return a


def rfibo(n: int) -> int:
    if n <= 1:
        return n
    return rfibo(n - 1) + rfibo(n - 2)


print(rfibo(10))
print(ifibo(10))
print(list(fibo_generator(10)))
