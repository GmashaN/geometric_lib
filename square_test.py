import unittest
import square


class SquareTestCase(unittest.TestCase):
    def test_area_wrong_type(self):
        self.assertEqual(square.area("a"), TypeError)

    def test_per_wrong_type(self):
        self.assertEqual(square.perimeter("d"), TypeError)

    def test_area_negative(self):
        self.assertEqual(square.area(-111), Exception)

    def test_per_negative(self):
        self.assertEqual(square.perimeter(-9), Exception)

    def test_area_zero(self):
        self.assertEqual(square.area(0), 0)

    def test_per_zero(self):
        self.assertEqual(square.perimeter(0), 0)

    def test_area_int(self):
        self.assertEqual(square.area(1), 1)
        self.assertEqual(square.area(10), 100)

    def test_per_int(self):
        self.assertEqual(square.perimeter(1), 4)
        self.assertEqual(square.perimeter(10), 40)

    def test_area_float(self):
        self.assertEqual(round(square.area(0.1), 2), 0.01)
        self.assertEqual(square.area(3.14), 9.8596)

    def test_per_float(self):
        self.assertEqual(square.perimeter(0.1), 0.4)
        self.assertEqual(square.perimeter(3.14), 12.56)


if __name__ == '__main__':
    unittest.main()
