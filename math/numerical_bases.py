def convert_from_decimal(decimal_number: int, base: int = 2):
    num: list[int] = []
    while decimal_number >= base - 1:
        num.append(decimal_number % base)
        decimal_number = decimal_number // base

    return list(reversed(num))

if __name__ == "__main__":
    num: int = int(input())
    base: int = int(input())
    print(convert_from_decimal(num, base))
