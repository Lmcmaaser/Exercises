import unittest
import math
#tax bracket function
# takes income and based on income and bracket, returns tax amount owed
# round to whole num


# income cap      marginal tax rate
#   ¤10,000           0.00 (0%)
#   ¤30,000           0.10 (10%)
#  ¤100,000           0.25 (25%)
#     --              0.40 (40%)

# test cases:
    # tax(0) => 0
    # tax(10000) => 0
    # tax(10009) => 0
    # tax(10010) => 1
    # tax(12000) => 200
    # tax(56789) => 8697

    # tax(1234567) => 473326

def taxCalc(income):
    brkt1 = (income - 0) * 0.0
    brkt2 = (income - 10000) * 0.10
    brkt3 = (20000 * 0.10) + ((income - 30000) * 0.25)
    brktmax = (20000 * 0.10) + (70000 * 0.25) + ((income - 100000) * 0.40)

    if income <= 10000: # $0 - $10,000
        return round(brkt1)
    elif income <= 30000: # $10,000 - $30,000
        return math.floor(brkt2)
    elif income <= 100000: # $30,000 - $100,000
        return math.floor(brkt3)
    elif income > 100000: # $100,000 and beyond
        return math.floor(brktmax)
print(taxCalc(1234567))

class MyTest(unittest.TestCase):
    def test(self):
        self.assertEqual(taxCalc(0), 0)
        self.assertEqual(taxCalc(10000), 0)
        self.assertEqual(taxCalc(10009), 0)
        self.assertEqual(taxCalc(10010), 1)
        self.assertEqual(taxCalc(12000), 200)
        self.assertEqual(taxCalc(56789), 8697)
        self.assertEqual(taxCalc(1234567), 473326)

if __name__ == '__main__':
    unittest.main()
