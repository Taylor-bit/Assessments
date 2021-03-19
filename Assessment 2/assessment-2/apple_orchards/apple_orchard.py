from apple_tree import AppleTree
from apple import Apple

class AppleOrchard:

    def __init__(self):
        self.trees = []
        self.apples = []

    def plant_tree(self):
        new_tree = AppleTree()
        self.trees.append(new_tree)

    def apples_in_orchard(self):
        self.apples = []
        for tree in self.trees:
            for apple in tree.apples:
                self.apples.append(apple)

    def alive_trees(self):
        alive = 0
        for tree in self.trees:
            if tree.is_dead() == False:
                alive += 1
        return alive

    def bulldoze_dead_trees(self):
        tree_count = 0
        for tree in self.trees:
            if tree.is_dead():
                self.trees.pop(tree_count)
                tree_count -= 1
            tree_count += 1

    def trees_producing_fruit(self):
        trees_producing = 0
        for tree in self.trees:
            if len(tree.apples) > 0:
                trees_producing += 1
        return trees_producing

    def trees_not_producing_fruit(self):
        trees_producing = self.trees_producing_fruit()
        trees_not_producing = len(self.trees) - trees_producing
        return trees_not_producing

    def avg_diameter_of_apples(self):
        self.apples_in_orchard()
        total_diameter = 0.0
        apple_count = len(self.apples)
        for apple in self.apples:
            total_diameter += apple.diameter
        avg_diameter = total_diameter / apple_count
        return avg_diameter