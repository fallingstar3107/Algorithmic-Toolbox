# python3


def lcs2(first_sequence, second_sequence):
    assert len(first_sequence) <= 100
    assert len(second_sequence) <= 100
    first_sequence = list(first_sequence)
    second_sequence = list(second_sequence)
    m = len(first_sequence)
    n = len(second_sequence)

    E = [[0 for j in range(n + 1)] for i in range(m + 1)]
    common_1 = []
    common_2 = []
    for i in range(m + 1):
        E[i][0] = i
    for j in range(n + 1):
        E[0][j] = j
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            diff = 1
            if first_sequence[i-1] == second_sequence[j-1]:
                diff = 0
                common_1.append(i-1)
                common_2.append(j-1)

            E[i][j] = min(E[i-1][j] + 1, E[i][j-1] + 1, E[i-1][j-1] + diff)

    if len(common_2) == 0:
        return 0

    length = len(common_2)

    T = [0] * length
    prev = [0] * length
    for x in range(length):
        T[x] = 1
        prev[x] = -1
        for y in range(x):
            if common_2[y] < common_2[x] and T[x] < T[y] + 1:
                T[x] = T[y] + 1
                prev[x] = y

    last = 0
    for k in range(1, length):
        if T[k] > T[last]:
            last = k
    lis = []
    current = last
    while current >= 0:
        lis.append(current)
        current = prev[current]
    lis.reverse()

    return len([common_2[l] for l in lis])

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    assert len(a) == n

    m = int(input())
    b = list(map(int, input().split()))
    assert len(b) == m

    print(lcs2(a, b))
