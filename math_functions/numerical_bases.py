def convert_from_decimal(num: int, base: int = 2) -> list[int]:
    digits: list[int] = []
    while num > base:
        quocient, remainder = divmod(num, base)
        digits.append(remainder)
        num = quocient
    else:
        digits.append(num)

    digits.reverse()
    return digits


def convert_to_decimal(num: list[int], base: int = 2):
    decimal_number: int = 0
    num.reverse()
    for i, digit in enumerate(num):
        decimal_number += digit * base**i
    return decimal_number


if __name__ == "__main__":
    num = 238
    digits = convert_from_decimal(num, 16)
    print(digits)
