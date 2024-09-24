from numerical_bases import convert_to_decimal

hex_num = [
    [5, 4],
    [6, 8],
    [6, 5],
    [2, 0],
    [5, 0],
    [7, 2],
    [6, 9],
    [6, 3],
    [6, 5],
    [2, 0],
    [4, 15],
    [6, 6],
    [2, 0],
    [4, 5],
    [7, 8],
    [6, 3],
    [6, 5],
    [6, 12],
    [6, 12],
    [6, 5],
    [6, 14],
    [6, 3],
    [6, 5],
    [2, 0],
    [4, 9],
    [7, 3],
    [2, 0],
    [4, 4],
    [6, 9],
    [7, 3],
    [6, 3],
    [6, 9],
    [7, 0],
    [6, 12],
    [6, 9],
    [6, 14],
    [6, 5],
]

decimal_numbers = [0 for _ in range(len(hex_num))]

for i, num in enumerate(hex_num):
    decimal_numbers[i] = convert_to_decimal(num, 16)

text = ""
for i, num in enumerate(decimal_numbers):
    text += chr(decimal_numbers[i])

print(text)
