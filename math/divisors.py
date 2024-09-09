from math import sqrt


def num_div(num: int) -> list[int]:
    divisores: list[int] = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisores.append(i)
    return divisores


def divisors_pairs(divisores: list[int]) -> list[tuple[int, int]]:
    i, j = 0, len(divisores) - 1
    pares: list[tuple[int, int]] = []
    while i < len(divisores) / 2:
        pares.append((divisores[i], divisores[j]))
        i += 1
        j -= 1
    return pares

def divisors(num: int) -> list[tuple[int, int]]:
    divisores: list[int] = []
    for i in range(1, int(sqrt(num) + 1)):
        if num % i == 0:
            divisores.append(i)
    
    return [(x, int(num / x)) for x in divisores]

def is_divisible_by(num: int, divisors: list[int]) -> bool:
    return True if num in divisors else False


if __name__ == "__main__":
    num = int(input())
    print(divisors(num))
    div = num_div(num)
    pares = divisors_pairs(div)
    print(pares)