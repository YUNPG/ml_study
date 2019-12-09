
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-10, 10, 0.1)
y = 1. / (1. + np.exp(-x))
x0 = np.arange(-12, 12, 0.1)
y0 = np.zeros(len(x0))
y1 = np.ones(len(x0))
y2 = np.ones(len(x0)) / 2
x1 = np.array([0, 0])
y3 = np.array([0, 1])
plt.plot(x, y)
plt.plot(x0, y0, 'black', linewidth=0.5, linestyle="--")
plt.plot(x0, y1, 'black', linewidth=0.5, linestyle="--")
plt.plot(x0, y2, 'black', linewidth=0.5, linestyle="--")
plt.plot(x1, y3, 'black', linewidth=1, linestyle="-")
plt.title('sigmoid')
plt.show()