from random import randint
from apple import Apple

class AppleTree:
    
    def __init__(self):
        self.height = 0
        self.age = 0
        self.apples = []
  
    def age_tree(self):
        if self.is_dead():
            return
        else:
            self.age += 1
            self.height += 5
            if self.age > 5:
                self.grow_apples()
    
    def grow_apples(self):
        for _ in range(randint(5,10)):
            new_apple = Apple()
            self.apples.append(new_apple)
   
    def is_dead(self):
        if self.age > 100:
            return True
        return False
    
    def any_apples(self):
        return len(self.apples) != 0

    def pick_an_apple(self):
        if not self.any_apples():
            raise Exception('No apples on your tree')
        return self.apples.pop()
