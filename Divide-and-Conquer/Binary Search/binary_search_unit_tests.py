import unittest
from binary_search import binary_search, linear_search


class TestBinarySearch(unittest.TestCase):
    def test_small(self):
        for (keys, query) in [
            ([1, 2, 3], 1),
            ([4, 5, 6], 7),
            ([1, 3, 5, 7, 9, 13, 18], 13)
        ]:
            self.assertEqual(
                linear_search(keys, query),
                binary_search(keys, query)
            )

    def test_large(self):
        for (keys, query, answer) in [
            (list(range(10 ** 4)), 10 ** 4, -1),
            (list(range(10 ** 4)), 10 ** 3, 10 ** 3),
            (list(range(10 ** 4)), 239, 239),
        ]:
            self.assertEqual(binary_search(keys, query), answer)


if __name__ == '__main__':
    unittest.main()
