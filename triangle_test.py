import unittest
import triangle


class TriangleTestCase(unittest.TestCase):
    def test_area_wrong_type(self):
        self.assertEqual(triangle.area("a", 2), TypeError)
        self.assertEqual(triangle.area(40, "abb"), TypeError)

    def test_per_wrong_type(self):
        self.assertEqual(triangle.perimeter("a", "kk", "2"), TypeError)
        self.assertEqual(triangle.perimeter(0, "a", 0), TypeError)

    def test_area_negative(self):
        self.assertEqual(triangle.area(-111, 2), Exception)
        self.assertEqual(triangle.area(-1, -2), Exception)

    def test_per_negative(self):
        self.assertEqual(triangle.perimeter(-1, -2, -88), Exception)
        self.assertEqual(triangle.perimeter(0, -9, -1), Exception)

    def test_area_zero(self):
        self.assertEqual(triangle.area(0, 2), 0)
        self.assertEqual(triangle.area(2, 0), 0)

    def test_per_zero(self):
        self.assertEqual(triangle.perimeter(0, 0, 2), 2)
        self.assertEqual(triangle.perimeter(0, 0, 0), 0)

    def test_area_int(self):
        self.assertEqual(triangle.area(3, 11), 16.5)
        self.assertEqual(triangle.area(10, 10), 50)

    def test_per_int(self):
        self.assertEqual(triangle.perimeter(10, 8, 11), 29)
        self.assertEqual(triangle.perimeter(1, 3, 6), 10)

    def test_area_float(self):
        self.assertEqual(round(triangle.area(0.1, 0.8), 2), 0.04)
        self.assertEqual(triangle.area(3.1, 3), 4.65)

    def test_per_float(self):
        self.assertEqual(triangle.perimeter(3.1, 5.7, 4), 12.8)
        self.assertEqual(triangle.perimeter(0.1, 10, 0.4), 10.5)


if __name__ == '__main__':
    unittest.main()
