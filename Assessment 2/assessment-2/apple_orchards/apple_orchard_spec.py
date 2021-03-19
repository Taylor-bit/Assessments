import unittest, itertools
from apple_tree import *
from apple import *
from apple_orchard import *

class ValidateAppleOrchardClass(unittest.TestCase):
    """Tests for `apple_orchard.py`."""

    def test_plant_tree(self):
        """When you plant a tree, an AppleTree is added to self.trees"""
        apple_orchard = AppleOrchard()
        self.assertEqual(apple_orchard.trees, [])
        apple_orchard.plant_tree()
        self.assertEqual(type(apple_orchard.trees[0]), AppleTree)

    def test_alive_trees(self):
        """When you check for alive trees you should get a count of living trees returned"""
        apple_orchard = AppleOrchard()
        self.assertEqual(apple_orchard.alive_trees(), 0)
        apple_orchard.plant_tree()
        self.assertEqual(apple_orchard.alive_trees(), 1)

    def test_bulldoze_dead_trees(self):
        """When you bulldoze all dead trees, all remaining trees in the orchard are alive"""
        apple_orchard = AppleOrchard()
        apple_orchard.plant_tree()
        apple = Apple()
        apple.diameter = 5
        apple2 = Apple()
        apple2.diameter = 7
        apple_orchard.trees[0].apples.append(apple)
        apple_orchard.trees[0].apples.append(apple2)
        self.assertEqual(apple_orchard.avg_diameter_of_apples(), 6)

if __name__ == '__main__':
    unittest.main()