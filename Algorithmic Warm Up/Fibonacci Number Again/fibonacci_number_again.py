# python3


def fibonacci_number_again_naive(n, m):
    assert 0 <= n <= 10 ** 18 and 2 <= m <= 10 ** 3

    if n <= 1:
        return n

    previous, current = 0, 1
    for _ in range(n - 1):
        previous, current = current, (previous + current) % m

    return current


def pisano_period(m):
    P = [0, 1]
    for i in range(m * m):
        P.append((P[i] + P[i+1]) % m)
        # A Pisano Period starts with 01
        if (P[i+1] == 0 and P[i+2] == 1):
            del P[i+1]
            del P[i+1]
            return i + 1, P


def fibonacci_number_again(n, m):
    assert 0 <= n <= 10 ** 18 and 2 <= m <= 10 ** 3

    pperiod, p_list = pisano_period(m)
    index = n % pperiod
    return p_list[index]


if __name__ == '__main__':
    input_n, input_m = map(int, input().split())
    print(fibonacci_number_again(input_n, input_m))
