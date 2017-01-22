"""
The next Python example makes use of three back references. We have an imaginary phone list of the Simpsons in a list. Not all entries contain a phone number, but if a phone number exists it is the first part of an entry. Then follows separated by a blank a surname, which is followed by first names. Surname and first name are separated by a comma. The task is to rewrite this example in the following way:

Allison Neu 555-8396
C. Montgomery Burns 
Lionel Putz 555-5299
Homer Jay Simpson 555-7334

"""

import re

l = ["555-8396 Neu, Allison", 
     "Burns, C. Montgomery", 
     "555-5299 Putz, Lionel",
     "555-7334 Simpson, Homer Jay"]

exp = r'^([\d-]*)\s?(\w+),\s(.+)'

for line in l:
	m_obj = re.search(exp, line)
	print(m_obj.group(3)+" "+m_obj.group(2)+" "+m_obj.group(1))
