# python3

def edit_distance(first_string, second_string):
    m = len(first_string)
    n = len(second_string)
    E = [[0 for j in range(n + 1)] for i in range(m + 1)]
    for i in range(m + 1):
        E[i][0] = i
    for j in range(n + 1):
        E[0][j] = j
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            diff = 1
            if first_string[i-1] == second_string[j-1]:
               diff = 0
            E[i][j] = min(E[i-1][j] + 1, E[i][j-1] + 1, E[i-1][j-1] + diff)

    return E[m][n]


if __name__ == "__main__":
    print(edit_distance(input(), input()))
