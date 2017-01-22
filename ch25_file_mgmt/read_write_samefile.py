fh = open('colours.txt', 'w+')
fh.write('The colour brown')

# Go to the 8th byte in the file
fh.seek(11)
print(fh.read(5))
print(fh.tell())
fh.seek(11)
fh.write('green')
fh.seek(0)
content = fh.read()
print(content)
