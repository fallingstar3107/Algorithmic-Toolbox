# python3

from sys import stdin


def maximum_gold(capacity, weights):
    assert 1 <= capacity <= 10 ** 4
    assert 1 <= len(weights) <= 10 ** 3
    assert all(1 <= w <= 10 ** 5 for w in weights)

    n = len(weights)
    value = [[0 for w in range(capacity+1)] for i in range(n+1)]

    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            value[i][w] = value[i-1][w]
            if weights[i-1] <= w:
                val = value[i-1][w - weights[i-1]] + weights[i-1]
                if value[i][w] < val:
                    value[i][w] = val

    return value[n][capacity]


if __name__ == '__main__':
    input_capacity, n, *input_weights = list(map(int, stdin.read().split()))
    assert len(input_weights) == n

    print(maximum_gold(input_capacity, input_weights))
