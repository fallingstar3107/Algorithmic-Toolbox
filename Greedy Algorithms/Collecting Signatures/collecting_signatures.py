# python3

from collections import namedtuple
from sys import stdin

Segment = namedtuple('Segment', 'start end')


def compute_optimal_points(segments):
    right_sort = sorted(segments, key=lambda x: x[1])

    points = []
    while len(right_sort) > 0:
        added_point = right_sort[0][1]
        points.append(added_point)
        right_sort = list(filter(lambda x: x[0] > added_point, right_sort))
    return points


if __name__ == '__main__':
    n, *data = map(int, stdin.read().split())
    input_segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    assert n == len(input_segments)
    output_points = compute_optimal_points(input_segments)
    print(len(output_points))
    print(*output_points)
