# python3
from sys import stdin
from bisect import bisect_left, bisect_right

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


def points_cover_naive(starts, ends, points):
    assert len(starts) == len(ends)
    count = [0] * len(points)

    for index, point in enumerate(points):
        for start, end in zip(starts, ends):
            if start <= point <= end:
                count[index] += 1

    return count


def points_cover(starts, ends, points):
    assert len(starts) == len(ends)
    n = len(starts)
    m = len(points)
    original_points = list(points)
    randomized_quick_sort(starts, 0, n - 1)
    randomized_quick_sort(ends, 0, n - 1)
    randomized_quick_sort(points, 0, m - 1)

    s = 0
    e = 0
    p = 0
    combination = []
    sorted_covers = dict()
    while p < m:
        if s < n and e < n:
            if starts[s] == min(starts[s], ends[e], points[p]):
                combination.append(starts[s])
                s += 1

            elif points[p] == min(starts[s], ends[e], points[p]):
                combination.append(points[p])
                sorted_covers[points[p]] = s - e
                p += 1

            else:
                combination.append(ends[e])
                e += 1

        elif e < n:
            if points[p] <= ends[e]:
                combination.append(points[p])
                sorted_covers[points[p]] = s - e
                p += 1

            else:
                combination.append(ends[e])
                e += 1

        else:
            combination.append(points[p])
            sorted_covers[points[p]] = s - e
            p += 1

    covers = []
    for point in original_points:
        covers.append(sorted_covers[point])

    return covers


if __name__ == '__main__':
    data = list(map(int, stdin.read().split()))
    n, m = data[0], data[1]
    input_starts, input_ends = data[2:2 * n + 2:2], data[3:2 * n + 2:2]
    input_points = data[2 * n + 2:]

    output_count = points_cover(input_starts, input_ends, input_points)
    print(*output_count)
