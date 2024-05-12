#EXERCISE 8.1

import numpy as np

# a

print(np.linspace(0, 1, 11))
print(np.arange(0, 1.1, 0.1, dtype=float))

# b
#print(np.zeros((5, 6), dtype=int))
print(np.zeros((5, 6), dtype="int8"))

# c

print(np.array([pow(1J, i) for i in range(9)]))
print(np.power(1J, np.arange(9)))
print(np.logspace(0, 8, base = complex(0,1), num=9))

#EXERCISE 8.2

#a
v1 = np.arange(5)
print(v1)

# b
v2 = v1[1::2]
print(v2)

# c
v3 = v1[::-1]
print(v3)

#EXERCISE 8.3

# a
m1 = np.arange(20).reshape((4,5))
print(m1)

# b
m2 = m1[:, ::-1]
print(m2)

# c 
m3 = m1[::-1,:]
print(m3)
print(np.flip(m3, axis=0))

# d
m4 = m1[1:-1,1:-1]
print(m4)