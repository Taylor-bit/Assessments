import unittest
from optimal_change import ChangeMaker



class ChangeMakerTestCases(unittest.TestCase):
    
    def test_simple_change_maker(self):
        """simple test case to check if optimal change is found"""
        change_maker = ChangeMaker(62.13, 100)
        change_maker.optimal_change()
        return "The optimal change for an item that costs $62.13 with an amount paid of $100 is 1 $20 bill, 1 $10 bill, 1 $5 bill, 2 $1 bills, 3 quarters, 1 dime, and 2 pennies."

    def test_change_maker(self):
        """simple test case to check if optimal change is found when paying with a $50"""
        change_maker2 = ChangeMaker(31.51, 50)
        change_maker2.optimal_change()
        return "The optimal change for an item that costs $31.51 with an amount paid of $50 is 1 $10 bill, 1 $5 bill, 3 $1 bills, 1 quarter, 2 dimes, and 4 pennies."

    def test_not_enough_money(self):
        """test case to check if enough money was given to buy item"""
        change_maker3 = ChangeMaker(62.13, 50)
        change_maker3.optimal_change()
        return "You don't have enough money."


if __name__ == "__main__":
    unittest.main()