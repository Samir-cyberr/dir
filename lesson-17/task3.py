import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


x = np.linspace(0.1, 5, 400)
fig, axs = plt.subplots(2, 2, figsize=(10, 8))
axs[0, 0].plot(x, x**3, color='purple')
axs[0, 0].set_title('f(x) = x^3')
axs[0, 1].plot(x, np.sin(x), color='green')
axs[0, 1].set_title('f(x) = sin(x)')
axs[1, 0].plot(x, np.exp(x), color='orange')
axs[1, 0].set_title('f(x) = e^x')
axs[1, 1].plot(x, np.log(x + 1), color='brown')
axs[1, 1].set_title('f(x) = log(x + 1)')
for ax in axs.flat:
    ax.set(xlabel='x', ylabel='f(x)')
    ax.grid(True)
fig.tight_layout()
plt.savefig('plot3_subplots.png')