import numpy as np

# Coefficients matrix for currents
A = np.array([
    [10, -2, 3],
    [-2, 8, -1],
    [3, -1, 6]
])

# Constants vector
B = np.array([12, -5, 15])

# Solve for currents
currents = np.linalg.solve(A, B)
print("Currents (I1, I2, I3):", currents)