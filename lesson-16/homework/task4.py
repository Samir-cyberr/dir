import numpy as np

# Coefficient matrix
A = np.array([[10, -2, 3],
              [-2, 8, -1],
              [3, -1, 6]])

# Constants vector
b = np.array([12, -5, 15])

# Solve the system
solution = np.linalg.solve(A, b)
print("Solution (I1, I2, I3):", solution)
