# fmt: off
A = [[5, 4, 3],
     [3, 2, 4]]

B = [[500, 200, 500, 150, 4],
     [400, 100, 300, 250, 5],
     [300, 150, 600, 0, 6]]
# fmt: on

# Uma matriz C = A * B deve ser igual a:
# [[5000, 1850, 5500, 1750, 58],
#  [3500, 1400, 4500, 950, 46]]


def product(a: list[list[int]], b: list[list[int]]) -> list[list[int]]:
    c = [[0 for _ in range(len(b[0]))] for _ in range(len(a))]
    aux = 0
    # (c)ij = sum((a)ik * (b)kj) for k in N 
    for i, linha in enumerate(c):
        for j, coluna in enumerate(linha):
            aux = 0
            for k in range(len(a[0])):
                aux += a[i][k] * b[k][j]
            c[i][j] = aux

    return c

print(product(A, B))
