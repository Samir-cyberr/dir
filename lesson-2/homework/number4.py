def integer_division_and_remainder(a, b):
    if b == 0:
        print("Error: Division by zero is not allowed.")
        return
    quotient = a // b
    remainder = a % b
    print(f"Integer Division: {a} // {b} = {quotient}")
    print(f"Remainder: {a} % {b} = {remainder}")

# Example usage
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
integer_division_and_remainder(a, b)
