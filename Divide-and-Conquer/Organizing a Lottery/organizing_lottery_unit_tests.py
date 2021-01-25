import unittest
from organizing_lottery import points_cover, points_cover_naive
from random import randint


class PointsAndSegments(unittest.TestCase):
    def test_small(self):
        for starts, ends, points in [
            ([0, 7], [5, 10], [1, 6, 11]),
            ([-10], [10], [-100, 100, 0]),
            ([0, -3, 7], [5, 2, 10], [1, 6])
        ]:
            self.assertEqual(points_cover(list(starts), list(ends), list(points)),
                             points_cover_naive(starts, ends, points))

    def test_random(self):
        for starts, ends, points in [
            ([randint(0, 10) for _ in range(5)],
             [randint(10, 20) for _ in range(5)],
             [randint(-10, 30) for _ in range(5)])
        ]:
            self.assertEqual(points_cover(list(starts), list(ends), list(points)),
                             points_cover_naive(starts, ends, points))


    def test_large(self):
        for starts, ends, points in [
            ([randint(0, 10 ** 4) for _ in range(5 * 10 ** 2)],
             [randint(10 ** 4, 2 * 10 ** 4) for _ in range(5 * 10 ** 2)],
             [randint(0, 2 * 10 ** 4) for _ in range(5 * 10 ** 2)])
        ]:
            self.assertEqual(points_cover(list(starts), list(ends), list(points)),
                             points_cover_naive(starts, ends, points))


if __name__ == '__main__':
    unittest.main()
