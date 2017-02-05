class Robot:
    def __init__(self, name, build_year):
        self.name = name
        self.build_year = build_year

    def __repr__(self):
        return "Robot(\"" + self.name + "\"," + str(self.build_year) + ")"

    def __str__(self):
        return "Name: " + self.name + ", Build Year: " + str(self.build_year)


if __name__ == "__main__":
    x = Robot("Marvin", 1979)

    x_str = str(x)
    print(x_str, type(x_str))
    # new1 = eval(x_str)	error
    
    x_repr = repr(x)
    print(x_repr, type(x_repr))
    new2 = eval(x_repr)
    print(new2)
    print("Type of new2:", type(new2))


# when to use repr?

# l = [3,8,9]
# s = repr(l)
# print(s)
# print(l == eval(s))
# print(l == eval(str(l)))

# import datetime
# today = datetime.datetime.now()
# str_s = str(today)
# # eval(str_s)
# 
# repr_s = repr(today)
# t = eval(repr_s)	# evaluation?
# print(type(t))
