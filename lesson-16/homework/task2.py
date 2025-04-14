
import numpy as np

def power_func(base, exponent):
    return base ** exponent

bases = np.array([2, 3, 4, 5])
exponents = np.array([1, 2, 3, 4])
vectorized_power = np.vectorize(power_func)
powers = vectorized_power(bases, exponents)

print("Powers:", powers)
