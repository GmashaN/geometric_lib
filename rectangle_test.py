import unittest
import rectangle


class RectangleTestCase(unittest.TestCase):
    def test_area_wrong_type(self):
        self.assertEqual(rectangle.area("a", 8), TypeError)
        self.assertEqual(rectangle.area(40, "abb"), TypeError)

    def test_per_wrong_type(self):
        self.assertEqual(rectangle.perimeter("d", 1), TypeError)
        self.assertEqual(rectangle.perimeter("a", "2"), TypeError)

    def test_area_negative(self):
        self.assertEqual(rectangle.area(-111, 1), Exception)
        self.assertEqual(rectangle.area(-1, -2), Exception)

    def test_per_negative(self):
        self.assertEqual(rectangle.perimeter(-9, 9), Exception)
        self.assertEqual(rectangle.perimeter(-1, -4), Exception)

    def test_area_zero(self):
        self.assertEqual(rectangle.area(10, 0), 0)
        self.assertEqual(rectangle.area(0, 10), 0)
        self.assertEqual(rectangle.area(0, 0), 0)

    def test_per_zero(self):
        self.assertEqual(rectangle.perimeter(10, 0), 20)
        self.assertEqual(rectangle.perimeter(0, 10), 20)
        self.assertEqual(rectangle.perimeter(0, 0), 0)

    def test_area_int(self):
        self.assertEqual(rectangle.area(10, 1), 10)

    def test_per_int(self):
        self.assertEqual(rectangle.perimeter(10, 5), 30)

    def test_area_float(self):
        self.assertEqual(rectangle.area(10, 0.1), 1)
        self.assertEqual(rectangle.area(5, 0.01), 0.05)

    def test_per_float(self):
        self.assertEqual(rectangle.perimeter(10, 0.1), 20.2)
        self.assertEqual(rectangle.perimeter(5, 0.01), 10.02)


if __name__ == '__main__':
    unittest.main()
