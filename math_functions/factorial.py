def factorial_iterative(n: int) -> int:
    result = 1
    for i in range(2, n+1):
        result *= i
    return result

def factorial(n: int) -> int:
    # equivalente a
    # if n == 1 or n == 0
    if n in [0, 1]:
        return n
    return n * factorial(n - 1)

print(factorial(5))
