def last_digit(n):
    return abs(n) % 10

# Example usage
n = int(input("Enter a number: "))
print(f"The last digit of {n} is {last_digit(n)}")