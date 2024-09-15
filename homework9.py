#EXERCISE 9.1

import numpy as np
import matplotlib.pyplot as plt

# x = np.linspace(0, 10)
# y1 = np.sin(x)
# y2 = np.cos(x)
# y3 = np.exp(-x)

# plt.plot(x, y1, 'r-', label='sin(x)') 
# plt.plot(x, y2, 'g:', label='cos(x)')
# plt.plot(x, y3, 'b-.', label='exp(x)')
# plt.title("Funkcje")
# plt.xlabel("x")
# plt.ylabel("y")
# plt.legend()
# plt.show()

#EXERCISE 9.2

n = 100
x = np.random.rand(n)
y = np.random.rand(n)
punkty = np.random.rand(n, 2)
x = punkty[:, 0]
y = punkty[:, 1]

kolory = ['g' if cond else 'r' for cond in x**2 + y**2 <1]
obszar = 50*(x + y)

plt.scatter(x, y, s=obszar, c=kolory)
plt.title("Liczby losowe")
plt.xlabel("x")
plt.ylabel("y")
plt.show()