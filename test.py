class test():
    def __init__(self):
        self.score = 1
    def print_score(self):
        print(self.score)
    def update_score(self):
        self.score = self.score + 1

test1 = test()
"""
score = 100
test1.print_score()
test1.update_score()
test1.print_score()
test1.update_score()
test1.print_score()
"""
test1.print_score()
test1.score = 100
print("Now I have set a class varible's value from 1 to 100. This was done outside the class defined.")
test1.print_score()