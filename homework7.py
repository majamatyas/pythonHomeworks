import math
import random

# EXERCISE 7.1

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


v1 = Vector(1, 2, 3)
v2 = Vector(1, 7, 12)

def find_axis(v1, v2):
    v3 = v1.cross(v2)
    if v3.x == 0 and v3.y ==0 and v3.z==0:
        raise ValueError
    l=v3.length()
    v3.x = v3.x/l
    v3.y = v3.y/l
    v3.z = v3.z/l
    return v3

print(find_axis(v1,v2))

# EXERCISE 7.2

def iterA():
    i = 0
    while i<10:
        yield 0
        yield 1
        i+=1

def iterB(seq):
    i = 0
    while i<10:
        yield random.choice(seq)
        i+=1

def iterC(seq):
    i = 0
    while i<10:
        for sign in seq:
            yield sign
            i+=1




for i in iterA():
    print(i) 
    
for i in iterB((0,1)):
    print(i) 
    
for i in iterC((0,1,0,-1)):
    print(i)                          