
class R2Vector:
    def __init__(self, *, x, y):
        self.x = x
        self.y = y

    def norm(self):
        return sum(val**2 for val in vars(self).values())**0.5
    def __str__(self):
        return (getattr(self, i) for i in vars(self))
class R3Vector(R2Vector):
    def __init__(self, *, x, y, z):
        super().__init__(x=x, y=y)
        self.z = z

v1 = R2Vector(x=2, y=3)
v2 = R3Vector(x=2, y=2, z=3)
print(v1.norm())
print(v2.norm())
