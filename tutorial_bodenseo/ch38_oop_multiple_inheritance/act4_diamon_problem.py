class A:
    def m(self):
        print("m of A called")


class B(A):
    pass
    # def m(self):
    #     print("m of B called")


class C(A):
    def m(self):
        print("m of C called")


class D(B, C):
    pass

x = D()
x.m()
