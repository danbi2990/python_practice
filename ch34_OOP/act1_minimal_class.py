# class Robot:
#     pass
# 
# x = Robot()
# y = Robot()
# 
# x.name = "Marvin"
# x.build_year = "1979"
# 
# y.name = "Caliban"
# y.build_year = "1993"
# 
# print(x.name)
# print(y.build_year)
# 
# print(x.__dict__)
# print(y.__dict__)


# class Robot(object):
#     pass
# 
# x = Robot()
# Robot.brand = "Kuka"
# print(x.brand)
# 
# x.brand = "Thales"
# print(Robot.brand)
# 
# y = Robot()
# print(y.brand)
# 
# Robot.brand = "Thales"
# print(y.brand)
# print(x.brand)
# 
# print(x.__dict__)
# print(y.__dict__)
# print(Robot.__dict__)

def f(x):
    f.counter = getattr(f, "counter", 0) + 1
    return "Monty Python"


for i in range(10):
    f(i)

print(f.counter)