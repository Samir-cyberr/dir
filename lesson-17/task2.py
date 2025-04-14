import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

x = np.linspace(0, 2 * np.pi, 400)
s = np.sin(x)
c = np.cos(x)
plt.figure()
plt.plot(x, s, label='sin(x)', linestyle='--', color='blue')
plt.plot(x, c, label='cos(x)', linestyle='-', color='red')
plt.title('Sine and Cosine Plot')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.legend()
plt.grid(True)
plt.savefig('plot2_sine_cosine.png')