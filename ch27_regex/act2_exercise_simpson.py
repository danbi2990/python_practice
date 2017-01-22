# file read
# regex: surname 'Neu', first name starts with 'J'
import re

rex = r'^J.*Neu'
with open("simpsons_phone_book.txt", "r") as f_obj:
	for line in f_obj:
		if re.search(rex, line):
			print(line)
