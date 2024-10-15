from itertools import combinations

# The n of subsets is equal to:
# C(N, 0) + C(N, 1) + C(N, 2) + ... + C(N, N)

def get_n_of_subsets(items: list | set) -> tuple[list[any], int]:
    subsets = []
    for i in range(len(items)):
        subsets.append(list(combinations(items, i)))
    return (subsets, len(subsets))
 