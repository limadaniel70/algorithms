def factorial(n: int) -> int:
    if n == 1:
        return n
    return n * factorial(n - 1)

print(factorial(5))
