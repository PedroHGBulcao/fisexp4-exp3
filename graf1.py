import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

x = np.arange(0, 40, .00001)
pts = np.arange(0, 41, 1)
n0 = 185


def f(x):
    return n0 * ((5 / 6) ** x)


plt.plot(x, f(x), zorder=1, label='Decaimento Radioativo')
plt.scatter(pts, f(pts), c='red', s=15, zorder=2, label='Número de Dados')
plt.legend()
plt.grid()
plt.xlabel('Geração')
plt.ylabel('Quantidade')
plt.axhline(linewidth=2, color="k")
plt.axvline(linewidth=2, color="k")
plt.show()


