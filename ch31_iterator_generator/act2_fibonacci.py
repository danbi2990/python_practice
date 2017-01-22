

# def fibonacci(n):
#     """Ein Fibonacci-Zahlen-Generator"""
#     a, b, counter = 0, 1, 0
#     while True:
#         if (counter > n): 
#             return
#         yield a
#         a, b = b, a + b
#         counter += 1
# f = fibonacci(5)
# for x in f:
# 	 # no linefeed is enforced by  end="":
#     print(x, " ", end="") # 
# print()


def fibonacci():
    """Generates an infinite sequence of Fibonacci numbers on demand"""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

f = fibonacci()

counter = 0
for x in f:
    print(x, " ", end="")
    counter += 1
    if (counter > 10): 
        break 
print()
