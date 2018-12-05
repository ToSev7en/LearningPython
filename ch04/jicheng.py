# 新式类
class D:
    pass

class E:
    pass

class B(D):
    pass

class C(E):
    pass

class A(B, C):
    pass

print(A.__mro__)