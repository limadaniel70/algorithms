def find_max(arr) -> int:
    max_value = arr[0]
    max_pos = 0
    for i, item in enumerate(arr):
        if item > max_value:
            max_value = item
            max_pos = i
    return max_pos


def find_min(arr) -> int:
    min_value = arr[0]
    min_pos = 0
    for i, item in enumerate(arr):
        if item < min_value:
            min_value = item
            min_pos = i
    return min_pos


def sort_by_max(arr) -> list[int]:
    sorted_arr = []
    # while arr significa: enquanto tiver itens
    # pode ser substituido por `for i in range(len(arr))`
    # ou `while len(ar`) > 0`
    while arr:
        max_value = find_max(arr)
        sorted_arr.append(arr.pop(max_value))
    return sorted_arr


def sort_by_min(arr) -> list[int]:
    sorted_arr = []
    while arr:
        min_value = find_min(arr)
        sorted_arr.append(arr.pop(min_value))
    return sorted_arr


nums = [8, 3, 0, 5, 2, 7, 1, 9]

print(f"Lista original: {nums}")
print(f"Max: {sort_by_max(nums.copy())}")
print(f"Min: {sort_by_min(nums.copy())}")
