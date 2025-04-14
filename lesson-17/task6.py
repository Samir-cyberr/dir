
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
x, y = np.meshgrid(x, y)
z = np.cos(x**2 + y**2)
surf = ax.plot_surface(x, y, z, cmap='viridis')
fig.colorbar(surf)
ax.set_title('3D Surface Plot: f(x, y) = cos(x^2 + y^2)')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('f(x, y)')
plt.savefig('plot6_3d_surface.png')

print("All plots saved successfully.")