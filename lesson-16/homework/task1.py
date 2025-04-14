import numpy as np

def fahrenheit_to_celsius(f):
    return (f - 32) * 5 / 9

temps_fahrenheit = np.array([32, 68, 100, 212, 77])
vectorized_converter = np.vectorize(fahrenheit_to_celsius)
temps_celsius = vectorized_converter(temps_fahrenheit)

print("Celsius temperatures:", temps_celsius)
