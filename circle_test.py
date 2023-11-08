import unittest
import circle

class CircleTestCase(unittest.TestCase):
    def test_area_wrong_type(self):
        self.assertEqual(circle.area("a"), TypeError)

    def test_per_wrong_type(self):
        self.assertEqual(circle.perimeter("d"), TypeError)

    def test_area_negative(self):
        self.assertEqual(circle.area(-111), Exception)

    def test_per_negative(self):
        self.assertEqual(circle.perimeter(-9), Exception)

    def test_area_zero(self):
        self.assertEqual(circle.area(0),0)

    def test_per_zero(self):
        self.assertEqual(circle.perimeter(0), 0)

    def test_area_int(self):
        self.assertEqual(circle.area(1), 3.141592653589793)
        self.assertEqual(circle.area(10), 314.1592653589793)

    def test_per_int(self):
        self.assertEqual(circle.perimeter(1), 6.283185307179586)
        self.assertEqual(circle.perimeter(10), 62.83185307179586)

    def test_area_float(self):
        self.assertEqual(circle.area(0.1), 0.031415926535897934)
        self.assertEqual(circle.area(3.14), 30.974846927333928)

    def test_per_float(self):
        self.assertEqual(circle.perimeter(0.1), 0.6283185307179586)
        self.assertEqual(circle.perimeter(3.14), 19.729201864543903)


if __name__ == '__main__':
    unittest.main()
