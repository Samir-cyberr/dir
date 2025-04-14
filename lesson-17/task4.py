import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


x = np.random.uniform(0, 10, 100)
y = np.random.uniform(0, 10, 100)
plt.figure()
plt.scatter(x, y, c='magenta', marker='o')
plt.title('Random Scatter Plot')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.savefig('plot4_scatter.png')