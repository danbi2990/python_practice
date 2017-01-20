
def decorator1(f):
    def helper():
        print("Decorating", f.__name__)
        f()
    return helper

@decorator1
def foo():
    print("inside foo()")


foo()


class decorator2(object):
    def __init__(self, f):
        super(decorator2, self).__init__()
        self.f = f

    def __call__(self):
        print("Decorating", self.f.__name__)
        self.f()


@decorator2
def foo():
    print("inside foo()")


foo()
