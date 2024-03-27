import math

#exercise 4.1

p1=(2,-4)
p2=(9,-6)
p3=(5,24)
p4=(7,0)
p5=(-2,14)
p6=(-4,-4)
p7=(12,4)
p8=(3,-5)

L = [p1, p2, p3, p4, p5, p6, p7, p8]

#a

#b
def checkIfPositive(p):
    if p[0] > 0 and p[1] > 0:
        return True
    else:
        return False
    
print(checkIfPositive(p1))

#c
L.sort(key=lambda p: (p[-1], p[0]))
print(L)

#d
L.sort(key=lambda p: abs(p[0])+abs(p[1]))
print(L)

#exercise 4.2
L2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

def reverseIterative(L, start, stop):
    for x in range(math.floor((stop - start)/2)+1):
        tmp = L[start]
        L[start] = L[stop]
        L[stop] = tmp
        start += 1
        stop -= 1

def reverseRecursive(L, start, stop):
    if start != stop and stop - start > 0:
        tmp = L[start]
        L[start] = L[stop]
        L[stop] = tmp
        start += 1
        stop -= 1
        reverseRecursive(L, start, stop)

# reverseIterative(L2, 3, 6)
reverseRecursive(L2, 3, 6)

print(L2)

#exercise 4.3

#a
def iter_even():
    i = 0
    while True:
        yield i
        i += 2

# for i in iter_even():
#     print(i)

#b
def iter_odd():
    i = 1
    while True:
        yield i
        i += 2

# for i in iter_odd():
#     print(i)

#c
# iter_power(k), producing powers of k (1, k, k*k, k*k*k, ...).
def iter_power(k):
    i = 0
    while True:
        yield k**i
        i += 1

for i in iter_power(2):
    print(i)