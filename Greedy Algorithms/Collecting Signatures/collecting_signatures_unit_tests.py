import unittest
from collecting_signatures import compute_optimal_points, Segment


class CollectingSignatures(unittest.TestCase):
    def test(self):
        for (segments, answer) in [
            ([Segment(1, 3), Segment(2, 5), Segment(3, 6)], 1),
            ([Segment(4, 7), Segment(1, 3), Segment(2, 5), Segment(5, 6)], 2),
            ([Segment(2, 6), Segment(5, 7), Segment(5, 10), Segment(4, 10),
              Segment(8, 11), Segment(9, 13), Segment(13, 15), Segment(8, 17),
              Segment(2, 18), Segment(17, 20), Segment(9, 21), Segment(21, 23),], 5)

        ]:
            self.assertEqual(len(compute_optimal_points(segments)), answer)


if __name__ == '__main__':
    unittest.main()
