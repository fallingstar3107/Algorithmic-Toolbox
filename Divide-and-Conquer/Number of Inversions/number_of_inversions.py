# python3

from itertools import combinations


def compute_inversions_naive(a):
    number_of_inversions = 0
    for i, j in combinations(range(len(a)), 2):
        if a[i] > a[j]:
            number_of_inversions += 1
    return number_of_inversions


def compute_inversions(a):
    left = 0
    right = len(a) - 1
    inversions = merge_sort(a, left, right)
    return inversions


def merge_sort(a, left, right):
    if left >= right:
        return 0
    mid_index = (left + right) // 2
    left_half_inversions = merge_sort(a, left, mid_index)
    right_half_inversions = merge_sort(a, mid_index + 1, right)

    return merge(a, left, mid_index, right) + left_half_inversions \
                                            + right_half_inversions


def merge(a, left, mid_index, right):
    n_1 = mid_index - left + 1
    n_2 = right - mid_index

    left_half = [x for x in a[left:mid_index + 1]]
    right_half = [x for x in a[mid_index + 1: right + 1]]

    i = 0
    j = 0
    inversions = 0
    for k in range(left, right + 1):
        if i < n_1 and j < n_2:
            if left_half[i] <= right_half[j]:
                a[k] = left_half[i]
                i += 1
            else:
                a[k] = right_half[j]
                j += 1
                inversions += n_1 - i
        elif i < n_1:
            a[k] = left_half[i]
            i += 1
        else:
            a[k] = right_half[j]
            j += 1
    return inversions


if __name__ == '__main__':
    input_n = int(input())
    elements = list(map(int, input().split()))
    assert len(elements) == input_n
    print(compute_inversions(elements))
