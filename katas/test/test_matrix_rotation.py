import unittest
from katas.matrix_rotate import rotate_matrix


class TestRotateMatrix(unittest.TestCase):
    def test_1x1_matrix(self):
        matrix = [[1]]
        expected = [[1]]
        rotate_matrix(matrix)
        self.assertEqual(matrix, expected)

    def test_2x2_matrix(self):
        matrix = [
            [1, 2],
            [3, 4]
        ]
        expected = [
            [3, 1],
            [4, 2]
        ]
        rotate_matrix(matrix)
        self.assertEqual(matrix, expected)

    def test_3x3_matrix(self):
        matrix = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
        expected = [
            [7, 4, 1],
            [8, 5, 2],
            [9, 6, 3]
        ]
        rotate_matrix(matrix)
        self.assertEqual(matrix, expected)

    def test_4x4_matrix(self):
        matrix = [
            [1,  2,  3,  4],
            [5,  6,  7,  8],
            [9, 10, 11, 12],
            [13,14, 15, 16]
        ]
        expected = [
            [13, 9, 5, 1],
            [14,10, 6, 2],
            [15,11, 7, 3],
            [16,12, 8, 4]
        ]
        rotate_matrix(matrix)
        self.assertEqual(matrix, expected)

    def test_5x5_matrix(self):
        matrix = [
            [ 1,  2,  3,  4,  5],
            [ 6,  7,  8,  9, 10],
            [11, 12, 13, 14, 15],
            [16, 17, 18, 19, 20],
            [21, 22, 23, 24, 25]
        ]
        expected = [
            [21, 16, 11,  6, 1],
            [22, 17, 12,  7, 2],
            [23, 18, 13,  8, 3],
            [24, 19, 14,  9, 4],
            [25, 20, 15, 10, 5]
        ]
        rotate_matrix(matrix)
        self.assertEqual(matrix, expected)

if __name__ == '__main__':
    unittest.main()
