def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Example usage
num = int(input("Enter a positive integer: "))
print(f"{num} is prime: {is_prime(num)}")