# python3

from itertools import product
from sys import stdin


def partition3(values):
    assert 1 <= len(values) <= 20
    assert all(1 <= v <= 30 for v in values)

    values = list(values)
    sub_sum = sum(values)/3
    #try
    if sub_sum % 1 != 0:
        return 0
    first_sum, first_partition_elements = \
        find_elements(int(sub_sum), values)
    if first_sum != int(sub_sum):
        return 0
    first_partition_elements = list(first_partition_elements)
    values = [values[i] for i in range(len(values)) if i not in first_partition_elements]

    second_sum, second_partition_elements = \
        find_elements(int(sub_sum), values)
    if second_sum != int(sub_sum):
        return 0

    return 1

    #except TypeError: # sub_sum is a float
    #    return 0


def find_elements(partial_sum, integers):
    n = len(integers)
    value = [[0 for w in range(partial_sum+1)] for i in range(n+1)]
    chosen_elements = []
    for i in range(1, n + 1):
        for p in range(1, partial_sum + 1):
            value[i][p] = value[i-1][p]
            if integers[i-1] <= p:
                val = value[i-1][p - integers[i-1]] + integers[i-1]
                if value[i][p] < val:
                    value[i][p] = val
    p = partial_sum
    result = value[n][p]
    for i in range(n, 0, -1):
        if result <= 0:
            break
        if result == value[i-1][p]:
            continue
        else:
            chosen_elements.append(integers[i-1])
            result -= integers[i-1]
            p -= integers[i-1]

    return value[n][partial_sum], chosen_elements






if __name__ == '__main__':
    input_n, *input_values = list(map(int, stdin.read().split()))
    assert input_n == len(input_values)
    print(partition3(input_values))
