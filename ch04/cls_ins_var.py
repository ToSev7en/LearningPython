
class A:
    aa = 99

    def __init__(self, x, y):
        self.x = x
        self.y = y


a = A(1,2)

print(a.x, a.y, a.aa)
print(A.aa)