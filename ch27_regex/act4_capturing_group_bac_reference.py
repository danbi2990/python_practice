import re

# mo = re.search("[0-9]+", "Customer number: 232454, Date: February 12, 2011")
# print(mo.group())
# print(mo.span())
# print(mo.start())
# print(mo.end())
# print(mo.span()[0])
# print(mo.span()[1])


# mo = re.search("([0-9]+).*: (.*)", "Customer number: 232454, Date: February 12, 2011")
# print(mo.group())
# print(mo.group(1))
# print(mo.group(2))
# print(mo.group(1,2))


fh = open("tags.txt")
for i in fh:
    res = re.search(r"<([a-z]+)>(.*)</\1>",i)
    print(res.group(1) + ": " + res.group(2))
