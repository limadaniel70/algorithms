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


def is_divisible_by(num: int, divisors: list[int]) -> bool:
    return true if num in divisors else false


if __name__ == "__main__":
    num = int(input())
    div = num_div(num)
    # print(div[0], div[len(div)-1])
    pares = divisors_pairs(div)
    print(
        f"""\nQuantidade de divisores: {len(div)}\nDivisores: {div}\nQuantidade de pares: {len(pares)}\nPares: {pares}"""
    )
