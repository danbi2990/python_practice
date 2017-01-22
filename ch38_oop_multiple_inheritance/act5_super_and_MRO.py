# from act6_super1 import A,B,C,D
# x = D()
# B.m(x)
# C.m(x)
# A.m(x)

# from act7_super3 import D
# x = D()
# x.m()


# from act8_super4 import D
# x = D()
# x.m()

# from act9_super5 import D
# x = D()
# x.m()

from act10_super_init import A,B,C,D
d = D()

print(D.mro())
print(B.mro())
print(A.mro())
