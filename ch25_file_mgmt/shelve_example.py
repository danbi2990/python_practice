import shelve

# s = shelve.open("MyShelve")

# s["street"] = "Fleet Str"
# s["city"] = "London"
# for key in s:
#     print(key + " " + s[key])

# print(s)
# print(type(s))

# d = dict(s)
# print(d)

# s.close()

# -----------------------------------------------------------------------

# tele = shelve.open("MyPhoneBook")
# tele["Mike"] = {"first":"Mike", "last":"Miller", "phone":"4689"}
# tele["Steve"] = {"first":"Stephan", "last":"Burns", "phone":"8745"}
# tele["Eve"] = {"first":"Eve", "last":"Naomi", "phone":"9069"}
# print(tele["Eve"]["phone"])
# tele.close()

# -----------------------------------------------------------------------

tele = shelve.open("MyPhoneBook")
print(tele["Steve"]["phone"])
