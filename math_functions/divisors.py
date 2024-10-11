from math import sqrt


# def num_div(num: int) -> list[int]:
#     divisores: list[int] = []
#     for i in range(1, num + 1):
#         if num % i == 0:
#             divisores.append(i)
#     return divisores

def num_div(num: int) -> list[int]:
    return [x for x in range(1, num + 1) if num % x == 0]

# def divisors_pairs(divisores: list[int]) -> list[tuple[int, int]]:
#     i, j = 0, len(divisores) - 1
#     pares: list[tuple[int, int]] = []
#     while i < len(divisores) / 2:
#         pares.append((divisores[i], divisores[j]))
#         i += 1
#         j -= 1
#     return pares

def divisors_pairs(num: int) -> list[tuple[int, int]]:
    divisors = [divisor for divisor in range(1, int(sqrt(num) + 1)) if num % divisor == 0]
    return [(x, int(num/x)) for x in divisors]

def pairs(divisors: list[int]) -> list[tuple[int, int]]:
    return [(x, int(num/x)) for x in divisors]

def is_divisible_by(num: int, divisors: list[int]) -> bool:
    return True if num in divisors else False


if __name__ == "__main__":
    num = int(input("Input a number: "))
    divisors = num_div(num)
    print(f"N. of divisors: {len(divisors)}\nDivisors: {divisors}\n")
    divisors_pair = pairs(divisors=divisors[:int(len(divisors)/2)])
    print(f"N. of pairs: {len(divisors_pair)}\nPairs: {divisors_pair}")