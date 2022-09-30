import numpy as np
import math
from matplotlib import pyplot as plt

x = np.arange(0, 15, .00001)
xx = np.arange(0, 16, 1)
n0 = 185*2
test1 = np.array([185, 161, 138, 118, 99, 85, 70, 59, 52, 51, 44, 39, 36, 31, 26, 21], float)
test2 = np.array([185, 160, 134, 113, 88, 78, 66, 53, 43, 34, 30, 25, 21, 18, 14, 13], float)
test3 = np.array([test1[i] + test2[i] for i in range(16)], float)


def f(x):
    return n0 * np.exp(-0.1823 * x)


def g(x, k):
    return n0 * np.exp(-k * x)


def exp(k, pts):
    return [n0 * math.exp(-k * i) for i in pts]


a = 0.01
b = .5
min_norm = 10000
c = 10000
step = 1.e-5
while a < b:
    if np.linalg.norm(test3 - exp(a, xx)) < min_norm:
        min_norm = np.linalg.norm(test3 - exp(a, xx))
        c = a
    a += step
print(c)

plt.plot(x, f(x), zorder=2, label='Decaimento Radioativo', c='blue')
plt.plot(x, g(x, c), zorder=2, label='Exponencial Ajustada', c='green')
plt.scatter(list(range(16)), test3, c='red', s=15, zorder=3, label='Número de Dados')
plt.legend()
plt.grid()
plt.xlabel('Geração')
plt.ylabel('Quantidade')
plt.axhline(linewidth=2, color="k")
plt.axvline(linewidth=2, color="k")
plt.show()
