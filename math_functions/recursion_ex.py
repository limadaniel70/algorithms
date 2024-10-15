######################################################
def isum(nums: list[int]) -> int:
    total = 0
    for num in nums:
        total += num
    return total


def rsum(nums: list[int]) -> int:
    # caso base
    if not nums:
        return 0
    elif len(nums) == 1:
        return nums[0]
    # caso recursivo
    return nums[0] + rsum(nums[1:])


n = [207, 281, 182, 287, 314, 95, 309, 355, 128, 136]
print(f"Soma iterativa: {isum(n)}")
print(f"Soma recursiva: {rsum(n)}")


######################################################
def ilen(l: list[any]) -> int:
    n_of_items = 0
    for item in l:
        n_of_items += 1
    return n_of_items


def rlen(l: list[any]) -> int:
    # caso base
    if l == []:
        return 0
    # caso recursivo
    return 1 + rlen(l[1:])


l1 = [0, 1, 3, 4, 5, 6, 7, 8]
print(f"Contagem iterativa: {ilen(n)}")

print(f"Contagem recursiva: {rlen(n)}")


######################################################
def get_max(num1, num2) -> int:
    return num1 if num1 > num2 else num2


def imax(l: list[int]) -> int:
    reference = l[0]
    for numero in l:
        if numero > reference:
            reference = numero
    return reference


def rmax(nums, n) -> int:
    if n == 1:
        return nums[0]
    return get_max(nums[n - 1], rmax(nums, n - 1))


l2 = [-8, -2, -3, 1, 12, 5, 18, 89]
print(f"Max: {rmax(l2, len(l2))}")


######################################################
def ibinary_search(arr: list[int], item: int) -> bool:
    start, end = 0, len(arr) - 1
    while start <= end:
        mid = (start + end) // 2
        guess = arr[mid]
        if guess == item:
            return True
        # Chute foi maior que o valor do item
        if guess > item:
            end = mid - 1
        # Chute menor que o valor do item
        else:
            start = mid + 1
    return False


def rbinary_search(arr: list[int], item) -> bool:
    # caso base
    if not arr:
        return False
    elif len(arr) == 1:
        return True if arr[0] == item else False
    # caso recursivo
    mid = len(arr) // 2
    if arr[mid] == item:
        return True
    elif arr[mid] > item:
        return rbinary_search(arr[:mid], item)
    else:
        return rbinary_search(arr[mid + 1 :], item)
