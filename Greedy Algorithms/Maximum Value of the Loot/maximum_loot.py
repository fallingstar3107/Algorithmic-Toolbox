# python3

from sys import stdin

def maximum_loot_value(capacity, weights, prices):
    assert 0 <= capacity <= 2 * 10 ** 6
    assert len(weights) == len(prices)
    assert 1 <= len(weights) <= 10 ** 3
    assert all(0 < w <= 2 * 10 ** 6 for w in weights)
    assert all(0 <= p <= 2 * 10 ** 6 for p in prices)

    denoms = dict()
    n = len(weights)
    for i in range(n):
        denoms[prices[i]/weights[i]] = weights[i]
    denoms = dict(sorted(denoms.items(), key=lambda item: item[0]))

    value = 0
    if capacity == 0:
        return value

    while capacity > 0 and len(denoms) > 0:
        amount = min(list(denoms.values())[-1], capacity)
        value = value + amount * list(denoms.keys())[-1]
        capacity = capacity - amount
        denoms[list(denoms.keys())[-1]] -= amount
        if denoms[list(denoms.keys())[-1]] == 0:
            denoms.popitem()

    return value


if __name__ == "__main__":
    data = list(map(int, stdin.read().split()))
    n, input_capacity = data[0:2]
    input_prices = data[2:(2 * n + 2):2]
    input_weights = data[3:(2 * n + 2):2]
    opt_value = maximum_loot_value(input_capacity, input_weights, input_prices)
    print("{:.10f}".format(opt_value))
