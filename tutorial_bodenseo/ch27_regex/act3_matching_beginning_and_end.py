import re
s1 = "Mayer is a very common Name"
s2 = "He is called Meyer but he isn't German."

s = s2 + "\n" + s1
print(re.search(r"^M[ae][iy]er", s))	# fail

print(re.search(r"^M[ae][iy]er", s, re.MULTILINE))	#succ
print(re.search(r"^M[ae][iy]er", s, re.M))	#succ
print(re.match(r"^M[ae][iy]er", s, re.M))	#fail


print(re.search(r"Python\.$","I like Python."))
print(re.search(r"Python\.$","I like Python and Perl."))
print(re.search(r"Python\.$","I like Python.\nSome prefer Java or Perl."))
print(re.search(r"Python\.$","I like Python.\nSome prefer Java or Perl.", re.M))
