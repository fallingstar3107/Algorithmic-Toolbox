# python3


def compute_operations_greedy(n):
    assert 1 <= n <= 10 ** 6
    num_operations = 0
    current_number = 1
    while current_number <= n:
        if current_number <= n/3:
            current_number *= 3
        elif current_number <= n/2:
            current_number *= 2
        else:
            current_number += 1
        num_operations+= 1
    return num_operations


def compute_min_operations(n):
    denoms = [3, 2]
    if n == 1:
        return 0
    min_num_operations = [n] * n
    min_num_operations[0] = 0
    for m in range(2, n + 1):
        min_num_operations[m-1] = m
        for denom in denoms:
            num_operations = min_num_operations[m//denom-1] + 1 + m % denom
            if num_operations < min_num_operations[m-1]:
                min_num_operations[m-1] = num_operations

    return min_num_operations

def compute_operations(n):
    assert 1 <= n <= 10 ** 6
    min_operations = compute_min_operations(n)
    sequence = [n]
    current_number = n
    i = current_number - 1
    while i >= 1 and current_number >= 1:
        if min_operations[i-1] < min_operations[current_number-1]\
                and i == current_number - 1:
            current_number = i
            sequence.append(current_number)

        elif min_operations[i-1] < min_operations[current_number-1]\
                and current_number % i == 0:
            current_number = i
            sequence.append(current_number)
        i -= 1

    reversed_sequence = [sequence[i] for i in range(len(sequence) - 1, -1, -1)]
    return reversed_sequence


if __name__ == '__main__':
    input_n = int(input())
    output_sequence = compute_operations(input_n)
    print(len(output_sequence) - 1)
    print(*output_sequence)
