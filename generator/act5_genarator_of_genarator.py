def fibonacci():
    """Ein Fibonacci-Zahlen-Generator"""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

def firstn(g, n):
	for i in range(n):
		yield next(g)

print(list(firstn(fibonacci(), 10)))
