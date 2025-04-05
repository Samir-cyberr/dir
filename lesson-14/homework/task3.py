import numpy as np

# Coefficients matrix
A = np.array([
    [4, 5, 6],
    [3, -1, 1],
    [2, 1, -2]
])

# Constants vector
B = np.array([7, 4, 5])

# Solve the system
solution = np.linalg.solve(A, B)
print("Solution (x, y, z):", solution)