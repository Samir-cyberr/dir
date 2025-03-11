try:
    a = float(input("Enter a float number: "))  # Take input and convert to float
    print(f"Rounded to 2 decimal places: {a:.2f}")  # Round to 2 decimal places
except ValueError:
    print("Invalid input! Please enter a valid float number.")
