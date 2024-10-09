import itertools
from typing import Iterable

letras: set[str] = ('a', 'b', 'c', 'd', 'e')
numeros: set[int] = (0, 1, 3, 4, 8, 9, 11, 14, 29)

def produto_cartesiano(iteravel1: Iterable, iteravel2: Iterable) -> set[tuple[any]]:
    result = set()
    for p in iteravel1:
        for q in iteravel2:
            result.add((p, q))
    return result

def duplas(iteravel: Iterable) -> set[tuple[any]]:
    if len(iteravel) <= 2:
        return iteravel
    
    result = set()

    for i in range(len(iteravel)):
        for j in range(i + 1, len(iteravel)):
            result.add((iteravel[i], iteravel[j]))

    return result

comb1 = set(itertools.combinations(letras, 2))
comb2 = duplas(letras)

print(f"Comb1: {comb1}\nComb2: {comb2}")

produto1 = set(itertools.product(letras, numeros))
produto2 = produto_cartesiano(letras, numeros)

print(f"Prod1: {produto1}\nProd2: {produto2}")
