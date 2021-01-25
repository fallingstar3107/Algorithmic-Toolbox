# python3

from itertools import permutations


def largest_number_naive(numbers):
    numbers = list(map(str, numbers))

    largest = 0

    for permutation in permutations(numbers):
        largest = max(largest, int("".join(permutation)))

    return largest


def largest_number(numbers):
    numbers = sorted(numbers)
    salary = ""

    while numbers:
        max_number = numbers[-1]
        max_index = -1
        for i in range(len(numbers) - 1):
            if is_better(numbers[i], max_number):
                max_number = numbers[i]
                max_index = i
        salary += str(max_number)
        del numbers[max_index]

    return int(salary)

def is_better(a, b):
    ab = str(a) + str(b)
    ba = str(b) + str(a)
    if int(ab) > int(ba):
        return True
    return False


if __name__ == '__main__':
    n = int(input())
    input_numbers = input().split()
    assert len(input_numbers) == n
    print(largest_number(input_numbers))
