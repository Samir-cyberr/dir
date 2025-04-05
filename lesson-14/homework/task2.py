import numpy as np
def power_function(number, power):
    return number ** power

numbers = np.array([2, 3, 4, 5])
powers = np.array([1, 2, 3, 4])
vectorized_power = np.vectorize(power_function)
results = vectorized_power(numbers, powers)
print("Power results:", results)