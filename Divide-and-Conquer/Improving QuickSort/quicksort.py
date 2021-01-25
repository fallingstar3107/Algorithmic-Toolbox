# python3

from random import randint


def partition3(array, left, right):
    pivot = array[right]
    begin = left - 1
    end = left - 1
    for j in range(left, right):
        if array[j] < pivot:
            begin += 1
            array[begin], array[j] = array[j], array[begin]
            end += 1
            if array[j] == pivot:
                array[end], array[j] = array[j], array[end]
        elif array[j] == pivot:
            end += 1
            array[end], array[j] = array[j], array[end]

    array[end + 1], array[right] = array[right], array[end + 1]
    return begin + 1, end + 1

def randomized_quick_sort(array, left, right):
    if left >= right:
        return
    k = randint(left, right)
    array[left], array[k] = array[k], array[left]

    small, equal = partition3(array, left, right)
    randomized_quick_sort(array, left, small - 1)
    randomized_quick_sort(array, equal + 1, right)


if __name__ == '__main__':
    input_n = int(input())
    elements = list(map(int, input().split()))
    assert len(elements) == input_n
    randomized_quick_sort(elements, 0, len(elements) - 1)
    print(*elements)
