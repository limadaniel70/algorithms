# Esse arquivo consiste na resolução desses exercícios:
#
#   1. Um programa que soma todos os itens de uma lista.
#
#   2. Um programa que encontra o maior item dentro de uma lista de números.
#
#   3. Um programa que checa se uma lista está vazia.
#
#   4. Um programa que verificia se todos os números de uma lista são pares.

# fmt: off
reference_list = [-72, 33, 60, -17, 32, -49, 53, 34, -68, 50, -99, 40,
                -94, 52, 31, -100, 50, -21, 46, -22, 72, 27, 16, -83,
                11, -91, 21, 78, 75, 29, 68, 31, -25, 43, 68, 63, -19,
                -68, 60, -6, -10, 51, 95, 77, -61, -23, 47, -35, -89,
                -32, -73, 80, 56, -57, -27, -56, 8, 54, 5, 98, -23, 75,
                -28, 23, -14, 16, -59, 18, 70, 50, 3, -82, -25, -2, -41,
                54, 23, -49, -85, -46, 52, 44, 10, 34, -98, -96, -35, -87,
                37, -87, 22, -47, -87, 98, -21, -87, 15, -69, -11, 21]
# fmt: on

#####################################
# exercício 1: O(n)
total = 0
for numero in reference_list:
    total += numero
print(total)
#####################################
# exercício 2: O(n)
reference = reference_list[0]
for numero in reference_list:
    if numero > reference:
        reference = numero
print(reference)
#####################################
# execício 3-1: O(1)
if len(reference_list) == 0:
    print("Vazia")
else:
    print("Possui itens")
#####################################
# exercício 3-2: O(1)
if not reference_list:
    print("Vazia")
else:
    print("Possui itens")
#####################################
# exercício 4: O(n)
par: bool = True
for numero in reference_list:
    if numero % 2 == 0:
        continue
    else:
        par = False
        break
print(f"Par: {par}")
#####################################
