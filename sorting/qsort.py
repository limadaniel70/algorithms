def qsort(arr: list[int]) -> list[int]:
    if len(arr) < 2:
        return arr
    else:
        pivo = arr[0]
        menores = [i for i in arr[1:] if i <= pivo]
        maiores = [i for i in arr[1:] if i > pivo]
        return qsort(menores) + [pivo] + qsort(maiores)