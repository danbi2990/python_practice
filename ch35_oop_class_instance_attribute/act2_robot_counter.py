
class Robot:

    Three_Laws = (
"""A robot may not injure a human being or, through inaction, allow a human being to come to harm.""",
"""A robot must obey the orders given to it by human beings, except where such orders would conflict with the First Law.,""",
"""A robot must protect its own existence as long as such protection does not conflict with the First or Second Law."""
)

    def __init__(self, name, build_year):
        self.name = name
        self.build_year = build_year

for number, text in enumerate(Robot.Three_Laws):
    print(str(number+1) + ":\n" + text)

class C:

    counter = 0
    
    def __init__(self): 
        type(self).counter += 1

    def __del__(self):
        type(self).counter -= 1

if __name__ == "__main__":
    x = C()
    print("Number of instances: : " + str(C.counter))
    y = C()
    print("Number of instances: : " + str(C.counter))
    del x
    print("Number of instances: : " + str(C.counter))
    del y
    print("Number of instances: : " + str(C.counter))
