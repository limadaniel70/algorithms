def binary_search(iterable: list | tuple | dict, item) -> int | None:
    start = 0
    end = len(iterable) - 1

    while start <= end:
        mid = int((start + end) / 2)
        guess = iterable[mid]
        if guess == item:
            return mid
        # Chute foi maior que o valor do item
        if guess > item:
            end = mid - 1
        # Chute menor que o valor do item
        else:
            start = mid + 1

    return None


nums = list(range(0, 10000, 9))
print(binary_search(nums, 3105))
