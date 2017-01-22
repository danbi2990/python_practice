
# read
# s1 = open("..\ch23_decorator\decorator_class.py", 'r').readlines()
# print(s1)

# reset cursor position

fh = open("buck_mulligan.txt", 'r')
print(fh.tell())
print(fh.read(7))

fh.close()
