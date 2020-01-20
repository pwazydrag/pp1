import unittest

from sum_numbers import sum_even


class TestSumEven(unittest.TestCase):
    def test_sum_even(self):
        # Testuj sumę liczb naturalnych parzystych 
        # z dowolnego przedziału m,n
        m = 1
        n = 5
        result = sum_even(m,n)
        self.assertEqual(result, 6)

    def test_sum_even_fromeven(self):
        # Testuj sumę liczb naturalnych parzystych 
        # z przedziału m,n, gdzie m parzyste
        m = 2
        n = 5
        result = sum_even(m,n)
        self.assertEqual(result, 6)

    def test_sum_even_nm(self):
        # Testuj sumę liczb naturalnych parzystych 
        # z przedziału m,n, gdzie n<m
        m = 5
        n = 2
        result = sum_even(m,n)
        self.assertEqual(result, 0)
        
    def test_sum_even_neven(self):
        m=2
        n=6
        result = sum_even(m,n)
        self.assertEqual(result, 12)
        
    def test_sum_even_frommnegative(self):
        m=-2
        n=4
        result = sum_even(m,n)
        self.assertEqual(result, 6)

    def test_sum_even_floats(self):
        self.assertRaises(TypeError, sum_even, 2.1, 1.2)
    
    def test_sum_even_strings(self):
        self.assertRaises(TypeError, sum_even, "j", "d")


if __name__ == '__main__':
    unittest.main()