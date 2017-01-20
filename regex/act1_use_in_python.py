import re
# x = re.search("cat","A cat and a rat can't be friends.")
# print(x)
# x = re.search("cow","A cat and a rat can't be friends.")
# print(x)


# if re.search("cat","A cat and a rat can't be friends."):
#     print("Some kind of cat has been found :-)")
# else:
#     print("No cat has been found :-)")


if re.search(" .at ","A cat and a rat can't be friends."):
    print("'.at' has been found.")
else:
    print("No '.at' around.")

