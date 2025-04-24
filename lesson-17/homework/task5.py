import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

data = np.random.normal(0, 1, 1000)
plt.figure()
plt.hist(data, bins=30, alpha=0.7, color='teal')
plt.title('Histogram of Normally Distributed Data')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.grid(True)
plt.savefig('plot5_histogram.png')