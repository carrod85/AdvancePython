import unittest
from triangle_carrod import area_triangle as at


class TestTriangle(unittest.TestCase):
    def test_triangle(self):
        self.assertEqual(at.calculate_area(0, 1), 0 * 1 / 2)
        self.assertEqual(at.calculate_area(3, 2.1), 3 * 2.1 / 2)


if __name__ == '__main__':
    unittest.main()
