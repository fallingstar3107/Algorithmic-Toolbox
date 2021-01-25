# python3


def find_maximum_value(dataset):
    assert 1 <= len(dataset) <= 29

    n = (len(dataset) + 1) // 2
    if n == 1:
        return int(dataset)
    dataset = [char for char in dataset]
    digits = [dataset[i] for i in range(len(dataset)) if i % 2 == 0]
    ops = [dataset[i] for i in range(len(dataset)) if i % 2 != 0]
    min_matrix = [[0 for i in range(n)] for i in range(n)]
    max_matrix = [[0 for i in range(n)] for i in range(n)]

    for i in range(n):
        min_matrix[i][i] = int(digits[i])
        max_matrix[i][i] = int(digits[i])

    for s in range(1, n):
        for i in range(n-s):
            j = i + s

            min_matrix[i][j], max_matrix[i][j] = min_max(i, j, min_matrix, max_matrix, ops)

    return max_matrix[0][n-1]


def min_max(i, j, min_matrix, max_matrix, ops):
    min_result = 10 ** 8
    max_result = -1 * 10 ** 8
    for k in range(i, j):
        a = operation(max_matrix[i][k], max_matrix[k+1][j], ops[k])
        b = operation(max_matrix[i][k], min_matrix[k+1][j], ops[k])
        c = operation(min_matrix[i][k], max_matrix[k+1][j], ops[k])
        d = operation(min_matrix[i][k], min_matrix[k+1][j], ops[k])

        min_result = min(min_result, a, b, c, d)
        max_result = max(max_result, a, b, c, d)

    return min_result, max_result


def operation(x, y, op):
    if op == "+":
        return x + y
    elif op == "-":
        return x - y
    elif op == "*":
        return x * y
    elif op == "/":
        return x / y


if __name__ == "__main__":
    print(find_maximum_value(input()))
