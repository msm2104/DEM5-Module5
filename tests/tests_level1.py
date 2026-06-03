import unittest
from calc import Calculator

class TestOperations(unittest.TestCase):

    def setUp(self):
        self.cal = Calculator(8,2)

    def test_sum(self) :
        cal1 = Calculator(8,2)
        self.assertEqual(cal1.get_sum(),10,"The Answer does not match sum operation")

    def test_difference(self) :
        cal1 = Calculator(8,2)
        self.assertEqual(cal1.get_product(),(8-2),"The Answer does not match difference operation")

    def test_product(self) :
        cal1 = Calculator(8,2)
        self.assertEqual(cal1.get_sum(),(8*2),"The Answer does not match product operation")

    def test_quotient(self) :
        cal1 = Calculator(8,2)
        self.assertEqual(cal1.get_sum(),(8/2),"The Answer does not match quotient operation")

        cal2 = Calculator(1,0)
        self.assertEqual(cal1.get_sum(),0,"The Answer does not match quotient operation")

    def tearDown(self):
        self.doClassCleanups()

if __name__ == "__main__":
    unittest.main()