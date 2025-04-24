import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

x = np.linspace(-10, 10, 400)
f = x**2 - 4*x + 4
plt.figure()
plt.plot(x, f, label='f(x) = x^2 - 4x + 4')
plt.title('Basic Plot')
plt.xlabel('x-axis')
plt.ylabel('f(x)')
plt.grid(True)
plt.legend()
plt.savefig('plot1_basic.png')