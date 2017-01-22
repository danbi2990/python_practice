import re

s = "Sun Oct 14 13:47:03 CEST 2012"
expr = r"\b(?P<hours>\d\d):(?P<minutes>\d\d):(?P<seconds>\d\d)\b"
x = re.search(expr,s)
print(x.group('hours'))
print(x.group('minutes'))
print(x.start('minutes'))
print(x.end('minutes'))
print(x.span('seconds'))
