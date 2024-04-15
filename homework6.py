import math

#Exercise 6.1

class Vector:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):             # Vector(x, y, z)
        return "Vector("+str(self.x)+", "+str(self.y)+", "+str(self.z)+")"

    def __eq__(self, other):        # v == w
        return True if (self.x == other.x and self.y == other.y and self.z == other.z) else False

    def __ne__(self, other):        # v != w
        return False if (self.x == other.x and self.y == other.y and self.z == other.z) else True

    def __add__(self, other):       # v + w
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):       # v - w
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, other):       # return the dot product (number)
        return self.x * other.x + self.y * other.y + self.z * other.z

    def cross(self, other):         # return the cross product (Vector)
        return Vector(self.y * other.z - self.z * other.y, self.z * other.x - self.x * other.z, self.x * other.y - self.y * other.x)

    def length(self):               # the length of the vector
        return math.sqrt(self * self)

    def __hash__(self):   # we assume that vectors are immutable
        return hash((self.x, self.y, self.z))   # recommended
    
# v1 = Vector(1, 2, 3)
# v2 = Vector(1, 2, 3)
# v3 = Vector(1, 2, 5)

# print(repr(v1))
# print(v1 == v2)
# print(v1 == v3)
# print(v1 != v2)
# print(v1 != v3)
# print(v1 + v2)
# print(v1 - v2)
# print(v1 * v2)
# print(v1.cross(v3))
# print(v1.length())
# print(hash(v1))

v = Vector(2, 4, 6)
w = Vector(1, 3, 5)
assert v != w
assert v + w == Vector(3, 7, 11)
assert v - w == Vector(1, 1, 1)
assert v * w == 44
assert v.cross(w) == Vector(2, -4, 2)
assert v.length() == math.sqrt(56)
S = set([v, v, w])
assert len(S) == 2

print("Tests passed")