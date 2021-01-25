# python3


def max_pairwise_product_naive(numbers):
    assert len(numbers) >= 2
    assert all(0 <= x <= 2 * 10 ** 5 for x in numbers)

    product = 0

    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            product = max(product, numbers[i] * numbers[j])

    return product


def max_pairwise_product(numbers):
    assert len(numbers) >= 2
    assert all(0 <= x <= 2 * 10 ** 5 for x in numbers)

    n = len(numbers)
    max_index1 = 0
    for i in range(1, n):
        if max_index1 == 0 or numbers[i] > numbers[max_index1]:
            max_index1 = i

    if max_index1 == 0:
        max_index2 = 1
    else:
        max_index2 = 0

    for j in range(1, n):
        if j != max_index1 and numbers[j] > numbers[max_index2]:
            max_index2 = j

    return numbers[max_index1] * numbers[max_index2]

def max_pairwise_product_faster(numbers):
    assert len(numbers) >= 2
    assert all(0 <= x <= 2 * 10 ** 5 for x in numbers)

    n = len(numbers)
    max1 = 0
    max2 = 0

    for i in range(0, n):
        if numbers[i] > max1 or numbers[i] > max2:
            max1 = max(max1, max2)
            max2 = numbers[i]

    return max1 * max2


if __name__ == '__main__':
    n = int(input())
    input_numbers = list(map(int, input().split()))
    assert len(input_numbers) == n
    print(max_pairwise_product(input_numbers))
