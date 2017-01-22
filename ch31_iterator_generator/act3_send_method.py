def abc():
    s = "abcdefg"
    count = 0
    while True:
        if count >= len(s):
            count = 0
        message = yield s[count]
        if message != None:
            count = 0 if message < 0 else message
        else:
            count += 1
            
            
x = abc()      
print(next(x))
print(next(x))
print(x.send(5))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
