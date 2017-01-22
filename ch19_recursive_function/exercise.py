def greeting(expr):
    def greeting_decorator(func):
        def function_wrapper(x):
            print(expr + ", " + func.__name__ + " returns:")
            func(x)
        return function_wrapper
    return greeting_decorator


@greeting("καλημερα")
def foo(x):
    print(42)

# greeting2 = greeting("καλημερα")

# foo = greeting_decorator(foo, "καλημερα")
foo("Hi")

# def foo(a,*l):
#     print(len(l))
#
# lst = [1,2,3]
# foo(0,*lst)

# def varpafu(*x):
#     print(x)
#     print(type(x))
#
# y = [1,2,3]
# print(type(*y))
# # varpafu(34, "Do you like python?", "Of course.")
# varpafu(*y)


## Think of a recusive version of the function f(n) = 3 * n, i.e. the multiples of 3
# def times3(n):
#     if n == 1:
#         return 3
#     else:
#         return times3(n-1) + 3
#
# def fibosumcci(n):
#     if n == 1:
#         return 1
#     else:
#         return n + fibosumcci(n-1)
#
# print(fibosumcci(5))
#
# def callbyreference(lst):
#     lst[0] = 2
#     return
#
# lst = [1,2,3]
# print(lst)
# callbyreference(lst)
# print(lst)
