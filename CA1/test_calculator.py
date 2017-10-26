import unittest

from calculator import Calculator 

# test the calculator functionality
class TestCalculator(unittest.TestCase):
 
    def setUp(self):
        self.calc = Calculator()
 
# this tests the add functionality
# 2 + 2 = 4
# 2 + 4 = 6
# 2 + (-2) = 0
    def test_calculator_add_method_returns_correct_result(self):
        result = self.calc.add(2, 2)
        self.assertEqual(4, result)
        result = self.calc.add(2,4)
        self.assertEqual(6, result)
        result = self.calc.add(2, -2)
        self.assertEqual(0, result)
 
    def test_calculator_subtract_method_returns_correct_result(self):
        result = self.calc.subtract(2, 2)
        self.assertEqual(0, result)
        result = self.calc.subtract(2,4)
        self.assertEqual(-2, result)
        result = self.calc.subtract(2, -4)
        self.assertEqual(6, result)
        
    def test_calculator_multi_method_returns_correct_result(self):
        result = self.calc.multi(2,5)
        self.assertEqual(10, result)
        result = self.calc.multi(3,7)
        self.assertEqual(21, result)
        result = self.calc.multi(8,5)
        self.assertEqual(40, result)

    def test_calculator_div_method_returns_correct_result(self):
        result = self.calc.div(5,5)
        self.assertEqual(1, result)
        result = self.calc.div(30,6)
        self.assertEqual(5, result)
        result = self.calc.div(80,10)
        self.assertEqual(8, result)

    def test_calculator_expo_method_returns_correct_result(self):
        result = self.calc.expo(3,3)
        self.assertEqual(27, result)
        result = self.calc.expo(5,4)
        self.assertEqual(625, result)
        result = self.calc.expo(15,6)
        self.assertEqual(11390625, result)        

    def test_calculator_sqr_method_returns_correct_result(self):
        result = self.calc.sqr(10)
        self.assertEqual(100, result)
        result = self.calc.sqr(6)
        self.assertEqual(36, result)
        result = self.calc.sqr(9)
        self.assertEqual(81, result)        

    def test_calculator_cbe_method_returns_correct_result(self):
        result = self.calc.cbe(10)
        self.assertEqual(1000, result)
        result = self.calc.cbe(6)
        self.assertEqual(216, result)
        result = self.calc.cbe(9)
        self.assertEqual(729, result)

    def test_calculator_tan_method_returns_correct_result(self):
        result = self.calc.tan(3)
        self.assertAlmostEqual(-0.142546543074, result)
        result = self.calc.tan(52)
        self.assertAlmostEqual(-6.05327238279, result)
        result = self.calc.tan(31)
        self.assertAlmostEqual(-0.441695568021, result)        

    def test_calculator_sin_method_returns_correct_result(self):
        result = self.calc.sin(68)
        self.assertAlmostEqual(-0.897927680689, result)
        result = self.calc.sin(12)
        self.assertAlmostEqual(-0.536572918, result)
        result = self.calc.sin(23)
        self.assertAlmostEqual(-0.846220404175, result)        
               
    def test_calculator_cos_calc_method_returns_correct_result(self):
        result = self.calc.cos_calc(25)
        self.assertAlmostEqual(0.991202811863, result)
        result = self.calc.cos_calc(45)
        self.assertAlmostEqual(0.525321988818, result)
        result = self.calc.cos_calc(7)
        self.assertAlmostEqual(0.753902254343, result)        


    
if __name__ == '__main__':
    unittest.main()