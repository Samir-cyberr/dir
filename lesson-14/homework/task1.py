import numpy as np

def fahrenheit_to_celsius(f):
    return (f - 32) * 5 / 9

temps_f = np.array([32, 68, 100, 212, 77])
vectorized_converter = np.vectorize(fahrenheit_to_celsius)
temps_c = vectorized_converter(temps_f)
print("Temperatures in Celsius:", temps_c)